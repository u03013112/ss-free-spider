#coding=utf-8
import base64

def fromURL(url):
    data = {}
    url = url.strip()
    if url[0:5] != "ss://" :
        return None
    noSSPrefixStr = url[5:]
    shapIndex = noSSPrefixStr.rfind("#")
    if shapIndex != -1 :
        data['backup'] = noSSPrefixStr[shapIndex + 1:]
        noSSPrefixStr = noSSPrefixStr[:shapIndex]
    
    base64DecodeStr = base64.b64decode(noSSPrefixStr).decode()
    s1Index = base64DecodeStr.find(":")
    if s1Index != -1:
        data['method'] = base64DecodeStr[:s1Index]
        step1Str = base64DecodeStr[s1Index + 1:]
        s2Index = step1Str.find("@")
        if s2Index != -1:
            data['passwd'] = step1Str[:s2Index]
            step2Str = step1Str[s2Index + 1 :]
            s3Index = step2Str.find(":")
            if s3Index != -1:
                data['port'] = step2Str[s3Index + 1:]
                data['domain'] = step2Str[:s3Index]
                return data
    return None

if __name__=='__main__':
    d = fromURL("ss://YWVzLTI1Ni1jZmI6ZUlXMERuazY5NDU0ZTZuU3d1c3B2OURtUzIwMXRRMERAMTcyLjEwNC44NC42MDo4MDk3#翻墙党150.20日本")
    print(d)