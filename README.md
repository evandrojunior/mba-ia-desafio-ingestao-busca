# Desafio MBA Engenharia de Software com IA - Full Cycle

Este projeto é uma solução para um sistema de chat baseado em conteúdo de documentos PDF. Ele utiliza técnicas modernas de processamento de linguagem natural (NLP) e armazenamento em vetor para permitir que os usuários façam perguntas e recebam respostas contextualizadas a partir do conteúdo do PDF.

## Descrição

O sistema consiste em três partes principais:

1. **Ingestão**: O script `ingest.py` é responsável por carregar um arquivo PDF, processá-lo para criar chunks de texto, gerar embeddings (representações vetoriais) desses chunks e armazená-los em um banco de dados PostgreSQL usando a biblioteca PGVector.

2. **Busca Similar**: O script `search.py` utiliza os embeddings armazenados para encontrar as partes do PDF mais relevantes para uma pergunta dada pelo usuário. Ele constrói uma resposta formatada baseada no contexto encontrado e usa um modelo de chat GPT para gerar a resposta final.

3. **Chat Interativo**: O script `chat.py` fornece uma interface interativa onde o usuário pode inserir perguntas e ver as respostas geradas pelo sistema.

## Requisitos

Antes de executar o projeto, você precisará:

1. Ter instalado o Python 3.x
2. Configurar as variáveis de ambiente necessárias (detalhadas abaixo)
3. Ter um banco de dados PostgreSQL disponível
4. Possuir uma chave de API da OpenAI para usar os serviços de embeddings e chat

## Instalação das Dependências

Execute o seguinte comando para instalar todas as dependências do projeto:

```bash
pip install -r requirements.txt
```

Se não houver um arquivo `requirements.txt`, você pode instalar as bibliotecas necessárias individualmente:

```bash
pip install langchain-community langchain-openai langchain-postgres dotenv python-dotenv
```

## Configuração das Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto, baseado no `.env.example`, e defina as seguintes variáveis de ambiente:

- `OPENAI_API_KEY`: Sua chave de API da OpenAI.
- `OPENAI_EMBEDDING_MODEL`: Nome do modelo de embeddings a ser usado (padrão: "text-embedding-3-small").
- `DATABASE_URL`: URL de conexão ao banco de dados PostgreSQL.
- `PG_VECTOR_COLLECTION_NAME`: Nome da coleção no banco de dados onde os embeddings serão armazenados.
- `PDF_PATH`: Caminho para o arquivo PDF que você deseja carregar.

**Observação sobre o Banco de Dados:**

Nós usamos o Docker para subir uma instância local do PostgreSQL. Execute o seguinte comando para iniciar o banco de dados:

```bash
docker compose up -d
```

Isso irá criar e iniciar uma instância do PostgreSQL em sua máquina local. Verifique se o serviço está rodando executando:

```bash
docker ps
```

A conexão com o banco de dados é feita via variável `DATABASE_URL`. Certifique-se que essa URL está correta no arquivo `.env` e que a porta, usuário e senha estão configuradas adequadamente para a instância Docker do PostgreSQL.

## Executando o Projeto

Siga os passos abaixo para executar o projeto:

1. **Ingestão do PDF**:
   Execute o seguinte comando para carregar e processar o arquivo PDF:

   ```bash
   python src/ingest.py
   ```

2. **Chat Interativo**:
   Após a ingestão bem-sucedida, inicie o chat executando:

   ```bash
   python src/chat.py
   ```

   Você será convidado a fazer uma pergunta, e o sistema retornará uma resposta baseada no conteúdo do PDF.

## Estrutura dos Arquivos

- `src/ingest.py`: Script para carregar e processar o arquivo PDF.
- `src/search.py`: Script para buscar similaridades no banco de dados e gerar respostas.
- `src/chat.py`: Interface interativa para conversa com o usuário.
- `.env`: Arquivo de configuração das variáveis de ambiente.
- `README.md`: Este arquivo, que descreve como executar o projeto.

## Testando o Sistema

Depois de executar os scripts acima, você pode testar o sistema fazendo perguntas sobre o conteúdo do PDF. Por exemplo:

```
Faça sua pergunta:

PERGUNTA: Qual é a principal vantagem do uso de embeddings no processamento de linguagem natural?
RESPOSTA: [Resposta gerada com base no conteúdo do PDF]
```

Se a pergunta não puder ser respondida adequadamente com base no conteúdo do PDF, o sistema retornará uma mensagem informando que não possui as informações necessárias.

## Conclusão

Este projeto demonstra como combinar técnicas de NLP com armazenamento em vetor para criar um sistema de Q&A interativo e eficiente. Ele pode ser adaptado para diferentes tipos de documentos e cenários, tornando-se uma ferramenta valiosa para análise e consulta de conteúdo textual.