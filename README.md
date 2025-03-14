# Comparador de ofertas de tarjetas graficas

## Objetivo

El objetivo es entrenar un modelo de Inteligencia Artificial capaz de obtener el precio de una tarjeta gráfica basandose en sus cualidades
## Proceso

### Obetner informacion

Para entrenar al model necesitabamos obtener informacion de distintas webs de venta de tarjetas graficas, hemos elegido las siguientes:

- PCBox
- RedComputer
- Coolmod
- Wipoid

De estas webs hemos obtenido los siguientes datos:

| Modelo | Precio     | VRAM    | Tipo VRAM | Puertos HDMI | Puertos HDMI   | Energuia Usada  | URL  |
| ------ | ---------- | ------- | --------- | ------------ | -------------- | --------------- | ---- |
| Texto  | Int (cent) | Int(GB) |   Texto   |     Int      |      Int       |       Int(w)    | Text |

### Backend

Para el backend hemos utilizado Flask (Python)

### Frontend

Para el frontend hemos optado por Flet (Python)
