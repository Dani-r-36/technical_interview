#task 1 - convert guardian (in upper case ) to score 
#assume upper case, one tile one time, given string 
#dict stores the score 
#string -> list -> for loop each letter check score -> add to final score 

#function to get letter from list of all letters using random to send 7 titles back to main where they hold 7 titles 
# for in range -> random number and get string position -> append to list -> back main -> testing function 

from random import randint

def main(word):
    letter_points = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10
    }
    total = 0
    for letter in word:
        total += letter_points[letter]
    return total

def random_letter():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tile_amount = 7
    returning_list =[] 
    for i in range (tile_amount):
        returning_list.append(alphabet[randint(0,25)])
    return returning_list

def player_rack():
    return random_letter