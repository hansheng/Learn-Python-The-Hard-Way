while True:
    print('Options')
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input = input("Please choose your option as listed above:")

    if user_input == "quit":
          break
    if user_input == 'add':
          num1 = float(input('Please input number 1:'))
          num2 = float(input('Please input number 2:'))
          result = num1 + num2
          print("The final value is ", result)

    elif user_input == 'subtract':
          num1 = float(input('Please input number 1:'))
          num2 = float(input('Please input number 2:'))
          result = num1 - num2
          print("The final value is " + str(result))

    elif user_input == 'multiply':
          num1 = float(input('Please input number 1:'))
          num2 = float(input('Please input number 2:'))
          result = num1 * num2
          print("The final value is " + str(result))

    elif user_input == 'divide':
          num1 = float(input('Please input number 1:'))
          num2 = float(input('Please input number 2:'))
          result = num1 / num2
          print("The final value is " + str("%.2f" % result))

    else:
          print("unkown error!")
