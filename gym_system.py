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

    def create_member(self, nombre, telefono, fecha_pago):
        new_member = Miembro(self.next_id, nombre, telefono, fecha_pago)
        self.miembros[self.next_id] = new_member
        self.next_id += 1
        return new_member

system = GymSystem()

if __name__ == "__main__":
    print("Sistema Fit Zone RD iniciado")
    
    #Prueba Create
    system.create_member("José Castillo", "809-555-0001", "2024-01-15")
    print(f"Miembros: {len(system.get_all_members())}")