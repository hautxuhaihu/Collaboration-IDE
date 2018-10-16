from django.shortcuts import render, redirect, HttpResponse
from .forms import LoginForm, SignUpForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

def formhandleview(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":

        if request.POST['check'] == "login":

            LoginFormRender = LoginForm(data=request.POST)

            if LoginFormRender.is_valid():
                user = LoginFormRender.get_user()
                login(request, user)
                return redirect('home')

            else:
                SignUpFormRender = SignUpForm()

                context = {
                    'LoginFormRender': LoginFormRender,
                    'SignUpFormRender': SignUpFormRender
                }

                print(LoginFormRender.non_field_errors())
                return render(request, 'accounts/register.html', context)

        elif request.POST['check'] == "signup":

            SignUpFormRender = SignUpForm(request.POST)
            print(request.POST)

            if SignUpFormRender.is_valid():
                user = SignUpFormRender.save(commit=False)

                password = SignUpFormRender.cleaned_data['password1']

                user.set_password(password)
                user.save()
                # login the user

                login(request, user)
                return redirect('home')

            else:
                print(SignUpFormRender.errors.as_data() , "a")
                LoginFormRender = LoginForm()

                context = {
                    'LoginFormRender': LoginFormRender,
                    'SignUpFormRender': SignUpFormRender
                }
                return render(request, 'accounts/register.html', context)

    else:
        LoginFormRender = LoginForm()
        SignUpFormRender = SignUpForm()

        context = {
            'LoginFormRender': LoginFormRender,
            'SignUpFormRender': SignUpFormRender
        }
        return render(request, 'accounts/register.html', context)
