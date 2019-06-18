import smtplib
from email.mime.text import MIMEText
from email.header import Header
mail_host = 'smtp.qq.com' #设置服务器
mail_user = '1132424753@qq.com' #qq邮箱账户
mail_pass = 'ksnrtofxifkbhcdc' #密码,授权码
sender = '1132424753@qq.com'
message = MIMEText('python发送邮件')  #正文,如html格式MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header('来源某个网站','utf-8')
subject = '消息推送'
message['Subject'] = Header(subject,'utf-8')


def send_email(recivers): #receivers接受者,可以是列表形式[邮箱地址,]
    try:
        # smtpObj = smtplib.SMTP()
        # smtpObj.connect(mail_host,465) #25 smtp的端口号 162是25,qq的则是465
        stmpObj = smtplib.SMTP_SSL(mail_host,465)  #可能需要安全认证
        # smtpObj.login(mail_user,mail_pass)
        # smtpObj.sendmail(sender,'1132424753@qq.com',message.as_string())
        stmpObj.login(sender, mail_pass)
        stmpObj.sendmail(sender, recivers, message.as_string())
    except smtplib.SMTPException as e:
        print("Error: 邮件发送失败 ",e)





