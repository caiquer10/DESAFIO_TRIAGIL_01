# Use a imagem oficial do Python 3.10.12
FROM python:3.10.12

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os arquivos do projeto para o contêiner
COPY . .

# Instala as bibliotecas necessárias
RUN pip install requests uuid

# Comando para iniciar o script Python
CMD ["python", "./app.py"]
