import json

#opens json that contains the food data
openJson = open('food.json')
#load json that contains the food data
foodLibrary = json.load(openJson)
#"finished" variable that will be used to initialize the while loop and also end it as long as the input is correct.
finished = False
#list that will store the the all food that was read from input.
foodMeal = []
#list that will store the nutrients. index [0] will be proteins, index[1] will be fats, index[2] will be carbohydrates, index[3] will be calories.
nutrientsMeal = [0,0,0,0]

#the function calculates the nutrients for each of the foods eaten taking into account the type and the quantity.
def calorieCounter(foodEaten,quantityEaten):
    nutritionalCounterProteins=quantityEaten*foodLibrary["foods"][foodEaten]["proteins"]/100
    nutrientsMeal[0]+=float(nutritionalCounterProteins)
    nutritionalCounterFats=quantityEaten*foodLibrary["foods"][foodEaten]["fats"]/100
    nutrientsMeal[1]+=float(nutritionalCounterFats)
    nutritionalCounterCarbohydrates=quantityEaten*foodLibrary["foods"][foodEaten]["carbohydrates"]/100
    nutrientsMeal[2]+=float(nutritionalCounterCarbohydrates)
    nutritionalCounterCalories=quantityEaten*foodLibrary["foods"][foodEaten]["calories"]/100
    nutrientsMeal[3]+=float(nutritionalCounterCalories)
    print(" The of this would be : \n"+
            " proteins: "+str(nutritionalCounterProteins)+"\n"+
            " fats: "+str(nutritionalCounterFats)+"\n"+
            " carbohydrates:"+str(nutritionalCounterCarbohydrates)+"\n"
            " calories:"+str(nutritionalCounterCalories)+"\n")

#function that prints out what was eaten during the meal alongside with the total for each nutrient.
def mealTracker():
    print("So you ate: "+ str(foodMeal)+" and your nutritional value for this meal is: \n"+
          "proteins: "+str(nutrientsMeal[0])+ "\n"
          "fats: "+str(nutrientsMeal[1])+ "\n"
          "carbohydrates: "+str(nutrientsMeal[2])+ "\n"
          "calories: "+str(nutrientsMeal[3])+ "\n"
          )

#while loop that will prompt the user for input regarding type of food, quantity and will invoke other functions to print more details about the meal.
while finished == False:
    foodEaten = input("What did you eat?: ")
    #checks if he type of food read from input exists in the json file.
    if foodEaten in foodLibrary["foods"]:
        #appends the food read from prompting the user for input to be stored in the foodMeal list for later use.
        foodMeal.append(foodEaten)
        print("Your nutritional Values per 100gr of " +foodEaten+" are the following: " + str(foodLibrary["foods"][foodEaten]))
        #a boolean variable that will be used to enter and exit the while loop if the input is correct.
        correct=False
        while(correct==False):
            try:
                quantityEaten = float(input("And how much did you eat?: "))
                calorieCounter(foodEaten,quantityEaten)
                correct=True
            except ValueError:
                print("The type of input you are trying to enter is invalid. Please try a numeric type.")
    #end of the loop in case all the inputs where correct.
    elif foodEaten=="Finished":
        mealTracker()
        finished=True
    elif foodEaten=="":
        print("You haven't provided a meal") 
        break
    else:
        print("Invalid input!")
        break