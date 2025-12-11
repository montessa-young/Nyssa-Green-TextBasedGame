
def npc_dialogue(player_name):
    dialogue_state = "START"
    while dialogue_state != "QUIT":
        if dialogue_state == "START":
            print(f"NPC: Well hello there stranger... What brings you here?")
            print("1. Helloo, my name is {player_name}. Im on an epic adventer to get treauser!")
            print("2. I'm just passing by... ")
            print("3. Walk by and ignore.")
            choice = input("> ").strip()
            if choice == "1":
                dialogue_state = "Well then.."
            elif choice == "2":
                dialogue_state = "Why's that?"
            elif choice == "3":
                dialogue_state = "How rude of you"
            else:
                print("NPC: Woww, really")