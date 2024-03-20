import smtplib
from email.mime.text import MIMEText

def send_news_email(news_data, recipient_email):
    sender_email = "jahongirraxmatjonov18@gmail.com@gmail.com"
    sender_password = "wpsj zier fwwc yrla"

    subject = news_data.get('title', 'No Title')
    description = news_data.get('description', 'No Description')
    url = news_data.get('url', 'No URL')

    message = f"Title: {subject}\nDescription: {description}\nURL: {url}"

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Email muvaffaqiyatli yuborildi!")
    except Exception as e:
        print(f"Email yuborishda xatolik: {e}")
