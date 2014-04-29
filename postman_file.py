import smtplib
import getpass
question = raw_input('if you want to send an email, type yes, if you want to quit, type no\n')
while question != 'no':

    
        try:
        
        
            sender = raw_input("from:\n")
            senders_pwd = getpass.getpass("password:\n")
            recipient = raw_input("to:\n")
            print 'ok, now compile your message:'
            subject = raw_input("subject:\n")
            body = raw_input("your message:\n") + '\n\nsent via listonosz ;) '
            message = "From: %s \nTo: %s \nSubject: %s\n%s" %(sender, recipient, subject,body)
            print message
        
            server = smtplib.SMTP("smtp.gmail.com",587)
            server.ehlo()
            print 'ok'
            server.starttls()
            print 'ok'
            server.ehlo()
            server.login(sender,senders_pwd)
            print 'logged'
            server.sendmail(sender,recipient,message)
            print 'sent'
            server.close()
            print 'message sent, server closed'
        except:
            print 'failed to send'
        question = raw_input('do you want me to send another mail? yes/no?\n')
quit()
import platform
if platform.system()=='Windows':
    input()
          
