# Импортируем библиотеку DearPyGui для создания графического интерфейса
import dearpygui.dearpygui as dpg

# Импортируем наши классы из пакета transport
from transport.client import Client
from transport.truck import Truck
from transport.train import Train
from transport.company import TransportCompany

# Импортируем модуль json для экспорта результатов
import json

# Списки для хранения клиентов и транспорта
clients = []
vehicles = []

# Создаём объект компании
company = TransportCompany("ООО Транспорт")

# ---------- Инициализация GUI ----------
dpg.create_context()  # создаём контекст DearPyGui

# Подключаем шрифт с поддержкой кириллицы
with dpg.font_registry():
    with dpg.font("fonts/NotoSans-Regular.ttf", 18) as default_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
dpg.bind_font(default_font)  # назначаем шрифт по умолчанию

# ---------- Добавление клиента ----------
def show_add_client():
    # Создаём модальное окно для ввода данных клиента
    with dpg.window(label="Добавить клиента", modal=True, width=300, height=200, tag="add_client_window"):
        dpg.add_input_text(label="Имя", tag="client_name")          # поле ввода имени
        dpg.add_input_text(label="Вес груза", tag="client_weight")  # поле ввода веса
        dpg.add_checkbox(label="VIP", tag="client_vip")             # чекбокс для VIP-статуса
        dpg.add_button(label="Сохранить", callback=add_client_callback)  # кнопка сохранить
        dpg.add_button(label="Отмена", callback=lambda: dpg.delete_item("add_client_window"))  # кнопка отмена

def add_client_callback():
    # Получаем значения из полей ввода
    name = dpg.get_value("client_name")
    weight = dpg.get_value("client_weight")
    vip = dpg.get_value("client_vip")

    # Проверка имени
    if not name.strip():
        dpg.configure_item("status_bar", default_value="Ошибка: имя некорректно")
        return

    # Проверка веса
    try:
        w = float(weight)
        if w <= 0 or w > 10000:
            raise ValueError
    except ValueError:
        dpg.configure_item("status_bar", default_value="Ошибка: вес некорректен")
        return

    # Создаём клиента и добавляем в список и компанию
    c = Client(name, w, vip)
    clients.append(c)
    company.add_client(c)

    # Добавляем строку в таблицу клиентов
    with dpg.table_row(parent="clients_table"):
        dpg.add_table_cell(); dpg.add_text(c.name)
        dpg.add_table_cell(); dpg.add_text(str(c.cargo_weight))
        dpg.add_table_cell(); dpg.add_text("VIP" if c.is_vip else "обычный")

    # Обновляем статус
    dpg.configure_item("status_bar", default_value="Клиент добавлен")

# ---------- Добавление транспорта ----------
def show_add_transport():
    # Создаём модальное окно для ввода данных транспорта
    with dpg.window(label="Добавить транспорт", modal=True, width=300, height=250, tag="add_transport_window"):
        dpg.add_combo(["Грузовик", "Поезд"], label="Тип", tag="transport_type")  # выбор типа
        dpg.add_input_text(label="Грузоподъемность", tag="transport_capacity")   # поле ввода грузоподъёмности
        dpg.add_input_text(label="Цвет (для грузовика)", tag="truck_color")      # поле для цвета
        dpg.add_input_text(label="Количество вагонов (для поезда)", tag="train_cars")  # поле для вагонов
        dpg.add_button(label="Сохранить", callback=add_transport_callback)       # кнопка сохранить
        dpg.add_button(label="Отмена", callback=lambda: dpg.delete_item("add_transport_window"))  # кнопка отмена

def add_transport_callback():
    # Получаем значения из полей
    t_type = dpg.get_value("transport_type")
    capacity = dpg.get_value("transport_capacity")

    # Проверка грузоподъёмности
    try:
        cap = float(capacity)
        if cap <= 0:
            raise ValueError
    except ValueError:
        dpg.configure_item("status_bar", default_value="Ошибка: грузоподъемность должна быть >0")
        return

    # Создаём объект транспорта
    if t_type == "Грузовик":
        color = dpg.get_value("truck_color") or "не указан"
        t = Truck(cap, color)
    else:
        try:
            cars = int(dpg.get_value("train_cars"))
            if cars <= 0:
                raise ValueError
        except ValueError:
            dpg.configure_item("status_bar", default_value="Ошибка: количество вагонов должно быть >0")
            return
        t = Train(cap, cars)

    # Добавляем транспорт в список и компанию
    vehicles.append(t)
    company.add_vehicle(t)

    # Добавляем строку в таблицу транспорта
    with dpg.table_row(parent="vehicles_table"):
        dpg.add_table_cell(); dpg.add_text(str(t.vehicle_id))
        dpg.add_table_cell(); dpg.add_text(t.__class__.__name__)
        dpg.add_table_cell(); dpg.add_text(str(t.capacity))
        dpg.add_table_cell(); dpg.add_text(str(t.current_load))
        if isinstance(t, Truck):
            dpg.add_table_cell(); dpg.add_text(t.color)
        elif isinstance(t, Train):
            dpg.add_table_cell(); dpg.add_text(str(t.number_of_cars))

    # Обновляем статус
    dpg.configure_item("status_bar", default_value="Транспорт добавлен")

# ---------- Распределение грузов ----------
def run_optimizer():
    # Проверяем наличие данных
    if not clients or not vehicles:
        dpg.configure_item("status_bar", default_value="Нет данных для распределения")
        return
    # Запускаем оптимизацию
    company.optimize_cargo_distribution()
    dpg.configure_item("status_bar", default_value="Грузы распределены")

# ---------- Экспорт результатов ----------
def export_results():
    # Формируем словарь для экспорта
    data = {
        "clients": [str(c) for c in company.clients],
        "vehicles": [str(v) for v in company.vehicles]
    }
    # Сохраняем в JSON
    with open("result.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    dpg.configure_item("status_bar", default_value="Результаты сохранены в result.json")

# ---------- О программе ----------
def show_about():
    # Создаём окно с информацией
    with dpg.window(label="О программе", modal=True, width=300, height=150):
        dpg.add_text("ЛР13, Вариант 1")
        dpg.add_text("Разработчик: Илья")

# ---------- Главное окно ----------
with dpg.window(label="Главное окно", width=900, height=600):
    # Меню
    with dpg.menu_bar():
        with dpg.menu(label="Файл"):
            dpg.add_menu_item(label="Экспорт результата", callback=export_results)
        with dpg.menu(label="О программе"):
            dpg.add_menu_item(label="Инфо", callback=show_about)

    # Кнопки управления
    dpg.add_button(label="Добавить клиента", callback=show_add_client)
    dpg.add_button(label="Добавить транспорт", callback=show_add_transport)
    dpg.add_button(label="Распределить грузы", callback=run_optimizer)

    # Таблица клиентов
    with dpg.table(tag="clients_table", header_row=True):
        dpg.add_table_column(label="Имя")
        dpg.add_table_column(label="Вес")
        dpg.add_table_column(label="Статус")

    # Таблица транспорта
    with dpg.table(tag="vehicles_table", header_row=True):
        dpg.add_table_column(label="ID")
        dpg.add_table_column(label="Тип")
        dpg.add_table_column(label="Грузоподъемность")
        dpg.add_table_column(label="Загрузка")
        dpg.add_table_column(label="Цвет/Вагоны")

    # Статусная строка
    dpg.add_input_text(tag="status_bar", readonly=True, default_value="Готово", width=600)

# ---------- Запуск приложения ----------
dpg.create_viewport(title='ЛР13 GUI', width=900, height=600)  # создаём окно приложения
dpg.setup_dearpygui()   # настраиваем DearPyGui
dpg.show_viewport()     # показываем окно
dpg.start_dearpygui()   # запускаем главный цикл
dpg.destroy_context()   # уничтожаем контекст после выхода
