import requests


def proxy_check(proxy):
    proxy_check_url = "http://www.panda.tv/"
    ip_check, port_check, user, password=proxy
    try:

        proxy_ip = {'http': "socks5://%s:%s@%s:%s"%(user,password,ip_check,port_check,)}
        # print proxy_ip
        html2 = requests.get(url=proxy_check_url,proxies=proxy_ip,timeout=3)
        # print html2
        if html2.status_code == 200 and 'panda' in html2.text :
            print 'add_ip:', ip_check, port_check,user,password
            return True
        return False

    except Exception,e:
        pass
        print e.message


if __name__=='__main__':
    for line in open('s5xu.txt').readlines():
        item = line.strip().split('----')
        proxy_check(item)