class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape)  # Convertir la cinta en una lista
        self.head = len(self.tape) - 2  # Coloca la cabeza antes de la 'B'
        self.state = 'q0'  # Estado inicial
        self.carry = 0  # Acarreo para la suma
    
    def step(self):
        if self.state == 'q0':
            # Estado inicial: mover la cabeza a la izquierda hasta encontrar el '#'
            if self.tape[self.head] == '#':
                self.state = 'q1'  # Cambiar al estado q1 cuando encontramos '#'
                self.head -= 1
            else:
                self.head -= 1

        elif self.state == 'q1':
            # Estado q1: leer los números desde la derecha y realizar la suma
            if self.tape[self.head] in '01':  # Si leemos un bit del primer número
                bit1 = int(self.tape[self.head])  # Leer el bit del primer número
                
                # Verificar si hay un bit del segundo número (a la izquierda de '#')
                if self.tape[self.head - 2] in '01':  # Si hay un bit válido del segundo número
                    bit2 = int(self.tape[self.head - 2])  # Leer el bit del segundo número
                else:  # Si no hay más bits del segundo número
                    bit2 = 0  # Considerar el segundo número como 0

                total = bit1 + bit2 + self.carry  # Sumar los bits con el acarreo

                if total == 0:
                    self.tape[self.head] = '0'  # Escribir 0 en la posición actual
                    self.carry = 0
                elif total == 1:
                    self.tape[self.head] = '1'  # Escribir 1 en la posición actual
                    self.carry = 0
                elif total == 2:
                    self.tape[self.head] = '0'  # Escribir 0 y llevar el acarreo
                    self.carry = 1
                elif total == 3:
                    self.tape[self.head] = '1'  # Escribir 1 y llevar el acarreo
                    self.carry = 1

                self.head -= 2  # Mover la cabeza hacia la izquierda dos posiciones

            elif self.tape[self.head] == 'B':  # Si encontramos un espacio en blanco
                if self.carry == 1:  # Si queda un acarreo por propagar
                    self.tape[self.head] = '1'  # Escribir el acarreo
                self.state = 'HALT'  # Finaliza la ejecución

    def run(self):
        # Ejecutar la máquina de Turing hasta que llegue al estado HALT
        print("Comienza la ejecución de la máquina de Turing...")
        while self.state != 'HALT':
            self.step()
        # Quitar el separador '#' y los caracteres 'B' sobrantes al final
        return ''.join(self.tape).replace('#', '').rstrip('B')


# Ejemplo de entrada: 10 + 50 en binario
input_tape = "1010#110010B"  # 10 (1010) + 50 (110010) en binario

# Crear la máquina de Turing con la cinta de entrada
tm = TuringMachine(input_tape)

# Ejecutar la simulación de la suma binaria
result_bin = tm.run()

# Convertir el resultado binario a decimal para verificación
result_int = int(result_bin, 2)

# Imprimir los resultados
print(f"Resultado de la suma binaria: {result_bin}")  # Debe mostrar: 111100 (el binario de 60)
print(f"Resultado de la suma en decimal: {result_int}")  # Debe mostrar: 60
