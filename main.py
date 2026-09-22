import operator
import turtle as t
print("Калькулятор")
f = int(input("Графики. 1 - прямая, 2 - гипербола"))
if f == 1:
    print("1")
elif f == 2:
    print("2")
elif f == 3:
    operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "//":operator.floordiv,
    "%": operator.mod,
    "**": operator.pow
    }
    a, op, b = input("Введите выражение: ").split()
    a = float(a)
    b = float(b)

    result = operations[op](a, b)

    print(result)

else:
    print("Ошибка ввода")
