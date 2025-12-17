def intro():
    print("PREVIEW:")

    def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

    print_slow("Dungeons & Dragons is a fantasy world. Where players create heroes while telling a story using your imagination.")

    introduction = [" BASIC [CHARACTER CREATION] Let's enter the journey of building your very own fantasy hero! [RACE] You must choose a race consisting of elf, dwarf, or human [CLASS] You will also choose a role defining your abilities.. but beginners include barbarains and fighters. There are also other roles such as wizards, sorcers, and rogue. [BACKGROUND] Your character must have an orgin. Like any normal person where you grew up, what you've done basic things like that. This step is custom and you may use your imagination for it. [STATS] Or ability scores are strength, dexterity, constitution, intelliegence, and charisma. [DM] Join a dungeon master and party!"]

while True:

    reply = input("DO YOU WANT THE INTRODUCTION? (yes/no): ")
    if reply == 'yes':
        print_slow (introduction)
        break

    else:
        print_slow("SKIPPING INTRODUCTION...")