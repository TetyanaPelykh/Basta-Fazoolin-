#Scrabble
#In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#We have provided you with two lists, letters and points. We would like to combine these two into a dictionary that would map a letter to its point value.
#Using a list comprehension and zip, create a dictionary called letter_to_points that has the elements of letters as the keys and the elements of points as the values.

letter_to_points = {key:value for key, value in zip(letters, points)}
print(letter_to_points)

#Our letters list did not take into Icono en blanco de la cuentas. Add an element to the letter_to_points dictionary that has a key of " " and a point value of 0.

letter_to_points[" "]= 0
print(letter_to_points)

#We want to create a function that will take in a word and return how many points that word is worth.
#Define a function called score_word that takes in a parameter word.
#Inside score_word, create a variable called point_total and set it to 0.
#After defining point_total, create a for loop that goes through the letters in word and adds the point value of each letter to point_total.
#You should get the point value from the letter_to_points dictionary. If the letter you are checking for is not in letter_to_points, add 0 to the point_total.
#After the for loop is finished, return point_total.

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points[letter]
  return point_total

#Let’s test this function! Create a variable called brownie_points and set it equal to the value returned by the score_word() function with an input of "BROWNIE".

brownie_points = score_word("BROWNIE")

#We expect the word BROWNIE to earn 15 points:
#(B + R + O + W + N + I + E)
#(3 + 1 + 1 + 4 + 4 + 1 + 1) = 15
#Let’s print out brownie_points to make sure we got it right.

print(brownie_points)

#Create a dictionary called player_to_words that maps players to a list of the words they have played. This table represents the data to transcribe into your dictionary:

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordnerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
print(player_to_words)
#Create an empty dictionary called player_to_points.
player_to_points = {}

#Iterate through the items in player_to_words. Call each player player and each list of words words.
#Within your loop, create a variable called player_points and set it to 0.

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)
