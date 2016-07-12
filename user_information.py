# -*- coding: utf-8 -*-
import pickle
import os

def make_dot_directory():
    try:
        os.makedirs(r'~/.kindle')
    except:
        pass

def save_user_information(user,user_email,user_password,user_kindle):
    user_information={'From':user_email,
                 'To':user_kindle,
                 'Password':user_password}
    with open('~/.kindle/%s'%user,'wb') as fp:
        pickle.dump(user_information,fp)

def get_user_information(user):
    with open('~/.kindle/%s'%user,'rb') as fp:
        return pickle.load(fp)

def del_user_information(user):
    os.remove('~/.kindle/%s'%user)

def list_users(users):
    if user==False:
        # show all user information
        files=os.walk('~/.kindle').next()[-1]
    else:
        with open('~/.kindle/%s'%user) as fp:
            pickle.load(fp)
            

