
# **BASE CODE**


####################################################################################################
# FUNCTIONS DEFINITIONS
####################################################################################################


def get_car_info(): 
  """Prompts the user for information about a car and then returns an object containing those properties"""

  brand = input("Enter brand: ")
  model = input("Enter model: ")
  year = 0
  price = 0
  while year <= 0: #I utilized a while loop for the purpose of repeating the print whenever necessary
    try:
      year = int(input("Enter year: ")) #This avoids the input being a word and makes sure it ends up being a whole number
      if year <= 0: #This is for whenever the year is a negative number
        raise Exception 
    except: #This works alongside the while loop whenever the input is a word or negative number
      print("Please enter valid year.")

  while price <= 0: #The loop will continue whenever there is an invalid input including anything less than or equal to zero
    try:
      price = float(input("Enter price: ")) #With floats this helps avoid the input being a word and prints it as a decimal
      if price <= 0: #Utilizing this if statement will avoid negative digits within inputing information
        raise Exception
    except: #This print will repeat whenever a word or negative numeral
      print("Please enter valid price.")

  return (brand, model, year, price)


def get_colors(brand, model, year): 
  """Prompts the user for information about the color of a car(s) and then returns an object containing those properties"""

  colors = []
  amt_colors = -1
  while amt_colors < 0: #Utilizing while loop it makes sure that through each iteration is zero and greater when taking in number of colors
    try:
      amt_colors = int(input(f"How many different colors are for the {brand} {model} of {year}? "))
      if amt_colors < 0: #This if statement is meant to identify negative numbers so that the input will end up a positive
        raise Exception
    except: #This will print whenever theres a word or a negative digit so that we get a proper positive input
      print("Please enter valid amount.")

  for lub in range(0,amt_colors): #Utilizing the for loop I identified the numerical value of the colors and each color will be added to a list
    color = input(f"Enter the color #{lub+1} for the {brand} {model} of {year}: ") 
    colors.append(color) 
  
  return colors

def save_inventory(brand, car_inventory):
  """Maintains and updates the brand and inventory based on new input provided by user"""

  car_inventory.append(brand)



def brand_counter(brand, brands, accum):
  """Prompts the user for information about the brands and then updates accordingly based on object containing those properties"""

  for lub in range(0,len(brands)): #This for loop is meant to take into consideration the amount of brands in a list
    if brands[lub] == brand:
      accum[lub] += 1
      break #I used break to disengage from this for loop so it wouldnt go on eternally and since its a void function nothing is returned


def max_brand(accum,brands):
  """Prompts the user for information about the highest ammount of brands and then returns an object containing those properties"""

  max_accum = 0 
  max_cars = []

  for lub in range(0,len(accum)): #This for loop is meant to analize the list to figure our which value if the max ammount of brand
    if accum[lub] > accum[max_accum]:
      max_accum = lub  
 
  for lub in range(0,len(brands)): #This is utilized for assessing the final max is actually the largest in the list
    if accum[lub] == accum[max_accum]:
      max_cars.append(brands[lub])

  return max_cars

def get_max_brand(brands, accum):
  """Prompts the user for information about list of highest amount of cars for each brand and then returns an object containing those properties"""

  max_cars = max_brand(accum, brands)

  print("\n~*~*~ CAR SUMMARY ~*~*~\n")
  print('The brand(s) with the most cars:' )

  for car in max_cars:
    print(car)

  print("\n~*~*~ END SUMMARY ~*~*~\n")

def main():

  car_inventory = []
  accum =[0,0,0,0]
  brands = ['Toyota','Tesla','Dodge','Cadillac']

  try:
    amount = int(input("How many cars do you want to add? "))
  except ValueError:
    print("Please enter a valid number.")
    amount = int(input("How many cars do you want to add? "))

  if amount <= 0:
    print("Please try again.")
    amount = int(input("How many cars do you want to add? "))
  else:
    i = 1

    while amount > 0:

      print(f"Enter information of car #{i}:")

      brand, model, year, price = get_car_info()
      save_inventory(brand, car_inventory)
      colors = get_colors(brand, model, year)
      brand_counter(brand,brands, accum)

      print("\n~*~*~ CAR SUMMARY ~*~*~\n")
      print(f"BRAND: {brand}")
      print(f"MODEL: {model}")
      print(f"YEAR: {year}")
      print(f"PRICE: {price}")
      print(f"COLORS: {colors}")
      print("\n~*~*~ END SUMMARY ~*~*~\n")

      i += 1
      amount -=1
    
  get_max_brand(brands, accum)

main()