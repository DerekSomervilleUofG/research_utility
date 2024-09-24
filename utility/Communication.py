import pymsteams
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utility.ReadWriteFile import ReadWriteFile
class Communication():

    read_write_file = ReadWriteFile()
    

    def __init__(self) -> None:
        self.connector = None
        if self.read_write_file.file_exists("ms_team.cfg", "resource/"):
            key = self.read_write_file.get_file_as_string("ms_team.cfg", "resource/")
            self.connector = pymsteams.connectorcard(key)

    def send_ms_team_message(self, message):
        if self.connector is not None:
            self.connector.text(message)
            self.connector.send()

    def get_sender_and_password(self):
        email_sender = None
        email_sender_password = None
        if self.read_write_file.file_exists("gmail.cfg", "resource/"):
            cfg = self.read_write_file.get_file_as_string("gmail.cfg", "resource/")
            email_sender = cfg.split(",")[0]
            email_sender_password = cfg.split(",")[1]
        return email_sender, email_sender_password


    def create_smtp_server(self, sender, password):
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(sender, password)
        return smtp_server

    def get_smtp_server(self):
        smtp_server = None
        email_sender, password = self.get_sender_and_password()
        if email_sender is not None:
            smtp_server = self.create_smtp_server(email_sender, password)
        return smtp_server, email_sender

    def get_email_message(self, sender, to_email_address, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = to_email_address
        return msg
    
    def send_email(self, to_email_address, subject, message):
        try:
            smtp_server, email_sender = self.get_smtp_server()
            if smtp_server is not None:
                msg = self.get_email_message(email_sender, to_email_address, subject, message)
                smtp_server.sendmail(email_sender, to_email_address, msg.as_string())
        except Exception as ex:
            print(f"Failed to send email. Error: {str(ex)}")