a,b=input("enter the values:")
operator=input("enter the operator:")
if operator=='+':
    print(int(a)+int(b))
elif operator=='-':
    print(int(a)-int(b))
elif operator=='*':
    print(int(a)*int(b))
elif operator=='/':
    print(int(a)/int(b))
elif operator=='%':
    print(int(a)%int(b))
elif operator=='**':
    print(int(a)**int(b))
elif operator=='//':
    print(int(a)//int(b))
elif operator=='and':
    print(int(a) and int(b))
else:
    print("invalid operator")