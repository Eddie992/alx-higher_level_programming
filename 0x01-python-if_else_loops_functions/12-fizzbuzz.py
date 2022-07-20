#!/usr/bin/python3
def fizzbuzz():
    for fiz in range(1, 100):
        if fiz % 3 == 0:
            print("Fizz", end=" ")
        elif fiz % 5 == 0:
            print ("Buzz", end=" ")
        elif fiz % 3 == 0 and fiz % 5 == 0:
            print("FizzBuzz", end=" ")
        else:
            print("{}".format(fiz), end=" ")
    return
