import operator
import turtle as t

k = 22

def introduce():
    return "Калькулятор, способный вычеслять два вида графиков и основные операции с числами"
f = int(input("Графики. 1 - прямая, 2 - гипербола, 4 - парабола, 4 - обычный калькулятор\n"))

def axes():
    t.tracer(0)
    # X
    t.up()
    t.goto(-20 * k, 0)
    t.down()
    t.goto(20 * k, 0)

    # Y
    t.up()
    t.goto(0, -20 * k)
    t.down()
    t.goto(0, 20 * k)

    t.up()

def line(a, b):
    axes()
    t.up()
    t.tracer(0)
    t.screensize(1000, 1000)

    
    for x in range(-10, 10):
        y = a*x + b
        t.goto(x*k, y*k)
        t.dot(5, 'red')

    t.mainloop()

def hyp(a, b, c):
    axes()
    t.up()
    t.tracer(0)
    t.screensize(1000, 1000)

    for x in range(-10, 10):
        y = a * x**2 + b * x + c
        t.goto(x*k, y*k)
        t.dot(5, 'red')

    t.mainloop()

if f == 1:
    print("Прямая y = ax + b")
    a, b = map(int, input("Введите данные в виде a b\n").split())
    line(a, b)
elif f == 2:
    print("Гипербола y = ax^2 + bx + c")
    a, b, c = map(int, input("Введите данные в виде a b c\n").split())
    hyp(a, b, c)
elif f == 3:
    print("Калькулятор чисел")
else:
    print("Ошибка ввода")

t.update()