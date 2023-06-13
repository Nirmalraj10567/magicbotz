import requests
from bs4 import BeautifulSoup
def pdiskunlink(v):
  mm = v.split("/")[-1]
  a = f"https://pdisk.investro1.com/6-things-you-probably-didnt-know-your-car-insurance-covered-{mm}.html"
  re = requests.get(a)
  soup = BeautifulSoup(re.text, 'html.parser')
  source = soup.find('source')
  if source:
    src = source['src']
    return src
  else:
    return "No source element found."
