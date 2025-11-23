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

    def get_member_by_id(self, member_id):
        return self.miembros.get(member_id)

    def update_member(self, member_id, nombre=None, telefono=None):
        member = self.get_member_by_id(member_id)
        if member:
            if nombre: member.nombre = nombre
            if telefono: member.telefono = telefono
            return True
        return False

system = GymSystem()

if __name__ == "__main__":
    print("Sistema Fit Zone RD iniciado")
    
    #Prueba Update
    u1 = system.create_member("José Castillo", "809-555-0001", "2024-01-15")
    system.update_member(u1.id, nombre="Juan Actualizado")
    print(f"Nombre nuevo: {system.get_member_by_id(u1.id).nombre}")
