from scipy.optimize import minimize
import numpy as np
from Food import Food


def objective(foodList):
    totalPrice = 0
    for food in foodList:
        totalPrice += food.price()
    return totalPrice


def fat(FoodList):
    fat = 0
    for food in FoodList:
        fat += food.fat()
    return 20 - fat


def sodium(FoodList):
    sodium = 0
    for food in FoodList:
        sodium += food.sodium()
    return 2400 - sodium


def vitC(FoodList):
    vitC = 0
    for food in FoodList:
        vitC += food.vitC()
    return vitC - 90


def vitA(FoodList):
    vitA = 0
    for food in FoodList:
        vitA += food.vitA()
    return vitA - 700


def protien(FoodList):
    protein = 0
    for food in FoodList:
        protein += food.protein()
    return protein - 56


def calories(FoodList):
    calories = 0
    for food in FoodList:
        calories += food.calories()
    return 2000 - calories


def main():
    #  Order of parameters (name, price, calories, fat, sodium, vitC, vitA, protein)
    apple = Food('Apple', 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    apple1 = Food('Apple1', 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    chips = Food('chips', 1.0, 10.0, 10.0, 1.0, 1.0, 1.0, 1.0)
    chips1 = Food('chips1', 1.0, 10.0, 10.0, 1.0, 1.0, 1.0, 1.0)
    chips2 = Food('chips2', 1.0, 10.0, 10.0, 1.0, 1.0, 1.0, 1.0)

    con1 = {'type': 'eq', 'fun': calories}
    con2 = {'type': 'ineq', 'fun': fat}
    con3 = {'type': 'ineq', 'fun': sodium}
    con4 = {'type': 'ineq', 'fun': vitC}
    con5 = {'type': 'ineq', 'fun': vitA}
    con6 = {'type': 'ineq', 'fun': protien}

    allcons = [con1, con2, con3, con4, con5, con6]

    myFood = [apple, apple1, chips, chips1, chips2]

    solution = minimize(objective, myFood,method='SLSQP', constraints=allcons)

    print(protien(myFood))


if __name__ == '__main__':
    main()
