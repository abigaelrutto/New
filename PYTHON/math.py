operator = input("Enter an operator :(+,-,/,*)")
numb1 = float(input("Enter a number: "))
numb2 = float(input("Enter a second number: "))

if operator == "+" :
    results = numb1 + numb2
    print(results)
elif  operator == "-":
    results = numb1 - numb2
    print(results)
elif operator == "*" :
    result = numb1 * numb2
    print(result)
elif operator == "/" :
    result = numb1 / numb2
    print(round(result,2))






