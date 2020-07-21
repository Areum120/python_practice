import re

'''
address를 넘기면 성남시분당구로 되어 있는 부분을 성남시 분당구로 분리해줌
ex) separate_gu('경기도 성남시 분당구서현동 263번지')
'''
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
