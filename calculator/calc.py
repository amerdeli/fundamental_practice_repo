def calculator():
    # basic calculator function

    math_operators_list = ['+', '-', '*', '/', '%']

    while True:
        try:
            x = float(input("Enter your first number :"))
        except ValueError:
            print("Incorrect input! Input needs to be a number.")
        else:
            break
            
    while True:
        try:
            y = float(input("Enter your second number :"))
        except ValueError:
            print("Incorrect input! Input needs to be a number.")
        else:
            break
    
    while True:
        try:
            math_operator = input("Enter mathematical operators :")
            if math_operator not in math_operators_list:
                raise Exception("Invalid mathematical operator!")
            if math_operator == '/' and y == 0:
                raise Exception("Division by zero not allowed!")
        except Exception as e:
            print(e)
        else:
            break

    if math_operator == '+':
       result = x + y
    elif math_operator == '-':
       result = x - y
    elif math_operator == '*':
        result = x * y
    elif math_operator == '/':
        result = x / y
    else:
        result = x % y

    print(F"{x} {math_operator} {y} = {result}")


calculator()
