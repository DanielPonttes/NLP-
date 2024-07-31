from math import log2

def calcular_entropia(palavra):
    #tamanho recebe o tamanho da palavra 
    tamanho = len(palavra)
    #cria um segundo vetor com a frequencia 
    frequencia = {}
    #percorre A string letra a letra 
    for letra in palavra:
        if letra in frequencia:
            frequencia[letra] += 1
        else:
            frequencia[letra] = 1 
    
    entropia = 0.0
    for letra in frequencia:
        probabilidade = frequencia[letra] / tamanho
        #H(X)=−∑ i=1 n P(xi)⋅log 2(P(xi))
        entropia -= probabilidade * log2(probabilidade)
    
    entropia_bits = round(entropia * tamanho)  
    # Arredondamos para o número inteiro mais próximo
    return entropia_bits

    
    # Palavras fornecidas
palavras = ["ARARAQUARA", "UFPEL", "PELOTAS" ,"COMPUTAÇÃO", "GUARULHOS"]
 
#cria um vetor com a entropia de cada palavra e imprime em bits  
entropias = {}
for palavra in palavras:
    entropias[palavra] = calcular_entropia(palavra)
    entropia_bits = calcular_entropia(palavra)
    print(f"A entropia de '{palavra}' é: {entropia_bits} bits")

#calcula o maior valor da entropia 
maior_entropia_palavra = max(entropias, key=entropias.get)
maior_entropia_valor = entropias[maior_entropia_palavra]

print(f"A palavra com a maior entropia é '{maior_entropia_palavra}' com {maior_entropia_valor} bits.")