import smtplib #simple mail transfer protocol library
from email.message import EmailMessage

while True:
    print("\n\nBefore signing in, make sure 'Access to less secure apps' was turned 'on' in google account\n")
    server = smtplib.SMTP("smtp.gmail.com", 587) #smtp sever name and port number(location)
    server.starttls() #asking smtp to trust (transport layer security)

    sender = input("Enter your email: ")
    password = input("Enter your password: ")
    receiver = input("Enter receiver's email address: ")
    subject = input("Subject: ")
    body = input("Body text: ")

    # header
    message = EmailMessage()
    message.set_content(body)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver
    try:
        server.login(sender,password)
        print("Logged in...")
        server.sendmail(sender, receiver, str(message))
        print("Email has been sent!")

    except smtplib.SMTPAuthenticationError: #This exception occured when "Acess to less secure app" is turned off
        print("unable to sign in")
        
    sendMore= input("\nWould you like to send more email to others? (y/n): ").lower()
    if sendMore != 'y' and sendMore != 'yes':
        print("Program is ended")
        break