#!/usr/bin/python3

from flask import Flask, request, render_template
from hyper import HTTP20Connection
import argparse

app = Flask(__name__)

@app.route("/search")
def return_static_page():
    keyword = request.args.get("q")

    browser = request.headers["User-Agent"]

    requestHeader = {
    'Host': 'cn.bing.com',
    'User-Agent': browser,
    'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': r'en-US,en;q=0.5',
    # 'Accept-Encoding': r'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Cookie': r'DUP=Q=JQz4tRx3Pz-NyLS-hnqaAg2&T=399428824&A=2&IG=9EED5C15633743E890EC89C277DA80C5; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=1CC9D2B4567F48B48BAB5666EFDCD066&dmnchg=1; SRCHUSR=DOB=20200825&T=1598574232000; _EDGE_V=1; MUID=147AE217C34B6C6E073BED26C2656D5D; MUIDB=147AE217C34B6C6E073BED26C2656D5D; SRCHHPGUSR=CW=2488&CH=678&DPR=1&UTC=480&DM=0&WTS=63734171032&HV=1598574430; ENSEARCH=BENVER=1; ULC=P=14320|13:2&H=14320|13:2&T=14320|13:2; _SS=SID=26531E714B6B6DCD376A11404A456C7F&bIm=021163; _EDGE_S=mkt=zh-cn&SID=26531E714B6B6DCD376A11404A456C7F; ipv6=hit=1598577835244&t=4; _FP=hta=on; MUIDB=32E00A7676396B7D13170544775E6A96',
    'Upgrade-Insecure-Requests': '1'
    }

    conn = HTTP20Connection('cn.bing.com:443')
    conn.request('GET', '/search?q=%s' % keyword, headers=requestHeader)
    resp = conn.get_response()

    return resp.read(), 200

@app.route("/soptest")
def return_soptest_page():
    diffOrigin = request.args.get("origin")

    print(diffOrigin)

    return render_template('soptest.html', origin = diffOrigin)

if __name__ == "__main__":
    # argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", help="input the ip address that the web server runs on")
    parser.add_argument("port", help="input the port that the web server runs on")
    args = parser.parse_args()

    try:
        app.run(host=args.ip, port=args.port)
    except:
        print("can not run web server. please check the ip address and the port")
