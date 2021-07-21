
def decorator(func):
    def decoration(input_text):
        print('함수 시작!')
        func(input_text)
        print('함수 끝!')
    return decoration

@decorator
def hello_world(input_text):
    print(input_text)


hello_world('Hello World')