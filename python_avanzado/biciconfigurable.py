class Director:
    
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def haceBici(self):
        bici = Bici()

        # Cuadro
        cuadro = self.__builder.getCuadro()
        bici.setCuadro(cuadro)

        # Tenga una determinada cantidad de ruedas (customizable)
        rueda = self.__builder.getRueda()
        bici.setRueda(rueda)
    
        # Tenga una determinada cantidad de asientos (customizable)
        asiento = self.__builder.getAsiento()
        bici.setAsiento(asiento)

        # Tenga una canasto adelante y/o atrás (customizable)
        canasto = self.__builder.getCanasto()
        bici.setCanasto(canasto)

        # Tenga una (o no) una lucecita (customizable)
        luz = self.__builder.getLuz()
        bici.setLuz(luz)

        # Tenga una (o no) motor (customizable)
        motor = self.__builder.getMotor()
        bici.setMotor(motor)

        # Tenga una (o no) GPS (customizable)
        gps = self.__builder.getGps()
        bici.setGps(gps)

        return Bici

class Bici:
    
    def __init__(self):
        self.__cuadro  = None
        self.__ruedas  = None
        self.__asiento = None
        self.__canasto = None
        self.__luz = None
        self.__motor = None
        self.__gps = None

    def setCuadro(self, cuadro):
        self.__cuadro = cuadro

    def setRueda(self, rueda):
        self.__ruedas = rueda

    def setAsiento(self, asiento):
        self.__asiento = asiento
    
    def setCanasto(self, canasto):
        self.__canasto = canasto

    def setLuz(self, luz):
        self.__luz = luz
        
    def setMotor(self, motor):
        self.__motor = motor
    
    def setGps(self, gps):
         self.__gps = gps

    def spec(self) -> None:
        print(f"Cuadro tipo : {self.__cuadro.tipo}")
        print(f"Ruedas rodado : {self.__ruedas.tipo}")
        # print(f"Asiento marca : {self.__asiento.tipo}")
        # print(f"Canasto marca: {self.__canasto.tipo}")
        # print(f"luz marca : {self.__luz.tipo}")
        # print(f"motor tipo : {self.__motor.tipo}")
        # print(f"gps marca: {self.__gps.tipo}")


class Builder:

    def getCuadro(self): pass
    def getRueda(self): pass
    def getAsiento(self): pass
    def getCanasto(self): pass
    def getLuz(self): pass
    def getMotor(self): pass
    def getGps(self): pass


class FabricamosMTB(Builder):

    def getCuadro(self):
        cuadro = Cuadro()
        cuadro.tipo = "MTB"
        return cuadro
    
    def getRueda(self):
        rueda = Rueda()
        rueda.tipo = "Rodado 29"
        return rueda

    def getAsiento(self):
        asiento = Asiento()
        asiento.tipo = "VELO"
        return asiento

    def getCanasto(self):
        canasto = Canasto()
        canasto.tipo = "VELO"
        return canasto

    def getLuz(self):
        luz = Luz()
        luz.tipo = "Luminosa"
        return luz

    def getMotor(self):
        motor = Motor()
        motor.tipo = "Asistido"
        return motor
    
    def getGps(self):
        gps = Gps()
        gps.tipo = "Garmin"
        return gps

class FabricamosFIXIE(Builder):

    def getCuadro(self):
        cuadro = Cuadro()
        cuadro.tipo = "FIXIE"
        return cuadro
    
    def getRueda(self):
        rueda = Rueda()
        rueda.tipo = "Rodado 28"
        return rueda

    def getAsiento(self):
        asiento = Asiento()
        asiento.tipo = "VELO"
        return asiento

    def getCanasto(self):
        canasto = Canasto()
        canasto.tipo = "NO TIENE"
        return canasto

    def getLuz(self):
        luz = Luz()
        luz.tipo = "POCO LUMINOSA"
        return luz

    def getMotor(self):
        motor = Motor()
        motor.tipo = "NO TIENE"
        return motor
    
    def getGps(self):
        gps = Gps()
        gps.tipo = "NO TIENE"
        return gps


# Bici parts
class Cuadro:
    tipo = None

class Rueda:
    tipo = None

class Asiento:
    tipo = None

class Canasto:
    tipo = None

class Luz:
    tipo = None

class Motor:
    tipo = None

class Gps:
    tipo = None

def main():
    director = Director()

    mtbBuilder = FabricamosMTB()
    fixieBuilder = FabricamosFIXIE()
    #director.haceBici = mtbBuilder
        

    # Build Jeep
    print ("Descripcion Bicicleta MTB")
    director.setBuilder(mtbBuilder)
    mtb = director.haceBici()
    mtb.spec(Bici)

    print ("")

    # Build Nissan
    print ("Descripcion Bicicleta FIXIE")
    director.setBuilder(fixieBuilder)
    fixie = director.haceBici()
    fixie.spec()

if __name__ == "__main__":
    main()