import re
#
#
# s='anand@gmail.com bhosle124@gmail.com bhosle#gmail.com anuo@gamil'
#
# d=re.compile('[a-zA-Z0-9]+@[a-z]+\.[a-z]{3}')
# f=d.findall(s)
#
#
# l='maths 209 sciecne 222 kannada 124 social 333 english 100'
#
# v=re.findall('([0-9]+)\s([a-z]+)',l)
# print(v)
# g=re.findall('[a-z]+',l)

import csv

# with open ('Social_Network_Ads.csv','r+')as file:
#     d=csv.reader(file)
#     for val in d:
#         print('hi',val[1])
#     d=re.sub('MALE','ANAND',val[1])
#
#     v=csv.writer(file)
#     v.writerows(file)
#     print(d)

with open('anna.txt','w+') as file:
    wri=file.write("hello how are you,i going to banglore ,i stay in pune ,i work in pune")
with open("anna.txt" ,'r') as f:
    d=f.read()
    print(d)
    import re
    r=re.sub('pune','goa',d)
with open ('anna.txt','w') as f1:
    d=f1.write(r)
