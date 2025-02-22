# Comparador de ofertas de tarjetas graficas

## Objetivo

El objetivo es conseguir un modelo de Inteligencia Artificial capaz de obtener si una oferta en una tarjeta grafica es buena o no

## Proceso

### Obetner informacion

Para entrenar al model necesitabamos obtener informacion de distintas webs de venta de tarjetas graficas, hemos elegido las siguientes:

- PCBox
- RedComputer
- Lifeinformatica
- Coolmod
- Wipoid
- Compucenter

De estas webs hemos obtenido los siguientes datos:

| Modelo | Precio     | VRAM    | Tipo VRAM | Puertos | Ventiladores | Dimensiones                         | Energuia Usada | URL  |
| ------ | ---------- | ------- | --------- | ------- | ------------ | ----------------------------------- | -------------- | ---- |
| Texto  | Int (cent) | Int(MB) | Texto     | Texto\* | Int(N.)      | Array[Int](Longitud, Ancho, Altura) | Int(w)         | Text |

### Donde guardar la informacion

Si bien tenemos diferentes opciones de bases de datos hemos optado por MongoDB

### Backend

Para el backend hemos utilizado Flask (Python)

### Frontend

Para el frontend hemos optado por Flert (Python)
