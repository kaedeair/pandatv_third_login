#coding=utf-8
import requests
import hashlib
import re
import os,tempfile
import rsa
from rk import RClient
import urllib
import tea
import binascii
import random
import base64
import time
import json
from get_gtk import get_tk
class Login():

    def __init__(self,user,pwd,proxy,rk_username,rk_password):
        self.user = user
        self.pwd = pwd
        self.rk_username=rk_username
        self.rk_password=rk_password
        if proxy is None:
            self.proxy=None
        elif len(proxy)==4:
            self.proxy={
                'http': "socks5://%s:%s@%s:%s"%(proxy[2],proxy[3],proxy[0],proxy[1]),
                'https': "socks5://%s:%s@%s:%s"%(proxy[2],proxy[3],proxy[0],proxy[1]),
            }
        else:
            self.proxy = {
                'http': "http://%s:%s" % ( proxy[0], proxy[1]),
                'https': "http://%s:%s" % ( proxy[0], proxy[1]),
            }
    session=requests.Session()

    appid='716027609'
    action='5-3-1495966725481'
    loginjumpurl='https://graph.qq.com/oauth/login_jump'
    feedbackurl='http://support.qq.com/write.shtml?fid=780&SSTAG=www.panda.tv.appidself.client_id'
    def fetch(self, url, data=None, **kw):
        if data is None:
            func = self.session.get
        else:
            kw['data'] = data
            func = self.session.post
        if kw.get('headers') is None:
            kw['headers']={}
        kw['headers']['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"

        return func(url,proxies=self.proxy,verify=False, timeout=10,**kw)

    def login(self):
        panda_url="https://u.panda.tv/third_login"
        g = self.fetch(panda_url, params={
            '__guid': "96554777.1847601958869270500.1492410605735.9417",
            '__plat': "pc_web",
            'pdftsrc': '{"os":"web","sessionId":"1496650458947-8936969","smid":"070ef069-9910-4ea5-a3a8-d2b0da34c818","canvas":"7d2223610ce73aebea7dadbddc80da78","h":1080,"ua":"de392fc362e3bacf610ade71d0fb6ed1","w":1920}',
            'psrc': '',
            'redirect': "http://www.panda.tv/rucbind?href=http://www.panda.tv/",
            'type':4,

        },allow_redirects=False)

        login_url=g.headers['Location']
        if login_url[0:20]=="https://graph.qq.com":
            pass
        else:
            return -1
        # login_url="https://graph.qq.com/oauth/show?which=Login&display=pc&response_type=code&client_id=101343674&redirect_uri=https%3A%2F%2Fu.panda.tv%2Foauth_callback%3Fjp%3D%26redirect%3Dhttp%253A%252F%252Fwww.panda.tv%252Frucbind%253Fhref%253Dhttp%253A%252F%252Fwww.panda.tv%252F%26__plat%3Dpc_web%26plat%3Dpc_web%26__guid%3D96554777.1847601958869270500.1492410605735.9417%26guid%3D96554777.1847601958869270500.1492410605735.9417%26psrc%3D%26ip%3D115.55.203.18%26refer%3D%26pdft%3D%26pdftsrc%3D%257B%2522os%2522%253A%2522web%2522%252C%2522sessionId%2522%253A%25221496650458947-8936969%2522%252C%2522smid%2522%253A%2522070ef069-9910-4ea5-a3a8-d2b0da34c818%2522%252C%2522canvas%2522%253A%25227d2223610ce73aebea7dadbddc80da78%2522%252C%2522h%2522%253A1080%252C%2522ua%2522%253A%2522de392fc362e3bacf610ade71d0fb6ed1%2522%252C%2522w%2522%253A1920%257D%26__version%3D%26version%3D%26third%3D1%26type%3D4%26port%3D443%26method%3DGET%26csrfstate%3Dc52908e4fef11b998ded79c3a75fc0c0&scope=get_user_info"
        self.client_id = re.findall('&client_id=(.*?)\&', login_url)[0]
        self.redirect_url=urllib.unquote(re.findall('&redirect_uri=(.*?)\&', login_url)[0])
        print self.redirect_url

        self.xloginurl = 'http://xui.ptlogin2.qq.com/cgi-bin/xlogin'
        self.fetch(login_url)
        g = self.fetch(self.xloginurl, params={
            'appid': self.appid,
            'daid':383,
            'style': 33,
            'login_text': '授权并登录',
            'hide_title_bar': 1,
            'hide_border':1,
            'target': 'self',
            's_url': self.loginjumpurl,
            'pt_3rd_aid': self.client_id,
            'pt_feedback_link': self.feedbackurl,
        }).text

        self.checkurl2 = 'http://check.ptlogin2.qq.com/check'

        g = self.fetch(self.checkurl2, params={
            'regmaster': '',
            'pt_tea': 2,
            'pt_vcode': 1,
            'uin': self.user,
            'appid': self.appid,
            'js_ver': 10220,
            'js_type': 1,
            'login_sig': self.session.cookies['pt_login_sig'],
            'u1': self.loginjumpurl,
            'r':str(random.random()),
            'pt_uistyle':'40',
            'pt_jstoken':2811643906
        }).text
        v = re.findall('\'(.*?)\'', g)
        vcode = v[1]
        uin = v[2]
        print vcode,uin

        self.loginurl2 = 'https://ssl.ptlogin2.qq.com/login'
        ticket=None
        v1=None
        if v[0] == '1':  # 需要校验码
            ticket,vcode = self.getVerifyCode(vcode)  # 获得校验码
            # print ticket,vcode
        g = self.fetch(self.loginurl2, params={
            'u': self.user,
            'verifycode': vcode,
            'pt_vcode_v1': v[0],
            'pt_verifysession_v1': ticket or self.session.cookies['ptvfsession'],
            'p': self.pwdencode(vcode, uin, self.pwd),
            'pt_randsalt': 0,#2 if v[0]=='1'else 2,
            'pt_jstoken':'2811643906',
            'u1': self.loginjumpurl,
            'ptredirect': 0,
            'h': 1,
            't': 1,
            'g': 1,
            'from_ui': 1,
            'ptlang': 2052,
            'action': self.action,
            'js_ver': 10220,
            'js_type': 1,
            'login_sig': self.session.cookies['pt_login_sig'],
            'pt_uistyle': 40,
            'aid': self.appid,
            'daia':383,
            'pt_3rd_aid': self.client_id,
            # 'pt_guid_sig':'382CC819CE7C860C023B83C03FA9F856B7B63B552C19AA35147AC8E741EC2C07919BE1248C83045B' or self.session.cookies['pt_guid_sig']
        })
        v = re.findall('\'(.*?)\'', g.text)
        if v[0]!='0':
            print v[4]
            return -2
        self.appsupporturl = 'https://graph.qq.com/oauth2.0/authorize'

        g = self.fetch(self.appsupporturl, data={
            'response_type': 'code',
            'client_id': self.client_id,
            'redirect_uri': self.redirect_url,
            'scope': 'get_user_info',
            'state': '',
            'switch': '',
            'src': 1,
            'update_auth': 1,
            'openapi':'80901010',
            'g_tk':get_tk(self.session.cookies),
            'auth_time': int(time.time()),
            'ui':'BF268E98-AE17-4E73-9CEA-648A7A49D27D'
        })
        # 正确的话返回{"ret":0,"msg":"成功"}
        result=[]
        cookie=self .session.cookies
        for name in ('I','M','R'):
            result.append(name+'='+cookie[name])
        return '; '.join(result)

    def fromhex(self, s):
        # Python 3: bytes.fromhex
        return bytes(bytearray.fromhex(s))

    # pip install rsa
    pubKey = rsa.PublicKey(int(
        'F20CE00BAE5361F8FA3AE9CEFA495362'
        'FF7DA1BA628F64A347F0A8C012BF0B25'
        '4A30CD92ABFFE7A6EE0DC424CB6166F8'
        '819EFA5BCCB20EDFB4AD02E412CCF579'
        'B1CA711D55B8B0B3AEB60153D5E0693A'
        '2A86F3167D7847A0CB8B00004716A909'
        '5D9BADC977CBB804DBDCBA6029A97108'
        '69A453F27DFDDF83C016D928B3CBF4C7',
        16
    ), 3)

    def pwdencode(self, vcode, uin, pwd):
        # uin is the bytes of QQ number stored in unsigned long (8 bytes)
        salt = uin.replace(r'\x', '')
        h1 = hashlib.md5(pwd.encode()).digest()
        s2 = hashlib.md5(h1 + self.fromhex(salt)).hexdigest().upper()
        rsaH1 = binascii.b2a_hex(rsa.encrypt(h1, self.pubKey)).decode()
        rsaH1Len = hex(len(rsaH1) // 2)[2:]
        hexVcode = binascii.b2a_hex(vcode.upper().encode()).decode()
        vcodeLen = hex(len(hexVcode) // 2)[2:]
        l = len(vcodeLen)
        if l < 4:
            vcodeLen = '0' * (4 - l) + vcodeLen
        l = len(rsaH1Len)
        if l < 4:
            rsaH1Len = '0' * (4 - l) + rsaH1Len
        pwd1 = rsaH1Len + rsaH1 + salt + vcodeLen + hexVcode
        saltPwd = base64.b64encode(
            tea.encrypt(self.fromhex(pwd1), self.fromhex(s2))
        ).decode().replace('/', '-').replace('+', '*').replace('=', '_')
        print saltPwd
        return saltPwd

    imgurl = 'https://ssl.captcha.qq.com/cap_union_new_gettype'

    def getVerifyCode(self, vcode):
        g = self.fetch(self.imgurl, params={
            'aid': self.appid,
            'apptype': 2,
            'asig': '',
            'callback': '',
            'cap_cd':vcode,
            'captype': '',
            'clientype': 2,
            'curenv': 'inner',
            'disturblevel': '',
            'lang': 2052,
            'protocol':'https',
            'uid': self.user
        })

        sess=json.loads(g.text[1:-1])['sess']

        for i in range(5):
            vsigurl="https://ssl.captcha.qq.com/cap_union_new_getsig"


            g = self.fetch(vsigurl,params={
                'aid': self.appid,
                'apptype': 2,
                'asig':'',
                'cap_cd': vcode,
                'captype': '',
                'clientype': 2,
                'curenv': 'inner',
                'disturblevel': '',
                'fb':1,
                'lang':2052,
                'noBorder':'noBorder',
                'protocol':'https',
                'rand':random.random(),
                'chartype':1,
                'rnd':628476,
                'sess':sess,
                'showtype':'embed',
                'theme':'',
                'uin': self.user,
            }
                )

            header_img={
                "Connection": "keep-alive",
                "Accept": "image/webp,image/*,*/*;q=0.8",
                 "Accept-Encoding": "gzip, deflate, sdch, br",
            }

            vsig=json.loads(g.text)['vsig']
            imgurl='https://ssl.captcha.qq.com/cap_union_new_getcapbysig'
            r = self.fetch(imgurl, headers=header_img,params={
                'aid': self.appid,
                'apptype': 2,
                'asig': '',
                'cap_cd': vcode,
                'captype': '',
                'clientype': 2,
                'curenv': 'inner',
                'disturblevel': '',
                'fb': 1,
                'ischartype':1,
                'lang': 2052,
                'noBorder': 'noborder',
                'protocol': 'https',
                'rand': random.random(),

                'rnd': 628476,
                'sess': sess,
                'showtype': 'embed',
                'theme': '',
                'uin': self.user,
                'vsig':vsig
            }
                           )

            tmp = tempfile.mkstemp(suffix='.jpg')
            os.write(tmp[0], r.content)
            os.close(tmp[0])
            # os.startfile(tmp[1])

            rc = RClient(self.rk_username, self.rk_password)
            im = open(tmp[1], 'rb').read()
            result = rc.rk_create(im, 3040)
            ans=result['Result']
            # print result['Result']


            # ans = raw_input('Verify code: ')


            os.remove(tmp[1])
            submiturl="https://ssl.captcha.qq.com/cap_union_new_verify?random=1496648280056"
            r = self.fetch(submiturl, data={
                'abaeea':"",#
                'aid': self.appid,
                'ans':ans,
                'apptype': 2,
                'asig': '',
                'cap_cd': vcode,
                'captype': '',
                'clientype': 2,
                'curenv': 'inner',
                'disturblevel': '',
                'fb': 1,
                'lang': 2052,
                'noBorder': 'noborder',
                'protocol': 'https',
                'rand': random.random(),

                'rnd': 713246,
                'sess': sess,
                'showtype': 'embed',
                'subcapclass':0,
                'theme': '',
                'uin': self.user,
                'vsig': vsig
            }
                           )
            result=json.loads(r.text)
            if result["errMessage"]=="OK":
                return result["ticket"],result["randstr"]
            else:

                continue
        return None
if __name__=='__main__':
    proxy="42.239.225.235 38382 test 123456".split(' ')
    user="xxx"
    password="xxx"
    print Login(user,password,proxy,'tempuser','tempuser321').login()