#!/usr/bin/env python
# -*- coding: utf-8 -*-

import poplib
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from user_information import get_user_information
import os


class SendMobi2Kindle:
    def __init__(self):
        "init instance with person_information"
        personal_information=self.get_personal_information(user,kindle)
        assert 'From' in personal_information
        assert 'To' in personal_information
        assert 'Password' in personal_information
        self.password = personal_information.get('Password')
        self.user_email = personal_information.get('From')
        self.kinle_email = personal_information.get('To')
        self.smtp = self.config_smtp()

    @staticmethod
    def get_personal_information(user):
        """return {"From":'xxx@xxx',"To":'xxx@xxx',"Password":"xxxxx"}
        """
        user_account=get_user_information(user)
        # user_account={'From':'lucius0720@163.com',
        #               'Password':'wlc123456'}
        # kindle={'To':'lucius0720@kindle.cn'}
        kindle.update(user_account)
        return kindle

    def email_content(self, file_path):
        """add attach file and email content
        :param file_path:
        :return msg: email message be sent later
        """
        msg = MIMEMultipart('related')
        part = MIMEText('holyshit')
        msg['Subject'] = 'My_work'
        msg['From'] = self.user_email
        msg['To'] = self.kinle_email
        with open(file_path, 'rb') as fp:
            attach = MIMEApplication(fp.read())
            attach[
                'Content-Disposition'] = 'attachment;filename="%s"' % os.path.split(
                    file_path)[-1]
            msg.attach(attach)
        msg.attach(part)
        return msg

    def config_smtp(self):
        """
        :return : smtp
        """
        address = 'smtp.' + self.user_email.split('@')[-1]
        smtp = smtplib.SMTP(address)
        smtp.login(self.user_email, self.password)
        return smtp

    def send2kindle(self, file_path):
        """
        Send email to kindle
        """
        smtp = self.smtp
        msg = self.email_content(file_path)
        smtp.sendmail(self.user_email, self.kinle_email, msg.as_string())

    def end_smtp_server(self):
        """
        Quit smtp
        """
        self.smtp.quit()
