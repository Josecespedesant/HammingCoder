# Función para verificar si una cadena hexadecimal es un número de 11 bits
# Entrada: una cadena que representa un número hexadecimal
# Salida: True si la cadena representa un número hexadecimal de 11 bits válido, False de lo contrario
# Restricciones: la entrada debe ser una cadena de longitud 3 que representa un número hexadecimal de 11 bits válido (0x000 a 0x7FF)

def is_hex_11bit(hex_input):

    # Rellenar con ceros a la izquierda si es necesario
    hex_input = pad_hex(hex_input)

    try:
        int_value = int(hex_input, 16)
    except ValueError:
        return False
    
    # Verificar si la entrada es un número hexadecimal válido de 11 bits
    if len(hex_input) != 3:
        return False

    try:
        int_value = int(hex_input, 16)
    except ValueError:
        return False

    if int_value < 0 or int_value > 2047:
        return False

    # Si no hay errores, la entrada es un valor hexadecimal de 11 bits válido
    return True

# Función para rellenar con ceros a la izquierda una cadena hexadecimal
# Entrada: una cadena que representa un número hexadecimal
# Salida: la misma cadena rellenada con ceros a la izquierda hasta alcanzar una longitud de 3 caracteres
# Restricciones: la entrada debe ser una cadena hexadecimal de longitud 1 o 2

def pad_hex(hex_string):
    # Obtener la longitud de la cadena hexadecimal
    length = len(hex_string)

    # Si la cadena es menor a 3 caracteres, agregar ceros a la izquierda
    if length < 3:
        hex_string = '0'*(3 - length) + hex_string

    return hex_string

# Función para rellenar con ceros a la izquierda una cadena octal
# Entrada: una cadena que representa un número octal
# Salida: la misma cadena rellenada con ceros a la izquierda hasta alcanzar una longitud de 4 caracteres
# Restricciones: la entrada debe ser una cadena octal de longitud 1 a 3

def pad_oct(octal_string):

    length = len(octal_string)

    if length < 4:
        octal_string = '0' * (4 - length) + octal_string

    return octal_string

# Función para verificar si una cadena es un número hexadecimal válido
# Entrada: una cadena que representa un número hexadecimal
# Salida: True si la cadena representa un número hexadecimal válido, False de lo contrario
# Restricciones: la entrada debe ser una cadena hexadecimal

def is_hex(hex_input):
    try:
        int(hex_input, 16)
        return True
    except ValueError:
        return False



def converter(input_string):

    input_string = pad_hex(input_string)
    
    if (not is_hex_11bit(input_string)):
        return [False, False, False, "Error en la cadena de bits"]

    binary_num = hex_to_bin(input_string)
    octal_num = hex_to_oct(input_string)

    return [binary_num.zfill(11), pad_oct(octal_num), input_string, "Exitoso"]
    


def hex_to_bin(hex_string):
    decimal_number = int(hex_string, 16)
    binary_number = bin(decimal_number)[2:]
    return binary_number

# Función para convertir hexadecimal a octal
def hex_to_oct(hex_string):
    decimal_number = int(hex_string, 16)
    octal_number = oct(decimal_number)[2:]
    return octal_number
