import flet as ft
import utils
card_data = utils.card_data
palette = utils.palette

def input(placeholder, type, name, options=[], size=6):
    match type:
        case 'text':
            return ft.Column(
                col={"sm": 12, "md": size, "lg": size},
                controls=[
                    ft.Container(
                        shadow=ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=4,
                            color=ft.Colors.BLACK,
                            offset=ft.Offset(0, 4)
                        ),
                        content=ft.TextField(
                            bgcolor=palette['blue'],
                            color=palette['white'],
                            border=ft.InputBorder.NONE,
                            content_padding=25,
                            hint_text=placeholder,
                            hint_style=ft.TextStyle(color=palette['grey']),
                            on_change=lambda e: set_value(name, e.control.value),
                            ),
                        border_radius=10,
                    )
                ]
            )
        case 'number':
            return ft.Column(
                col={"sm": 12, "md": size, "lg": size},
                controls=[
                    ft.Container(
                        shadow=ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=4,
                            color=ft.Colors.BLACK,
                            offset=ft.Offset(0, 4)
                        ),
                        content=ft.TextField(
                            input_filter=ft.NumbersOnlyInputFilter(),
                            bgcolor=palette['blue'],
                            color=palette['white'],
                            border=ft.InputBorder.NONE,
                            content_padding=25,
                            hint_text=placeholder,
                            hint_style=ft.TextStyle(color=palette['grey']),
                            on_change=lambda e: set_value(name, e.control.value),
                            ),
                        border_radius=10,
                    )
                ]
            )
        case 'dropdown':
            return ft.Column(
                col={"sm": 12, "md": size, "lg": size},
                controls=[
                    ft.Container(
                        shadow=ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=4,
                            color=ft.Colors.BLACK,
                            offset=ft.Offset(0, 4)
                        ),
                        content=ft.Dropdown(
                            hint_text="Tipo de VRAM",
                            hint_style=ft.TextStyle(color=palette['grey']),
                            bgcolor=palette['blue'],
                            color=palette['white'],
                            border=ft.InputBorder.NONE,
                            enable_filter=True,
                            content_padding=25,
                            width=1920,
                            options=get_options(options),
                            on_change=lambda e: dropdown_changed(name, e.control.value),
                        ),
                        border_radius=10,
                        bgcolor=palette['blue'],
                        expand=True
                    )
                ]
            )
            


def set_value(type, new_value):
    card_data[type] = new_value

def dropdown_changed(type, new_value):
    card_data[type] = new_value

def get_options(options):
    print('options')
    
    flet_options = []
    for option in options:
        flet_options.append(
            ft.DropdownOption(
                key=option,
                content=ft.Text(
                    value=option,
                    color=palette['white'],
            ),
        ))
    return flet_options

