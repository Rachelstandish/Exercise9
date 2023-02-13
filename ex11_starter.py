#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
dog = "dog"
print(len(Belgium))
digitCount = len(Belgium)
num = 0
while num < digitCount:
    print("-", end="")
    num += 1
print()
print("-" * len(Belgium))

print(Belgium.replace(",", ":"))
myList = Belgium.split(",")

print(int(myList[1]) + int(myList[3]))













