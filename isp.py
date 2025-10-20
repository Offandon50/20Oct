# Clase base (aunque creo que es opcional en este ejercicio)
class Impresora:
    def __init__(self):
        #Atributos comunes
        pass

    def imprimir(self):
        print("Imprimiendo...")

class ImprimeBN(Impresora):
    def imprimir(self):
        print("Imprimiento en B/N")

class ImprimeColor(Impresora):
    def imrpimir(self):
        print("Imprimiendo a color")

class Multifunción(ImprimeColor):
    def escanear(self):
        print("Escaneando")

    def fax(self):
        print("Enviando fax")

""" COMPROBACIÓN -- Cada rol es independiente y definido -- 
ImpresoraMultifuncion implementa varias interfaces
porque realmente presta todas esas funciones."""

impresora_color = ImprimeColor()
impresora_bn = ImprimeBN()
impresora_multi = Multifunción()

if __name__ == "__main__":
    impresora_color.imrpimir()
    impresora_bn.imprimir()
    impresora_multi.fax()
