# Vigilante:
# 1 huevo
# 10g de harina
# 20 g de crema pastelera.
import configparser

config = configparser.ConfigParser()
config.read('GASTOS.ENV')
var_agua = config.get("GASTOS", "AGUA")
var_luz = config.get("GASTOS", "LUZ")

class GastosFijos(object):
    
    
    def __new__(cls, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(GastosFijos, cls).__new__(cls)
            cls._instance.agua = kwargs.get("agua")
            cls._instance.luz = kwargs.get("luz")
            
        return cls._instance
    

# Genera instancia de MiSingleton
s = GastosFijos(**{"agua":{var_agua},"luz":{var_luz}})

print(f'Objeto s - propiedad AGUA: {s.agua}')
print(f'Objeto s - propiedad LUZ: {s.luz}')
print("##################################")
