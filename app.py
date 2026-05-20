# app.py
from flask import Flask
app = Flask(__name__)  # Cria a instância da aplicação


@app.route("/")  # Cria uma rota, para a raiz do projeto. (GET por padrão)
def hello_world():  # Metodo a ser executado ao navegar
    return 'Hello World!'


# Verifica se o script está sendo executado diretamente e executa a aplicação
if __name__ == '__main__':
    #  debug = True, reinicia automaticamente a cada mudança de arquivo
    #  mude a porta, caso ela estiver em uso
    app.run(debug=True, host='0.0.0.0', port=8000)