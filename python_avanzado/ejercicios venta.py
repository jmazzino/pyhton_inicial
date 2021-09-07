""" Les dejo la consigna del ejercicio que comenzamos a hacer ayer sobre diseño orientado a objetos. Requerimos tener personas (con nombre y apellido) que tengan cuenta bancaria, en la cual se puede modificar el saldo de dos maneras: extraer dinero o depositar dinero.
Se destaca que las personas pueden comprarse y venderse cosas mutuamente. Si bien no tiene relevancia cuáles son esas cosas, sí es relevante el monto de esas compras y ventas. Así, el saldo de las respectivas cuentas bancarias, debe "acomodarse" sólo. Es decir, debe poder reflejar el saldo correcto después de llevar a cabo la operación.


Ejemplo


Escenario
Persona A (Esteban Quito) tiene una cuenta bancaria con $10000 de saldo.
Persona B (Elsa Capunta) tiene una cuenta bancaria con $15000 de saldo.
Persona C (Susana Oria) tiene una cuenta bancaria con $0 de saldo.

Eventos
Elsa Capunta le compra algo de $1000 a Esteban Quito.
Susana Oria le vende algo de $2000 a Esteban Quito.

Resultado
Esteban Quito tiene su cuenta bancaria con $9000 de saldo.
A su vez, Elsa Capunta tiene su cuenta bancaria con $14000 de saldo.
Por último, Susana Oria queda con $2000 de saldo en su cuenta bancaria. """
#!/usr/bin/python3

class CuentaBancaria:
	def __init__(self, saldo):
		self.__saldo = saldo
		
	
	@property
	def saldo(self):
		return self.__saldo
	
	def depositar(self, monto):
		self.__saldo += monto
	
	def retirar(self, monto):
		if monto > self.__saldo:
			raise ValueError('Saldo insuficiente')
		else:
			self.__saldo -= monto

class Persona:
	def __init__(self, nombre, apellido, cuenta_bancaria):
		self.__nombre = nombre
		self.__apellido = apellido
		self.__mi_cuenta = cuenta_bancaria
	
	@property
	def nombre(self):
		return self.__nombre
	
	@property
	def apellido(self):
		return self.__apellido
	
	def pagame(self, precio):
		self.__mi_cuenta.retirar(precio)
		return precio
	
	def te_pago(self, precio):
		self.__mi_cuenta.depositar(precio)
	
	def vende(self, comprador, precio):
		self.__mi_cuenta.depositar(comprador.pagame(precio))
	
	def compra(self, vendedor, precio):
		self.__mi_cuenta.retirar(precio)
		vendedor.te_pago(precio)
	
	def cuanto_tenes(self):
		return self.__mi_cuenta.saldo

if __name__ == '__main__':
	esteban = Persona('Esteban', 'Quito', CuentaBancaria(10000))
	elsa = Persona('Elsa', 'Capunta', CuentaBancaria(15000))
	susana = Persona('Susana', 'Oria', CuentaBancaria(0))
	
	print(f'Elsa tiene ${elsa.cuanto_tenes()} en el banco')
	print(f'Esteban tiene ${esteban.cuanto_tenes()} en el banco')
	elsa.compra(esteban, 1000)
	print('Elsa le compró un lápiz de $1000 a Esteban')
	print(f'Elsa tiene ahora ${elsa.cuanto_tenes()} en el banco')
	print(f'Esteban tiene ahora ${esteban.cuanto_tenes()} en el banco')
	print(f'Susana tiene ${susana.cuanto_tenes()} en el banco')
	susana.vende(esteban, 2000)
	print('Susana le vendió un almohadón de $2000 a Esteban')
	print(f'Susana tiene ahora ${susana.cuanto_tenes()} en el banco')
	print(f'Esteban tiene ahora ${esteban.cuanto_tenes()} en el banco')