# ...
from os import environ
from waitress import serve

# app = Flask(__name__)

# joke_list = [
# ...
def start_server(host: str = "0.0.0.0", port: int = 8000):
    if environ("FLASK_ENV") == "dev":
        # Servidor de desenvolvimento do kit Werkzeug
        return app.run(debug=True, host=host, port=port)
    else:
        # Este é o Waitress, um servidor de produção otimizado
        serve(app, host=host, port=port)

# if __name__ == "__main__":
#     start_server()
