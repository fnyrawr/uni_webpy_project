from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.views import LoginView
from .models import CustomUser
from django.contrib.auth import (
    login as auth_login,
)
from .forms import SignUpForm
from django.http import HttpResponseRedirect
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
import threading


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

def send_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Email verification'
    email_body = render_to_string('activation-email.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.id)),
        'token': generate_token.make_token(user)
    })
    
    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_FROM_USER,
                         to=[user.email]
                         )

    EmailThread(email).start()

def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(id=uid)

    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_verified = True
        user.save()
        
        return redirect("login")

    return render(request, 'activation-failed.html', {"user": user})


class CustomSignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"
    
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            print(form.data)
            user = form.save()
            send_email(user, request)
            
            return redirect("login")
        return render(request, self.template_name, {'form': form})
    
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        """Security check complete. Log the user in. PERFORM CUSTOM CODE."""
        auth_login(self.request, form.get_user())
        # custom
        return HttpResponseRedirect(self.get_success_url())
    
class MyUserListView(generic.ListView):
    model = CustomUser
    context_object_name = 'all_users'
    template_name = 'customuser-list.html'