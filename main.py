from art import logo
# from replit import clear

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 10,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

profit = 0
resources = {
  "water" : 300,
  "milk" : 200,
  "coffee" : 100,
}

print(logo)

def is_resource_enough(order_ingredients):
  """Returns True when order can be made, False if ingredients are insufficient"""
  for item in order_ingredients:
    if order_ingredients[item] > resources[item]:
      print(f"♥ Sorry, there is not enough {item}.")
      return False
  return True

def process_coin():
  """Returns the total calculated from coins inserted."""
  print("✷｡  🎀  𝒫𝓁𝑒𝒶𝓈𝑒 𝒾𝓃𝓈𝑒𝓇𝓉 𝓉𝒽𝑒 𝒸💍𝒾𝓃𝓈.  🎀  ｡✷")
  Q = int(input("How many 100's? : ")) * 100
  D = int(input("How many 50's? : ")) * 50
  N = int(input("How many 10's? : ")) * 10
  P = int(input("How many 5's? :")) * 5
  total = (Q + D + N + P)
  return total

def is_transaction_sucessful(money_received, drink_cost):
  """Returns True when the payment is accepted, or False if money is insufficient."""
  if money_received >= drink_cost:
    change = round(money_received - drink_cost, 2)   
    print(f"Here is Rs.{change} in change.")
    global profit
    profit += drink_cost
    return True
  else:
    print("𝕊𝕠𝕣𝕣𝕪, 𝕥𝕙𝕖 𝕞𝕠𝕟𝕖𝕪 𝕪𝕠𝕦 𝕚𝕟𝕤𝕖𝕣𝕥𝕖𝕕 𝕚𝕤 𝕟𝕠𝕥 𝕤𝕦𝕗𝕗𝕚𝕔𝕚𝕖𝕟𝕥.")
    return False

def make_coffee(drink_name, order_ingredients):
  """Deduct the required ingredients from the resources."""
  for item in order_ingredients:
    resources[item] -= order_ingredients[item]
  print(f"🅷🅴🆁🅴 🅸🆂 🆈🅾🆄🆁 {drink_name} ☕. 🅴🅽🅹🅾🆈!")

is_on = True

while is_on:
  choice = input("What would you like? ░(░e░s░p░r░e░s░s░o░/░l░a░t░t░e░/░c░a░p░p░u░c░c░i░n░o░)░: \n")
  if choice == 'off':
    is_on = False
  elif choice == 'report':
    print(f"Water: {resources['water']}ml.")
    print(f"Milk: {resources['milk']}ml.")
    print(f"Coffee: {resources['coffee']}gm.")
    print(f"Money: Rs.{profit}")
  else:
    drink = MENU[choice]
    if is_resource_enough(drink["ingredients"]):
      payment = process_coin()
      if is_transaction_sucessful(payment, drink['cost']):
        make_coffee(choice ,drink["ingredients"])
    # clear()
