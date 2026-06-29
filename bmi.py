weight,height=map(float,input("enter values:").split())
bmi=weight/(height**2)
print(bmi)
if bmi<18.5:
    print("underweight")
elif bmi>=18.5 and bmi<24.9:
    print("normal weight")
else:
    print("overweight")