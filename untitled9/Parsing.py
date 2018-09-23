import json
import string
import re
line_generator = open('user_timeline_ayyusss.json','r')
with open('output.csv' , 'w') as f:
    f.write('text,created_at,lang\n')
    for ine in line_generator:
        parsed = json.loads(ine)
        text = re.sub(r'http\S+', '', parsed['text'])
        text = re.sub('['+string.punctuation+']', ' ', text)
        f.write('{} ,{} ,{} \n'.format(text , parsed['created_at'],parsed['lang']))


        print('\n')

#print(parsed['text'].strip()
#f.write(parsed['text'])
#print(parsed['created_at'])
#f.write(parsed['created_at'])
#print(parsed['lang'])
#f.write(parsed['created_at'])