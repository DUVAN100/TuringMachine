from sumBinary import Operations  

class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape)  # Convierte la cinta de entrada (tape) en una lista de caracteres
        self.head = len(tape) - 2  # Posición inicial del cabezal (antes del último carácter 'B')
        self.state = 'q0'  # Estado inicial de la máquina de Turing
        self.carry = 0  # Inicializa el acarreo en 0

    def print_state(self):
        print(f"State: {self.state}, Head: {self.head}, Carry: {self.carry}")
        print(''.join(self.tape))  
        print(' ' * self.head + '^') 

    def get_corresponding_bits(self):
        separator_pos = ''.join(self.tape).find('#')  # Encuentra la posición del separador '#'
        num1 = ''.join(self.tape[:separator_pos])  # Extrae la primera parte del número (antes del '#')
        num2 = ''.join(self.tape[separator_pos+1:]).rstrip('B')  # Extrae la segunda parte del número (después del '#', eliminando los 'B')
        max_len = max(len(num1), len(num2))  # Determina la longitud máxima de ambos números
        self.tape = list(f"{num1.zfill(max_len)}#{num2.zfill(max_len)}B")  # Rellena ambos números con ceros a la izquierda y forma la nueva cinta
        return num1, num2  # Devuelve los dos números binarios como cadenas

    def step(self):
        self.print_state()  # Imprime el estado actual de la máquina en cada paso
        if self.state == 'q0':  # Si el estado es 'q0', se procesa la entrada
            num1, num2 = self.get_corresponding_bits()  # Obtiene los dos números binarios
            self.state = 'q1'  # Cambia al estado 'q1' para la siguiente fase
            self.head = len(num1) - 1  # Coloca el cabezal al final del primer número binario
            return
        elif self.state == 'q1':  # Si el estado es 'q1', se ejecuta la suma
            if self.head < 0:  # Si el cabezal alcanza el inicio de la cinta
                if self.carry == 1:  # Si hay acarreo, añade un '1' al inicio
                    self.tape.insert(0, '1')
                self.state = 'HALT'  # Cambia el estado a 'HALT' para detener la máquina
                return
            separator_pos = ''.join(self.tape).find('#')  # Encuentra la posición del separador '#'
            bit1 = int(self.tape[self.head]) if self.tape[self.head] in '01' else 0  # Obtiene el valor de la primera parte del número en la posición actual del cabezal
            pos2 = separator_pos + 1 + self.head  # Calcula la posición correspondiente en el segundo número
            bit2 = int(self.tape[pos2]) if pos2 < len(self.tape) - 1 and self.tape[pos2] in '01' else 0  # Obtiene el valor de la segunda parte del número
            total = bit1 + bit2 + self.carry  # Suma los dos bits y el acarreo
            self.carry = total // 2  # Calcula el nuevo acarreo (división entera por 2)
            self.tape[self.head] = str(total % 2)  # Escribe el bit resultante (el residuo de la división)
            self.head -= 1  # Mueve el cabezal a la izquierda para procesar el siguiente bit

    def run(self):
        while self.state != 'HALT':  # Mientras el estado no sea 'HALT', sigue ejecutando pasos
            self.step()  # Ejecuta un paso de la máquina
        result = ''.join(self.tape).split('#')[0].rstrip('B')  # Obtiene el resultado final de la suma (antes del '#', eliminando los 'B')
        return result  # Devuelve el resultado binario de la suma

    def execute_sum(self):
        # Extrae los dos números binarios desde la cinta, eliminando 'B' y dividiendo en la posición del '#'
        bin_one, bin_two = ''.join(self.tape).replace('B', '').split('#')
        return Operations.sum_binaries(bin_one, bin_two)  # Llama a la función de suma en la clase Operations

if __name__ == "__main__":
    input_tape = "110010#111100B"  # La entrada de la máquina es '110010' + '#' + '111100' + 'B' (10 + 50 en binario)
    tm = TuringMachine(input_tape)  
    # result_int = tm.execute_sum()  
    result_bin = tm.run()  

