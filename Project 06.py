import numpy as np
from fractions import Fraction
import sys

class protein_charge_calc:

    aa_pka = [] # made as a class variable, so I can extend this further for different projects

    def __init__(self, pH):

        protein = ""
        protein_list = [] # for three letter code format
        protein_length = 0 # without any new line char

        with open("Protein.txt", "r") as file:
            protein = file.read()

        one_or_three = input("\nAre your amino acids in one - letter code format [y/n] ")

        if(one_or_three != "y" and one_or_three != "n"):
            print("\nYou typed " + one_or_three + " instead y or n. Please try again...\n")
            sys.exit(0)

        protein = protein.split("\n")[0]
        protein_length = len(protein)

        if(one_or_three == "y"):
            answer = self.protein_charge(protein, pH)
            print("The average net charge is: " + str(sum(answer)))
            # sum is O(N)
        else: # three letter code format
            for x in range(0, len(protein_length[0]), 3):
                protein_list.append(protein[x : x + 3])
            answer = self.protein_charge(protein_list, pH)
            print("The average net charge is: " + str(sum(answer)))

        # Overall complexity is O(N)

    def protein_charge(self, seq, pH):

        # Feel free to change the pka to anything that makes sense based on your reference

        # Based on a Biochemistry textbook these are the pka for the aa and N/C term.

        # Lys-> 10.8
        # Arg -> 12.5
        # His -> 6.0
        # Asp -> 3.65
        # Glu -> 4.25
        # Cys -> 8.3
        # Tyr -> 10.9
        # N-term -> 8.0
        # C-term -> 3.1

        charge_arr = np.array([])
         
         # three cases 
         # 1. pH > pka -> -1
         # 2. pH < pka -> +1
         # 3. pH == pka -> Henderson Hasselbalch  equation (also called buffer equation) 

        for x in seq: # O(N)

            if(x == "Lys" or x == "K"):
                self.aa_pka.append((x, 10.8, 1)) # Lys has as a NH3+ group 
            elif(x == "Arg" or x == "R"):
                self.aa_pka.append((x ,12.5, 1)) # Arg has as a NH3+ group 
            elif(x == "His" or x == "H"):
                self.aa_pka.append((x, 6, 1)) # His has as a NH+ group 
            elif(x == "Asp" or x == "D"):
                self.aa_pka.append((x, 3.65, 0)) # Asp has as a OH group 
            elif(x == "Glu" or x == "E"): 
                self.aa_pka.append((x, 4.25, 0)) # Glu has as a OH group 
            elif(x == "Cys" or x == "C"):
                self.aa_pka.append((x, 8.3, 0)) # Cys has a SH group
            elif(x == "Tyr" or x == "Y"):
                self.aa_pka.append((x, 10.9, 0)) # Tyr has a OH group

        self.aa_pka.append(("NH3", 8.0, 1)) # for N - terminus
        self.aa_pka.append(("COOH", 3.1, 0)) # for C - terminus
    
        for x in self.aa_pka: #O(N)
            if(x[1] != 0):
                if(pH > x[1]):
                    charge_arr = np.append(charge_arr, x[2] - 1) # very simple
                elif(pH < x[1]): # easier than the first case
                    charge_arr = np.append(charge_arr, x[2])
                elif(pH == x[1]): # a little difficult since have to use buffer equation
                    ratio_base_to_acid = 10 ** (pH - x[1])
                    ratio_base_to_acid_simp = Fraction(ratio_base_to_acid).limit_denominator()
            
                    if(ratio_base_to_acid_simp > 1):
                        charge_arr = np.append(charge_arr, -1)
                    elif(ratio_base_to_acid_simp < 1):
                        charge_arr = np.append(charge_arr, 0)
                    elif(ratio_base_to_acid_simp == 1):
                        charge_arr = np.append(charge_arr, -0.5)
        return charge_arr
    

obj = protein_charge_calc(2.34) # change pH value here
