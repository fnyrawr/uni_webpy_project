from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    pdf = models.FileField(null= True, blank=True, validators=[FileExtensionValidator(['pdf'])])
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Product'
        verbose_name_plural = 'Product'
    
    def review(self, user, **kwargs):
        ReviewVote.objects.filter(user=user, product = self).delete()
        ReviewVote.objects.create(user=user, product = self,
                                        title = kwargs.get('title'),
                                        review=self
                                    )
    
    def __str__(self):
        return self.name + ' (' + self.price + ')'

    def __repr__(self):
        return self.name+ ' / ' + self.description + ' / ' + self.price

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_pictures/', blank = True, null = True)

    def __str__(self):
        return self.product.name

class Review(models.Model):
    stars = models.IntegerField(default=1)
    title = models.TextField(max_length=100)
    text = models.TextField(max_length=500)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def get_useful(self):
        upvotes = ReviewVote.objects.filter(useful_or_not='U',
                                      review=self)
        return upvotes

    def get_useful_count(self):
        return len(self.get_useful())

    def get_useless(self):
        upvotes = ReviewVote.objects.filter(up_or_down='N',
                                      review=self)
        return upvotes

    def get_useless_count(self):
        return len(self.get_useless())
    
    def vote(self, user, useful_or_not):
        U_or_N = 'U'
        if useful_or_not == 'not':
            U_or_N = 'N'
        if (ReviewVote.objects.filter(user=user, review=self, up_or_down=U_or_N).exists()):
            ReviewVote.objects.filter(user=user, review=self, up_or_down=U_or_N).delete()
        else:
            ReviewVote.objects.filter(user=user, review=self).delete()
            ReviewVote.objects.create(useful_or_not=U_or_N,
                                        user=user,
                                        review=self
                                    )
    
    def __str__(self):
        return self.stars + "Stars " + self.text + "for " + self.product
    
class ReviewVote(models.Model):
    VOTE_TYPES = [
        ('U', 'useful'),
        ('N', 'not useful'),
    ]
    useful_or_not = models.CharField(max_length=1,
                                  choices=VOTE_TYPES,
                                 )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.review + " " + self.useful_or_not + "by " + self.user.username
    
class Report(models.Model):
    TYPES = [
        ('O', 'Other'),
        ('H', 'Hatespeech'),
        ('S', 'Spam_or_Scam'),
        ('V', 'Violence'),
    ]
    
    type = models.CharField(max_length=1,
                            choices=TYPES,
                            default ="O"
                            )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.type + "for " + self.review.title