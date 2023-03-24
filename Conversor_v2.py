def convertir_base(hex_num, base_destino):
    
    # Convertir el número hexadecimal a decimal
    decimal = 0
    for i in range(len(hex_num)):
        decimal += int(hex_num[i], 16) * (16 ** (len(hex_num) - i - 1))

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
