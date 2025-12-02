import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.font_registry():
    with dpg.font("fonts/NotoSans-Regular.ttf", 20) as font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)  # теперь правильно — внутри font

dpg.bind_font(font)

with dpg.window(label="Тест кириллицы", width=400, height=200):
    dpg.add_text("Привет, мир!")
    dpg.add_text("Съешь ещё этих мягких французских булок, да выпей же чаю")

dpg.create_viewport(title='Тест', width=400, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
