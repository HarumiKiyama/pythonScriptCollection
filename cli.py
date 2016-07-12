#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import os

from email_kindle import SendMobi2Kindle
from user_information import *



APP_DESC="""
A Command Line Tool for sending mobi,aw3,pdf files to kindle
"""

def parse():
    parser=argparse.ArgumentParser(description=APP_DESC)
    # parser.add_argument('-c','--config',dest='user_information',
    #                     nargs=4,help='Set user name,Useremail,Password and kindle email')
    parser.add_argument('-u','--user',dest='Push_user',help='appoint user to push file')
    parser.add_argument('-p','--push',nargs='+',dest='Files',
                        help='Push files to kindle')
    parser.add_argument('-r','--remove',dest='Remove_user',
                        help='Remove user account')
    parser.add_argument('-l','--list',dest='List_user',
                        const=False,nargs='?',
                        help='list all of the users and their accounts')
    parser.add_argument('-c','--config',dest='Config',nargs=4,metavar=('User_name','User_email',
                                                         'User_password','User_kindle'),
                        help='Add a user')
    args=parser.parse_args(['-l','dsd','-c','2131','dsdjksd','13213','13123'])
    return vars(args)

def filter_args(args):
    return {i:args[i] for i in args if args[i] is not None}
def process_args(args):
    if 'Config' in args:
        assert len(args)==1
        make_dot_directory()
        save_user_information(*args['Config'])
    elif 'Remove_user' in args:
        assert len(args)==1
        del_user_information(args['Remove_user'])
    elif 'List_user' in args:
        pass
    elif 'Files' in args:
        pass


print(parse())
