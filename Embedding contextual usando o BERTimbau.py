from transformers import BertTokenizer, BertForMaskedLM
import torch

# Tokenizador e o modelo BERT pré-treinado para prever palavras mascaradas
tokenizer = BertTokenizer.from_pretrained('neuralmind/bert-base-portuguese-cased')
modelo = BertForMaskedLM.from_pretrained('neuralmind/bert-base-portuguese-cased')

# Sentença
sentenca = "Eu gosto de fazer carinho em [MASK] ."

# Sentença tokenizada
sentenca_tokenizada = tokenizer.tokenize(sentenca)

# Encontre a posição da palavra mascarada (MASK token)
index_mascarada = sentenca_tokenizada.index('[MASK]')

# Converta para IDs de token BERT
tokens_indexados = tokenizer.convert_tokens_to_ids(sentenca_tokenizada)

# Previsão da palavra mascarada
with torch.no_grad():
    previsao = modelo(torch.tensor([tokens_indexados]))[0]

# As 5 melhores previsões para a palavra mascarada
previsões_mascaradas = previsao[0, index_mascarada].topk(5)

# Converte os IDs de token de volta para palavras
tokens_previstos = tokenizer.convert_ids_to_tokens(previsões_mascaradas.indices.tolist())

# Filtrar as previsões para excluir acentos e a conjunção "e"
previsoes_filtradas = [(token, pontuaçao) for token, pontuaçao in zip(tokens_previstos, previsões_mascaradas.values.tolist())
                       if token not in ['.', '"', ')', ',']]

# Verificar se há previsões filtradas antes de imprimir
if previsoes_filtradas:
    # Imprimir as previsões filtradas
    print("Previsões para a palavra mascarada: ")
    for token, pontuacao in previsoes_filtradas:
        print(f"- {token}: {pontuacao}")
else:
    print("Não há previsões disponíveis após a filtragem.")
