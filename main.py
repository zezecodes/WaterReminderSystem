import random
import schedule
import time

print("Welcome to the water reminder system!\n-------------------------------------")

# List of healthy water facts that change everytime user launches program
waterQuotesList = ["Adult humans are 60 percent water, and our blood is 90 percent water", 
    "The average amount of water you need per day is about 3 liters (13 cups) for men and 2.2 liters (9 cups) for women",
    "Water is essential for the kidneys and other bodily functions", 
    "When dehydrated, the skin can become more vulnerable to skin disorders and wrinkling",
    "Drinking water instead of soda can help with weight loss", 
    "Around 71 percent of the planet’s surface is covered by water", 
    "Drinking water cushions the brain, spinal cord, and other sensitive tissues",
    "Approximately 80'%' of your brain tissue is made of water", 
]

# Generates and prints quotes from quotes list
randomQuotesGenerator = random.choice(waterQuotesList).lower()
emojis = "✨"
print(f"{emojis} Did you know {randomQuotesGenerator}?\n----------------------------------")


# Gets the number of bottles put in users fridge daily
bottleInput = input("How many bottles do you normally put in the refrigerator daily? - ")
bottleInputSplit = bottleInput.split()
bottleInputNumber = int(''.join(map(str, bottleInputSplit)))

# Gets the number of times users fridge is refilled daily
bottleRefillInput = input("How many times do you refill your fridge daily? - ")
bottleRefillSplit = bottleRefillInput.split()
bottleRefillNumber = int(''.join(map(str, bottleRefillSplit)))


# Gets the amount of bottles removed from the fridge daily
bottleTakeoutInput = input("How many times do you take water out of the fridge daily? - ")
bottleTakeoutSplit = bottleTakeoutInput.split()
bottleTakeoutNumber = int(''.join(map(str, bottleTakeoutSplit)))


# Asks the user when he wants to be reminded to refill based on the number of bottles in the fridge 
bottleReminderInput = input("What number of bottles have to be in the fridge when you want to be prompted for a refill? - ")
bottleReminderinputSplit = bottleReminderInput.split()
bottleReminderInputNumber = int(''.join(map(str, bottleReminderinputSplit)))

# Shows the total amount of bottles that will be in the fridge based on the info given
totalBottleEstimation = bottleInputNumber * bottleRefillNumber
print("\nCalculating estimated total number of bottles in your fridge...")
if totalBottleEstimation >= bottleTakeoutNumber:
    print("Estimated number of bottles is: "+ totalBottleEstimation + " bottles \n")
else:
    print("Estimation cannot occur because number of bottles to be taken out is more than " +
            "number of bottles put in the fridge. Please try again \n")

# Functioon responsible for the visualization of the bottle reduction
def reduction():  
    print("Initializing reminder...\nYou will be prompted for a refill when bottle number has been reached.")  
    i=bottleInput       
    while i>bottleReminderInputNumber and i<=bottleInput:
        print(i) 
        i=i-1
    print(bottleReminderInputNumber, "\nTime to refill")
reduction()


   
  
  

# x=lambda a,b:a+b
# print(x(2,3))