#WOW this class is ugly. TODO: stop being ugly, class.
class Log:
    showV = True
    showE = True
    notifyMe = True
    @staticmethod
    def v(tag,event):
        if Log.showV:
            print bcolors.OKGREEN + "[VERBOSE] " + "[" + tag + "]" + " " + Log.sanitizeOuput(event) + bcolors.ENDC

    @staticmethod
    def e(tag, event):
        if Log.showE:
            print bcolors.FAIL + "[ERROR] " + "[" + tag + "]" + " " + Log.sanitizeOuput(event) + bcolors.ENDC

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