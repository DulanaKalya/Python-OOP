#---------------------------------Abstraction-----------------------------------

#Reduce Complexity by hiding unneccssary details

class EmailService:
    def _connect(self):
        print("Connecting to email server")

    def _authenticate(self):
        print("Authenticating...")

    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending email...")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from email server ...")

user = EmailService()

user.send_email()
user._disconnect()




