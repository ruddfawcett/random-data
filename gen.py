import csv
import pandas
from random import randrange

ppvs = [0, 1, 3, 5]
ppa = ['left', 'right']

df = pandas.DataFrame(columns=['posts_seen', 'post_alignment', 'point_delta', 'point_value'])
df.loc[0] = [0, '', 0, 0]

for number in range(25):
    idx = number + 1
    alignment = randrange(0, len(ppa))
    pd = ppvs[randrange(0, len(ppvs))]

    if alignment == 0:
        pd *= -1

    pv = int(df.loc[number]['point_value']) + pd
    df.loc[idx] = [idx, ppa[alignment], pd, pv]

df.to_csv('random-data.csv', index=False)
