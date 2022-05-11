class Calculator:

    def __init__(self):
        self.stack = []
        self.operations = ['/', '*', '%', '+', '-']

    def calculate(self, expression: str) -> int:
        e_arr = expression.strip().split()
        if not self._valid_input(e_arr):
            raise RuntimeError("Not a valid expression")
        return self._find_answer(e_arr)

    def _valid_input(self, e_arr: []) -> bool:
        for val in e_arr:
            if (not self._is_whole_number(val)) and \
                    (val not in self.operations):
                return False
        return True

    def _is_whole_number(self, val: str) -> bool:
        return val.isdigit() and int(val) >= 0

    def _find_answer(self, e_arr: []) -> bool:
        for val in e_arr:
            if val in self.operations:
                val1 = self.stack.pop()
                try:
                    val2 = self.stack.pop()
                    formula = f'{val2}{val}{val1}'
                    answer = int(eval(formula))
                except IndexError:
                    answer = val1
                except ZeroDivisionError:
                    answer = 0
                self.stack.append(answer)
            else:
                self.stack.append(int(val))

        return self.stack.pop()


if __name__ == '__main__':
    print('Enter expression:')
    print(f'The answer is: {Calculator().calculate(input())}')
