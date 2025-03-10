import flet as ft

palette = {
    'black': '#191E29',
    'blue': '#132D46',
    'green': '#01C38D',
    'grey': '#696E79',
    'white': '#FFFFFF'
}

def main(page: ft.Page):
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
        )
    )
    page.add(ft.Row([
        ft.Text('Graphic Comparator',size=36,
                font_family="JetBrains Mono",
                text_align="CENTER")],
        alignment=ft.MainAxisAlignment.CENTER,))


ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)
