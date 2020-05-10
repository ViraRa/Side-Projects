import numpy as np
from fractions import Fraction
import sys

class protein_charge_calc:

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

    @staticmethod
    def protein_charge(seq, pH):

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

        aa_pka = []

        for x in range(0, len(seq)): # O(N)

            if(seq[x] == "Lys" or seq[x] == "K"):
                aa_pka.append((seq[x], 10.8, 1)) # Lys has as a NH3+ group 
            elif(seq[x] == "Arg" or seq[x] == "R"):
                aa_pka.append((seq[x] ,12.5, 1)) # Arg has as a NH3+ group 
            elif(seq[x] == "His" or seq[x] == "H"):
                aa_pka.append((seq[x], 6, 1)) # His has as a NH+ group 
            elif(seq[x] == "Asp" or seq[x] == "D"):
                aa_pka.append((seq[x], 3.65, 0)) # Asp has as a OH group 
            elif(seq[x] == "Glu" or seq[x] == "E"): 
                aa_pka.append((seq[x], 4.25, 0)) # Glu has as a OH group 
            elif(seq[x] == "Cys" or seq[x] == "C"):
                aa_pka.append((seq[x], 8.3, 0)) # Cys has a SH group
            elif(seq[x] == "Tyr" or seq[x] == "Y"):
                aa_pka.append((seq[x], 10.9, 0)) # Tyr has a OH group
            else:
                aa_pka.append((seq[x], 0)) # these aa are not ionizable 

        aa_pka.append(("NH3", 8.0, 1)) # for N - terminus
        aa_pka.append(("COOH", 3.1, 0)) # for C - terminus
    
        for x in range(0, len(aa_pka)): #O(N)
            if(aa_pka[x][1] != 0):
                if(pH > aa_pka[x][1]):
                    charge_arr = np.append(charge_arr, aa_pka[x][2] - 1) # very simple
                elif(pH < aa_pka[x][1]): # easier than the first case
                    charge_arr = np.append(charge_arr, aa_pka[x][2])
                elif(pH == aa_pka[x][1]): # a little difficult since have to use buffer equation
                    ratio_base_to_acid = 10 ** (pH - aa_pka[x][1])
                    ratio_base_to_acid_simp = Fraction(ratio_base_to_acid).limit_denominator()
            
                    if(ratio_base_to_acid_simp > 1):
                        charge_arr = np.append(charge_arr, -1)
                    elif(ratio_base_to_acid_simp < 1):
                        charge_arr = np.append(charge_arr, 0)
                    elif(ratio_base_to_acid_simp == 1):
                        charge_arr = np.append(charge_arr, -0.5)
        return charge_arr

obj = protein_charge_calc(2.34) # change pH value here
