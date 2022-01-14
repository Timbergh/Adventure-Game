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
    input("Press enter to continue")
    clearConsole()
    print("I will now calculate your stats...\n")
    time.sleep(0)  # ÄNDRA PÅ TIDEN INNAN INLÄMNING
    print(f"HP = {player.maxhp}")
    time.sleep(0)  # ÄNDRA PÅ TIDEN INNAN INLÄMNING
    print(f"Damage = {player.dmg}\n")
    input("Press enter to continue")
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
             _____________________
               \ ______________/                          
             ..(.....    ...../,.            
       ,/(((,( ..             . /*((((/      
       /((/( ..    ,******,     . **(((.     
       //(.      .//////////.      .(,/.     
    /(//((((*(((/  ...,,...  /(((/(((((/(/   
   /((/(((((/((((/  ..,,..  /((((/(((((//(/  
  *(((//(((((/((((((((((((((((((//(((((/(((* 
  ,/(((/((((((//////////(///////((((((/(((/, 
   /((// @@ /((,,,,,,((((,,,,,,//( @&  (/(/  
    /(//(// //........((......../( //(////   
    .,//'  //////((((((((((//////  .. //.   
      .......                    ........    
                                                                                                                                                                                                          
        Innocent little puppy:                                                                                                                                                                                              
                                   ..,,,,,,,,,.. 
                     .,;%%%%%%%%%%%%%%%%%%%%;,. 
                   %%%%%%%%%%%%%%%%%%%%////%%%%%%, .,;%%;, 
            .,;%/,%%%%%/////%%%%%%%%%%%%%%////%%%%,%%//%%%, 
        .,;%%%%/,%%%///%%%%%%%%%%%%%%%%%%%%%%%%%%%%,////%%%%;, 
     .,%%%%%%//,%%%%%%%%%%%%%%%%@@%a%%%%%%%%%%%%%%%%,%%/%%%%%%%;, 
   .,%//%%%%//,%%%%///////%%%%%%%@@@%%%%%%///////%%%%,%%//%%%%%%%%, 
 ,%%%%%///%%//,%%//%%%%%///%%%%%@@@%%%%%////%%%%%%%%%,/%%%%%%%%%%%%% 
.%%%%%%%%%////,%%%%%%%//%///%%%%@@@@%%%////%%/////%%%,/;%%%%%%%%/%%% 
%/%%%%%%%/////,%%%%///%%////%%%@@@@@%%%///%%/%%%%%//%,////%%%%//%%%' 
%//%%%%%//////,%/%a`  'a%///%%%@@@@@@%%////a`  'a%%%%,//%///%/%%%%% 
%///%%%%%%///,%%%%@@aa@@%//%%%@@@@S@@@%%///@@aa@@%%%%%,/%////%%%%% 
%%//%%%%%%%//,%%%%%///////%%%@S@@@@SS@@@%%/////%%%%%%%,%////%%%%%' 
%%//%%%%%%%//,%%%%/////%%@%@SS@@@@@@@S@@@@%%%%/////%%%,////%%%%%' 
`%/%%%%//%%//,%%%///%%%%@@@S@@@@@@@@@@@@@@@S%%%%////%%,///%%%%%' 
  %%%%//%%%%/,%%%%%%%%@@@@@@@@@@@@@@@@@@@@@SS@%%%%%%%%,//%%%%%' 
  `%%%//%%%%/,%%%%@%@@@@@@@@@@@@@@@@@@@@@@@@@S@@%%%%%,/////%%' 
   `%%%//%%%/,%%%@@@SS@@SSs@@@@@@@@@@@@@sSS@@@@@@%%%,//%%//%' 
    `%%%%%%/  %%S@@SS@@@@@Ss` .,,.    'sS@@@S@@@@%'  ///%/%' 
      `%%%/    %SS@@@@SSS@@S.         .S@@SSS@@@@'    //%%' 
               /`S@@@@@@SSSSSs,     ,sSSSSS@@@@@' 
             %%//`@@@@@@@@@@@@@Ss,sS@@@@@@@@@@@'/ 
           %%%%@@00`@@@@@@@@@@@@@'@@@@@@@@@@@'//%% 
       %%%%%%a%@@@@000aaaaaaaaa00a00aaaaaaa00%@%%%%% 
    %%%%%%a%%@@@@@@@@@@000000000000000000@@@%@@%%%@%%% 
 %%%%%%a%%@@@%@@@@@@@@@@@00000000000000@@@@@@@@@%@@%%@%% 
%%%aa%@@@@@@@@@@@@@@0000000000000000000000@@@@@@@@%@@@%%%% 
%%@@@@@@@@@@@@@@@00000000000000000000000000000@@@@@@@@@%%%%%      
                                                                                                                    
 """
