from client import Client

def main():
    print("=== Задание 1: Создание клиента ===")
    # Запрашиваем данные у пользователя
    name = input("Введите имя клиента: ")
    weight = float(input("Введите вес груза (т): "))
    vip = input("VIP клиент? (y/n): ").lower() == "y"

    # Создаем объект клиента
    client = Client(name, weight, vip)

    # Выводим результат
    print("\nСоздан клиент:")
    print(client)

if __name__ == "__main__":
    main()
