from django.core.mail import send_mail
from django.conf import settings
import random


from .models import User


def send_otp_via_email(email):
    otp = random.randint(1000, 9999)
    subject = "Your jobboard OTP code"
    message = f"Your jobboard account verification OTP code is {otp}"
    email_from = f"Job Board <{settings.EMAIL_HOST_USER}>"

    # send_mail(subject, message, email_from, [email])
    print(subject, message, email_from, [email])

    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()
