from django.shortcuts import render, redirect

from django.views.generic import FormView, View
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from django.http import HttpResponseRedirect

from  .forms import LoginForm




class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = "/dashboard/"

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("dashboard-home")
        return render(self.request, self.template_name)

    def form_valid(self, form):
        uname = self.request.POST["username"]
        pword = self.request.POST["password"]
        user = authenticate(username=uname, password=pword)
        
        if user is not None:
            login(self.request, user)
        else:
            return render(
                self.request,
                self.template_name,
                {"error": "Your Username or Password do not match.", "form": form},
            )
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy("accounts:login"))