# Syed Shams
# 1820287

class FoodItem:
    # Initialize attributes of the class
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        # function to output results
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__" :

    test_FoodItem = FoodItem()                  # Declaring the variable with the template class

    food_name = input()                         # Declaring variables for inputs
    fat_amount = float(input())
    carb_amount = float(input())
    protein_amount = float(input())

    user_FoodItem = FoodItem(food_name, fat_amount, carb_amount, protein_amount)
    # Actual food item class

    num_Servings = float(input())               # Input number of servings

    test_FoodItem.print_info()                  # Call for object --> print info for Name = none
    print("Number of calories for {:.2f} serving(s): {:.2f}".format(num_Servings,
                                                                      test_FoodItem.get_calories(num_Servings)))
    print()
    user_FoodItem.print_info()                  # Call for object --> print info for user inputted values
    print("Number of calories for {:.2f} serving(s): {:.2f}".format(num_Servings,
                                                                     user_FoodItem.get_calories(num_Servings)))
