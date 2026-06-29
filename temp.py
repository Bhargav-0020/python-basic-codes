a,b=map(int,input("enter the values:").split())
conversion=input("enter the conversion:")
if conversion=="celcius to fahrenheit":
    fahrenheit=(a*9/5)+32
    print(f"{a} degree celcius is equal to {fahrenheit} degree fahrenheit")
else:
    celcius=(b-32)*5/9
    print(f"{b} degree fahrenheit is equal to {celcius} degree celcius")