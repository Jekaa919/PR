import smtplib
from email.mime.text import MIMEText


def send_email(sender_email, recipient_email, subject, message):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, "0dLg2V0PUgU5fCPtXGCi")
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")


if __name__ == "__main__":
    send_email("jekaa919@gmail.com", "jekaa919@gmail.com", "Test Subject", "test")
