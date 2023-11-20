from django.conf import settings
from django.shortcuts import render
from account.models import MyUser as User
from account.forms import RegistrationUserForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from services.generator import Generator
from django.core.mail import send_mail


def register_view(request):
    form = RegistrationUserForm()

    if request.method == "POST":
        form = RegistrationUserForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data.get("password1"))
            new_user.is_active = False
            activation_code = Generator.create_activation_code(size=8, model_=User)
            new_user.activation_code = activation_code
            new_user.save()

            subject = "Activation Message"
            message = f"CODE: {activation_code}"
            from_mail = settings.EMAIL_HOST_USER
            to_mail = [new_user.email]

            send_mail(
                subject, message, from_mail, to_mail
            )

            return redirect("activate", slug=new_user.slug)




    context = {
        "form": form,
    }
    return render(request, "register.html", context)

def activate_view(request,slug):
    user = User.objects.get(slug=slug) 
    if request.method == 'POST':
       code = request.POST.get('otp') 

       if user.activation_code == code:
           user.is_active = True
           user.activation_code = None
           user.save()
           login(request,user)
           return redirect('index')
       


    context = {}

    return render(request,'activate.html',context)
