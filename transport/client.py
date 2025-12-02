class Client:
    def __init__(self, name: str, cargo_weight: float, is_vip: bool = False):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя клиента должно быть непустой строкой")
        if not isinstance(cargo_weight, (int, float)) or cargo_weight <= 0:
            raise ValueError("Вес груза должен быть положительным числом")
        if not isinstance(is_vip, bool):
            raise ValueError("VIP-статус должен быть булевым значением")

        self.name = name
        self.cargo_weight = cargo_weight
        self.is_vip = is_vip

    def __str__(self):
        return f"Клиент: {self.name}, груз: {self.cargo_weight}т, VIP: {self.is_vip}"
