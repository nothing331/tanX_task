import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config

def send_email(user, alert):
    print(f"Attempting to send email for alert: {alert.cryptocurrency} at ${alert.target_price}")
    
    # Check if user email is valid
    if not user.email:
        print("Error: User email is missing or invalid")
        return
    
    msg = MIMEMultipart()
    msg['From'] = Config.MAIL_USERNAME
    msg['To'] = user.email
    msg['Subject'] = f"Price Alert for {alert.cryptocurrency}"
   
    body = f"Your price alert for {alert.cryptocurrency} at ${alert.target_price} has been triggered."
    msg.attach(MIMEText(body, 'plain'))
   
    try:
        # if not all([Config.MAIL_SERVER, Config.MAIL_PORT, Config.MAIL_USERNAME, Config.MAIL_PASSWORD]):
        #     raise ValueError("SMTP configuration is incomplete")

        #For the submission sake I am not using an .env file to keep my id's and passwords so that it runs when you fetch the repo is cloned

        if not all([Config.MAIL_SERVER, Config.MAIL_PORT, "nothinggame4@gmail.com", "vvwjipjhofkmotup"]):
            raise ValueError("SMTP configuration is incomplete")
        
        server = smtplib.SMTP(Config.MAIL_SERVER, Config.MAIL_PORT)
        server.starttls()
        server.login("nothinggame4@gmail.com", "vvwjipjhofkmotup")
        text = msg.as_string()
        server.sendmail("nothinggame4@gmail.com", user.email, text)
        server.quit()
        print(f"Email sent successfully to {user.email}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        print(f"SMTP Server: {Config.MAIL_SERVER}")
        print(f"SMTP Port: {Config.MAIL_PORT}")
        print(f"SMTP Username: nothinggame4@gmail.com")
        print(f"User Email: {user.email}")
        # Don't print the password for security reasons