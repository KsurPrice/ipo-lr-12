# Класс TransportCompany — копия из transport/company.py
from task1.client import Client
from task2.vehicle import Vehicle

class TransportCompany:
    def __init__(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название компании должно быть строкой")
        self.name = name
        self.vehicles = []
        self.clients = []

    def add_vehicle(self, vehicle: Vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Ожидается объект класса Vehicle")
        self.vehicles.append(vehicle)

    def list_vehicles(self):
        return [str(v) for v in self.vehicles]

    def add_client(self, client: Client):
        if not isinstance(client, Client):
            raise TypeError("Ожидается объект класса Client")
        self.clients.append(client)

    def optimize_cargo_distribution(self):
        sorted_clients = sorted(self.clients, key=lambda c: not c.is_vip)
        for client in sorted_clients:
            for vehicle in self.vehicles:
                if vehicle.current_load + client.cargo_weight <= vehicle.capacity:
                    vehicle.load_cargo(client)
                    break
