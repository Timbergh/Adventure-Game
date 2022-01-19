import time
import random as rand

from doors import doors
from clearConsole import clearConsole
from inventory import *
from create_character import create_character
from stats import stats
from random_encounter import trap_pool


def main():
    rand.shuffle(trap_pool)
    rounds = 0
    player = create_character()
    clearConsole()
    character = open("art/char1.txt", "r")
    print(f"Hello {player.name}\nThis is you")
    print(character.read())
    input("Press enter to continue").casefold()
    clearConsole()
    print("I will now calculate your stats...\n")
    time.sleep(0)  # ÄNDRA PÅ TIDEN INNAN INLÄMNING
    print(f"HP = {player.maxhp}")
    time.sleep(0)  # ÄNDRA PÅ TIDEN INNAN INLÄMNING
    print(f"Damage = {player.dmg}\n")
    input("Press enter to continue").casefold()
    clearConsole()
    while True:
        if player.hp <= 0:
            clearConsole()
            print("You died...")
            game_over = open("art/gameover.txt", "r")
            print(game_over.read())
            time.sleep(5)
            break
        menu = input("""
        --------------MENU--------------
        | [i] Inventory                |
        | [s] Stats                    |
        | [c] Continue                 |
        | [q] Quit                     |
        |                              |
        |                              |
        --------------------------------
        """).casefold()
        if menu == "i":
            clearConsole()
            player = inventory(player, your_items)
        elif menu == "c":
            clearConsole()
            rounds = rounds + 1
            doors(player, rounds)
        elif menu == "s":
            clearConsole()
            stats(player, player.name)
        elif menu == "q":
            clearConsole()
            print("Quiting game...")
            break
        if menu != "i":
            clearConsole()


main()


"""
Katt-guden Frasse:
       ,
       \`-._           __
        \\  `-..____,.'  `.
         :`.         /    \`.
         :  )       :      : \
          ;'        '   ;  |  :
          )..      .. .:.`.;  :
         /::...  .:::...   ` ;
         ; _ '    __        /:\
         `:o>   /\o_>      ;:. `.
        `-`.__ ;   __..--- /:.   \
        === \_/   ;=====_.':.     ;
         ,/'`--'...`--....        ;
              ;                    ;
            .'                      ;
          .'                        ;
        .'     ..     ,      .       ;
       :       ::..  /      ;::.     |
      /      `.;::.  |       ;:..    ;
     :         |:.   :       ;:.    ;
     :         ::     ;:..   |.    ;
      :       :;      :::....|     |
      /\     ,/ \      ;:::::;     ;
    .:. \:..|    :     ; '.--|     ;
   ::.  :''  `-.,,;     ;'   ;     ;
.-'. _.'\      / `;      \,__:      \
`---'    `----'   ;      /    \,.,,,/
                   `----`                   
                                                                                                                    
 """
