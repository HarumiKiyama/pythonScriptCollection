#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using python and my hotmail account to send mobi, aw or pdf file to my kindle"""
import smtplib
from email.mime.text import MIMEText


def email_content(file_path):
    with open(file_path,'rb') as fp:
        fp=get_file('path')
        msg=MIMEText(fp.read())
        personal_information=('lucius0720@hotmail.com','*****',
        'lucius0720@kindle.cn')
        msg['Subject']='The contents of my book'
        msg['From']=personal_information[0]
        msg['To']=personal_information[2]


def send2kindle():
    pass
def main():
    my_information=crucial_information('lucius0720@hotmail.com','*****',
                                       'lucius0720@kindle.cn')


if __name__ == '__main__':
    main()
