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
		last_update_data = {'status':"Wallet is connected", 'time':time}
	else:
		data= {time:" Wallet is not connected"}
		last_update_data = {'status':"Wallet is Not connected", 'time':time}
	
	fb.patch(fb_link+'wallet_log/'+date, data)
	
	fb.patch(fb_link+'last_update/', last_update_data)
	
