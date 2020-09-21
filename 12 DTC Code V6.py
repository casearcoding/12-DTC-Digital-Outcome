import random

# User Weapon Variables
B = "Brushing"
F = "Floss"
D = "Dental Wash"
L = "Low-Sugar Diet"
M = "Medicine (Probiotics)"
User_Weapons = ['B', 'F', 'D', 'L', 'M']
chosenUW = ""

# User Attack Variables
P = "Plaque"
G = "Gum Disease"
T = "Tooth Sensitivity"
S = "Stained Teeth"
U = "Unpleasant Breath"
Computer_Attacks = [P, G, T, S, U]
chosen_CA = ""

# Point Combination Dictionaries and Lists
Three_Point_Combinations = {T:L, U:M, S:D, P:B, G:F}
One_Point_Combinations_O = [T, L, U, M, S, D]
One_Point_Combinations_T = [B, S, D, P, G, F]

# Computer and User Health
user_health = 12
computer_health = 12

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
        chosen_UW = input("Please enter a valid option ").capitalize()
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
            
    if Three_Point_Combinations[chosen_CA] == chosen_UW:
        computer_health -= 3
        print("""**                                                                                                                                                **
**                                                                                                                                                **
** You chose...                                                                                                                                   **
** {} against {}
**                                                     Good choice, this is extremely effective!                                                  **
**                                                                  You score...                                                                  **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                     33333                                                                      **
**                                                                   333333333                                                                    **
**                                                                  333     333                                                                   **
**                                                                          333                                                                   **
**                                                                         333                                                                    **
**                                                                     333333                                                                     **
**                                                                     333333                                                                     **
**                                                                         333                                                                    **
**                                                                          333                                                                   **
**                                                                  333     333                                                                   **
**                                                                   333333333                                                                    **
**                                                                     33333                                                                      **
**                                                                                                                                                **
**                                                      points against the Dental Monster!                                                        **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **
**                                                                                                                                                **""".format(chosen_UW, chosen_CA))


    

