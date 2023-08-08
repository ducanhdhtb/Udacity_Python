#print(x)

def divide(a, b):
    if b == 0:
        raise Exception("Cannot Divide by Zero")
    return a/b

def input_divide():
    try:
        a = int(input('Divisor: '))
        b = int(input('Dividend: '))
        print(f'{a}/{b} = {divide(a, b)}')
    except Exception as e:
        print(e)
        input_divide()
divide(10,0)
input_divide()