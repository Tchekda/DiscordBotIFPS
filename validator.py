import requests
from bs4 import BeautifulSoup

print("Entrez votre plan de vol : ")
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
print("FPL received, analysing...")
req = requests.post("http://validation.eurofpl.eu/", data={'freeEntry': text})
data = BeautifulSoup(req.text, features="html.parser")
for span in data.find_all('span', 'ifpuv_result'):
    if span.get_text() == 'NO ERRORS':
        print('Success : No Errors')
    else:
        print("Error : ", span.get_text())
