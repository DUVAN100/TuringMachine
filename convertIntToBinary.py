# def int_binary(number):
#     if number == 0:
#         return "0"
#     binario = ""
#     while number > 0:
#         residuo = number % 2  
#         binario = str(residuo) + binario 
#         number = number // 2 
#     return binario
# print(int_binary(110))


def binary_int(bin):
    int = 0
    potencia = 0
    for bit in reversed(bin):
        if bit == '1':
            int += 2 ** potencia  
        potencia += 1 
    return int

#"111100"  
print(binary_int("1100010"))




