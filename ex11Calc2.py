print("Hi, Do you need to do some calculations?")
chooseFunction = input("Choose your operator, key +, -, *, / from the keyboard: ")
if chooseFunction not in ["+", "-", "*", "/"]:
    chooseFunction = input("That didn't work, try again use +, -, x or / from your keyboard: ")
else:
    firstNumber = input("Thanks, what is your first number?: ")
    listNumbers = firstNumber.split()
    listNumbers.append(input("and your next number please?: "))
    x = int(len(listNumbers))
    y = x - 1
    while listNumbers[y] != "N":
        listNumbers.append(input("another number? key in number or choose N for no: "))
        print(listNumbers[y])
    print(listNumbers)
    calcFunction = " " + chooseFunction + " "
    listNumbersString = calcFunction.join(listNumbers)
    finalString = listNumbersString[:-3]
    calculation = eval(finalString)
    print(calculation)







































