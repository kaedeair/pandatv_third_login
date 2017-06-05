# coding:utf-8

import sys
import re


def LongToInt(value):  # 由于int+int超出范围后自动转为long型，通过这个转回来
    if isinstance(value, int):
        return int(value)
    else:
        return int(value & sys.maxint)


def LeftShiftInt(number, step):  # 由于左移可能自动转为long型，通过这个转回来
    if isinstance((number << step), long):
        return int((number << step) - 0x200000000L)
    else:
        return int(number << step)


def getOldGTK(skey):
    a = 5381
    for i in range(0, len(skey)):
        a = a + LeftShiftInt(a, 5) + ord(skey[i])
        a = LongToInt(a)
    return a & 0x7fffffff


def getNewGTK(p_skey, skey, rv2):
    b = p_skey or skey or rv2
    a = 5381
    for i in range(0, len(b)):
        a = a + LeftShiftInt(a, 5) + ord(b[i])
        a = LongToInt(a)
    return a & 0x7fffffff

def get_tk2(cookieStr):
# @1h4BB3B54 804BF877775DC07D0B313E9BC345C0C10A8DC211948584EB47 1081244980
# cookieStr = ' RK=qKGLSRdfW/; pgv_pvi=3284304896; pac_uid=1_530959754; pgv_pvid=4075368924; o_cookie=530959754; pgv_si=s7067778048; _qpsvr_localtk=0.22683323386035803; rv2=800D50959F25324051158CADEBFC969C174BF319CE16DF09D5; property20=9F5571A6DFF676E7EC09CC8DC645195C30EDC67BF4A051DBF2EB034218C99B3D965C111906CF14B1; pgv_info=ssid=s7962560590; ui=BF268E98-AE17-4E73-9CEA-648A7A49D27D; ptui_loginuin=531158472; ptisp=ctc; ptcz=1fc31601df04da48cfd3b0feb7ac5aa4170d40c67d726b8f7bd621570c3427fe; pt2gguin=o0531158472; uin=o0531158472; skey=@yJIhy3mTu; p_uin=o0531158472; p_skey=qMspJ7KJGMGkHXB8RWOMAMsEWcUmX2H8*cYjsDNthOw_; pt4_token=kx-4t9tmzU5rUI6fhEe*z-SD-XOhe-l8ms1-jRNtS*c_'
    if re.search(r'p_skey=(?P<p_skey>[^;]*)', cookieStr):
        p_skey = re.search(r'p_skey=(?P<p_skey>[^;]*)', cookieStr).group('p_skey')
    else:
        p_skey = None
    if re.search(r'skey=(?P<skey>[^;]*)', cookieStr):
        skey = re.search(r'skey=(?P<skey>[^;]*)', cookieStr).group('skey')
    else:
        skey = None
    if re.search(r'rv2=(?P<rv2>[^;]*)', cookieStr):
        rv2 = re.search(r'rv2=(?P<rv2>[^;]*)', cookieStr).group('rv2')
    else:
        rv2 = None
def get_tk(cookieJar):
# @1h4BB3B54 804BF877775DC07D0B313E9BC345C0C10A8DC211948584EB47 1081244980
# cookieStr = ' RK=qKGLSRdfW/; pgv_pvi=3284304896; pac_uid=1_530959754; pgv_pvid=4075368924; o_cookie=530959754; pgv_si=s7067778048; _qpsvr_localtk=0.22683323386035803; rv2=800D50959F25324051158CADEBFC969C174BF319CE16DF09D5; property20=9F5571A6DFF676E7EC09CC8DC645195C30EDC67BF4A051DBF2EB034218C99B3D965C111906CF14B1; pgv_info=ssid=s7962560590; ui=BF268E98-AE17-4E73-9CEA-648A7A49D27D; ptui_loginuin=531158472; ptisp=ctc; ptcz=1fc31601df04da48cfd3b0feb7ac5aa4170d40c67d726b8f7bd621570c3427fe; pt2gguin=o0531158472; uin=o0531158472; skey=@yJIhy3mTu; p_uin=o0531158472; p_skey=qMspJ7KJGMGkHXB8RWOMAMsEWcUmX2H8*cYjsDNthOw_; pt4_token=kx-4t9tmzU5rUI6fhEe*z-SD-XOhe-l8ms1-jRNtS*c_'

    # p_skey = cookieJar.get('p_skey')
    skey = cookieJar.get('skey')
    # else:
    #     p_skey = None
    # if re.search(r'skey=(?P<skey>[^;]*)', cookieStr):
    #     skey = re.search(r'skey=(?P<skey>[^;]*)', cookieStr).group('skey')
    # else:
    #     skey = None
    # if re.search(r'rv2=(?P<rv2>[^;]*)', cookieStr):
    #     rv2 = re.search(r'rv2=(?P<rv2>[^;]*)', cookieStr).group('rv2')
    # else:
    #     rv2 = None
# print p_skey
# print skey
# print rv2
    return getOldGTK(skey)
# print getNewGTK(p_skey, skey, rv2)
if __name__=='__main__':
    cookieStr = ' RK=qKGLSRdfW/; pgv_pvi=3284304896; pac_uid=1_530959754; pgv_pvid=4075368924; o_cookie=530959754; pgv_si=s7067778048; _qpsvr_localtk=0.22683323386035803; rv2=800D50959F25324051158CADEBFC969C174BF319CE16DF09D5; property20=9F5571A6DFF676E7EC09CC8DC645195C30EDC67BF4A051DBF2EB034218C99B3D965C111906CF14B1; pgv_info=ssid=s7962560590; ui=BF268E98-AE17-4E73-9CEA-648A7A49D27D; ptui_loginuin=531158472; ptisp=ctc; ptcz=1fc31601df04da48cfd3b0feb7ac5aa4170d40c67d726b8f7bd621570c3427fe; pt2gguin=o0531158472; uin=o0531158472; skey=@yJIhy3mTu; p_uin=o0531158472; p_skey=qMspJ7KJGMGkHXB8RWOMAMsEWcUmX2H8*cYjsDNthOw_; pt4_token=kx-4t9tmzU5rUI6fhEe*z-SD-XOhe-l8ms1-jRNtS*c_'

    print get_tk2(cookieStr)