import json

openJson = open('food.json')
foodLibrary = json.load(openJson)
finished = False
foodMeal = []
nutrientsMeal = [0,0,0,0]

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
def mealTracker(    ):
    print("So you ate: "+ str(foodMeal)+" and your nutritional value for this meal is: \n"+
          "proteins: "+str(nutrientsMeal[0])+ "\n"
          "fats: "+str(nutrientsMeal[1])+ "\n"
          "carbohydrates: "+str(nutrientsMeal[2])+ "\n"
          "calories: "+str(nutrientsMeal[3])+ "\n"
          )


while finished == False:
    foodEaten = input("What did you eat?: ")
    if foodEaten in foodLibrary["foods"]:
        foodMeal.append(foodEaten)
        print("Your nutritional Values per 100gr of " +foodEaten+" are the following: " + str(foodLibrary["foods"][foodEaten]))
        correct=False
        while(correct==False):
            try:
                quantityEaten = float(input("And how much did you eat?: "))
                calorieCounter(foodEaten,quantityEaten)
                mealTracker()
                correct=True
            except ValueError:
                print("The type of input you are trying to enter is invalid. Please try a numeric type.")
    elif foodEaten=="":
        print("You haven't provided a meal") 
        break
    else:
        print("Invalid input!")
        break