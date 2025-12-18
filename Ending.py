import random
import time
#character begining & endings #NPC 1,2,3,4


def ending():
    play = 0
    while play < 1:
        roll = random.randint(1,15)
        print(f"You rolled a {roll}")
        if roll == 1:
            print ("The Dungeon Master tells the NPC's to go on a journey")
        elif roll == 2:
            print ("NPC 1, NPC 2, NPC 3, NPC 4 unite together and head out on a journey")
        elif roll == 3:
            print ("The party encounters a Giant Spider")
            print("Rolling the dice again")
            time.sleep(3)
            spider_roll = random.randint(1,25)
            if spider_roll < 14:
                print ("The party rolls less than a 14 barely able to defeat the Giant Spider")
            else:
                print ("The party continues on their journey")
        elif roll == 4:
            print ("The party stumbles across a Stone Golem")
            print("Rolling the dice again")
            time.sleep(3)
            golem_roll = random.randint(1,25)
            if golem_roll > 18:
                print (" The party rolls with an attack roll, the party rolls greater than an 18")
                print (" The party takes down the Stone Golem with their fearless attacks")
            else:
                print ("The party continues on their journey")
        elif roll == 5:
            print (" The party grows weary luckly they find a Tavern to rest in")
        elif roll == 6:
            print (" The party recovers hit points, and replenish their resources")
        elif roll == 7:
            print (" The party continues on their long and dangerous journey")
        elif roll == 8:
            print ("The party encounters a Cloud Giant")
            print("Rolling the dice again")
            time.sleep(3)
            cloud_roll = random.randint(1,25)
            if cloud_roll > 18:
                print ("The party rolls with a attack roll")
                print ("The party takes down the Cloud Giant with their fearless attacks")
            else:
                print("The party fails to roll a high roll")
                print ("The party is in serious danger and NPC 3 gets struck down")
        elif roll == 9:
            print ("The party is weary and need rest")
        elif roll == 10:
            print ("The party encounter goblins")
            print("Rolling the dice again")
            time.sleep(3)
            goblin_roll = random.randint(1,25)
            if goblin_roll > 10:
                print ("The party uses an attack roll")
            else:
                print ("The party fails to roll a high enough roll")
                print ("The Goblin strikes down NPC 3")
                print ("NPC 3 has fallen and is now unconscious")
        elif roll == 11:
            print ("The party grows to be uneasy")
        elif roll == 12:
            print ("The party defeats the Goblin and shortly after they found a Tavern")
            print ("The party rests in the Tavern and has recovered as well as well as stock on resources")
        elif roll == 13:
            print ("The party encounters an Ancient Dragon")
            print("Rolling the dice again")
            time.sleep(3)
            dragon_roll = random.randint(1,25)
            if dragon_roll > 10:
                print ("The party uses an attack roll")
                print ("The party shivers in fear but they are filled with determination")
                print ("The party rolls an attack roll as well with other die and manage to scrape by")
            else:
                print ("NPC 3 has fallen and is now unconscious")
        elif roll == 14:
            print(" NPC 3 has made a full recovery and joins back in the battle")
        elif roll == 15:
            print("The party encounters a Gold Ancient Dragon")
            print ("Your party are stuck with fear wondering if they will become moribund")
        elif roll == 16:
            print ("The party shakes their heads and with a small glint in their eyes")
            print ("They are ready for this monster that they are going to take on")
        else:
            print (" NPC 3 has made a full recovery and joins back in the battle")
        choice = input("Do you want to roll again? type yes or no: ")
        if choice == "yes":
            play = 0
        else:
            play = 1



