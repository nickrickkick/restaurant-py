"""Restaurant rating lister."""


# put your code here
def processScores():

    scoresTxt = open('scores.txt')

    scores = {}

    for line in scoresTxt:
        line = line.rstrip()
        restaurant, score = line.split(":")
        scores[restaurant] = int(score)

    return scores


def addRestaurant(scores):

    print("add a rating to a restaurant")
    restaurant = input("Restaurant name: ")
    rating = int(input("Rating: "))

    scores[restaurant] = rating


def printScores(scores):

    for restaurant, rating in sorted(scores.items()):
        print(f"{restaurant} is rated at {rating}.")


scores = processScores()
addRestaurant(scores)
printScores(scores)