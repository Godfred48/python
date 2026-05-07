# AN ADVENTURE GAME
print("THE LAST KINGDOM OF ELDORIA")
print()
print("The kingdom is under attack. You are the last knight \n What do you do: ")
user_entry = input("*FIGHT      *SNEAK     *FLEE : ").strip()
print("=" * 50)
 
if user_entry.upper() == "FIGHT":
    print("You charge into battle")
    fight = input("The enemy looms near. Face the DRAGON or the ARMY: ").strip()
    print("=" * 50)
    if fight.upper() == "DRAGON":
        fight_option = input("Dragon stands before you. \n Use SWORD or RUN: ").strip()
        print("=" * 50)
        if fight_option.upper() == "SWORD":
            print("You slay it. Victory!!!!")
        elif fight_option.upper() == "RUN":
            print("Failed. You flee.")
        else:
            print("Invalid input. Your town is destroyed.")
    elif fight.upper() == "ARMY":
        fight_option1 = input("10,000 troops ahead. \n RALLY troops or TRICK them: ").strip()
        print("=" * 50)
        if fight_option1.upper() == "RALLY":
            print("Good! Army joins your side.")
        elif fight_option1.upper() == "TRICK":
            print("Great Job! Your trick works.")
        else:
            print("Invalid input. Your town is destroyed.")
    else:
        print("Invalid input. Your town is destroyed.")
 
elif user_entry.upper() == "SNEAK":
    sneak_entry = input("You are in enemy territory.\n Enter CASTLE or steal MAP: ").strip()
    print("=" * 50)
    if sneak_entry.upper() == "CASTLE":
        print("Inside the castle walls.")
        castle_option = input("Use DISGUISE or ROOFTOPS? ").strip()
        print("=" * 50)
        if castle_option.upper() == "DISGUISE":
            print("Exposed! You were captured.")
        elif castle_option.upper() == "ROOFTOPs":
            print("You shut the gates. You saved the kingdom!")
        else:
            print("Invalid input. Your town is destroyed.")
    elif sneak_entry.upper() == "MAP":
        map_option = input("Map is within reach. \n PICKPOCKET or BRIBE the guard: ").strip()
        print("=" * 50)
        if map_option.upper() == "PICKPOCKET":
            print("Map stolen. Plan revealed!")
        elif map_option.upper() == "BRIBE":
            print("Guard takes bribe. You were betrayed.")
        else:
            print("Invalid input. You were killed.")
    else:
        print("Invalid input. Your town is destroyed.")
 
elif user_entry.upper() == "FLEE":
    flee_option = input("Deep in the forest now. \n Seek for WIZARD, VILLAGE or hide ALONE in CAVE: ").strip()
    print("=" * 50)
    if flee_option.upper() == "WIZARD":
        wizard_entry = input("Old wizard appears to you.\n Ask for WISDOM or POWER: ").strip()
        print("=" * 50)
        if wizard_entry.upper() == "POWER":
            print("Power corrupts you... You lost the battle.")
        elif wizard_entry.upper() == "WISDOM":
            print("Wisdom wins the war!!!!")
        else:
            print("Invalid input. The wizard kills you!")
    elif flee_option.upper() == "VILLAGE":
        village_entry = input("Villagers look to you. \n Lead a CHARGE or FORTIFY walls: ").strip()
        print("=" * 50)
        if village_entry.upper() == "CHARGE":
            print("You lead the charge. Victory!!!")
        elif village_entry.upper() == "FORTIFY":
            print("Walls are fortified. Enemy starves and flees. You win!!!")
        else:
            print("Invalid input. Villagers turn against you.")
    elif flee_option.upper() == "ALONE":
        alone_entry = input("You are alone in the darkness. \n HIDE in ruins or find WEAPON?: ").strip()
        print("=" * 50)
        if alone_entry.upper() == "HIDE":
            print("Found and captured by enemy. You lose.")
        elif alone_entry.upper() == "WEAPON":
            print("You find a hidden weapon. You defeat the enemy and save the kingdom!!!")
        else:
            print("Invalid input. You are lost in the darkness.")
    else:
        print("Invalid input. You are lost in the forest.")
 
else:
    print("Invalid input. Your town is destroyed. You were killed!")
 
print("=" * 50)
print("        GAME OVER — THE LEGEND OF ELDORIA ENDS")
print("=" * 50)
 
