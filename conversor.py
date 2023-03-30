
def is_hex_11bit(hex_input):
    """
    :param hex_input:
    :return True si la cadena representa un número hexadecimal válido de 11 bits, False de lo contrario:
    """


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

def pad_hex(hex_string):
    """
    :param hex_string:
    :return la misma cadena rellenada con ceros a la izquierda hasta alcanzar una longitud de 3 caracteres:
    """


    # Obtener la longitud de la cadena hexadecimal
    length = len(hex_string)

    # Si la cadena es menor a 3 caracteres, agregar ceros a la izquierda
    if length < 3:
        hex_string = '0'*(3 - length) + hex_string

    return hex_string

def pad_oct(octal_string):
    """
    :param octal_string:
    :return la misma cadena rellenada con ceros a la izquierda hasta alcanzar una longitud de 4 caracteres:
    """

    length = len(octal_string)

    if length < 4:
        octal_string = '0' * (4 - length) + octal_string

    return octal_string

def converter(input_string):
    """
    :param input_string:
    :return <tuple> binary_num, octal_num, dec_num, hex_num:
    """


    input_string = pad_hex(input_string)
    
    if (not is_hex_11bit(input_string)):
        return [False, False, False, False]

    binary_num = convertir_base(input_string, 2)
    octal_num = convertir_base(input_string, 8)
    dec_num = convertir_base(input_string, 10)

    return [binary_num.zfill(11), pad_oct(octal_num), dec_num, input_string]


def convertir_base(hex_num, base_destino):
    """
    :param hex_num:
    :param base_destino:
    :return <string> resultado:
    """
    # Convertir el número hexadecimal a decimal
    decimal = 0
    for i in range(len(hex_num)):
        decimal += int(hex_num[i], 16) * (16 ** (len(hex_num) - i - 1))

    # En caso de que la base sea 10, el resultado está listo
    if base_destino == 10:
        resultado = str(decimal)

    # Convertir el número decimal a binario u octal, según la base de destino
    if base_destino == 2:
        resultado = ''
        while decimal > 0:
            resultado = str(decimal % 2) + resultado
            decimal //= 2
    elif base_destino == 8:
        resultado = ''
        while decimal > 0:
            resultado = str(decimal % 8) + resultado
            decimal //= 8

    return resultado
