# Домашнее задание 4 📚 (57 1-2)

import flet as ft 
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Моё первое приложение!'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text(value="Hello world!")
    greeting_history = []
    history_text = ft.Text("История приветствий:")

    history_visible = True

    def on_button_click(_):
        name = name_input.value.strip()
        if name:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            greeting_text.value = f"Hello {name}! Время: {current_time}"
            name_input.value = ''
            greeting_history.append(f'{name} — {current_time}')
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = "Пожалуйста, введите имя!"
        page.update()

    def clear_history(_):
        greeting_history.clear()
        history_text.value = "История приветствий"
        page.update()

    def change_button(_):
        nonlocal history_visible
        history_visible = not history_visible
        history_text.visible = history_visible
        page.update()

    def change_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT  
        page.update()

    name_input = ft.TextField(label="Введите имя", on_submit=on_button_click)
    name_button = ft.ElevatedButton(text='SEND', on_click=on_button_click)
    clean_history_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    toggle_history_button = ft.IconButton(icon=ft.Icons.VISIBILITY, on_click=change_button, tooltip="Скрыть/Показать историю")
    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=change_theme, tooltip='Cменить тему')

    page.add(greeting_text, name_input, name_button, clean_history_button, toggle_history_button, theme_button, history_text)

ft.app(target=main, view=ft.WEB_BROWSER)
