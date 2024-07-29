import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config

def send_email(user, alert):
    print("Trigger")
    msg = MIMEMultipart()
    msg['From'] = Config.MAIL_USERNAME
    msg['To'] = user.email
    msg['Subject'] = f"Price Alert for {alert.cryptocurrency}"
    
    body = f"Your price alert for {alert.cryptocurrency} at ${alert.target_price} has been triggered."
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP(Config.MAIL_SERVER, Config.MAIL_PORT)
        server.starttls()
        server.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(Config.MAIL_USERNAME, user.email, text)
        server.quit()
        print(f"Email sent to {user.email}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")