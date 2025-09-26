import flet as ft

def main(page: ft.Page):
    page.title = "To-Do список"
    page.theme_mode = ft.ThemeMode.LIGHT

    tasks_column = ft.Column()


    task_input = ft.TextField(label="Новая задача", width=300)

    def add_task(e):
        task_text = task_input.value.strip()
        if task_text:
            task_field = ft.Text(task_text)
            task_edit = ft.TextField(value=task_text, visible=False)


            def edit_task(ev):
                task_field.visible = False
                task_edit.visible = True
                edit_button.visible = False
                save_button.visible = True
                page.update()

        
            def save_task(ev):
                task_field.value = task_edit.value
                task_field.visible = True
                task_edit.visible = False
                edit_button.visible = True
                save_button.visible = False
                page.update()

            def delete_task(ev):
                tasks_column.controls.remove(task_row)
                page.update()

            edit_button = ft.ElevatedButton("Редактировать", on_click=edit_task)
            save_button = ft.ElevatedButton("Сохранить", on_click=save_task, visible=False)
            delete_button = ft.ElevatedButton(
                "Удалить", 
                color="white", 
                bgcolor="red", 
                on_click=delete_task
            )

            
            task_row = ft.Row(
                [task_field, task_edit, edit_button, save_button, delete_button],
                alignment="spaceBetween"
            )

            tasks_column.controls.append(task_row)
            task_input.value = ""
            page.update()

    
    add_button = ft.ElevatedButton("Добавить", on_click=add_task)

    
    page.add(
        ft.Row([task_input, add_button]),
        tasks_column
    )

ft.app(target=main)
