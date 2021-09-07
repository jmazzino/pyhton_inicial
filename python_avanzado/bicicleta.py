from abc import ABC, abstractmethod

class Bike(ABC):
	shifts = 1
	
	def __init__(self, shifts):
		self.shifts = shifts
	
	@abstractmethod
	def moveForward(self, meters):
		pass
		
	@abstractmethod
	def stop(self):
		pass

class MTB(Bike):
	def moveForward(self, meters):
		print(f'Avance {meters} metros')
		
	def stop(self):
		print('Me detuve')
		
class Fixie(Bike):
	def moveForward(self, meters):
		print(f'Avance {meters} metros')
		
	def stop(self):
		print('Me detuve')

class BikeFactory(ABC):
	
	@abstractmethod
	def buildMTB(self):
		pass
	
	@abstractmethod
	def buildFixie(self):
		pass

class Specialized(BikeFactory):
	
	def buildMTB(self):
		return MTB(21)
	
	def buildFixie(self):
		return Fixie(1)

class Cannondale(BikeFactory):
	
	def buildMTB(self):
		return MTB(18)
	
	def buildFixie(self):
		return Fixie(1)



### main
if __name__ == "__main__":
    

    ## creación de las personas
    canndondalefixie = Cannondale.buildFixie
    #canndondalemtb = Cannondale.crear_mtb
    #specializedfixie = Specialized.crear_fixie
    #specializedmtb  =  Specialized.crear_mtb


    ## listas con las personas y maquinas de cafes para random
    print(f"repeticiones: {canndondalefixie}")
    #print(f"repeticiones: {canndondalemtb}")
    #print(f"repeticiones: {specializedfixie}")
    #print(f"repeticiones: {specializedmtb}")
