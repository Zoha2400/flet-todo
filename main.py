import flet as ft
import keyboard
from flet import TextField, Row, Text, Checkbox, FloatingActionButton
import keyboard as kb


def main(page: ft.Page):
    page.title = "ToDo App"
    page.window_width = 400
    page.window_height = 550
    page.window_max_width = 400
    page.window_max_height = 550


    new_task_value = ""

    error = False


    def add_click(e):
        nonlocal new_task_value
        nonlocal error

        if task_input.value:
            if error:
                task_input.bgcolor = 'transparent'
                task_input.hint_text = 'Do you have something to do'
            new_task_value = task_input.value
            page.add(Checkbox(label=new_task_value))
            task_input.value = ''
            page.update()
        else:
            task_input.bgcolor = 'red'
            task_input.hint_text = 'You need type something!'
            error = True
            page.update()



    task_input = TextField(hint_text='Do you have something to do...?', width=270, height=50)
    task_button = FloatingActionButton(icon=ft.icons.ADD, on_click=add_click, width=50, height=50, bgcolor="green")


    page.add(
        Row(
            [
                task_input,
                task_button
            ], alignment=ft.MainAxisAlignment.SPACE_AROUND
        ),

    )


ft.app(target=main)
