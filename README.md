# Previsão de Palavras Mascaradas com BERT(Embedding Contextual)
Este repositório contém um exemplo de código que utiliza o modelo BERT pré-treinado em português, fornecido pela neuralmind, para prever palavras mascaradas em uma frase.

## Descrição
 O script realiza as seguintes etapas:
  1. Carregamento e utilização do Tokenizador e Modelo BERT(para português):
``` tokenizer = BertTokenizer.from_pretrained('neuralmind/bert-base-portuguese-cased') ``` e ``` modelo = BertForMaskedLM.from_pretrained('neuralmind/bert-base-portuguese-cased') ```

  2. Tokenização da Sentença:
   
  * A sentença é tokenizada, e o token [MASK] é identificado.
    
  3. Conversão de Tokens para IDs:

  * Os tokens são convertidos em IDs específicos do BERT, que são utilizados como entrada para o modelo.
  
  4. Previsão da Palavra Mascarada:

  * O modelo BERT faz previsões para o token mascarado e retorna as cinco palavras mais prováveis.
    
  5. Filtragem das Previsões:

  * Previsões irrelevantes como pontuações e conjunções são removidas para uma melhor interpretação dos resultados.

  6. Exibição das Previsões:

  * As palavras previstas, juntamente com suas respectivas pontuações, são exibidas.

## Requisitos
* Python 3.7 ou superior
* PyTorch
* Transformers (Hugging Face)

## Instalação

Para instalar as dependências, execute no bash:


*     pip install torch transformers


## Resultados

Previsões para a palavra mascarada: 
- gatos: 10.123456
- cachorros: 9.654321
- pássaros: 8.876543
  
**Observações:**
O exemplo usa o modelo BERT específico para português (neuralmind/bert-base-portuguese-cased).
As previsões podem variar de acordo com o contexto da sentença e o modelo utilizado.
