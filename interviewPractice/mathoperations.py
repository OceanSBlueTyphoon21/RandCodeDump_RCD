def basic_op(operator, value1, value2):
    match operator:
        case "+":
            return value1+value2
        case "-":
            return value1-value2
        case "*":
            return value1*value2
        case "/":
            return value1/value2
        case _:
            return "Invalid operator input"

print(basic_op('+',4,7))