from task3.company import TransportCompany
from task3.truck import Truck
from task3.train import Train
from task1.client import Client

def main():
    print("=== Задание 3: Транспортная компания ===")
    company = TransportCompany("Тестовая компания")

    # Добавляем транспорт
    print("\nДобавление транспорта:")
    t_type = input("Введите тип транспорта (truck/train): ").lower()
    capacity = float(input("Введите грузоподъемность (т): "))
    if t_type == "truck":
        color = input("Введите цвет грузовика: ")
        company.add_vehicle(Truck(capacity, color))
    elif t_type == "train":
        cars = int(input("Введите количество вагонов: "))
        company.add_vehicle(Train(capacity, cars))
    else:
        print("Неизвестный тип транспорта")

    # Добавляем клиентов
    print("\nДобавление клиентов:")
    count = int(input("Сколько клиентов добавить? "))
    for i in range(count):
        name = input(f"Введите имя клиента {i+1}: ")
        weight = float(input("Введите вес груза (т): "))
        vip = input("VIP клиент? (y/n): ").lower() == "y"
        company.add_client(Client(name, weight, vip))

    # Оптимизация распределения
    print("\nОптимизация распределения грузов...")
    company.optimize_cargo_distribution()

    # Выводим транспорт
    print("\nСписок транспорта после распределения:")
    for v in company.list_vehicles():
        print(v)

if __name__ == "__main__":
    main()
