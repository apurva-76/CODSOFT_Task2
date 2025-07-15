def calculator():
    print("Simple Calculator ")

    while True:
        print("\nChoose operation:")
        print("1. Addition ")
        print("2. Subtraction ")
        print("3. Multiplication ")
        print("4. Division ")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Calculator closed. Thank you!")
            break

        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("Please enter valid integers only.")
            continue

        if choice == '1':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':
            if num2 != 0:
                if num1 % num2 == 0:
                    result = num1 // num2
                else:
                    result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid choice. Please select from 1 to 5.")


calculator()