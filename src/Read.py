import RPi.GPIO as GPIO
import MFRC522
import signal
from firebase_connect import post_onto_fb
import time

continue_reading = True

card_uid = [67, 228, 155, 46]
chain_uid = [34, 217, 81, 115]

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    
    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"
    
    else:
		print "Card Not detected"
		post_onto_fb(False)
		time.sleep(5)
		print("done")
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
		print "Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])
		print "Card read UID: %s,%s,%s,%s" % (card_uid[0], card_uid[1], card_uid[2], card_uid[3])
		if(uid[0]==card_uid[0] and uid[1]==card_uid[1] and uid[2]==card_uid[2] and uid[3] == card_uid[3]):
			post_onto_fb(True)
		else:
			post_onto_fb("Some Other card has been placed!")
		
