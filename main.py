print("Welcome to the water remainder system!")
print("Please follow the instructions to successfully run the program.")

question1 = input("How many bottles do you normally put in the refrigerator? - ")
questionSplit = question1.split()
questionInt = int(''.join(map(str, questionSplit)))
remainder = round((questionInt / 2))
referenceValue = round((remainder / 2))

timeRefill = input("How many times do you refill your fridge daily? - ")
timeRefillSplit = timeRefill.split()
timeRefillInt = int(''.join(map(str, timeRefillSplit)))

timeTakeout = input("How many times do you take water out of the fridge daily? - ")
timeTakeoutSplit = timeTakeout.split()
timeTakeoutInt = int(''.join(map(str, timeTakeoutSplit)))

reminderTime = round((timeRefillInt * questionInt) / timeTakeoutInt) 

while reminderTime > 0 and questionInt != remainder:
    if referenceValue <= remainder :
        print("Please consider refilling your refridgerator with water bottle \n Thank you!")
        break
else:
    print("You won't be needing a refill.\nWe will prompt you when the need arises.\nThank you.")
    
