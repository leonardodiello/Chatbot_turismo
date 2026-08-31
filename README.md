# Chatbot de Turismo

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![GitHub](https://img.shields.io/badge/GitHub-Leonardo%20Diello-black?logo=github)](https://github.com/leonardodiello)
[![Status](https://img.shields.io/badge/Status-Em%20melhoria-yellow)](https://github.com/leonardodiello/Chatbot_turismo)

Chatbot desenvolvido em **Python** durante o curso de **Python e Chatbot do Samsung Ocean**, com o objetivo de criar um assistente virtual capaz de responder perguntas relacionadas ao turismo no Brasil.

O projeto utiliza técnicas de **Processamento de Linguagem Natural (PLN)** para analisar as perguntas do usuário e encontrar, dentro de uma base de dados, a resposta mais semelhante à pergunta recebida.

## Sobre o projeto

O chatbot recebe uma pergunta do usuário, realiza um processo de tratamento do texto e utiliza **TF-IDF** juntamente com a **similaridade do cosseno** para identificar a pergunta mais próxima dentro do dataset.

Após encontrar a pergunta com maior similaridade, o sistema retorna a resposta correspondente.

A aplicação também foi integrada ao **Telegram**, permitindo que o chatbot seja utilizado diretamente pela plataforma.

## Funcionalidades

* Responder perguntas relacionadas ao turismo brasileiro.
* Identificar perguntas semelhantes utilizando Processamento de Linguagem Natural.
* Pesquisar respostas dentro de um dataset.
* Processar textos em português.
* Remover pontuação e acentuação.
* Remover stopwords.
* Utilizar TF-IDF para representação dos textos.
* Calcular similaridade entre perguntas.
* Integração com Telegram.

## Tecnologias utilizadas

* Python.
* Pandas.
* NLTK.
* Scikit-learn.
* Unidecode.
* PyTelegramBotAPI.
* Python-dotenv.
* Telegram Bot API.

## Processamento de Linguagem Natural

Antes de comparar a pergunta do usuário com o dataset, o texto passa por algumas etapas de pré-processamento:

* Conversão para letras minúsculas.
* Remoção de pontuação.
* Remoção de acentos.
* Tokenização.
* Remoção de stopwords em português.

Após o pré-processamento, o **TfidfVectorizer**, da biblioteca Scikit-learn, transforma os textos em vetores numéricos.

A aplicação utiliza então a **similaridade do cosseno** para identificar qual pergunta presente no dataset possui maior semelhança com a pergunta enviada pelo usuário.

## Como funciona

O funcionamento do chatbot pode ser representado pelo seguinte fluxo:

```text
Usuário
   ↓
Pergunta no Telegram
   ↓
Pré-processamento do texto
   ↓
Tokenização e remoção de stopwords
   ↓
TF-IDF
   ↓
Similaridade do cosseno
   ↓
Pergunta mais semelhante no dataset
   ↓
Resposta
```

## Dataset

O projeto utiliza datasets com perguntas e respostas relacionadas ao turismo brasileiro.

A base contém informações relacionadas a:

* Destinos turísticos.
* Praias.
* Cultura.
* Gastronomia.
* Ecoturismo.
* Esportes.
* Eventos culturais.
* Pontos turísticos.
* Cidades brasileiras.
* Dicas de viagem.

Entre os arquivos utilizados estão:

```text
dataset_expandido.csv
dataset_todas_cidades_brasil.csv
```

## Integração com Telegram

O chatbot foi integrado ao Telegram utilizando a biblioteca **PyTelegramBotAPI**.

O token do bot é armazenado em uma variável de ambiente para evitar que informações sensíveis sejam publicadas no código-fonte.

Exemplo do arquivo `.env`:

```env
TELEGRAM_TOKEN=seu_token_aqui
```

O arquivo `.env` não deve ser enviado para o GitHub.

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/leonardodiello/Chatbot_turismo.git
```

Entre na pasta:

```bash
cd Chatbot_turismo
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente virtual.

**macOS/Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install pandas nltk unidecode scikit-learn pyTelegramBotAPI python-dotenv
```

### 4. Configure o token do Telegram

Crie um arquivo `.env` na raiz do projeto:

```env
TELEGRAM_TOKEN=seu_token_aqui
```

### 5. Execute o chatbot

```bash
python chat.py
```

Após iniciar a aplicação, o bot ficará aguardando mensagens no Telegram.

## Estrutura do projeto

```text
Chatbot_turismo/
│
├── chat.py
├── dataset_expandido.csv
├── dataset_todas_cidades_brasil.csv
├── .gitignore
├── .env
└── README.md
```

> O arquivo `.env` é utilizado localmente e está incluído no `.gitignore`, portanto não deve ser enviado para o repositório.

## Exemplo de interação

```text
Usuário:
O que fazer em Manaus?

Chatbot:
Manaus possui diversos pontos turísticos, como o Teatro
Amazonas, o Encontro das Águas e o Museu do Seringal.
```

## Objetivos de aprendizado

Este projeto foi desenvolvido como prática dos conceitos apresentados durante o curso de **Python e Chatbot do Samsung Ocean**.

Durante o desenvolvimento foram aplicados conhecimentos de:

* Manipulação de dados com Pandas.
* Processamento de Linguagem Natural.
* Tokenização de textos.
* Stopwords.
* Vetorização TF-IDF.
* Similaridade do cosseno.
* Manipulação de arquivos CSV.
* Variáveis de ambiente.
* Integração com APIs.
* Desenvolvimento de bots para Telegram.
* Desenvolvimento de aplicações em Python.

## Próximos passos

Algumas melhorias que podem ser implementadas futuramente:

* Melhorar o tratamento de perguntas semelhantes.
* Adicionar um sistema de pontuação mínima para respostas.
* Expandir a base de conhecimento.
* Adicionar informações atualizadas sobre destinos.
* Implementar memória de conversa.
* Criar uma interface web.
* Melhorar o reconhecimento da intenção do usuário.
* Integrar APIs de clima, mapas e informações turísticas.

## Curso

Projeto desenvolvido durante o curso de **Python e Chatbot do Samsung Ocean**, como prática dos conceitos apresentados durante as aulas.

## Autor

**Leonardo Diello**

Estudante de **Engenharia de Software no Instituto Federal do Amazonas (IFAM)**.

[![GitHub](https://img.shields.io/badge/GitHub-Leonardo%20Diello-black?logo=github)](https://github.com/leonardodiello)

---

Se este projeto foi útil para você, considere deixar uma estrela no repositório.
