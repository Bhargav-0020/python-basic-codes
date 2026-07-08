a=input("enter the value:")
b=input("enter the value:")
operator=input("enter the operator:")
match operator:
    case '+':
        print(int(a)+int(b))
    case '-':
        print(int(a)-int(b))
    case '*':
        print(int(a)*int(b))
    case "diff":
        if int(a)%2==0:
            print("even")
        else:
            print("odd")
    case "/" if b!=0:
        print(int(a)/int(b))