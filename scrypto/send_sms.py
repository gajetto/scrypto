# -*- coding: utf-8 -*-
#/usr/bin/env python
#/usr/bin/python
#/usr/local/bin/python
# python

import os
from twilio.rest import Client

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_ACCOUNT_TOKEN")
cellphone = os.environ.get("CELLPHONE")
twiliophone = os.environ.get("TWILIOPHONE")
client = Client(account_sid, auth_token)
client.messages.create(from_=twiliophone,
                       to=cellphone,
                       body='message basique test #1')
