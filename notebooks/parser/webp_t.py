import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

def web_s(p:int=5) -> dict:
    game = {}
    for i in range(1,p):
        page = 'p{}'.format(i)
        r = requests.get('https://stopgame.ru/review/new/stopchoice/' + page)
        soup = bs(r.content, 'html.parser')
        find = soup.find_all(attrs={'class': "article-description"})
        b = []
        for i in find:
            title = i.select("a")
            b.append(title[0].text[:-7])
        game[page] = b
    return game
    
## print(title[0].text[:-7])
## print(soup.prettify())

# game = web_s(5)
# pprint(game)




## пример с авторизацией
## get CSRF
# s = requests.Session()
# auth_html = s.get('web_page')
# auth_bs = bs(auth_html.content, 'html.parser')
# csrf = auth_bs.select('input[name=YII_CSRF_TOKEN]')[0]['value']
# print(csrf) # <- тут токен авторизации

## do login
# payload = {
#     # post data
#     'YII_CSRF_TOKEN': csrf,
#     'returnUrl': '/',
#     'UserLoginForm[email]': 'admin@mail.com',
#     'UserLoginForm[password]': 'test123',
#     'UserLoginForm[rememberMe]': 1
# }

# answ = s.post("web_page/user/login/", data=payload)
# answ_bs = bs(answ.content, 'html.parser')
# name = answ_bs.select('.user-menu__name')[0].text.split()
# lvl = answ_bs.select('.user-menu__info-text--lvl')[0].text.split()
# exp = answ_bs.select('.user-menu__info-text--exp')[0].text.split()
# обход блока по ip  через прокси





