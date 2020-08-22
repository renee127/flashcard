
"""
   Uses a dictionary to create flashcards.
"""

import turtle
import random
import textwrap
import csv

# Use spreadsheet csv to create dictionary.

reader = csv.reader(open('gre_words.csv'))

terms = {}
for row in reader:
    key = row[0]
    terms[key] = row[1]
print(terms)


while terms:

    # Find a random term/definition combo
    idx = random.randint(0, (len(terms)-1))
    first_key = list(terms)[idx]
    print(first_key)
    first_def = list(terms.values())[idx]
    print(first_def)
    first_def = textwrap.fill(first_def, width=30)
    print(first_key, first_def)

    # Create interface window.
    win = turtle.Screen()
    win.title('Flash Cards')
    win.bgcolor('grey')
    win.setup(width = 600, height = 300)

    # Use tracer to stop window from automatically updating
    win.tracer(0)

    # TODO: remove this test term
    term = 'silly'

    # Pen to write terms.
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color('white')
    pen.penup() # avoids the line
    pen.hideturtle() # don't need to see it, just text
    pen.goto(0,80)
    pen.write(first_key, align='center', font=('Courier', 30,))

    # TODO: find a way to activate the definition
    # TODO: find a way to limit size with text wrap?

    # Pen to write definitions.
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color('white')
    pen.penup() # avoids the line
    pen.hideturtle() # don't need to see it, just text
    pen.goto(0,-100)
    pen.write(first_def, align='center', font=('Courier', 30,))
    first_def = list(terms.values())[0]

    # clear(), reset(), write()

    # TODO onclick reset window
    #win.onscreenclick(None, reset)
    # TODO find way to advnance through flashcards
    # TODO find way to allow user to get rid of card

    # This keeps the window open
    turtle.mainloop()
