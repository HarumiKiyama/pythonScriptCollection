#!/usr/bin/env python
# -*- coding: utf-8 -*-

import poplib
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from send2kindle.core.user_information import get_user_information
import os


class SendMobi2Kindle:
    def __init__(self, user):
        "init instance with person_information"
        personal_information = self.get_personal_information(user)
        assert 'From' in personal_information, 'No such user'
        assert 'To' in personal_information, 'No such user'
        assert 'Password' in personal_information, 'No such user'
        self.password = personal_information.get('Password')
        self.user_email = personal_information.get('From')
        self.kinle_email = personal_information.get('To')
        self.smtp = self.config_smtp()

    @staticmethod
    def get_personal_information(user):
        """return {"From":'xxx@xxx',"To":'xxx@xxx',"Password":"xxxxx"}
        """
        return get_user_information(user)

    def email_content(self, file_path):
        """add attach file and email content
        :param file_path:
        :return msg: email message be sent later
        """
        msg = MIMEMultipart('related')
        part = MIMEText('holyshit')
        msg['Subject'] = 'File that I want to read'
        msg['From'] = self.user_email
        msg['To'] = self.kinle_email
        if file_path.startswith('~'):
            file_path=os.path.expanduser(file_path)
            assert file_path is not None, 'You should set your $HOME variable'
        assert os.access(file_path,os.F_OK),'No such file'
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
        if '@hotmail' in self.user_email:
            address = 'smtp.live.com'
        else:
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
        single_file = os.path.split(file_path)[-1]
        print('Successfully push %s to kindle' % single_file)

    def end_smtp_server(self):
        """
        Quit smtp
        """
        self.smtp.quit()
        print('Thank you for using my service')


def send2kindle(user, files):
    client = SendMobi2Kindle(user)
    if files == []:
        print('There are no such file exist')
    else:
        for i in files:
            client.send2kindle(i)
        # map(client.send2kindle, files)
    client.end_smtp_server()
