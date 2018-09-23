import pandas as pd
import json
from operator import itemgetter
df = pd.read_csv('output.csv')

data = pd.DataFrame(df)
wordsdict = dict()

for i in data['text']:
    words  = i.split()
  #  print(type(i))
  #  print(type(words))
  #  print(words[1])
  #  print(len(words))
    print(type(len(words)))
    for temp in range(len(words)):

        if words[temp] is not None:
          try:
            if words[temp] in wordsdict.keys():
                wordsdict[words[temp]] += 1

            elif words[temp] not in wordsdict.keys():
                wordsdict[words[temp]] = 1
          except KeyError as e:
              print("there is an kePPandPPandas2.py:22as2.py:22y error")

sorted_list = sorted(wordsdict.items(),key=itemgetter(1) , reverse=True)

data = pd.DataFrame(sorted_list)
data.to_csv('output2.csv')
for word , repeat in sorted_list:
  print(str(repeat) + '++++++++' + word)



