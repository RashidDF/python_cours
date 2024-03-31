while True:
    num1 = str(input("Number one: "))
    num2 = str(input("Number two: "))
    if (float(num2) == 0.0):
        print("Number two is zero try again")
        continue

    print("Division result : ", float(num1) / float(num2))
    response = input("Continue yes/no: ")
    if (response == 'yes'):
        continue
    else:
        print("The END")
        break
