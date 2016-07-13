# -*- coding: utf-8 -*-
import pickle
import os


def make_dot_directory():
    assert os.path.expanduser('~'),'You should set your $HOME variable'
    try:
        os.makedirs(os.path.expanduser('~/.kindle'))
    except:
        pass


def save_user_information(user, user_email, user_password, user_kindle):
    user_information = {'From': user_email,
                        'To': user_kindle,
                        'Password': user_password}
    with open(os.path.expanduser('~/.kindle')+'/%s' % user, 'wb') as fp:
        pickle.dump(user_information, fp)
    print('User information save successfully')


def get_user_information(user):
    if os.access(os.path.expanduser('~/.kindle')+'/%s' % user, os.F_OK):
        with open(os.path.expanduser('~/.kindle')+'/%s' % user, 'rb') as fp:
            return pickle.load(fp)
    else:
        print('%s does not exsit' % user)


def del_user_information(user):
    if os.access(os.path.expanduser('~/.kindle')+'/%s' % user, os.F_OK):
        os.remove(os.path.expanduser('~/.kindle')+'/%s' % user)
        print("successfully remove %s's information" % user)
    else:
        print('No such user')


def list_users(user):
    if user == False:
        # show all user information
        files = tuple(os.walk(os.path.expanduser('~/.kindle')))[0][-1]
        if len(files)==0:
            print('There is no user')
        else:
            for i in files:
                print(i)
    else:
        user_information = get_user_information(user)
        if user_information is None:
            return
        print('User name:   ' + user)
        print('User email:  ' + user_information['From'])
        print('User kindle  ' + user_information['To'])
