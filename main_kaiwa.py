import requests
from bs4 import BeautifulSoup
import re

#http://ninjinix.x0.com/wolfg/index.rb?vid=2087&meslog=004_progress
url = "http://ninjinix.x0.com/wolfg/index.rb?vid="
n = 774
all_result = ""
num_people = ""
for i in range(9):
    url += str(n)
    url += "&meslog=00"
    url += str(i)
    url += "_progress"
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    #print([tag.text for tag in soup("a")])
    a = [tag.text for tag in soup("a")]
    a_in = [s for s in a if '>' not in s]
    a_num = [s for s in a_in if ' ' not in s]
    hatugenflg = False
    a_in_range = len(a_in)
    hogonums = []
    for st in range(a_in_range):
        if hatugenflg:
            hogonums.append(a_in[st])
            hatugenflg = False
        if '.' in a_in[st]:
            hatugenflg = True
    for i in hogonums:
        num_people += (i + " ")
    print(num_people)


    #a_in = [s for s in a_in if ' ' in s]
    td = [tag.text for tag in soup("td")]
    result =""
    td = [s for s in td if s != '']
