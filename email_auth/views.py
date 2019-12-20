from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .forms import SignupForm,LoginForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from . import models
from django.urls import reverse_lazy
from django.views import generic


def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Confirmation Mail'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user)
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request,'inform.html')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        obj=user
        return render(request,'confirm.html',{'user':user})
    else:
        return HttpResponse('Activation link is invalid!')

def dashboard(request):
    #user = {}
    #user["username"] = request.GET['username']
    #user["email"] = request.GET['email']
    #print(user)
    #print(type(user))
    return render(request,'dashboard.html')

def user_logout(request,name,email):
    user=User.objects.get(username=name,email=email)
    logout(request)
    return redirect('home')

def view(request):
    obj=User.objects.filter(is_active=True)
    return render(request,'view.html',{'object':obj ,'length':len(obj)})

    
"""
class LoginView(generic.FormView):
    form_class = LoginForm
    #success_url = reverse_lazy('home')
    template_name = 'registration/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            print('logged in')
            #return super(LoginView, self).form_valid(form)
            return HttpResponse('hello you are logged in ')
        else:
            print('not li')
            #return self.form_invalid(form)
            return HttpResponse('hello you are not logged in ')
            """
            