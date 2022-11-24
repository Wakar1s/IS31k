class Quad():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def disc(self):
        self.d = self.b ** 2 - 4 * self.a * self.c
        return self.d

    def root(self):
        try:
            if self.d < 0:
                print('Корней нет')
            elif self.d == 0:
                x = -self.b / (2 * self.a)
                print(f'x = {x}')
            else:
                x1 = (-self.b + self.d ** 0.5) / (2 * self.a)
                x2 = (-self.b - self.d ** 0.5) / (2 * self.a)
                print(f'x1 = {x1}')
                print(f'x2 = {x2}')
        except (ZeroDivisionError, TypeError) as e:
            return 'Введите корректные значения'
