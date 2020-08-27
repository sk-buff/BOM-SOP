#!/bin/python3

from hyper import HTTP20Connection, HTTPConnection
import sys

'''GET /search?q=456&qs=n&form=QBRE&sp=-1&pq=456&sc=8-3&sk=&cvid=E7682FAF6E344C20B3BB0F704A91DD70 HTTP/2
Host: cn.bing.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://cn.bing.com/search?q=123
Connection: keep-alive
Cookie: DUP=Q=ICy5YqxZB1uWSwcVLSNLcA2&T=399295592&A=2&IG=E7682FAF6E344C20B3BB0F704A91DD70; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=1CC9D2B4567F48B48BAB5666EFDCD066&dmnchg=1; SRCHUSR=DOB=20200825&T=1598440798000; _EDGE_V=1; MUID=147AE217C34B6C6E073BED26C2656D5D; MUIDB=147AE217C34B6C6E073BED26C2656D5D; SRCHHPGUSR=CW=2488&CH=533&DPR=1&UTC=480&DM=0&WTS=63734037598&HV=1598441195; ENSEARCH=BENVER=1; ULC=P=14258|8:1&H=14258|8:1&T=14258|8:1; _SS=SID=26531E714B6B6DCD376A11404A456C7F&bIm=021; _EDGE_S=mkt=zh-cn&SID=26531E714B6B6DCD376A11404A456C7F; ipv6=hit=1598444406088&t=4; _FP=hta=on; MUIDB=
Upgrade-Insecure-Requests: 1
TE: Trailers'''

browserHeader = {
    # 'Host': 'cn.bing.com',
    # 'user-agent': r'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
    'accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-Language': r'en-US,en;q=0.5'
    # 'Accept-Encoding': r'gzip, deflate, br'
}

'''GET /search?q=123 HTTP/2
> Host: cn.bing.com
> user-agent: curl/7.68.0
> accept: */*'''

curlHeader = {
    # 'Host': 'cn.bing.com',
    'user-agent': r'curl/7.68.0',
    'accept': r'*/*'
}

headerType = ['browser', 'curl']

if __name__ == "__main__":
    headerTypeParam = sys.argv[1]
    while headerTypeParam not in headerType:
        print("header type not supported, currently supported types: %s" % ', '.join(headerType))
        headerTypeParam = input()    

    conn = HTTP20Connection('cn.bing.com:443')
    conn.request('GET', '/search?q=123', headers=eval(headerTypeParam + 'Header'))
    resp = conn.get_response()

    resFile = open("trash/%s_res.html" % headerTypeParam, "wb")
    resFile.write(resp.read())