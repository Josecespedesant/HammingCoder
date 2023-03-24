from tkinter import *


# Función que dibuja la representación NRZI en el canvas
def draw_NRZI(canvas, bits):
    x = 10  # posición inicial en el eje x
    y = 100  # posición en el eje y
    mov = 20

    # Dibujar la línea base
    canvas.create_line(x, y + 20, x + len(bits) * 20, y + 20, fill="black", width=2)

    # Dibujar la representación NRZI
    pos_up = 1

    for i in range(0, len(bits)):

        bit = int(bits[i])

        x_inicial = x + mov * i

        x_final = x + mov * i + mov

        if i == 0:
            y_inicial = y + mov
        else:
            y_inicial = y - mov * (-1) ** pos_up

        y_final = y + (-mov) * (-1) ** (pos_up + bit)

        canvas.create_line(x_inicial, y_inicial, x_inicial, y_final, fill="red", width=2)
        canvas.create_line(x_inicial, y_final, x_final, y_final, fill="red", width=2)
        pos_up += bit

        #print("bit", bit, pos_up, "y_inicial", y_inicial)

        canvas.create_text(x_inicial + (x_final - x_inicial) / 2, 60, text=bits[i], fill="black")



