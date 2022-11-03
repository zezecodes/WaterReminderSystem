import random
import schedule
import time

print("Welcome to the water reminder system!\n-------------------------------------")

# List of healthy water facts that change everytime user launches program
waterQuotesList = ["Adult humans are 60 percent water, and our blood is 90 percent water", "The average amount of water you need per day is about 3 liters (13 cups) for men and 2.2 liters (9 cups) for women",
    "Water is essential for the kidneys and other bodily functions", "When dehydrated, the skin can become more vulnerable to skin disorders and wrinkling",
    "Drinking water instead of soda can help with weight loss", "Around 71 percent of the planet’s surface is covered by water", "Drinking water cushions the brain, spinal cord, and other sensitive tissues",
    "Approximately 80'%' of your brain tissue is made of water", 
]
randomQuotesGenerator = random.choice(waterQuotesList).lower()
emojis = "✨"
print(f"{emojis} Did you know {randomQuotesGenerator}?\n----------------------------------")


# Gets the number of bottles put in users fridge daily
question1 = input("How many bottles do you normally put in the refrigerator daily? - ")
questionSplit = question1.split()
questionInt = int(''.join(map(str, questionSplit)))

# Gets the number of times users fridge is refilled daily
timeRefill = input("How many times do you refill your fridge daily? - ")
timeRefillSplit = timeRefill.split()
timeRefillInt = int(''.join(map(str, timeRefillSplit)))


# Gets the amount of bottles removed from the fridge daily
timeTakeout = input("How many times do you take water out of the fridge daily? - ")
timeTakeoutSplit = timeTakeout.split()
timeTakeoutInt = int(''.join(map(str, timeTakeoutSplit)))


# Asks the user when he wants to be reminded to refill based on the number of bottles in the fridge 
userReminderInput = input("What number of bottles have to be in the fridge when you want to be prompted for a refill? - ")
userReminderinputSplit = userReminderInput.split()
userReminderInputInt = int(''.join(map(str, userReminderinputSplit)))


def reduction():    
    i=questionInt       
    while i>userReminderInputInt and i<=questionInt:
        print(i) 
        i=i-1
    print("Time to refill")
reduction()


   
  
  


