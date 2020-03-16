import  requests

def pythonLibs():
	nome_lib = 'instapy'                               #aqui chama o nome da lib
	url = (f'https://pypi.org/pypi/{nome_lib}/json')   #esta url vc pode testar trocar por de outras API
	req = requests.get(url, timeout=3000)              #isto é meio padrao sei la
	retorno = req.json()                               #aqui ele ja retorna dados se der um print...
	info = retorno['info']                             #como a porra do retorno era um dicionario dentro de um dicionario        
                                                       #desempacotamos uma vez
	print(info)                                        #printei so para ver que ja saiu de um dicionario agora so tem um
	

 #agora uso a variavel info que desepacotou o primeiro dicionario para desempactar as coisas que tao em outro dicionario conforme print acima....

	print(f"""Autor: {info['author']} 
Url: {info['package_url']}""")

pythonLibs()