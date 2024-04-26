#!/usr/bin/python3
"""Take in a URL, send request to URL and display value of `X-Request-Id`"""

if __name__ == '__main__':
    import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    content = response.read().decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
