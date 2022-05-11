# Reverse Polish Notation (RPN) Implementation

In ordinary mathematical notation we place operations in the middle of their operands, e.g. in `“1+2”`, the `+` operation sits in-between the operands `1` and `2`. There’s another method, called `Reverse Polish Notation (RPN)`, where operations are written after their operands. For instance, the expression `"1 + 2"` is written as `"1 2 +"`. (this is also known as `postfix notation`).

Here are some more examples:

`5 2 /` is equivalent to `5/2`

`3 7 *` is equivalent to `3*7`

`4 7 + 2 *` is equivalent to `(4+7)*2`

`2 3 * 11 14 * +` is equivalent to `2*3 + 11*14`


Many Linux distributions come with a command line tool called dc (`Desk Calculator`) which implements RPN. Unlike in ordinary mathematical notation, there's no need to use braces in RPN.

This implementation is a command line program that accepts an RPN expression as input and evaluates it. It supports the following operations:

Addition (`+`), subtraction (`-`) and multiplication (`*`)

Integer division (`/`). Example: `“5 2 /” => 2` (not 2.5; only return the integer part)

Remainder or modulo (`%`). Example: `“5 2 %” => 1`

The calculator only accepts whole numbers as inputs and outputs whole numbers.

### Valid Examples

| Input        | Output |
|--------------|--------|
 | 5 2 / | 2 |
 | 3 7 * | 21 |
 | 5 2 % | 1 |
 | 4 7 + 2 * | 22 |
 | 1 2 3 + | 5 |
 | 2 3 * 11 14 * + | 160 |
 | 1 2 + 3 * 4 5 + + | 18 |
 | 1 2 + 3 * 4 + 1 2 * | 2 |
 | 1 2 + 3 * 4 + | 13 |
 | 1 2 + 3 * 4 + * - + / % | 13 |
 | 1 2 + 3 * 4 + * | 13 |
 | 1 2 + 3 * 4 + - * * 2 *  | 26 |
 | 1 2 + 3 * 4 + - * * 0 /  | 0 |
 | 10 6 9 3 + 11 / 17 + 5 + | 23 |
 | 2147483648 2147483648 + | 4294967296 |
 | 9223372036854775807 9223372036854775807 + | 18446744073709551614 |


### Invalid Examples

| Input        | Reason |
|--------------|--------|
| (1 2) + (3 * 4) + | Contains paranthesis |
 | 10 6 9 3 + -11 * / * 17 + 5 + | Contains negative number |
 | one two + | Contains strings |

### Commands

1. Run Unit Tests
   
  - `pytest test_calculator.py -v`  

2. Run code from command line
 
  - `python calculator.py` or `python3 calculator.py`
