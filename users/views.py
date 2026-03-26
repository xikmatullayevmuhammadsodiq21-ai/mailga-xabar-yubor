from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def index(request):
    

    if request.method == "POST":
        subject = request.POST.get("subject")
        text = request.POST.get("text")
        email = request.POST.get("email")
        try:
            send_mail(subject=subject, message=text, from_email=settings.EMAIL_HOST_USER, recipient_list=[email], fail_silently=True)
        except Exception as e:
            print(e)
        
    return render(request, 'index.html')
