#-*- encoding:utf-8 -*-

import re
import email
import poplib

import falcon


class EmailCode:

    def on_get(self, req, resp):
        hostname = 'pop.mail.ru'
        user = req.get_param('user')
        passwd = req.get_param('passwd')
        if not user or not passwd:
            result = {'status': 'failed', 'reason':'no user or passwd provided'}
        else:
            p = poplib.POP3_SSL('pop.mail.ru')
            try:
                p.user(user) 
                p.pass_(passwd)
            except poplib.error_proto:
                result = {'status': 'failed', 'reason':'login failed'}

            else:
                response, listings, octets = p.list()
                last_email = listings[-1]
                number, size = last_email.split()
                number = bytes.decode(number)
                response, lines, octets = p.top(number , 0)
                lines = list(map(lambda x: bytes.decode(x), lines))
                message = email.message_from_string('\n'.join(lines))
                title = message['Subject']
                if 'Facebook' in title:
                    m = re.search(r'(\d+)', title)
                    if m:
                        code = m.group(1)
                        result = {'status': 'ok', 'code': code}
                    else:
                        result = {'status': 'failed', 'reason': 'no match'}
                else:
                    result = {'status': 'failed', 'reason': 'no match'}
        resp.media = result

api = falcon.API()
api.add_route('/api/code', EmailCode())
api.add_route
