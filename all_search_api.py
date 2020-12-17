from requests_html import HTMLSession
from myhtmlparser import parse_a

def yandex(q):
  session = HTMLSession()
  r = session.get('https://yandex.ru/search/?text='+q)
  r.html.render()
  html = r.text.replace("'",'"')
  search_res_mass = html.split('<div class="organic typo typo_text_m typo_line_s i-bem"')
  return search_res_mass[0]

def google(q):
  session = HTMLSession()
  r = session.get('https://google.com/search?q='+q)
  r.html.render()
  html = r.text.replace("'",'"')
  search_res_mass = html.split('<div class="g"')
  start = 1
  end = len(search_res_mass)
  links = []
  while start<end:
    alink = search_res_mass[start]
    alink_mass = alink.split('<a ')
    links.append(parse_a(alink_mass[1]))
    start+=1
  return links

def bing(q):
  session = HTMLSession()
  r = session.get('https://python.org/')
  r.html.render()
  return r.text