#WOW this class is ugly. TODO: stop being ugly, class.

import smtplib
from config import email_host
from config import email_username
class Log:
    showV = True
    showE = True
    notifyMe = True
    @staticmethod
    def v(tag,event):
        if Log.showV:
            print bcolors.OKGREEN + "[VERBOSE] " + "[" + tag + "]" + " " + Log.sanitizeOuput(event) + bcolors.ENDC

    @staticmethod
    def report_exception(e, traceback):
         Log.e("EXCEPTION", str(e) + "\n" + traceback.format_exc() )
    @staticmethod
    def e(tag, event):
        if Log.showE:
            print bcolors.FAIL + "[ERROR] " + "[" + tag + "]" + " " + Log.sanitizeOuput(event) + bcolors.ENDC
        if Log.notifyMe:
            Log._send_mail(tag, event)

    @staticmethod
    def _send_mail(tag, event):
        sender = email_username
        receivers = [email_username]

        message = "From: Dogebot " + "<" + email_username +  ">\n"
        message += "To: Dogebot <"+ email_username +">\n"
        message += "Subject: Dogebot error report\n\n"
        message += "Tag: " + tag + "\n"
        message += "Event: " + event + "\n"

        try:
           smtpObj = smtplib.SMTP(email_host)
           smtpObj.sendmail(sender, receivers, message)
           print "Successfully sent email report"
        except Exception as e:
           print e



    @staticmethod
    def sanitizeOuput(output):
        if output.__class__.__name__ is "Status" or output.__class__.__name__ is "StatusMock":
            return output.text
        elif output.__class__.__name__ is "TweetResponse":
            return output.get_status().encode('ascii', 'ignore')
        else:
            return output.encode('ascii', 'ignore')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'