from bs4 import BeautifulSoup
import requests

produto = input('Coloque o produto que você quer pesquisar o preço: ')

def mercadoLivre(produto):
    URL_BASE = "https://lista.mercadolivre.com.br/"  
    URL = URL_BASE + produto 
    response = requests.get(URL)
    soup = BeautifulSoup(response.text,'html.parser')
    precos = []
    preco_dict = {}
    produtos = soup.find_all('div', class_='andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16 andes-card--animated')
    
    for item in produtos:
        titulo = item.find('h2', class_='ui-search-item__title')
        preco_inteiro = item.find('span', class_='andes-money-amount__fraction')
        link = item.find('a', class_='ui-search-item__group__element ui-search-link__title-card ui-search-link')
        
        if titulo and preco_inteiro:
            preco = preco_inteiro.text.replace('.', '')
            precos.append(int(preco))
            preco_dict[preco] = link['href']
    
    if precos:
        menorPreco = min(precos)
        linkMenorPreco = preco_dict[f'{menorPreco}']
        return f'Preço: R${menorPreco} Link: {linkMenorPreco}'
    else:
        return 'Produto inexistente'

def magazine(produto):
    URL_BASE = "https://www.magazineluiza.com.br/busca/"
    URL = URL_BASE + produto
    response = requests.get(URL)
    soup = BeautifulSoup(response.text,'html.parser')
    precos = []
    preco_dict = {}
    produtos = soup.find_all('li', class_='sc-kTbCBX ciMFyT')
    
    for item in produtos:
        titulo = item.find('h2', class_='sc-fvwjDU ehjgcW')
        preco_inteiro = item.find('p', class_='sc-kpDqfm eCPtRw sc-bOhtcR dOwMgM')
        link = item.find('a', class_='sc-eBMEME uPWog sc-cDnByv dgyHCD sc-cDnByv dgyHCD')
        
        if titulo and preco_inteiro and link:
            preco = preco_inteiro.text.replace('R$', '').replace('.', '').replace(',', '')
            precos.append(int(preco))
            preco_dict[preco] = link['href']
    
    if precos:
        menorPreco = min(precos)
        linkMenorPreco = preco_dict[f'{menorPreco}']
        return f'Preço: R${menorPreco} Link: https://www.magazineluiza.com.br{linkMenorPreco}'
    else:
        return 'Produto inexistente'

def CeA(produto):
    URL_BASE = "https://www.cea.com.br/search/"
    URL = URL_BASE + produto
    response = requests.get(URL)
    soup = BeautifulSoup(response.text,'html.parser')
    precos = []
    preco_dict = {}
    produtos = soup.find_all('div', class_='vtex-search-result-3-x-galleryItem vtex-search-result-3-x-galleryItem--normal vtex-search-result-3-x-galleryItem--THREE_COLUMNS pa4')
    
    for item in produtos:
        titulo = item.find('span', class_='vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body')
        preco_inteiro = item.find('span', class_='vtex-product-price-1-x-currencyInteger')
        link = item.find('a', class_='vtex-product-summary-2-x-clearLink h-100 flex flex-column')
        
        if titulo and preco_inteiro and link:
            preco = preco_inteiro.text.replace('.', '')
            precos.append(int(preco))
            preco_dict[preco] = link['href']
    
    if precos:
        menorPreco = min(precos)
        linkMenorPreco = preco_dict[f'{menorPreco}']
        return f'Preço: R${menorPreco} Link: https://www.cea.com.br{linkMenorPreco}'
    else:
        return 'Produto inexistente'

x = mercadoLivre(produto)
y = magazine(produto)
z = CeA(produto)

lista = [x, y, z]
for item in lista:
    if item:
        print(f'{item}\n')
