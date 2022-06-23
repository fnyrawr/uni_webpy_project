from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from .models import CustomUser
from django.contrib.auth import (
    login as auth_login,
)
from .forms import SignUpForm
from django.http import HttpResponseRedirect

class CustomSignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
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