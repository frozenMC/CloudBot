from util import hook
import re
import random

insults = ["You are the son of a motherless ogre.",
        "Your mother was a hamster and your father smelled of elderberries.",
        "I once owned a dog that was smarter than you. ",
        "Go climb a wall of dicks.",
        "You fight like a dairy farmer.",
        "I've spoken to apes more polite than you.",
        "Go and boil your bottom! Son of a silly person! ",
        "I fart in your general direction.",
        "Go away or I shall taunt you a second time. ",
        "Shouldn't you have a license for being that ugly?",
        "Calling you an idiot would be an insult to all the stupid people.",
        "Why don't you slip into something more comfortable...like a coma.",
        "Well, they do say opposites attact...so I sincerely hope you meet somebody who is attractive, honest, intelligent, and cultured..",
        "Are you always this stupid or are you just making a special effort today?",
        "Yo momma so fat when she sits around the house she sits AROUND the house.",
        "Yo momma so ugly she made an onion cry.",
        "Is your name Maple Syrup? It should be, you sap.",
        "Bite my shiny metal ass!",
        "Up yours, meatbag.",
        "Jam a bastard in it you crap!",
        "Don't piss me off today, I'm running out of places to hide to bodies",
        "Why don't you go outside and play hide and go fuck yourself",
        "I'll use small words you're sure to understand, you warthog-faced buffoon.",
        "You are a sad, strange little man, and you have my pity.",
        "Sit your five dollar ass down before I make change.",
        "What you've just said is one of the most insanely idiotic things I've ever heard. Everyone in this room is now dumber for having listened to it. May God have mercy on your soul.",
        "Look up Idiot in the dictionary. Know what you'll find? The definition of the word IDIOT, which you are.",
        "You're dumber than a bag of hammers.",
        "Why don't you go back to your home on Whore Island?",
        "If I had a dick this is when I'd tell you to suck it.",
        "Go play in traffic.",
        "The village called, they want their idiot back."]

@hook.command(autohelp=False)
def insult(inp, nick=None, say=None, input=None):
    ".insult <user> -- Makes the bot insult <user>."
 
    msg = "(" + nick + ") " + random.choice(insults)
    if re.match("^[A-Za-z0-9_|.-\]\[]*$", inp.lower()) and inp != "":
        msg = "(@" + inp + ") " + random.choice(insults)

    if inp == input.conn.nick.lower() or inp == "itself":
        msg = "*stares at " + nick + "*"

    say(msg)
