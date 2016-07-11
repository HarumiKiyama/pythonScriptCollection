#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import os

from email_kindle import SendMobi2Kindle

APP_DESC="""
A Command Line Tool for sending mobi,aw3,pdf files to kindle
"""

def parse():
    parser=argparse.ArgumentParser(description=APP_DESC)
    parser.add_argument('file-paths',metavar='files',type=str,
                        help='files send to kindle')
    parser.add_argument('Useremail',metavar='email',type=str,
                        help='User email account')
    parser.add_argument('Password',metavar='passwd',type=str,
                        help='User email passward')
    parser.add_argument('Kinlde email',metavar='kindle',type=str,
                        help='Kindle email account')
    parser.add_argument('-s',action='store_const', const=sum,
                        help='Set user name,kindle email,Useremail and Password')
    args=parser.parse_args()

if __name__ == '__main__':
    main()
