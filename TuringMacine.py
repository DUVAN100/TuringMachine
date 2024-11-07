from sumBinary import Operations

class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape)
        self.head = len(tape) - 2  
        self.state = 'q0'
        self.carry = 0

    def print_state(self):
        print(f"State: {self.state}, Head: {self.head}, Carry: {self.carry}")
        print(''.join(self.tape))
        print(' ' * self.head + '^')
    
    def get_corresponding_bits(self):
        separator_pos = ''.join(self.tape).find('#')
        num1 = ''.join(self.tape[:separator_pos])
        num2 = ''.join(self.tape[separator_pos+1:]).rstrip('B')
        max_len = max(len(num1), len(num2))
        self.tape = list(f"{num1.zfill(max_len)}#{num2.zfill(max_len)}B")
        return num1, num2

    def step(self):
        self.print_state()
        if self.state == 'q0':
            num1 = self.get_corresponding_bits()
            self.state = 'q1'
            self.head = len(num1) - 1  
            return
        elif self.state == 'q1':
            if self.head < 0:
                if self.carry == 1:
                    self.tape.insert(0, '1')
                self.state = 'HALT'
                return
            separator_pos = ''.join(self.tape).find('#')
            bit1 = int(self.tape[self.head]) if self.tape[self.head] in '01' else 0
            pos2 = separator_pos + 1 + self.head
            bit2 = int(self.tape[pos2]) if pos2 < len(self.tape) - 1 and self.tape[pos2] in '01' else 0
            total = bit1 + bit2 + self.carry
            self.carry = total // 2
            self.tape[self.head] = str(total % 2)
            self.head -= 1
            
    def run(self):
        while self.state != 'HALT':
            self.step()
        result = ''.join(self.tape).split('#')[0].rstrip('B')
        return result

    def execute_sum(self):
        bin_one, bin_two = ''.join(self.tape).replace('B', '').split('#')
        return Operations.sum_binaries(bin_one, bin_two)

if __name__ == "__main__":
    input_tape = "110010#111100B"  # 50 + 60
    tm = TuringMachine(input_tape)

    result_int = tm.execute_sum()
    result_bin = tm.run()

    print(f"Result of sum binary: {result_bin}") #
    print(f"Result of sum int: {result_int}") # 


