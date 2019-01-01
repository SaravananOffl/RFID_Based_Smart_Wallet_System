import auth_keys
from datetime import datetime
from firebase import firebase 

time = datetime.now()
fb_link = auth_keys.firebase_link
time =str(time)
date = time[0:10]
time = time[11:19]
print(time)
def post_onto_fb(status):
	fb= firebase.FirebaseApplication(fb_link)
	if status is True:
		data = {time: "Wallet is present"}
	else:
		data= {time:" Wallet is not connected"}
	
	fb.patch(fb_link+'wallet_log/'+date, data)
	
post_onto_fb(True)
