
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from user_management.forms import CreateUserForm, MyUserUpdateForm
from user_management.models import MyUser, Roles
from course_management.models import Course
from .classes import Auth

class LogInPage(View):
    def get(self,request):
        return render(request, template_name="core/login.html")
    def post(self, request):
        email = request.POST['name']
        password = request.POST['password']
        auth = Auth(email, password)

        if not auth.logIn():
            return render(request, template_name="core/login.html", context={"message": "Wrong email or password"})
        else:
            request.session["email"] = email
            return redirect("/courses/")

class Homepage(View):
    def get(self,request):
        return render(request, "core/homepage.html")
    def post(self,request):
        return render(request, template_name="core/homepage.html")

class UserCreateView(View):
    model = MyUser
    form_class = CreateUserForm
    template_name = 'user_management/create_user.html'
    success_url = reverse_lazy('user_management:user_list')


class UserUpdateView(View):
    model = MyUser
    form_class = MyUserUpdateForm
    template_name = 'user_management/update_user.html'
    success_url = reverse_lazy('user_management:user_list')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.id == self.kwargs['pk']



