from email import message
import smtplib, ssl

def send_email(email, prodlink, price):
    port = 465
    password = 'CTZ9npn5acq4ukb@kxq'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
        server.login("notifier.here@gmail.com", password)
        message = "Price for your product has dropped to " + price + ". Go to the product page here -> " + prodlink
        server.sendmail("notifier.here@gmail.com", email, message)