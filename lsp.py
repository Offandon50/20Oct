# Clase base
class Vehiculo:
    def __init__(self):
        self.acelerar_secs = 0
        self.frenar_secs = 0

    def acelerar(self):
        print(f"El vehículo aceleró en {self.acelerar_secs} segundos")

    def frenar(self):
        print(f"El vehículo frenó en {self.frenar_secs} segundos")

# Clases hijas
class Bicicleta(Vehiculo):
    def __init__ (self):
        self.acelerar_secs = 10
        self.frenar_secs = 3


class Coche(Vehiculo):
    def __init__ (self):
        self.acelerar_secs = 5
        self.frenar_secs = 5     

class Moto(Vehiculo):
    def __init__ (self):
        self.acelerar_secs = 3
        self.frenar_secs = 7    

# Las clases hijas pueden sustituir a la clase base en sus métodos
bici = Bicicleta()
coche = Coche()
moto = Moto()

bici.acelerar()
coche.acelerar()
moto.acelerar()