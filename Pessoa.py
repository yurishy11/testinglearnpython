import requests

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obter_todos_os_dados(self):
        # Essa conexão não ocorre pois ela está sendo simulada no tests
        resposta = requests.get('https://jsonplaceholder.typicode.com/users/1')

        # Simplificando
        if resposta.ok:
            self.dados_obtidos = True
            return "CONECTADO"
        else:
            self.dados_obtidos = False
            return "ERRO 404"