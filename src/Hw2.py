# This is a Linear Programming solver. It takes nutrition facts about 5 food items.
# Tries to give the food recommendation that minimizes the cost.
# Written By - Sarun Luitel

from scipy.optimize import minimize
import numpy as np
from Food import Food

# nutrition contents are calculated per kilogram of food.
# Fat in grams, sodium, Vit C in milligrams,VitA in mcg)
# prices from: https://www.ers.usda.gov/data-products/fruit-and-vegetable-prices.aspx


apple = Food('Apple', 3.0, 520, 0, 10.4, 45.6, 572, 2.4)
# http://nutritiondata.self.com/facts/fruits-and-fruit-juices/1809/2

brownRice = Food('Brown Rice', 9.06, 1110, 2, 50, 0, 0, 26)
# https://www.livescience.com/50461-brown-rice-health-benefits-nutrition-facts.html

chickenBreast = Food('Chicken Breast', 12.05, 2930, 38, 4570, 0.0, 0.0, 158)  # chicken Breast
# http://nutritiondata.self.com/facts/poultry-products/10046/2

kidneyBeans = Food('Kidney Beans', 10.99, 1240, 0.0, 40, 12, 31.8, 91)
# http://nutritiondata.self.com/facts/legumes-and-legume-products/4300/2

yogurt = Food('Yogurt', 5.5, 610, 21, 460, 50, 1048.7, 35)
# http://nutritiondata.self.com/facts/dairy-and-egg-products/104/2

FoodList = [apple, brownRice, chickenBreast, kidneyBeans, yogurt]


def objective(foodNum):
    totalPrice, index = 0, 0
    for food in FoodList:
        totalPrice += foodNum[index] * food.price()
        index += 1
    return totalPrice


def fat(foodNum):
    fat, index = 0, 0
    for food in FoodList:
        fat += foodNum[index] * food.fat()
        index += 1
    return 20 - fat


def sodium(foodNum):
    sodium, index = 0, 0
    for food in FoodList:
        sodium += foodNum[index] * food.sodium()
        index += 1
    return 2400 - sodium


def vitC(foodNum):
    vitC, index = 0, 0
    for food in FoodList:
        vitC += foodNum[index] * food.vitC()
        index += 1
    return vitC - 90


def vitA(foodNum):
    vitA, index = 0, 0
    for food in FoodList:
        vitA += foodNum[index] * food.vitA()
        index += 1
    return vitA - 700


def protien(foodNum):
    protein, index = 0, 0
    for food in FoodList:
        protein += foodNum[index] * food.protein()
        index += 1
    return protein - 56


def calories(foodNum):
    calories, index = 0, 0
    for food in FoodList:
        calories += foodNum[index] * food.calories()
        index += 1
    return 2000 - calories


def main():
    #  Order of parameters (name, price, calories, fat, sodium, vitC, vitA, protein)

    con1 = {'type': 'ineq', 'fun': fat}
    con2 = {'type': 'ineq', 'fun': sodium}
    con3 = {'type': 'ineq', 'fun': vitC}
    con4 = {'type': 'ineq', 'fun': vitA}
    con5 = {'type': 'ineq', 'fun': protien}
    con6 = {'type': 'eq', 'fun': calories}

    allcons = [con1, con2, con3, con4, con5, con6]
    foodnum = np.array([1.0, 100000.0, 1.0, 10000.0, 1.0])

    b = (0.1, None)
    bounds = (b, b, b, b, b)

    solution = minimize(objective, foodnum, method='SLSQP', constraints=allcons, bounds=bounds)

    print(solution)


if __name__ == '__main__':
    main()
