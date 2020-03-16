

import requests
import webbrowser


def github():
	text = 'gorpo'
	url = (f'https://api.github.com/users/{text}')
	req = requests.get(url, timeout=3000)
	rjson = req.json()
	print(f"""Este usuário usa o seu login como {rjson['login']},seu nome no github é {rjson['name']}.
Companhia registada neste perfil {rjson['company']}, país de origem {rjson['location']}.
o Usuario possui {rjson['public_repos']} repositorios publicos,{rjson['followers']} seguidores e segue {rjson['following']} pessoas
""")
	webbrowser.open_new_tab(f'https://github.com/{text}')

github()