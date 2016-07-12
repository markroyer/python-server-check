#!/usr/bin/env python

# Author - Mark Royer

import os
import time
import smtplib

from email.mime.text import MIMEText

hostname = "example.com"
sender = "mark.e.royer@gmail.com"
# Additional receivers can be added, but they must be comma separated 
receivers = sender + ",someone_else@gmail.com"

def ping():
    print "Attempting to ping host %s..." % hostname
    # Send one packet and wait up to 10 seconds for a response
    return os.system("ping -c 1 -W 10 " + hostname  + " > /dev/null")

def main():
    response = ping()
    attempts = 1
    waitTime = 20 # seconds
    while response != 0 and attempts <= 10:
        print "Attempt %d to ping host %s failed. Trying again in %d seconds." % (attempts, hostname, waitTime)
        time.sleep(waitTime)
        response = ping()
        attempts+=1

    if response != 0:
        msg = MIMEText("%s failed to respond after %d ping attempts.  Someone should probably investigate." % (hostname, attempts))
        msg['Subject'] = "Host %s is unresponsive." % hostname
        msg['From'] = sender
        msg['To'] = receivers

        s = smtplib.SMTP("127.0.0.1")
        s.sendmail(sender, msg["To"].split(","), msg.as_string())
        s.quit()

        print "Failed to ping %s.  Sent email to %s." % (hostname, receivers)

    else:
        print "Succesful ping response from %s.  It's alive!" % hostname

if __name__ == "__main__":
    main()
