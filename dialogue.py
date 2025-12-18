import random

def gorlock_dialogue():
    print("Gorlock the Destroyer: The mysterious stranger stands before you, a weathered map clutched in their hand. 'The path ahead is uncertain, traveler. How do you respond?'\n")

    print("1. 'I've faced worse. Point me in the right direction.'")
    print("2. 'Uncertainty is just another word for adventure. Lead on!'")
    print("3. 'I'm not so sure... perhaps I should turn back.'")
    print("4. 'Tell me more about the dangers before I decide.'\n")

    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        print(f"\nYou selected option {choice}. The story continues from here...\n")
    elif choice == 2:
        print(f"\nYou selected option {choice}. The story continues from here...\n")
    elif choice == 3:
        print(f"\nYou selected option {choice}. The story ends here...\n")
    elif choice == 4:
        print(f"\nYou selected option {choice}. You ask more questions...\n")