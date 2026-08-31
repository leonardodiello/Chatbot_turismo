import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from unidecode import unidecode
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

dataset = pd.read_csv('dataset_todas_cidades_brasil.csv', delimiter=';')

dataset.head()

nltk.download('stopwords')
nltk.download('punkt_tab')

def remove_pontuacao(text):
    texto_limpo = ''
    for palavra in text:
      if palavra not in string.punctuation:
        texto_limpo += palavra

    return texto_limpo

print(string.punctuation)

def preprocessamento(texto):
    # Remove pontuações e símbolos
    texto = remove_pontuacao(texto)

    # Remover acentos
    texto = unidecode(texto)

    # Converte para minúsculo
    texto = texto.lower()

    # Tokenização
    tokens = word_tokenize(texto)

    # Remover stopwords
    stop_words = stopwords.words('portuguese')
    tokens = [token for token in tokens if token not in stop_words]

    # Juntar as palavras novamente em uma string
    texto_preprocessado = ' '.join(tokens)

    return texto_preprocessado

dataset["Pergunta_Preprocessada"] = dataset["Pergunta"].apply(preprocessamento)

dataset

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(dataset["Pergunta_Preprocessada"])

def obter_resposta(pergunta):
    # Pré processa a sentença da pergunta
    pergunta_processada = preprocessamento(pergunta)

    # Transforma a pergunta para um vetor
    pergunta_vector = vectorizer.transform([pergunta_processada])

    # Calcula a similaridade do cosseno
    similaridades = cosine_similarity(pergunta_vector, tfidf_matrix)

    # Obtém o índice da pergunta mais similar
    pergunta_index = similaridades.argmax()

    # Devolve a resposta para o usuário
    return dataset["Resposta"].iloc[pergunta_index]

import os

import telebot
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(func=lambda message: True)
def default(message):
    resposta = obter_resposta(message.text)

    bot.reply_to(
        message,
        resposta
    )

bot.polling()