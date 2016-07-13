#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import os

from send2kindle.core.email_kindle import send2kindle
from send2kindle.core.user_information import *



APP_DESC="""
A Command Line Tool for sending mobi,aw3,pdf files to kindle
"""

def parse():
    parser=argparse.ArgumentParser(description=APP_DESC)
    # parser.add_argument('-c','--config',dest='user_information',
    #                     nargs=4,help='Set user name,Useremail,Password and kindle email')
    parser.add_argument('-u',dest='Push_user',help='appoint user to push file')
    parser.add_argument('-p',nargs='+',dest='Files',
                        help='Push files to kindle')
    parser.add_argument('-r',dest='Remove_user',
                        help='Remove user account')
    parser.add_argument('-l',dest='List_user',
                        const=False,nargs='?',
                        help='list user information')
    parser.add_argument('-c',dest='Config',nargs=4,metavar=('User_name','User_email',
                                                         'User_password','User_kindle'),
                        help='Add a user')
    args=parser.parse_args()
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
        assert len(args)==1
        list_users(args['List_user'])
    elif 'Files' in args:
        assert 'Push_user' in args
        send2kindle(args['Push_user'],args['Files'])



def main():
    args=parse()
    args=filter_args(args)
    process_args(args)

if __name__ == '__main__':
    main()
