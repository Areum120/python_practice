import pandas as pd
import re
from libs.separate_gu import separate_gu

df = pd.read_csv('시장및마트현황.csv')
seongnam_df = df[df['시군명'] == '성남시']
seongnam_df['소재지지번주소'] = seongnam_df['소재지지번주소'].apply(lambda x:separate_gu(x))
seongnam_df['dong'] = seongnam_df['소재지지번주소'].apply(lambda x: x.split(' ')[3])
print(seongnam_df.head())

gr_dong = seongnam_df.groupby('dong')
print(gr_dong.count())
