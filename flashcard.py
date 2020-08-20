
"""
   Uses a dictionary to create flashcards.
"""

import turtle
import random
import textwrap

# Create a dictionary of terms.
terms = {
   "acerbic": "having a sour or bitter taste or character, sharp, biting",
   "aggrandize": "to increase in intensity, power, influence, or prestige",
   "amenable": "agreeable, responsive to suggestion",
   "astringent": "having a tightening effect on living tissue, harsh, severe, something with a tightening effect on tissue",
   "contiguous": "sharing a border, touching, adjacent",
   "alacrity": "eager and enthusiastic willingness",
   "approbation": "an expression of approval or praise",
   "axiomatic": "taken as a given; possessing self-evident truth, axiom",
   'canonical': "following or in agreement with accepted, traditional standards, canon",
   "chicanery" : "trickery or subterfuge",
   "disabuse" : "to undeceive, to set right",
   'equivocate' : 'to use ambiguous language with a deceptive intent',
   "effrontery" : "extreme boldness, presumptuousness",
   'enervate' : 'to weaken, to reduce in vitality',
   'ennui' : 'dissatisfaction and restlessness resulting from boredom or apathy',
   'equivocate' : 'to use ambiguous language with a deceptive intent',
   'exigent' : 'urgent, pressing, requiring immediate action or attention',
   'extemporaneous' : 'improvised, off the cuff, done without preparation',
   'fulminate' : 'to loudly attack or denounce',
   'ingenuous' : 'artless, frank and candid, lacking in sophistication',
   'inured' : 'accustomed to accepting something undesirable',
   'irascible' : 'easily angered, prone to temperamental outbursts',
   'laud' : 'to praise highly, laudatory',
   'magnanimity' : 'the quality of being generously noble in mind and heart, especially in forgiving',
   'martial' : 'associated with war and the armed forces',
   'neologism' : 'a new word, expression, or usage, the creation or use of new words or senses',
   'obviate' : 'to anticipate and make unnecessary',
   'paean' : 'a song or hymn of praise and thanksgiving',
   'perennial' : 'recurrent through the year or many years, happening repeatedly',
   'perfidy' : 'intentional breach of faith, treachery'}

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
