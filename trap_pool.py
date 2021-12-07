from Trap import Trap

boulder = Trap("Bouldertrap", "A large boulder comes rolling towards you what will you do?", "You punched the boulder and took damage what did you expect?",
               "You tried to flee but did not make it your toes got cruched", "You did nothing and the boulder decided to leave you alone")
cheese = Trap("Cheesetrap", "You see a large block of cheese on a pedestal what do you want to do?",
              "You ate the cheese and went to sleep", "You moved on and tripped hitting your knee", "You fed the cheese to a mouse and he gave you his dripcap")
santa = Trap("Santatrap", "You walked in to a room and saw Santa claus :D, what do you want to do?", "You opened the present and found a bomb, ouch!", "Whilst you were sitting on his lap, santa stole one of your items",
             "Santa became furious and hit you with a belt 4 times, but you managed to catch and take the belt")
jordan = Trap("Jordantrap", "After entering through the door you find yourself on a basketball court with Michael Jordan, he asks you to play a 1v1 basketball game, what do you do?",
              "You chose to let him win and he gave you a token of appreciation", "You beat him in the most embarrasing way possible, and in return, he beats you to a pulp", "You run away crying and escape with your life")
joebiden = Trap("Joebidentrap", "You enter the oval office and you see president Joseph Robinette Biden Junior sitting at his desk, what is your next action?",
                "You waved and left", "You sneezed killing the president in an instant, and took the oppertunity to steal his tie", "You got an asswhooping by Joe")
alchemist = Trap("Alchemisttrap", "You enter an alchemist shop where they offer you one free potion, you can choose between three different potions",
                 "You picked the green potion and suffer some damage (-2Hp)", "You picked the red potion and take it with you", "You picked the blue potion and feel permanently healthier(+1 Max HP)")
lake = Trap("Laketrap", "After walking through the door you find yourself on a cliff next to a lake, you see that there are fish in the water, what do you do?", "You reeled in a fish!",
            "You dove in to catch the fish barehanded but you hit your head on the side of the cliff", "You rest up for a bit, enjoying the nice ambience, and then move on")
monke = Trap("Monketrap", "You enter a room and find a monke sitting on a log, it looks at you as if it had been waiting for your arrival, what do you do?", "you slowly walk away from the monke, you get away safely", "You trade with the monke, losing 1 random item but gaining a knife it had saved away ",
             "You run away in a haste, but the monke flings its poop after you and it hits your back")
theo = Trap("Theotrap", "You find yourself standing in a room with your childhood crush Theodor, What do you do? ", "You tell the handsome boy that you are cold, and he offers you his jacket ",
            "You confess your love for him however, he does not feel the same way and you suffer emotional damage(-1 Max Hp) ", "You choose to avoid confrontation and run away")
computer = Trap("Computertrap", "You find a 1990's apple macintosh in an old dusty room, what do you do with it? ", "You violently smash it to pieces, and in the wreckage, you find an old cd-rom disc ",
                "You try to plug it in, but instead your entire body gets filled with electric shocks (-2hp) ", "You walk away despite being curious what secrets that old dusty thing might've held. ")
spikes = Trap("Spiketrap ", "You walk into a room and see a spiketrap on the ground, how do you continue?", "you try to jump over the spikes but fail horribly and fall into them ",
              "You break off one of the spikes and walk back the way you came ", "You carefully walk through the trap, being delicate so to not trigger it, and you get away safely ",)
old_man = Trap("Oldmantrap ", "You see an old man sitting on a stone holding a cane, you slowly approach him and he offers you three different bags, which one do you take? ", "You took the first bag, and recieved a red potion!",
               "You picked the second bag and recieved a stick! ", "you picked the second bag, and found a strange note that said *look behind you* but before you could turn around, you fell unconsious")
caves = Trap("Cavetrap ", "After walking through the door you fins yourself in a cavesystem with three different caves you can walk towards, which one do you choose? ", "You walk through the left cave and find a treasure chest! ",
             "You walk throught the middle-most cave and keep walking for what feels like forever, eventually reaching another door ", "You walk through the right cave and a stalactite falls on your head ")
""" smt = Trap(" ", " ", " ", " "," ")"""
""" smt = Trap(" ", " ", " ", " ","")"""
""" smt = Trap(" ", " ", " ", " ","")"""
""" smt = Trap(" ", " ", " ", " ","")"""
""" smt = Trap(" ", " ", " ", " ","")"""
""" smt = Trap(" ", " ", " ", " ","")"""
""" smt = Trap(" ", " ", " ", " ","")"""

trap_pool = [boulder, cheese, santa, jordan,
             joebiden, alchemist, lake, monke, theo, computer]
