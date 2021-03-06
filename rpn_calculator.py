import constants

class RPNCalculator:

    def __init__(self):
        self.stack = []

    def calculate(self, expression: str) -> int:
        expr_values = expression.strip().split()
        if not self.__is_valid_expression(expr_values):
            raise RuntimeError(f"Invalid expression: {expression}")
        return self.__find_answer(expr_values)

    def __is_valid_expression(self, expr_values: []) -> bool:
        for val in expr_values:
            if not self.__is_whole_number(val) and val not in constants.VALID_OPERATIONS:
                return False
        return True

    def __is_whole_number(self, val: str) -> bool:
        return val.isdigit() and int(val) >= 0

    def __find_answer(self, expr_values: []) -> bool:
        for val in expr_values:
            if val in constants.VALID_OPERATIONS:
                right_operand = self.stack.pop()
                try:
                    left_operand = self.stack.pop()
                    answer = int(eval(f'{left_operand}{val}{right_operand}'))
                except IndexError:
                    answer = right_operand
                except ZeroDivisionError:
                    answer = 0
                self.stack.append(answer)
            else:
                self.stack.append(int(val))

        return self.stack.pop()


if __name__ == '__main__':
    print('Enter expression:')
    print(f'The answer is: {RPNCalculator().calculate(input())}')
