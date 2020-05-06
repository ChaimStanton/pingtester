#! ./venv/bin/python3

import urllib.request


def am_I_connected(host="http://google.com"):
    try:
        urllib.request.urlopen(host)
        return True
    except urllib.error.URLError:
        return False


print(am_I_connected())
