import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
subject = "This is a test email" 
me = 'sender@sender.com'
you = 'recipient@recipient.com'
msg['Subject'] = subject
msg['From'] = me
msg['To'] = you

server = smtplib.SMTP('smtp-mail.outlook.com', 587)
server.starttls()
body = "Incident Description:1057512 Firewall Session Closed Severity: Unknown Device: NA Source IP: 8.8.8.8 Source Port: 80 Source Name: NA  Target IP: 192.168.0.1 Target Port: 4444 Target Name: testpc Occurrences: NA Occurred Time: 2021-06-05T00:42:06.922+08:00 Pick Up Time: 2021-06-16T15:51:12+08:00 Threat Analysis: NA Recommendation: NA"
msg.attach(MIMEText(body, 'plain'))
server.sendmail('noreply@xxx.com','receiver@yyy.com',msg.as_string())
server.quit()

