'''
Николаю требуется проверить, возможно ли из представленных отрезков
условной длины сформировать треугольник. Для этого он
решил создать класс TriangleChecker, принимающий только положительные
числа. С помощью метода is_triangle() возвращаются
следующие значения (в зависимости от ситуации):
– Ура, можно построить треугольник!;
– С отрицательными числами ничего не выйдет!;
– Нужно вводить только числа!;
– Жаль, но из этого треугольник не сделать.
'''

class TriangleChecker:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        
    def is_triangle(self):
        if isinstance(self.num1, str) or isinstance(self.num2, str) or isinstance(self.num3, str):
            print('Нужно вводить только числа!;')
            return
        elif self.num1 <= 0 or self.num2 <= 0 or self.num3 <=0:
            print('С отрицательными числами ничего не выйдет!')
            return
        numbers = sorted([self.num1, self.num2, self.num3])
        if numbers[0] + numbers[1] <= numbers[2]:
            print('Жаль, но из этого треугольник не сделать.')
        else: print('Ура, можно построить треугольник!')

check = TriangleChecker(1, 1, 3)
check.is_triangle()