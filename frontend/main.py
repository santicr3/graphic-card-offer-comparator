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
    ft.TextStyle.color = ft.Colors.YELLOW
    page.font = {
        'JetBrains Mono': 'https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,100..800;1,100..800&display=swap'
    }
    page.add(ft.Text('Hello', Text=ft.Colors.YELLOW))
    

ft.app(target=main)
