
def run_calculator():
    while True:
        print("What operation would you like to perform? (Pick a number)")
        print('1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Mixed Operations\n6. Algebraic Operations')
        operation = input("Operation: ")

        addition_values = []
        subtraction_values = []
        multiplication_values = []
        division_values = []
        mixed_values = []
        algebraic_values = []
        def x():
            return x
        def y():
            return y

        if "1" in operation.lower():
            print("Addition is selected, type '=' when finished")
            while True:
                user_input = input("Value input: ").strip()
                if not user_input:
                    continue
                if user_input == "=":
                    break
                addition_values.append(user_input)
            if addition_values:
                expression =" + ".join(str(value)for value in addition_values)
                total = eval(expression)
                print(f"Total is: {total}")
                boolean = input("Would you like to perform another operation? (yes/no): ")
                if "yes" in boolean.lower():
                    run_calculator()
                else:
                    print("Thank you for using the calculator!")
                    break

        if "2" in operation.lower():
            print("Subtraction is selected, type '=' when finished")
            while True:
                user_input = input("Value input: ").strip()
                if not user_input:
                    continue
                if user_input == "=":
                    break
                subtraction_values.append(user_input)
            if subtraction_values:
                expression =" - ".join(str(value)for value in subtraction_values)
                total = eval(expression)
                print(f"Total is: {total}")
                boolean = input("Would you like to perform another operation? (yes/no): ")
                if "yes" in boolean.lower():
                    run_calculator()
                else:
                    print("Thank you for using the calculator!")
                    break

        if "3" in operation.lower():
            print("Multiplication is selected, type '=' when finished")
            while True:
                user_input = input("Value input: ").strip()
                if not user_input:
                    continue
                if user_input == "=":
                    break
                multiplication_values.append(user_input)
            if multiplication_values:
                expression =" * ".join(str(value)for value in multiplication_values)
                total = eval(expression)
                print(f"Total is: {total}")
                boolean = input("Would you like to perform another operation? (yes/no): ")
                if "yes" in boolean.lower():
                    run_calculator()
                else:
                    print("Thank you for using the calculator!")
                    break

        if "4" in operation.lower():
            print("Division is selected, type '=' when finished")
            while True:
                user_input = input("Value input: ").strip()
                if not user_input:
                    continue
                if user_input == "=":
                    break
                division_values.append(user_input)
            if division_values:
                expression =" / ".join(str(value)for value in division_values)
                total = eval(expression)
                print(f"Total is: {total}")
                boolean = input("Would you like to perform another operation? (yes/no): ")
                if "yes" in boolean.lower():
                    run_calculator()
                else:
                    print("Thank you for using the calculator!")
                    break

        if "5" in operation.lower():
            print("Mixed Operations is selected, type '=' when finished")
            print("You can input numbers and operators (+, -, *, /) in any order.")
            print("For example: 5 + 3 * 2 - 1 =")
            print("You can put all the numbers and operators in any order in one input and the calculator will evaluate it correctly.")
            while True:
                user_input = input("Value input: ").strip()
                if not user_input:
                    continue
                elif user_input in ["+", "-", "*", "/"]:
                    mixed_values.append(user_input)
                if user_input == "=":
                    break
                mixed_values.append(user_input)
            if mixed_values:
                expression = " ".join(str(value) for value in mixed_values)
                total = eval(expression)
                print(f"Total is: {total}")
                boolean = input("Would you like to perform another operation? (yes/no): ")
                if "yes" in boolean.lower():
                    run_calculator()
                else:
                    print("Thank you for using the calculator!")
                    break

        if "6" in operation.lower():
            print("Algebraic Operations is selected, type '=' when expression is finished")
            print("You can input algebraic expressions with variables (x and y).")
            print("For example: 2*x + 3*y")
            print("After entering the expression, you will need to type '=' to finish and then input the values for x and y.")
            while True:
                user_input = input("Value input: ").strip()
                if not user_input:
                    continue
                if user_input == "=":
                    break
                algebraic_values.append(user_input)
            if algebraic_values:
                expression = " ".join(str(value) for value in algebraic_values)
                x = int(input("x input: "))
                y = int(input("y input: "))
                total = eval(expression.replace('x', str(x)).replace('y', str(y)))
                print(f"Total is: {total}")
                boolean = input("Would you like to perform another operation? (yes/no): ")
                if "yes" in boolean.lower():
                    run_calculator()
                else:
                    print("Thank you for using the calculator!")
                    break


print("Welcome to the calculator!, type 'run' to start the calculator")
user_choice = input("Input: ").strip().lower()
if user_choice == "run":
    run_calculator()
