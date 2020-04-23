#################################################################     Send Email Text  ###################################################################
#                               
#           INSTAL:             
#           Activate:                             
#           DEFINITION:             
#           DOCUMENTATION:      Download also Index.html
#                          
##########################################################################################################################################################



import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

email = EmailMessage()

#for who I want to send
email['from'] = 'Mk'  #to change
email['to'] = 'email@gmail.com' #to change
email['subject'] = 'You won 1,000,000 dollars!' #to change


#text I want to send
email.set_content('Hi how are you :D')

#protocol
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    #say hi to server
    smtp.ehlo()
    #incription
    smtp.starttls()

    #Source account - your mail and password
    smtp.login('my_@gmail.com', 'password') # To change: my_@hotmail.com password
    smtp.send_message(email)
    print('All good Boss!!')