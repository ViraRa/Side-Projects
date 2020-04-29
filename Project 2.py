class Comp_Strand:

    def __init__(self):
        self.DNA_Seq = ["GGATCC"]
    
    def complimentary_DNA(self):

        new_seq = []

        if isinstance(self.DNA_Seq, list):

            self.DNA_Seq_str = str(self.DNA_Seq)
            self.DNA_Seq_list = list(self.DNA_Seq_str)

        else:
            pass

        for x in self.DNA_Seq_list:

            if(x == "G"):
                
                new_seq.append("C")

            elif(x == "A"):

                new_seq.append("T")

            elif(x == "C"):

                new_seq.append("G")

            elif(x == "T"):

                new_seq.append("A")

        return new_seq

    

obj = Comp_Strand()
comp_seq = obj.complimentary_DNA()

#check Palidrome?
comp_seq.reverse()
check_seq = "".join(comp_seq)

if(obj.DNA_Seq[0] == check_seq):
    print(obj.DNA_Seq[0] + " IS a Palidrome! ")
else:
    print(obj.DNA_Seq[0] + " NOT a Palidrome! ")
