class Client:
    def __init__(self, name: str, weight: float, vip: bool = False):
        self.name = name
        self.weight = weight
        self.vip = vip

    def __repr__(self):
        return f"Client({self.name}, {self.weight}, {'VIP' if self.vip else 'обычный'})"


class Transport:
    _id_counter = 1

    def __init__(self, capacity: float):
        self.id = Transport._id_counter
        Transport._id_counter += 1
        self.capacity = capacity
        self.load = 0
        self.clients = []

    def can_take(self, client: Client) -> bool:
        return self.load + client.weight <= self.capacity

    def add_client(self, client: Client):
        if self.can_take(client):
            self.clients.append(client)
            self.load += client.weight
            return True
        return False

    def __repr__(self):
        return f"Transport(ID={self.id}, cap={self.capacity}, load={self.load})"


class Truck(Transport):
    def __init__(self, capacity: float):
        super().__init__(capacity)


class Train(Transport):
    def __init__(self, capacity: float):
        super().__init__(capacity)


class TransportCompany:
    def __init__(self, name: str):
        self.name = name
        self.clients = []
        self.transports = []

    def add_client(self, client: Client):
        self.clients.append(client)

    def add_transport(self, transport: Transport):
        self.transports.append(transport)

    def distribute(self):
        results = []
        # VIP клиенты распределяются первыми
        sorted_clients = sorted(self.clients, key=lambda c: not c.vip)
        for client in sorted_clients:
            placed = False
            for transport in self.transports:
                if transport.add_client(client):
                    results.append({
                        "client": client.name,
                        "weight": client.weight,
                        "vip": client.vip,
                        "transport_id": transport.id
                    })
                    placed = True
                    break
            if not placed:
                results.append({
                    "client": client.name,
                    "weight": client.weight,
                    "vip": client.vip,
                    "transport_id": None
                })
        return results


# Пример использования при запуске напрямую
if __name__ == "__main__":
    company = TransportCompany("Rhythora")
    c1 = Client("Иван", 120, vip=True)
    c2 = Client("Петр", 80)
    t1 = Truck(200)
    t2 = Train(500)

    company.add_client(c1)
    company.add_client(c2)
    company.add_transport(t1)
    company.add_transport(t2)

    result = company.distribute()
    for r in result:
        print(r)
