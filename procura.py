from bs4 import BeautifulSoup
import requests
produto = input('coloque o produto que você quer pesquisar o preço: ')
def mercadoLivre(produto):
    URL_BASE = "https://lista.mercadolivre.com.br/"  
    URL = URL_BASE + produto 
    response = requests.get(URL)
    soup = BeautifulSoup(response.text,'html.parser')
    precos = []
    dict = {}
    produtos= soup.find_all('div', class_='andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16 andes-card--animated')
    for produto in produtos:
        titulo = produto.find('h2', class_='ui-search-item__title')
        preco_inteiro = produto.find('span', class_='andes-money-amount__fraction')
        link = produto.find('a', class_='ui-search-item__group__element ui-search-link__title-card ui-search-link')
        if titulo is not None:
            if preco_inteiro is not None:
                preco_inteiro = preco_inteiro.text 
                preco_inteiro = preco_inteiro.replace('.', '')
                precos.append(int(preco_inteiro))
                dict[preco_inteiro] = link['href']
                menorPreco = min(precos)
                linkMenorPreco = dict[f'{menorPreco}']
                infoFinal = f'preço:R${menorPreco} link:{linkMenorPreco}'

        else:
            continue
    if precos != []:
        menorPreco = min(precos)
        linkMenorPreco = dict[f'{menorPreco}']
        infoFinal = f'preço:R${menorPreco} link:{linkMenorPreco}' 
        return infoFinal
    else:
        return print('produto inexistente')
def magazine(produto):
    URL_BASE = "https://www.magazineluiza.com.br/busca/"
    URL = URL_BASE + produto 
    response = requests.get(URL)
    soup = BeautifulSoup(response.text,'html.parser')
    produtos= soup.find_all('li', class_='sc-kTbCBX ciMFyT')
    precos = []
    dict = {}
    for produto in produtos:
        titulo = produto.find('h2', class_='sc-fvwjDU ehjgcW')
        preco_inteiro = produto.find('p', class_='sc-kpDqfm eCPtRw sc-bOhtcR dOwMgM')
        link = produto.find('a', class_='sc-eBMEME uPWog sc-cDnByv dgyHCD sc-cDnByv dgyHCD')
        if titulo is not None:
            if preco is not None:
                preco = preco_inteiro.text
                for letra in ['R', '$', ' ']:
                    preco= preco.replace(letra,'')
                preco = ''.join(c for c in preco if c.isdigit()or c in ['.',','])
                preco = preco.split(',')[0]
                preco = preco.replace('.' or ',','')
                precos.append(int(preco))
                dict[preco] = link['href']
        else:
            continue
    if  precos != []:
        menorPreco = min(precos)
        linkMenorPreco = dict[f'{menorPreco}']
        infoFinal = f'preço:R${menorPreco} link:https://www.magazineluiza.com.br{linkMenorPreco}'   
        return infoFinal
    else:
        return print('produto inexistente')
def CeA(produto):
    URL_BASE = "https://www.cea.com.br/search/"
    URL = URL_BASE + produto 
    response = requests.get(URL)
    soup = BeautifulSoup(response.text,'html.parser')
    produtos= soup.find_all('div', class_='vtex-search-result-3-x-galleryItem vtex-search-result-3-x-galleryItem--normal vtex-search-result-3-x-galleryItem--THREE_COLUMNS pa4')
    precos = []
    dict = {}
    for produto in produtos:
        titulo = produto.find('span', class_='vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body')
        preco_inteiro = produto.find('span', class_='vtex-product-price-1-x-currencyInteger')
        if titulo is not None:
            if preco is not None:
                preco = preco_inteiro.text
                link = produto.find('a', class_='vtex-product-summary-2-x-clearLink h-100 flex flex-column')
                preco.replace('.', '')
                precos.append(int(preco))
                dict[preco] = link['href']
        else:
            continue 
    if precos != []:
        menorPreco = min(precos)
        linkMenorPreco = dict[f'{menorPreco}']
        infoFinal = f'preço:R${menorPreco} link:https://www.cea.com.br/{linkMenorPreco}'    
        return infoFinal
    else:
        return print('produto inexistente')
x= mercadoLivre(produto)
y= magazine(produto)
z = CeA(produto)
lista = [x,y,z]
for itens in lista:
    if itens is not None:
        print(f'{itens} \n')
    else:
        continue