from tkinter import *

# Función que dibuja la representación NRZI en el canvas
def draw_NRZI(canvas, bits):
    x = 10 # posición inicial en el eje x
    y = 50 # posición en el eje y

    # Dibujar la línea base
    canvas.create_line(x, y, x+len(bits)*20, y, fill="black", width=2)

    # Dibujar la representación NRZI
    prev_bit = 0
    for bit in bits:
        if bit == 0:
            if prev_bit == 0:
                canvas.create_line(x, y, x+20, y, fill="red", width=2)
            else:
                canvas.create_line(x, y-40, x+20, y-40, fill="red", width=2)
                canvas.create_line(x+20, y-40, x+20, y, fill="red", width=2)
        else:
            if prev_bit == 0:
                canvas.create_line(x, y, x+20, y, fill="blue", width=2)
            else:
                canvas.create_line(x, y+40, x+20, y+40, fill="blue", width=2)
                canvas.create_line(x+20, y+40, x+20, y, fill="blue", width=2)
        prev_bit = bit
        x += 20

        # Verificar que la señal se ajuste al canvas
        if x > canvas.winfo_width() - 20:
            break


# Crear la ventana y el canvas
root = Tk()
canvas = Canvas(root, width=500, height=200)
canvas.pack()

# Ejemplo de una cadena de bits
bits = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1,0,0]

# Dibujar la representación NRZI
draw_NRZI(canvas, bits)

root.mainloop()
