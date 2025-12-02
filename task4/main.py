from transport.client import Client
from transport.truck import Truck
from transport.train import Train
from transport.company import TransportCompany

def main():
    company = TransportCompany("ООО Транспорт")

    while True:
        print("\n=== Главное меню ===")
        print("1. Добавить клиента")
        print("2. Добавить транспорт")
        print("3. Показать список транспорта")
        print("4. Оптимизировать распределение грузов")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите имя клиента: ")
            weight = float(input("Введите вес груза (т): "))
            vip = input("VIP клиент? (y/n): ").lower() == "y"
            client = Client(name, weight, vip)
            company.add_client(client)
            print("Клиент добавлен!")

        elif choice == "2":
            t_type = input("Введите тип транспорта (truck/train): ").lower()
            capacity = float(input("Введите грузоподъемность (т): "))
            if t_type == "truck":
                color = input("Введите цвет грузовика: ")
                company.add_vehicle(Truck(capacity, color))
                print("Грузовик добавлен!")
            elif t_type == "train":
                cars = int(input("Введите количество вагонов: "))
                company.add_vehicle(Train(capacity, cars))
                print("Поезд добавлен!")
            else:
                print("Неизвестный тип транспорта")

        elif choice == "3":
            print("\nСписок транспорта:")
            for v in company.list_vehicles():
                print(v)

        elif choice == "4":
            company.optimize_cargo_distribution()
            print("Грузы распределены!")

        elif choice == "5":
            print("Выход из программы...")
            break

        else:
            print("Неверный выбор! Попробуйте снова.")

if __name__ == "__main__":
    main()
