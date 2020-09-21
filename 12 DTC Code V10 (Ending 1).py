import random

# User Weapon Variables
B = "Brushing"
F = "Floss"
D = "Dental Wash"
L = "Low-Sugar Diet"
M = "Medicine (Probiotics)"
User_Weapons = ['B', 'F', 'D', 'L', 'M']
chosen_UW = ""
user_damage = 0

# User Attack Variables
P = "Plaque"
G = "Gum Disease"
T = "Tooth Sensitivity"
S = "Stained Teeth"
U = "Unpleasant Breath"
Computer_Attacks = [P, G, T, S, U]
chosen_CA = ""
computer_damage = 0

# Point Combination Dictionaries and Lists
Three_Point_Combinations = {T:L, U:M, S:D, P:B, G:F}
One_Point_Combinations_O = [T, L, U, M, S, D]
One_Point_Combinations_T = [B, S, D, P, G, F]

# Computer and User Health
user_health = 12
computer_health = 12

# For readability
next = ""

# Menu
print("""****************************************************************************************************************************************************
**                                                                                                                                                **
**                                         Welcome to this Epic Battle against the Deadly Dental Monster!                                         **
**     *           *           *           *           *           *           *           *           *           *           *           *      **
**           *           *           *           *           *           *           *           *           *           *           *            **                                        
**                     Face an assault of cracked teeth, plaque and gum disease, all with one goal: The ruin of your teeth…                       **              
** Use your basic dental hygiene knowledge to choose a weapon to defend yourself, but choose wisely; some will cause far more damage than others. **
**  Each round, you will have to defeat a new attack, in which both you and the dental monster can score up to three points against each other.   **
**                                     You have fifteen layers of enamel to protect you, don’t lose them all…                                     **
**                                         Good luck, and don’t let the dental monster wreck your teeth!                                          **
**                                                                                                                                                **
****************************************************************************************************************************************************""")

# Random Component Function
def damage_point_chance(user_damage):
    print("""**                                                                                                                                                **
**                                                  A New, UNTESTED Dental Product has come out.                                                  **
**                                                If it works, you can DOUBLE your damage points!                                                 **
**                                                                      BUT                                                                       **
**                                                    If it doesn't, you LOSE ALL your points!                                                    **
**                                                             Do you want to try it?                                                             **
**                                               Type 'Y' to take a chance, or any other key to quit                                              **
**                                                                                                                                                **""")
    next = input("** Type here: ").capitalize()
    if next == "Y":
        chance = random.randint(0,1)
        if chance == 1:
            user_damage = user_damage*2
            print("""**                                                                                                                                                **
**                                                        CONGRATS! Your points are DOUBLED!                                                      **
**                                                                                                                                                **""")
        else:
            user_damage = 0
            print("""**                                                                                                                                                **
**                                                        OH NO! You LOST ALL your points :(                                                      **
**                                                                                                                                                **""")
    else:
        quit

    return user_damage

    

# Attack Menu
while user_health and computer_health > 0:
    chosen_CA = Computer_Attacks[random.randint(0,4)]
    print("""                                                                                                                                                
** The Dental Monster is attacking you with...                                                                                                    **
                                                                    
                                                                ** {}! **
""".format(chosen_CA))
    chosen_UW = input( """** Choose a weapon to defend yourself! Type:                                                                                                      **
**       'B' for Brushing                                                                                                                         **
**       'F' for Floss                                                                                                                            **
**       'D' for Dental Wash                                                                                                                      **
**       'L' for Low-Surgar Diet                                                                                                                  **
**       'M' for Medicine (Probiotics)                                                                                                            **
**        """).capitalize()
    while chosen_UW.isalpha() == False or chosen_UW not in User_Weapons:
        chosen_UW = input("** Please enter a valid option                                                                                                                    **").capitalize()
    if chosen_UW == 'B':
        chosen_UW = 'Brushing'
    elif chosen_UW == 'F':
        chosen_UW = 'Floss'
    elif chosen_UW == 'D':
        chosen_UW = 'Dental Wash'
    elif chosen_UW == 'L':
        chosen_UW = 'Low-Sugar Diet'
    else:
        chosen_UW = "Medicine (Probiotics)"

# Three Point Attack Combination            
    if Three_Point_Combinations[chosen_CA] == chosen_UW:
        user_damage = 3
        computer_damage = 0
        print("""**                                                                                                                                                **
**                                                                                                                                                **
** You chose...                                                                                                                                   **
** {} against {}
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **
**                                           Good choice, this is extremely effective!                                                            **
**                                                        You score...                                                                            **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                           33333                                                                                **
**                                                         333333333                                                                              **
**                                                        333     333                                                                             **
**                                                                333                                                                             **
**                                                               333                                                                              **
**                                                           333333                                                                               **
**                                                           333333                                                                               **
**                                                               333                                                                              **
**                                                                333                                                                             **
**                                                        333     333                                                                             **
**                                                         333333333                                                                              **
**                                                           33333                                                                                **
**                                                                                                                                                **
**                                              points against the Dental Monster!                                                                **
**                                                                                                                                                **
**                                                                                                                                                **""".format(chosen_UW, chosen_CA))

        print("""**                                                                                                                                                **
**                                                                                                  The Dental Monster Scores...                  **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                             00000                              **
**                                                                                                           000000000                            **
**                                                                                                          000     000                           **
**                                                                                                          000     000                           **
**                                                                                                          000     000                           **
**                                                                                                          000     000                           **
**                                                                                                          000     000                           **
**                                                                                                          000     000                           **
**                                                                                                          000     000                           **
**                                                                                                           000000000                            **
**                                                                                                             00000                              **
**                                                                                                                                                **
**                                                                                                      points against You!                       **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **""")

# One Point Attack Combination
    elif chosen_CA in One_Point_Combinations_O and chosen_UW in One_Point_Combinations_O or chosen_CA in One_Point_Combinations_T and chosen_UW in One_Point_Combinations_T:
        user_damage = 1
        computer_damage = 2
        print("""**                                                                                                                                                **
**                                                                                                                                                **
** You chose...                                                                                                                                   **
** {} against {}
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                This is somewhat effective!                                                                     **
**                                                        You score...                                                                            **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                              1                                                                                 **
**                                                            111                                                                                 **
**                                                          11111                                                                                 **
**                                                        111 111                                                                                 **
**                                                            111                                                                                 **
**                                                            111                                                                                 **
**                                                            111                                                                                 **
**                                                            111                                                                                 **
**                                                            111                                                                                 **
**                                                            111                                                                                 **
**                                                            111                                                                                 **
**                                                        11111111111                                                                             **
**                                                                                                                                                **
**                                             point against the Dental Monster!                                                                  **
**                                                                                                                                                **
**                                                                                                                                                **""".format(chosen_UW, chosen_CA))

        print("""**                                                                                                                                                **
**                                                                                                The Dental Monster Scores...                    **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                           22222                                **
**                                                                                                         222222222                              **
**                                                                                                        222     222                             **
**                                                                                                               222                              **
**                                                                                                              222                               **
**                                                                                                             222                                **
**                                                                                                            222                                 **
**                                                                                                           222                                  **
**                                                                                                          222     2                             **
**                                                                                                         222     22                             **
**                                                                                                        22222222222                             **
**                                                                                                                                                **
**                                                                                                    points against You!                         **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **""")
# Zero Point Attack Combination
    else:
        user_damage = 0
        computer_damage = 3
        print("""**                                                                                                                                                **
**                                                                                                                                                **
** You chose...                                                                                                                                   **
** {} against {}
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **
**                                          Bad choice, this is not very effective!                                                               **
**                                                        You score...                                                                            **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                           00000                                                                                **
**                                                         000000000                                                                              **
**                                                        000     000                                                                             **
**                                                        000     000                                                                             **
**                                                        000     000                                                                             **
**                                                        000     000                                                                             **
**                                                        000     000                                                                             **
**                                                        000     000                                                                             **
**                                                        000     000                                                                             **
**                                                        000     000                                                                             **
**                                                         000000000                                                                              **
**                                                           00000                                                                                **
**                                                                                                                                                **
**                                            points against the Dental Monster!                                                                  **
**                                                                                                                                                **""".format(chosen_UW, chosen_CA))

        print("""**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                The Dental Monster Scores...                    **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                           33333                                **
**                                                                                                         333333333                              **
**                                                                                                        333     333                             **
**                                                                                                                333                             **
**                                                                                                               333                              **
**                                                                                                           333333                               **
**                                                                                                           333333                               **
**                                                                                                               333                              **
**                                                                                                                333                             **
**                                                                                                        333     333                             **
**                                                                                                         333333333                              **
**                                                                                                           33333                                **
**                                                                                                                                                **
**                                                                                                    points against You!                         **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **""")

# Health calculator
    next = input("** Press ENTER to continue                                                                                                                        **")
    if user_damage > 0:
        user_damage = damage_point_chance(user_damage)
    user_health -= computer_damage
    computer_health -= user_damage
    print("""**                                                                                                                                                **
**                                              ********** YOU have {} Layers of Enamel Left **********
**                                             ********** The Dental MONSTER has {} Lives Left **********
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **
**     *           *           *           *           *           *           *           *           *           *           *           *      **
**           *           *           *           *           *           *           *           *           *           *           *            **
**                                                                                                                                                **""".format(user_health, computer_health))
    next = input("** The Deadly Dental monster is ready to attack! Press ENTER to Start the Next Round!                                                             **")

# End of Game
if user_health > 0:
    print("""**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **
**                YYY         YYY            OOO            UUU         UUU                                                                       **
**                 YYY       YYY          OOOOOOOOO         UUU         UUU                                                                       **
**                  YYY     YYY         OOO       OOO       UUU         UUU                                                                       **
**                   YYY   YYY         OOO         OOO      UUU         UUU                                                                       **
**                    YYY YYY          OOO         OOO      UUU         UUU                                                                       **
**                     YYYYY           OOO         OOO      UUU         UUU                                                                       **
**                      YYY            OOO         OOO      UUU         UUU                                                                       **
**                      YYY            OOO         OOO      UUU         UUU                                                                       **
**                      YYY            OOO         OOO      UUU         UUU                                                                       **
**                      YYY            OOO         OOO      UUU         UUU                                                                       **
**                      YYY            OOO         OOO      UUU         UUU                                                                       **
**                      YYY             OOO       OOO        UUU       UUU                                                                        **
**                      YYY               OOOOOOOOO            UUUUUUUUU                                                                          **
**                      YYY                  OOO                  UUU                                                                             **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                          WWW                     WWW      IIIIIIIIIIIIIII            NNN                       **
**                                                          WWW                     WWW            III               NNNNNNNNN                    **
**                                                          WWW                     WWW            III             NNN       NNN                  **
**                                                          WWW         WWW         WWW            III            NNN         NNN                 **
**                                                          WWW         WWW         WWW            III            NNN         NNN                 **
**                                                          WWW         WWW         WWW            III            NNN         NNN                 **
**                                                          WWW         WWW         WWW            III            NNN         NNN                 **
**                                                          WWW         WWW         WWW            III            NNN         NNN                 **
**                                                          WWW         WWW         WWW            III            NNN         NNN                 **
**                                                          WWW         WWW         WWW            III            NNN         NNN                 **
**                                                          WWW         WWW         WWW            III            NNN         NNN                 **
**                                                           WWW       WWWWW       WWW             III            NNN         NNN                 **
**                                                             WWWWWWWWW   WWWWWWWWW               III            NNN         NNN                 **
**                                                                WWW         WWW            IIIIIIIIIIIIIII      NNN         NNN                 **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **
****************************************************************************************************************************************************""")
