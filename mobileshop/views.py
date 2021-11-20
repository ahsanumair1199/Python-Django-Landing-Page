from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail
def home(request):
    return render(request, 'index.html')

def send_mail1(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        send_mail(
            'Best Mobiles Shop',
            'Thank You For Subscribing at Our Website.',
            'ahsanumair1199@gmail.com',
            [email],
            fail_silently=False,
        )
        messages.success(request, "Thank you for subscribing us")
    return redirect('home')