class Miembro:
    def __init__(self, id, nombre, telefono, fecha_pago):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.fecha_pago = fecha_pago

class GymSystem:
    def __init__(self):
        self.miembros = {}
        self.next_id = 1

    def get_all_members(self):
        return self.miembros

system = GymSystem()

if __name__ == "__main__":
    print("Sistema Fit Zone RD iniciado")