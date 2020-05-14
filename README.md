# Side-Projects (On-going)
### The point of these short projects is to implement any ideas I come up with spontaneously. They are written in Python 3. 

**Project 1** - Randomly generate a number from 0 to and including 20, and the user needs to guess a number from this range. I guide the user to enter a number (not a string) from this range. I tell him/her if the number is too high or too low. 

**Project 2** - Check if a short DNA sequence is a palidrome by finding the sequence's complimentary strand. I provide the short DNA sequence in the constructor.

**Project 3** - Simple dynamic programming using the bottom-up approach on fibonacci sequence. I provide the input when I am creating an object.  

**Project 4** - A binary search program. The complexity is log<sub>2</sub>(N). 

**Project 5** - A daily compound interest calculator that outputs the total return after n years. It also outputs daily and monthly interest that accrued during n years. All of this is determined by a series of questions that the user answers. The algorithm takes account of leap years and non-leap years. Time complexity is approx. O(N).

**Project 6** - Finds an average net charge of a single peptide based on a pH provided by the user.The pka for AA and N/C terminal comes from a Biochemistry textbook. You can change the pka based on your needs. This short project works with any peptide size. The algorithm is O(N) complexity.

**Project 7** - Use dynamic programming to solve the Fibonacci sequence. This is an O(N) algorithm as opposed to an exponential one if the naive approach is implemented. I also performed unit testing to test the code. 

**Project 8** - This project modifies Project 6 by adding the pI function to find the pI of an peptide. pI or isoelectric point is defined as the pH when the peptide has an average net charge of zero (meaning it is electrically neutral). pI algorithm is O(Nlog<sub>2</sub>(N)) because of python's in-built sorting algorithm (time sort), which does no better than merge sort.

**Project 9** - This project extends Project 8 by adding MW calculation. The code is reading from an excel workbook that contains the individual aa's molecular weight found on Thermo Fisher website. I then created a simple GUI to display the results. The overall program went up in time complexity to O(n<sup>2</sup>). 
