import numpy as np
from fractions import Fraction
import sys
from xlrd import open_workbook # for reading excel worksheet
from collections import deque
import tkinter as gui #tkinter is all about widgets 
import webbrowser

class protein_charge_calc:

    def __init__(self, pH, polar_list, pka_dict):

        protein = ""
        protein_list = [] # for three letter code format
        protein_length = 0 # without any new line char
        aa_pka = [] 

        if not isinstance(polar_list, list) or not isinstance(pka_dict, dict):
            print("\nPlease provide a list of polar amino acids and a dictionary of pka values. Try again...")
            sys.exit(0)

        self.GUI(protein, protein_list, protein_length, aa_pka, pH, polar_list, pka_dict)
        # Overall complexity is O(N^2)


    # simple GUI
    def GUI(self, protein, protein_list, protein_length, aa_pka, pH, polar_list, pka_dict):

        with open("Protein.txt", "r") as file:
            protein = file.read()

        # make sure to answer the question below correctly if you want the correct output

        one_or_three = input("\nAre your amino acids in one - letter code format [y/n] ")

        if(one_or_three != "y" and one_or_three != "n"):
            print("\nYou typed " + one_or_three + " instead y or n. Please try again...\n")
            sys.exit(0)

        protein = protein.strip("\n").replace("\n", "")
        protein_length = len(protein)

        if protein.isupper() and one_or_three == "n":
            print("\nYour amino acids are in one - letter code format. Please try again...")
            sys.exit(0)
        
        if not protein.isupper() and not protein.islower() and one_or_three == "y":
            print("\nYour amino acids are in three - letter code format. Please try again...")
            sys.exit(0)

        if(one_or_three == "y"): # one - letter format
            charge = self.protein_charge(protein, pH, aa_pka, pka_dict)
            M_W = self.protein_MW(protein)
            pI = self.protein_pI(aa_pka)
            polar = self.polar(protein, polar_list)
        else: # three letter code format
            for x in range(0, protein_length, 3): protein_list.append(protein[x : x + 3])
            charge = self.protein_charge(protein_list, pH, aa_pka, pka_dict)
            M_W = self.protein_MW(protein_list)
            pI = self.protein_pI(aa_pka)
            polar = self.polar(protein_list, polar_list)

        # used this MW table found on Thermo Fisher website
        def openMW():
            webbrowser.open_new_tab("https://www.thermofisher.com/us/en/home/references/ambion-tech-support/rna-tools-and-calculators/proteins-and-amino-acids.html")
        
        # cool bioinformatics tool
        def openBio():
            webbrowser.open_new_tab("https://www.bioinformatics.org/sms2/sample_protein.html")
    

        root = gui.Tk()
        root.title("Protein Stats")
        
        charge_label = gui.Label(root, text="The Average Net Charge is: " + str(sum(charge)),font=12)
        pI_label = gui.Label(root, text="The Isoelectric Point is (pI) is: " + str(pI), font=12)
        M_W_label = gui.Label(root, text="The Molecular Weight is: " + str(round(M_W/1000, 3)) + " kDa", font=12)
        polar_label = gui.Label(root, text="Polar Percentage: " + str(polar) + " % ", font=12)
        blank = gui.Label(root, text="   ")
        MW_b = gui.Button(root, text ="MW reference table", command=openMW, font=12, borderwidth=3)
        ex = gui.Button(root, text="Exit", font=12, command=root.quit, borderwidth=3, padx=15, pady=1)
        Bio = gui.Button(root, text="SMS bioinformatics tool", command=openBio, font=12)

        charge_label.grid(row=1,column=0)
        pI_label.grid(row=2,column=0)
        M_W_label.grid(row=3,column=0)
        blank.grid(row=3, column=2)
        polar_label.grid(row=4, column=0)
        MW_b.grid(row=3, column=3, columnspan=1)
        Bio.grid(row=5, column=3)
        ex.grid(row=5, column=0)

        root.mainloop()

    @staticmethod
    def protein_charge(seq, pH, aa_pka, pka_dict):

        charge_arr = np.array([])
         
         # three cases 
         # 1. pH > pka -> -1
         # 2. pH < pka -> +1
         # 3. pH == pka -> Henderson Hasselbalch  equation (also called buffer equation) 

        for x in seq: # O(N)

            if(x == "Lys" or x == "K"):
                aa_pka.append((x, pka_dict.get(("Lys", "K")), 1)) # Lys has as a NH3+ group 
            elif(x == "Arg" or x == "R"):
               aa_pka.append((x, pka_dict.get(("Arg", "R")), 1)) # Arg has as a NH3+ group 
            elif(x == "His" or x == "H"):
                aa_pka.append((x, pka_dict.get(("His", "H")), 1)) # His has as a NH+ group 
            elif(x == "Asp" or x == "D"):
                aa_pka.append((x, pka_dict.get(("Asp", "D")), 0)) # Asp has as a OH group 
            elif(x == "Glu" or x == "E"): 
                aa_pka.append((x, pka_dict.get(("Glu", "E")), 0)) # Glu has as a OH group 
            elif(x == "Cys" or x == "C"):
                aa_pka.append((x, pka_dict.get(("Cys", "C")), 0)) # Cys has a SH group
            elif(x == "Tyr" or x == "Y"):
                aa_pka.append((x, pka_dict.get(("Tyr", "Y")), 0)) # Tyr has a OH group

        aa_pka.append(("NH3", pka_dict.get("NH3"), 1)) # for N - terminus
        aa_pka.append(("COOH", pka_dict.get("COOH"), 0)) # for C - terminus
    
        for x in aa_pka: #O(N)
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

    @staticmethod
    def protein_pI(aa_pka):

        # calcuate at the most pronated state of sequence
        # take the smallest pka of sequence and subtract one from the most pronated state
        # keep doing this until the most pronated state has a charge of -1
        # average the last two pka to find pI
        pronated_state_charge = 0 
        minimum_list = sorted(aa_pka, key = lambda x: x[1]) 
        # sort based on pka values (smallest to highest) in aa_pka list
        pka_count = np.array([]) 

        for x in aa_pka: pronated_state_charge += x[2] 
        # finding the overall charge of when every aa is pronated
        # this is your pronated state
              
        for aa in minimum_list:
            pronated_state_charge -= 1 # subtract one every time until break
            pka_count = np.append(pka_count, aa[1]) # keep track of pka values
            if(pronated_state_charge == -1): # break when the overall charge is -1
                break 
        pI = (pka_count[-1] + pka_count[-2])/2 # float divison (avoid  using //)
        return pI

        # pI will change based on the reference of your pka's
    
    @staticmethod
    def protein_MW(protein):

        # MW based on aa's individual MW in excel file

        MW_deq = deque([]) # contains three letter code, one-letter code and MW
        Total_MW = 0
        i = 0

        # getting MW values from excel file
        with open_workbook("MW_protein.xlsx") as wb:
           sheet = wb.sheet_by_index(0) # get the first sheet
           cell = sheet

           for x in sheet.get_rows(): MW_deq.append(x)

        MW_deq.popleft() # delete the first element (not needed)

        if isinstance(protein, list): # three - letter code
            protein.sort()
            for i in MW_deq: Total_MW += (protein.count(i[0].value) * i[2].value)
        else: # protein is a string (i.e in one - letter code)
            protein = sorted(protein, key = lambda x: x)
            for i in MW_deq: Total_MW += (protein.count(i[1].value) * i[2].value)
        return Total_MW

    @staticmethod
    def polar(protein, polar_list):

        polar_count = 0

        for pro in protein:
            if pro in polar_list:
                polar_count += 1
            
        polar_percentage = (polar_count/len(protein)) * 100
        return polar_percentage


# driver
if __name__ == "__main__":

    polar_list = ["Q", "N", "H", "S", "T", "Y", "C"]
    pka_dict = {("Lys", "K"): 10.8, 
                ("Arg", "R"): 12.5, 
                ("His", "H"): 6.0, 
                ("Asp", "D"): 3.65, 
                ("Glu", "E"): 4.25, 
                ("Cys", "C"): 8.3, 
                ("Tyr", "Y"): 10.9,
                "NH3": 8.0,
                "COOH": 3.1}
    
    obj = protein_charge_calc(8.3, polar_list, pka_dict) 

# 1st input is pH value 
# 2nd input is a list of polar amino acids. Make sure the list is in the same format (one/three letter) as your protein sequence
# 3rd input is a dictionary of amino acids' pka values. Change the pka value only
