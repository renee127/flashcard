
"""
   Uses a dictionary to create flashcards.
"""

import turtle

# Create interface window.
win = turtle.Screen()
win.title('Flash Card')
win.bgcolor('grey')
win.setup(width = 600, height = 300)

# Use tracer to stop window from automatically updating
win.tracer(0)

# Create dictionary of terms.
# gre_dict = {adulterate : to reduce purity by combining with inferior ingredients
#             amalgamate : to combine several elements into a whole
#             aver : to state as a fact, too declare or assert
#             bolster : to provide support or reinforcement
#             bombastic : pompous, grandiloquent
#             diatribe : a harsh denunciation
#             assemble : to disguise or conceal, to mislead
#             endemic : characteristic of or often found in a particular locality, region, or people
#             evanescent : tending to disappear like vapor, vanishing
#             fortuitous : happening by accident or chance
#             hackneyed : rendered trite or commonplace by frequent usage
#             halcyon : calm and peaceful
#             hegemony : the consistent dominance of one state or group over others
#             iconoclast : one who attacks or undermines traditional conventions or institutions
#             idolatrous : given to intense or excessive devotion to something
#             impassive : revealing no emotion
#             imperturbable : marked by extreme calm, impassivity, and steadiness
#             implacable : not capable of being appeased or significantly changed
#             impunity : immunity from punishment or penalty
#             inchoate : in an initial stage, not fully formed
#             insipid : lacking in qualities that interest, stimulate or challenge
#             malleable : capable of being shaped or formed, tractable, pliable
#             mendacity : the condition of being untruthful, dishonest, mendacious
#             misanthrope : one who hates all other humans, misanthropic
#             obdurate : unyielding, hardhearted, intractable
#             obsequious : exhibiting a fawning attentiveness
#             occlude : to obstruct or block
#             opprobrium : disgrace, contempt, scorn
#             pedagogy : the profession or principles of teaching or instructing
#             pedantic : overly concerned with the trivial details of learning or education, show offish 
#             penury : poverty, destitution
#             pine : to yearn intensely, to languish, to lose vigor
#             pith : the essential or central part
#             pithy : precise and brief
#             placate : to appease, to calm by making concessions
#             platitude : a superficial remark, especially one offered as meaningful
#             polemical : controversial, argumentative
#             prodigal : recklessly wasteful, extravagant, profuse, lavish
#             profuse : given or coming forth abundantly, extravagant
#             proliferate : to grow or increase swiftly and abundantly
#             queries : questions, inquiries, doubts in the mind, reservations
#             querulous : prone to complaining or grumbling, peevish
#             rancorous : characterized by bitter, long lasting resentment
#             recalcitrant : obstinately defiant of authority, difficult to manage
#             repudiate : to refuse to have anything to do with, to disown
#             rescind : to invalidate, to repeal, to retract
#             reverent : marked by, feeling, or expressing a feeling of profound awe and respect
#             rhetoric : the art or study of effective use of language for communication and persuasion
#             salubrious : promoting health or well being
#             solvent : able to meet financial obligations, able to dissolve another substance
#             specious : seeming true, but actually being fallacious, misleadingly attractive, plausible but false
#             spurious : lacking authenticity or validity, false, counterfeit
#             superfluous : exceeding what is sufficient or necessary
#             surfeit : an overabundant supply, excess, to feed or supply to excess
#             tirade : a long and extremely critical speech, a harsh denunciation
# }

# Find random term
term = 'silly'

# Pen to write terms
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup() # avoids the line
pen.hideturtle() # don't need to see it, just text
pen.goto(0,50)
pen.write(term, align='center', font=('Courier', 30,))

# This keeps the window open
turtle.mainloop()
