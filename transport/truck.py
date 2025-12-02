from transport.vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, capacity: float, color: str):
        super().__init__(capacity)
        if not isinstance(color, str) or not color.strip():
            raise ValueError("Цвет должен быть строкой")
        self.color = color

    def __str__(self):
        return f"Грузовик {self.vehicle_id}, цвет: {self.color}, грузоподъемность: {self.capacity}т, загружено: {self.current_load}т"
