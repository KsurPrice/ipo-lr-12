from task2.vehicle import Vehicle
from task1.client import Client


def main():
    print("=== Задание 2: Работа с транспортом ===")
    # Запрашиваем грузоподъемность транспорта
    capacity = float(input("Введите грузоподъемность транспорта (т): "))
    vehicle = Vehicle(capacity)

    # Запрашиваем данные клиента
    name = input("Введите имя клиента: ")
    weight = float(input("Введите вес груза (т): "))
    vip = input("VIP клиент? (y/n): ").lower() == "y"
    client = Client(name, weight, vip)

    # Загружаем груз
    try:
        vehicle.load_cargo(client)
        print("\nПосле загрузки клиента транспорт выглядит так:")
        print(vehicle)
    except ValueError as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    main()
