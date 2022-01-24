 
import math
if __name__ == "__main__":
    a = float(input('Введите коэф. а:'))
    b = float(input('Введите коэф. b:'))
    c = float(input('Введите коэф. c:'))
    d = b**2-4*a*c
    if d >= 0:
        if d == 0:
            print('Корень квадратного уравнения:\n', -b/2*a)
        else:
            print('Корни уравнения:\n', (-b-math.sqrt(d))/2*a, '\n', (-b+math.sqrt(d))/2*a)
    else:
        print('Нет корней уравнения')
