
def mean_npc_dialogue(player_name="GORLOCK THE DESTROYER"):
    dialogue_state = "START"
    while dialogue_state != "QUIT":
        if dialogue_state == "START":
            print(f"NPC: Watcha looking at? Make it quick. My time is worth more than whatever coins are jangling in your sad little pouch.")
            print("1. I'm just wonderig around and trying to get dircetions to go on my epic adventure....")
            print("2. No need to be a jerk, I was just looking for help to get dircetions ")
            print("3. Walk by and ignore.")
            choice = input("> ").strip()
            if choice == "1":
                dialogue_state = "Don't look at me for dircetions, go look for someone who cares"
            elif choice == "2":
                dialogue_state = "Get lost, and toughen up your to sensitve if you can't hanndle a bit of additude"
            elif choice == "3":
                dialogue_state = "You give me a look and now your walking away? Wowww you think your all that? think your Mr tought guy?"
            else:
                print("NPC: Whatever your not even worth my time")

        elif dialogue_state == "Don't look at me for dircetions, go look for someone who cares":
            print(f"\nNPC: 'Epic adventure'? Please. You look like you're lost on your way to the market.")
            print("NPC: Treasure hunting is a fool's errand. You'll probably end up eaten by a slime.")
            print("1. You don't need to be so rude! All I'm asking is to show me dircetions so I can go on my adventure")
            print("2. YOU KNOW WHAT FORGET IT! I BET YOUR TO DUMB TO EVEN KNOW THE DIRCTIONS TO THE BATHROOM")
            print("3. End conversation (Quit).")
            choice = input("> ").strip()

            if choice == "1":
                dialogue_state = "GET_LAUGHTED_AT"
            elif choice == "2":
                dialogue_state = "YOU_GET_ROBBED"
            elif choice == "3":
                dialogue_state = "QUIT"
            else:
                print("NPC: Make a proper choice, you amateur.")

        elif dialogue_state == "GET_LAUGHTED_AT":
            print("\nNPC: Did you come here looking for kindness? You chose the wrong person and the wrong town.")
            dialogue_state = "Don't look at me for dircetions, go look for someone who cares"


        elif dialogue_state == "YOU_GET_ROBBED":
            print("\nNPC: *You have gotten beaten up and have lost $200 coins*")
            dialogue_state = "QUIT"



