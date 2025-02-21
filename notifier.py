import smtplib
from email.message import EmailMessage

def send_email_notification(to_email, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = "your_email@example.com"
    msg["To"] = to_email

    with smtplib.SMTP("smtp.example.com") as server:
        server.login("your_email@example.com", "your_password")
        server.send_message(msg)

def notify_developer(defect_id):
    # Fetch developer's email from database (mocked here)
    developer_email = "developer@example.com"
    subject = f"Update Required for Defect ID: {defect_id}"
    body = f"Please update the defect report with ID: {defect_id}."
    send_email_notification(developer_email, subject, body)

def main():
    # Example: Notify a developer for a specific defect ID
    notify_developer(123)

if __name__ == "__main__":
    main()