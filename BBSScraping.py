import requests
from bs4 import BeautifulSoup

#http://ninjinix.x0.com/wolfg/index.rb?vid=2087&meslog=004_progress
url = "http://ninjinix.x0.com/wolfg/index.rb?vid="
n = 774
all_result = ""
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
    a_in = [s for s in a_in if ' ' in s]
    td = [tag.text for tag in soup("td")]
    result =""
    td = [s for s in td if s != '']

    while(len(td) > 0 and len(a_in) > 0):
      result+=("name; " + a_in.pop(0) + "   ")
      result+=("text; " + td.pop(0) + "\n")
    print(result)
    all_result+=result
f = open("BBSlogdata.txt","a",encoding = "UTF-8")
f.write(all_result)
f.close
