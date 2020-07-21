import pandas as pd
import re

df = pd.read_csv('시장및마트현황.csv')

seongnam_df = df[df['시군명'] == '성남시']

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

seongnam_df['소재지지번주소'] = seongnam_df['소재지지번주소'].apply(lambda x:separate_gu(x))

seongnam_df['dong'] = seongnam_df['소재지지번주소'].apply(lambda x: x.split(' ')[3])
print(seongnam_df.head())

# seongnam.to_csv('성남_시장및마트현황.csv')

gr_dong = seongnam_df.groupby('dong')

print(gr_dong.count())
