import re

def separate_gu(address):
    res = re.search('성남시[가-힣]{2,4}구',address)
    if res != None:
        span = res.span()
        si_gu = address[span[0]:span[1]]
        si = si_gu[0:3]
        gu = si_gu[3:]
        return address.replace(si + gu, si + ' ' + gu)
    else:
        return address
