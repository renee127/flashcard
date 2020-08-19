
"""
   Uses a dictionary to create flashcards.
"""



import turtle
import random

# Create a dictionary of terms.
terms = {
   "acerbic": "having a sour or bitter taste or character, sharp, biting",
   "aggrandize": "to increase in intensity, power, influence, or prestige",
   "amenable": "agreeable, responsive to suggestion",
   "astringent": "having a tightening effect on living tissue, harsh, severe, something with a tightening effect on tissue",
   "contiguous": "sharing a border, touching, adjacent"}

idx = random.randint(0, (len(terms)-1))
print(idx)
first_key = list(terms)[idx]

# Create interface window.
win = turtle.Screen()
win.title('Flash Cards')
win.bgcolor('grey')
win.setup(width = 600, height = 300)

# Use tracer to stop window from automatically updating
win.tracer(0)



# Find random term
term = 'silly'

# Pen to write terms
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup() # avoids the line
pen.hideturtle() # don't need to see it, just text
pen.goto(0,50)
pen.write(first_key, align='center', font=('Courier', 30,))

# clear(), reset(), write()

# TODO onclick reset window
win.onscreenclick(None, reset)


#turtle.onclick(pen.write(term, align='center', font=('Courier', 30,)))


# This keeps the window open
turtle.mainloop()
