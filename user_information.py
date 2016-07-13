# -*- coding: utf-8 -*-
import pickle
import os


def make_dot_directory():
    try:
        os.makedirs(r'.kindle')
    except:
        pass


def save_user_information(user, user_email, user_password, user_kindle):
    user_information = {'From': user_email,
                        'To': user_kindle,
                        'Password': user_password}
    with open('.kindle/%s' % user, 'wb') as fp:
        pickle.dump(user_information, fp)
    print('User information save successfully')


def get_user_information(user):
    if os.access('.kindle/%s' % user, os.F_OK):
        with open('.kindle/%s' % user, 'rb') as fp:
            return pickle.load(fp)
    else:
        print('%s does not exsit' % user)


def del_user_information(user):
    os.remove('.kindle/%s' % user)
    print("successfully remove %s's information" % user)


def list_users(user):
    if user == False:
        # show all user information
        files = tuple(os.walk('.kindle'))[0][-1]
        for i in files:
            print(i)
    else:
        user_information = get_user_information(user)
        if user_information is None:
            return
        print('User name:   ' + user)
        print('User email:  ' + user_information['From'])
        print('User kindle  ' + user_information['To'])
