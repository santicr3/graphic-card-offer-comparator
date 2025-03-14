import flet as ft
import utils
card_data = utils.card_data
palette = utils.palette

def input(placeholder, type, name, options=[], size=6):
    match type:
        case 'text':
            input = ft.TextField(
                            bgcolor=palette['blue'],
                            color=palette['white'],
                            border=ft.InputBorder.NONE,
                            content_padding=25,
                            label=placeholder,
                            hint_style=ft.TextStyle(color=palette['grey']),
                            on_change=lambda e: set_value(name, e.control.value),
                            )
            input_wrap = ft.Column(
                col={"sm": 12, "md": size, "lg": size},
                controls=[
                    ft.Container(
                        shadow=ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=4,
                            color=ft.Colors.BLACK,
                            offset=ft.Offset(0, 4)
                        ),
                        content=input,
                        border_radius=10,
                    )
                ]
            )
            return input, input_wrap
        case 'number':
            input = ft.TextField(
                            input_filter=ft.InputFilter(allow=True, regex_string=r'^\d*([.,]?\d*)?$', replacement_string=""),
                            bgcolor=palette['blue'],
                            color=palette['white'],
                            border=ft.InputBorder.NONE,
                            content_padding=25,
                            label=placeholder,
                            hint_style=ft.TextStyle(color=palette['grey']),
                            on_change=lambda e: set_value(name, e.control.value),
                            )
            input_wrap = ft.Column(
                col={"sm": 12, "md": size, "lg": size},
                controls=[
                    ft.Container(
                        shadow=ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=4,
                            color=ft.Colors.BLACK,
                            offset=ft.Offset(0, 4)
                        ),
                        content=input,
                        border_radius=10,
                    )
                ]
            )
            return input, input_wrap
        case 'dropdown':
            input =ft.Dropdown(
                            label="Tipo de VRAM",
                            hint_style=ft.TextStyle(color=palette['grey']),
                            bgcolor=palette['blue'],
                            color=palette['white'],
                            border=ft.InputBorder.NONE,
                            enable_filter=True,
                            content_padding=25,
                            width=1920,
                            options=get_options(options),
                            on_change=lambda e: dropdown_changed(name, e.control.value),
                        )
            input_wrap = ft.Column(
                col={"sm": 12, "md": size, "lg": size},
                controls=[
                    ft.Container(
                        shadow=ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=4,
                            color=ft.Colors.BLACK,
                            offset=ft.Offset(0, 4)
                        ),
                        bgcolor=palette['blue'],
                        content=input,
                        border_radius=10,
                    )
                ]
            )
            return input, input_wrap
            


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

