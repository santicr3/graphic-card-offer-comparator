import flet as ft
import requests
import custom_components
import utils

def main(page: ft.Page):

    card_data = utils.card_data
    palette = utils.palette

    model = custom_components.input('Nombre del modelo...', 'text', 'model')
    price = custom_components.input('Precio...', 'number', 'price')
        
    vram_size = custom_components.input('Tamaño de VRAM', 'number', 'vram_size')
    vram_type = custom_components.input('Tipo de VRAM', 'dropdown', 'vram_type', ['GDDR3', 'GDDR4', 'GDDR5', 'GDDR6', 'GDDR6X', 'GDDR7', 5])

    hdmi_ports = custom_components.input('HDMI Ports...', 'number', 'hdmi_ports', size=4)
    dp_ports = custom_components.input('DisplayPort Ports...', 'number', 'dp_ports', size=4)
    consume = custom_components.input('Energetic consume...', 'number', 'consume', size=4)

    def submit(e):
        print(f"http://127.0.0.1:5000/grafica/{card_data['price']}/{card_data['vram_size']}/{card_data['hdmi_ports']}/{card_data['dp_ports']}/{card_data['consume']}/{card_data['vram_type']}")
        response = requests.get(f"http://127.0.0.1:5000/grafica/{card_data['price']}/{card_data['vram_size']}/{card_data['hdmi_ports']}/{card_data['dp_ports']}/{card_data['consume']}/{card_data['vram_type']}")
        if response.status_code == 200:
            result_text.value = response.json()["title"]
            page.update()
        print(response.json())

    def clean(e):
        card_data = {
        'model': '',
        'price': 0.0,
        'vram_size': 0,
        'vram_type': ' ',
        'hdmi_ports': 0,
        'dp_ports': 0,
        'consume': 0
        }

        model.value = ''
        model.update() 
        page.update()
        print(model)


    page.bgcolor = palette['black']
    default_text = ft.TextStyle(color=palette['green'])
    page.font = {
        'JetBrains Mono': 'JetBrainsMono-VariableFont_wght.ttf'
    }

    page.theme = ft.Theme(
        text_theme=ft.TextTheme(
            body_medium=ft.TextStyle(
                size=16, 
                font_family="JetBrains Mono",
                color=palette['green']
            )
        ),
        font_family="JetBrains Mono"
    )
    page.add(ft.Row([
        ft.Text('Graphic Comparator',size=36,
                font_family="JetBrains Mono",
                text_align="CENTER")],
        alignment=ft.MainAxisAlignment.CENTER,))


    
    page.add(ft.ResponsiveRow([
        model,
        price,
        ]),
        ft.ResponsiveRow([
        vram_size,
        vram_type,
        ]),
        ft.ResponsiveRow([
        hdmi_ports,
        dp_ports,
        consume
        ])
    )
    
    page.add(ft.ResponsiveRow([
    # First Column
    ft.Column(
        col={"xs": 12, "sm": 3, "md": 3, "lg": 3},  # 100% on mobile, 50% on PC
        controls=[
            ft.Container(
                expand=True,
                shadow=ft.BoxShadow(
                    spread_radius=0,
                    blur_radius=4,
                    color=ft.colors.BLACK,
                    offset=ft.Offset(0, 4)
                ),
                content=ft.CupertinoButton(
                    content=ft.Text('Limpiar', color=palette['white']),
                    bgcolor=palette['red'],
                    on_click=clean,
                    expand=True,
                    width=1920
                ),
                border_radius=10,
                alignment=ft.alignment.center_right,
            ),
        ],
    ),

    # Second Column
    ft.Column(
        col={"xs": 12, "sm": 3, "md": 3, "lg": 3},
        controls=[
            ft.Container(
                expand=True,
                shadow=ft.BoxShadow(
                    spread_radius=0,
                    blur_radius=4,
                    color=ft.colors.BLACK,
                    offset=ft.Offset(0, 4)
                ),
                content=ft.CupertinoButton(
                    content=ft.Text('Envíar', color=palette['white']),
                    bgcolor=palette['green'],
                    on_click=submit,
                    width=1920,
                ),
                border_radius=10,
                alignment=ft.alignment.center_left,
            )
        ],
    )
], alignment=ft.MainAxisAlignment.CENTER)
)
    
    
ft.app(target=main, assets_dir="assets")
