def add(a,b):
    sum=a+b
    return sum
def minus(a,b):
    subract=a-b
    return subract
def multiply(a,b):
    into=a*b
    return into
def divide(a,b):
    quotient=a/b
    return quotient
def operator():
    while True:
        print("+")
        print("-")
        print("*")
        print("/")
sairam=input("enter the symbol:")
match sairam:
    case "+":
        print(add(5,3))
    case "-":
        print(minus(6,5))
    case "*":
        print(multiply(5,3))
    case "/":
        print(divide(10/2))
