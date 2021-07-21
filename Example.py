
def decorator(func):
    def decorated(a, b, h):
        if a >= 0 and b >= 0 and h >= 0:
            func(a, b, h)
        else:
            print('fdd')

    return decorated



@decorator
def math(a, b, h):
    square = a * b * h
    triangle = a * b * h * 0.5
    print(square)
    print(triangle)

math(10, 4, -1)
