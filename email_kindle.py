#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using python and my hotmail account to send mobi, aw or pdf file to my kindle"""
import poplib
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import os


def get_personal_information():
    with open('confidential.txt', 'r') as fp:
        return eval(fp.read())


PersonalInformation = get_personal_information()


def email_content(file_path):
    msg = MIMEMultipart('related')
    part = MIMEText('holyshit')
    msg['Subject'] = 'My_work'
    msg['From'] = PersonalInformation['From']
    msg['To'] = PersonalInformation['To']
    with open(file_path, 'rb') as fp:
        attach = MIMEApplication(fp.read())
        attach['Content-Disposition'] = 'attachment;filename="%s"' % os.path.split(file_path)[-1]
        msg.attach(attach)
    msg.attach(part)
    return msg


def config_smtp(address):
    address = 'smtp.' + address
    smtp = smtplib.SMTP(address)
    smtp.login(PersonalInformation['From'], PersonalInformation['Password'])
    return smtp


def send2kindle(file_path, address='163.com'):
    smtp = config_smtp(address)
    msg = email_content(file_path)
    smtp.sendmail(PersonalInformation['From'], PersonalInformation['To'],
                  msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    from time import clock
    start = clock()
    # send2kindle('text.txt','live.com')
    send2kindle('text.txt')
    finish = clock()
    print(finish - start)
