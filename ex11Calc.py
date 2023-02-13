inputCalc = input("enter your calculation with spaces eg 1 + 3 - 2: ")
listCalc = inputCalc.split()
listOps = listCalc[1::2]
listNums = listCalc[0::2]
for i in listOps:
    if i not in ["+", "-", "*", "/"]:
        print("Operator not valid")
    else:
        for e in listNums:
            if int(e):
                x = eval(inputCalc)
                print(x)
            else:
                print("you have not followed the format")








