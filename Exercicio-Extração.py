from bs4 import BeautifulSoup

# Abre o arquivo HTML local nomeado exemplo.html
with open("C:/Users/ACER/Downloads/exemplo.html", "r" , encoding="utf-8") as arquivo:
    # Lê o conteúdo do arquivo HTML
    conteudo = arquivo.read()

    # Cria um objeto BeautifulSoup para fazer o parsing do conteúdo HTML
    soup = BeautifulSoup(conteudo, 'html.parser')

    #Procura todos o articles
    articles = soup.find_all('article')

    #Itera sobre as tags "article" encontradas e imprime seus conteúdos
    for article in articles:
        #remove as tagas do html
        texto_artigo = article.get_text(strip=True)
        #imprime a article
        print(texto_artigo)
