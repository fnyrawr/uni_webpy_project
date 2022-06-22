from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from django.contrib.auth.models import User
from .models import CustomUser
from django.shortcuts import redirect
from django.contrib.auth import (
    login as auth_login,
)
from User.models import get_customuser_from_user
from django.http import HttpResponseRedirect

class CustomSignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(username=data['username'],
                                        password=data['password'],
                                        first_name=data['first_name'],
                                        last_name=data['last_name'],
                                        email=data['email'],
                                        )
        cUser = CustomUser.objects.create(user=user,
                                        profile_picture=data['profile_picture'],
                                        )
        return redirect('login')
    
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        """Security check complete. Log the user in. PERFORM CUSTOM CODE."""
        auth_login(self.request, form.get_user())

        user = form.get_user()  # Class is User, not MyUser
        
        cUser = get_customuser_from_user(user)
        if cUser is not None:
            pass # Custom code
        return HttpResponseRedirect(self.get_success_url())
    
class MyUserListView(generic.ListView):
    model = CustomUser
    context_object_name = 'all_users'
    template_name = 'customuser-list.html'