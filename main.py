import smtplib

# To use gmail: You must turn on 2FA through settings and then make an app password. Set MY_PASSWORD as the app password
MY_EMAIL = "INSERT EMAIL HERE"
MY_PASSWORD = "INSERT PASSWORD TO ABOVE EMAIL HERE"

with open("sampleInput.txt", mode='r') as input:
    # splits the lines in our sampleInput.txt file into lists to create a nested list structure of the whole document
    clients = list(input.read().split("\n"))

    for i in range(len(clients)):
        # we split each individual nested list by commas to separate the receiver's name from the email address
        x = clients[i].split(",")

        # this opens our email template  and replaces the placeholder with the name of the specific client
        with open("template.txt", mode='r') as temp:
            template = temp.read()
            custom_email = template.replace('[Client]', x[0])

        # Change 'Automated Marketing Emails' below to whatever you want the subject line to be
        # this uses smtplib.SMTP to send our custom created email from our email address to the receiver's email
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=x[1],
                msg=f"Automated Marketing Emails\n\n{custom_email}"
            )
