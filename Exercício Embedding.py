import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from gensim.models import Word2Vec
import string


def get_wordnet_pos(word):
    """Mapeia a tag POS para o formato usado pela lemmatizer."""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)


corpus = """Python é uma linguagem de programação amplamente reconhecida e utilizada em uma variedade de campos, desempenhando um papel fundamental em diversas áreas da tecnologia e além.
Em ciência de dados e análise de dados, Python se destaca como uma escolha popular devido à sua facilidade de uso e à riqueza de bibliotecas, como NumPy, pandas e scikit-learn, que facilitam a manipulação, visualização e análise de dados complexos.
No desenvolvimento web, frameworks como Django e Flask tornam mais simples a criação de aplicações web robustas e escaláveis, permitindo que desenvolvedores construam desde pequenos sites até grandes sistemas de comércio eletrônico com facilidade.
Em inteligência artificial e aprendizado de máquina, Python é a linguagem preferida de muitos profissionais devido à sua flexibilidade e à disponibilidade de frameworks como TensorFlow, Keras e PyTorch, que possibilitam a implementação de modelos complexos de forma eficiente.
Além disso, Python é frequentemente usado em automação de tarefas, desenvolvimento de scripts e prototipagem rápida de soluções de software, ajudando a simplificar processos e aumentar a produtividade em diversas áreas profissionais.
Com uma comunidade ativa, vasto ecossistema de bibliotecas e sua facilidade de aprendizado, Python continua a desempenhar um papel crucial na inovação e no avanço tecnológico em todo o mundo, tornando-se uma linguagem indispensável para desenvolvedores, cientistas de dados e profissionais de tecnologia em geral."""

# normalização
corpus = corpus.lower()

# Tokenização
tokens = word_tokenize(corpus)

# Remoção de stopwords
stop_words = set(stopwords.words('portuguese'))
filtro_tokens = [token for token in tokens if token.lower() not in stop_words]

# Remoção de pontuações
filtro_tokens = [token for token in filtro_tokens if token not in string.punctuation]

# Lematização
lemmatizer = WordNetLemmatizer()

tokens_lemmatizados = [lemmatizer.lemmatize(token, get_wordnet_pos(token)) for token in filtro_tokens]

# Treinamento do modelo Word2Vec
model = Word2Vec([tokens_lemmatizados], vector_size=100, window=5, min_count=2, workers=4)

#vector size = cada palavra será representada por 1 vetor de 100 dimensões
#window = determina o intervalo de palavras que o treino ira considerar(5 nesse caso)
#min cout = número minimo de vezes que a palavra tem que aparecer para ser considerada
#define quantos threads serão usados

#encontrar palavras similares
palavras_similares = model.wv.most_similar('python')
print("Palavras similares a 'python':", palavras_similares)

#vetor de palavra especifica
word_vector = model.wv['python']
print("Vetor da palavra 'python':", word_vector)

print("Tokens originais:", tokens)
print("Tokens sem stopwords:", filtro_tokens)
print("Tokens lematizados:", tokens_lemmatizados)
