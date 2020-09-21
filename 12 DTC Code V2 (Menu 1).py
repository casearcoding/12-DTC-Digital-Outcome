import random

# User Weapon Variables
B = "Brushing"
F = "Floss"
D = "Dental Wash"
L = "Low-Sugar Diet"
M = "Medicine (Probiotics)"
User_Weapons = [B, F, D, L, M]
chosen_UW = ""

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
print("""                                        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                        !!                                                                !!
                                        !! Welcome to this Epic Battle against the Deadly Dental Monster! !!
                                        !!                                                                !!
                                        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                        
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!                     Face an assault of cracked teeth, plaque and gum disease, all with one goal: The ruin of your teeth…                       !!               
!! Use your basic dental hygiene knowledge to choose a weapon to defend yourself, but choose wisely; some will cause far more damage than others. !!
!!  Each round, you will have to defeat a new attack, in which both you and the dental monster can score up to three points against each other.   !!
!!                                     You have fifteen layers of enamel to protect you, don’t lose them all…                                     !!
!!                                         Good luck, and don’t let the dental monster wreck your teeth!                                          !!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!""")

chosen_CA = Computer_Attacks[random.randint(0,4)]
print("""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   The Dental Monster is attacking you with...                                                                                                      
                                                                   {}!
                                                                                                                                                    
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!""".format(chosen_CA))
print( """
   Choose a weapon to defend yourself! Type:
         'B' for Brushing
         'F' for Floss
         'D' for Dental Wash
         'L' for Low-Surgar Diet
         'M' for Medicine (Probiotics)
         
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!""")

