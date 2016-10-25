# Program to generate a random number between 0 and 9

# import the random module
# Python program to shuffle a deck of card using the module random and draw 5 cards

# import modules
import itertools, random

print(random.randint(0,9))
# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

print deck
# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got:")
for i in range(13):
   print(deck[i][0], "of", deck[i][1])

'''

In program, we used the product() function in itertools module to create a
deck of cards. This function performs the Cartesian product of the two sequence. The two sequence are, numbers from 1 to 13 and the four suits. So, altogether we have 13 * 4 = 52 items in the deck with each card as a tuple. For e.g. deck[0] = (1, 'Spade'). Our deck is ordered, so we shuffle it using the function shuffle() in random module. Finally, we draw the first five cards and display it to the user. We will get different output each time you run this program as shown in our two outputs.

Here we have used the standard modules itertools and random that comes with
Python.

'''
# Python program to display calendar of given month of the year

# import module
import calendar

# ask of month and year
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy,mm))
