from abc import ABC, abstractmethod

# Clase abstracta para anviar mensajes
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje: str):
        pass

""" Clases específicas que cumplen implementaciones específicas
para enviar notificaciones"""
class Email(Notificador):
    def enviar(self, mensaje: str):
        print(f"[EMAIL] Enviando mensaje: {mensaje}")

class Push(Notificador):
    def enviar(self, mensaje: str):
        print(f"[PUSH] Enviando mensaje: {mensaje}")

class SMS(Notificador):
    def enviar(self, mensaje: str):
        print(f"[SMS] Enviando mensaje: {mensaje}")

""" Clase del sistema que puede implementar cualquiera de las
implementaciones espcífcias"""    

class SistemaDeNotificaciones:
    def __init__(self, notificador: Notificador):
        self.notificador = notificador

    def notificar(self, mensaje: str):
        self.notificador.enviar(mensaje)


if __name__ == "__main__":
    # Objetos para cada implementación
    email_notif = Email()
    push_notif = Push()
    sms_notif = SMS()

    # Sistema puede usar cualquier notificador (cumple LSP y DIP)
    sistema1 = SistemaDeNotificaciones(Email())
    sistema2 = SistemaDeNotificaciones(push_notif)
    sistema3 = SistemaDeNotificaciones(sms_notif)

    sistema1.notificar("Reunión a las 10:00")
    sistema2.notificar("Tienes una nueva tarea asignada")
    sistema3.notificar("Código de verificación: 123456")
