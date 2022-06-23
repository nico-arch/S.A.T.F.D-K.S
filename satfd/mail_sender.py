# from django.shortcuts import render
# from pcl.settings import EMAIL_HOST_USER
# from . import forms
# from django.core.mail import send_mail
# # Create your views here.
# #DataFlair #Send Email
# def subscribe(request):
#     sub = forms.Subscribe()
#     if request.method == 'POST':
#         sub = forms.Subscribe(request.POST)
#         subject = 'Welcome to DataFlair'
#         message = 'Hope you are enjoying your Django Tutorials'
#         recepient = str(sub['Email'].value())
#         send_mail(subject,
#             message, EMAIL_HOST_USER, [recepient], fail_silently = False)
#         return render(request, 'subscribe/success.html', {'recepient': recepient})
#     return render(request, 'subscribe/index.html', {'form':sub})


from django.shortcuts import render
from django_project.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
from django.contrib.auth.models import Group, User
import logging
# Create your views here.
#DataFlair #Send Email
def send_email( subjects, msg, recipient):
    strings = []
    strings.append(recipient)

    subject = subjects
    message = msg
    recepient = recipient
    # recepient = strings
    send_mail(subject,message, EMAIL_HOST_USER, recepient, fail_silently = False)


def send_email_to_group( subjects, msg, groupe):

    print("Into to function send_email_to_group")
    email_strings = []
    group_list = Group.objects.all()
    if groupe == 1:
        for group in group_list:
            print("for group in group_list:")
            if group.name == 'Administration (ok)':
                emails = User.objects.filter(groups=group, is_active=True, is_staff =True).values_list('email', flat = True)
                print("Emails = "+str(emails))
                # break
                send_email( subjects, msg, emails )
                break
        pass
    if groupe == 2:
        for group in group_list:
            print("for group in group_list:")
            if group.name == 'Comptabilité (ok)':
                emails = User.objects.filter(groups=group, is_active=True, is_staff =True).values_list('email', flat = True)
                print("Emails = "+str(emails))
                # break
                send_email( subjects, msg, emails )
                break
        pass
    if groupe == 3:
        for group in group_list:
            print("for group in group_list:")
            if group.name == 'Directions générale (ok)':
                emails = User.objects.filter(groups=group, is_active=True, is_staff =True).values_list('email', flat = True)
                print("Emails = "+str(emails))
                # break
                send_email( subjects, msg, emails )
                break
        pass
    if groupe == 4:
        for group in group_list:
            print("for group in group_list:")
            if group.name == 'Grande Caisse (ok)':
                emails = User.objects.filter(groups=group, is_active=True, is_staff =True).values_list('email', flat = True)
                print("Emails = "+str(emails))
                # break
                send_email( subjects, msg, emails )
                break
        pass
    if groupe == 5:
        for group in group_list:
            print("for group in group_list:")
            if group.name == 'Petite caisse (ok)':
                emails = User.objects.filter(groups=group, is_active=True, is_staff =True).values_list('email', flat = True)
                print("Emails = "+str(emails))
                # break
                send_email( subjects, msg, emails )
                break
        pass
    if groupe == 6:
        for group in group_list:
            print("for group in group_list:")
            if group.name == 'Ressources humaines (ok)':
                emails = User.objects.filter(groups=group, is_active=True, is_staff =True).values_list('email', flat = True)
                print("Emails = "+str(emails))
                # break
                send_email( subjects, msg, emails )
                break
        pass
    if groupe == 7:
        for group in group_list:
            print("for group in group_list:")
            if group.name == 'Vérificateurs (ok)':
                emails = User.objects.filter(groups=group, is_active=True, is_staff =True).values_list('email', flat = True)
                print("Emails = "+str(emails))
                # break
                send_email( subjects, msg, emails )
                break
        pass
    if groupe == 8:
        for group in group_list:
            print("for group in group_list:")
            if group.name == 'Vérificateurs - pourcentage (ok)':
                emails = User.objects.filter(groups=group, is_active=True, is_staff =True).values_list('email', flat = True)
                print("Emails = "+str(emails))
                # break
                send_email( subjects, msg, emails )
                break
        pass
