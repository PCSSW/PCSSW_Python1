class Retangulo:
    """Classe que define um retângulo"""
    def __init__(self,b, h):
        """Construtor (b = base h = altura)"""
        self.__base = b
        self.__altura = h


    def mudar_valor_lados(self, novo_b, novo_h):
        """Muda o valor dos lados(base, altura)"""
        self.__base = novo_b
        self.__altura = novo_h


    def retornar_valor_lados(self):
        """Retorna o valor da base"""
        return self.__base


    def retornar_valor_lados(self):
        """Retorna o valor da altura"""
        return self.__altura

