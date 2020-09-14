#!/usr/bin/python3

from hyper import HTTP20Connection, HTTPConnection
import sys

'''GET /search?q=123 HTTP/2
Host: cn.bing.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Cookie: DUP=Q=JQz4tRx3Pz-NyLS-hnqaAg2&T=399428824&A=2&IG=9EED5C15633743E890EC89C277DA80C5; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=1CC9D2B4567F48B48BAB5666EFDCD066&dmnchg=1; SRCHUSR=DOB=20200825&T=1598574232000; _EDGE_V=1; MUID=147AE217C34B6C6E073BED26C2656D5D; MUIDB=147AE217C34B6C6E073BED26C2656D5D; SRCHHPGUSR=CW=2488&CH=678&DPR=1&UTC=480&DM=0&WTS=63734171032&HV=1598574430; ENSEARCH=BENVER=1; ULC=P=14320|13:2&H=14320|13:2&T=14320|13:2; _SS=SID=26531E714B6B6DCD376A11404A456C7F&bIm=021163; _EDGE_S=mkt=zh-cn&SID=26531E714B6B6DCD376A11404A456C7F; ipv6=hit=1598577835244&t=4; _FP=hta=on; MUIDB=32E00A7676396B7D13170544775E6A96
Upgrade-Insecure-Requests: 1'''

browserHeader = {
    'Host': 'cn.bing.com',
    'User-Agent': r'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
    'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': r'en-US,en;q=0.5',
    # 'Accept-Encoding': r'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Cookie': r'DUP=Q=JQz4tRx3Pz-NyLS-hnqaAg2&T=399428824&A=2&IG=9EED5C15633743E890EC89C277DA80C5; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=1CC9D2B4567F48B48BAB5666EFDCD066&dmnchg=1; SRCHUSR=DOB=20200825&T=1598574232000; _EDGE_V=1; MUID=147AE217C34B6C6E073BED26C2656D5D; MUIDB=147AE217C34B6C6E073BED26C2656D5D; SRCHHPGUSR=CW=2488&CH=678&DPR=1&UTC=480&DM=0&WTS=63734171032&HV=1598574430; ENSEARCH=BENVER=1; ULC=P=14320|13:2&H=14320|13:2&T=14320|13:2; _SS=SID=26531E714B6B6DCD376A11404A456C7F&bIm=021163; _EDGE_S=mkt=zh-cn&SID=26531E714B6B6DCD376A11404A456C7F; ipv6=hit=1598577835244&t=4; _FP=hta=on; MUIDB=32E00A7676396B7D13170544775E6A96',
    'Upgrade-Insecure-Requests': '1'
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