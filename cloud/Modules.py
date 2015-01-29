import socket
import uuid
from uuid import getnode as get_mac
from datetime import timedelta
from datetime import datetime

from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse

from cloud.models import UserProfile,MacAddress,FileAccess


#---------------------------------------------------------------------------------------------------------------------------

def mail(usr):
	toAddress=usr.email 
	name=usr.first_name+" "+usr.last_name
	otp=str(uuid.uuid4())
	timeOut=datetime.now() + timedelta(minutes=15)
	subject=' OTP - Do not Show with Anyone !'
	message="<center><h1> High Secure Cloud Data Storage<h1></center>\n<p>Hello "+name+",\n\n</p>This is your OTP please do not share with anyone.\n\n\n <center><h4>"+otp+"</center></h4>\n\n\n -Thanks,\n<b>HighSecureCloudStorage Team</b>"
	mail=EmailMessage(subject, message, settings.EMAIL_HOST_USER, [toAddress])
	mail.content_subtype = "html"
	#mail.send()

	users = UserProfile.objects.get(user=usr)
	
	timeDifference=datetime.utcnow()-users.timeout.astimezone(timezone.utc).replace(tzinfo=None) #To subtract offset-naive and offset-aware datetimes
	if timeDifference.total_seconds()>0:
		users.OTP=None
	if users.OTP==None:
		users.timeout=timeOut
		users.OTP=otp
		mail.send()
	
	users.save()
#---------------------------------------------------------------------------------------------------------------------------

def login_check(usrname):
	
	mac = get_mac()
	mac = (hex(mac))
	mac =str(mac)
	ValidUser=False
	current_user=User.objects.get(username=usrname)
	users = UserProfile.objects.get(user=current_user)
	if usrname:
		for macAdd in users.MAC.all(): 
			macAdd=str(macAdd)
			if macAdd==mac:
				ValidUser=True

	if ValidUser==True:
		return 1
	else:
		mail(current_user)
		return 0

#---------------------------------------------------------------------------------------------------------------------------
def Rearrange(key):
	key=key.split('$#$')[0]
	fileaccess=FileAccess.objects.get(serverUid=key)
	return fileaccess.owner