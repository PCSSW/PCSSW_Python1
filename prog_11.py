class Retangulo:
	"""Classe que define um retângulo"""
	def __init__(self, b, h):
		"""Construtor (b = base h = altura)"""
		self.__base = b
		self.__altura = h
	
	
	def mudar_valor_lados(self, nova_b, nova_h):
		"""Muda o valor dos lados (base e altura)"""
		if nova_b > 0 and nova_h > 0:
			self.__base = nova_b
			self.__altura = nova_h
		else:
			return False 
	
	
	def retornar_base(self):
		"""Retorna o valor da base"""
		if self.__base > 0:
		    return self.__base
		else:
			return False
		
	
	def retornar_altura(self):
		"""Retorna o valor da altura"""
		if self.__altura > 0:
		    return self.__altura
		else:
			return False
		
		
	def calcular_area(self):
		"""Calcula a área do retângulo (b * h)"""
		if self.__base > 0 and self.__altura > 0:
		    return self.__base * self.__altura
		else:
			return False
	
	
	def calcular_perimetro(self):
		"""Calcula o perímetro do retângulo (2(b + h))"""
		if self.__base > 0 and self.__altura > 0:
		    return 2 * (self.__base + self.__altura)
		else:
			return False
		
		
