#################################################################     Send Email   ###################################################################
#                               
#           INSTAL:             
#           Activate:                             
#           DEFINITION:             
#           DOCUMENTATION:      Download also Index.html
#                          
############################################################################################################################################################


import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

#para podermos trocar os nomes com $
from string import Template

#Tipo os path
from pathlib import Path

#access the html file
html = Template(Path('index.html').read_text())

email = EmailMessage()

#for who I want to send
email['from'] = 'Mk'  #to change
email['to'] = 'email@gmail.com' #to change
email['subject'] = 'You won 1,000,000 dollars!' #to change

email.set_content(html.substitute({'name': 'Tony'}), 'html') #Tony - to change

#protocol
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    #say hi to server
    smtp.ehlo()
    #incription
    smtp.starttls()

    #Source account - your mail and password
    smtp.login('my_@hotmail.com', 'password') # To change: my_@hotmail.com password
    smtp.send_message(email)
    print('All good Boss!!')
