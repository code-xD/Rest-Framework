from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pinax.notifications.models import NoticeType, send
from .models import Snippet
from django.utils.translation import ugettext_noop as _
from django.core.mail import send_mail


@receiver(post_save, sender=Snippet)
def send_notification(sender, instance, created, **kwargs):
    # NoticeType.create("friends_invite", _("Invitation Received"),
    #                   _("you have received an invitation"))
    # NoticeType.create("friends_accept", _("Acceptance Received"),
    #                   _("an invitation you sent has been accepted"))
    # print("notifications sent.")
    # u = User.objects.all().filter(username='xd101')
    # send(u, "friends_invite")
    send_mail('Subject here', 'Here is the message.', 'shivansh586@gmail.com',
              ['shivanshanand012@gmail.com'], fail_silently=False)
    print('submitted')
