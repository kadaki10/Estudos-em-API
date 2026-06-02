# joke_model.py
import random
from .db import db
from .abstract_model import AbstractModel


# Herdando a classe abstrata que domina o uso do mongodb
class JokeModel(AbstractModel):
    # Define que a coleção do banco se chamara jokes
    # Uma coleção é equivalente a uma tabela do mySQL
    _colection = db["jokes"]

    # Nosso construtor receberá um dicionario (JSON)
    # Para instanciar um objeto
    def __init__(self, json_data):
        super().__init__(json_data)

    # Retornar uma piada aleatoria é uma regra de negocio especifica
    # Fazendo sentido manter somente para a model joke
    @classmethod
    def get_random(cls):
        data = cls.find()
        if not data:
            return 
        return random.choice(data)
    
    # Define as regras de como um joke model pode virar um dict
    def to_dict(self):
        return {
            'id': str(self.data['_id']),
            'joke': self.data['joke']
        }
