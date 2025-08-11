# This program determines the probability of getting n heads in a row when flipping a coin
# n times per data set for m trials, n and m is determined by the user
import random
import time

Trialflag=0
count=0
Hcount=0
Normalcount=0
Totalcount=0
Timeflag=0
Setsize=0

Trialnum=int(input("How many trials would you like to run? \n"))
Setsize=int(input("How many coin flips per trial? \n"))

while Timeflag != 1:
	t0=time.time() # Sets the initial time

	while Trialflag < Trialnum: # Runs the program for n (Trialnum) trials
		ht = []
		for i in range(0,Setsize): # Creates the list of numbers (runs n times for n trials)
			ht.insert(i, (str(random.choice(['H', 'T']))) )

		print(ht) # Prints out the set of data
		print(" ")
		print("\n")

		if ht[0] == 'H' and all(x == ht[0] for x in ht): # Checks if the first value in the data set is H and if all the rest are the same
			Hcount = Hcount + 1
		else: # If all data values are not H, then it is counted as not an H
			Normalcount = Normalcount + 1

		Totalcount=Totalcount+1 # Keeps track of the total amount of trials ran
		Trialflag=Trialflag+1 # The exit condition for the loop, when the desired trial number n is reached, the loop will break

	Timeflag=1 # Once the exit condition is reached for the trials being ran, this exit condition will be reached by the loop keeping track of time

t_final=time.time() # Sets the final time when the loop breaks

Totaltime = t_final-t0 # Calculates the total time that the simulation lasts (Difference in Unix time stamps)

print("")

if Totaltime <= 60: # If the time is over a minute, then it converts the time to minutes, if not then it just shows the time in seconds
	print("The elapsed time has been: " + str(round(Totaltime,2)) + " seconds")
else:
	print("The elapsed time has been: " + str(round(Totaltime / 60,2)) + " minutes" + " (" + str(round(Totaltime,2)) + " seconds)")

print("The number of H or T in a data set is: " + str(Setsize))
print("Total number of times " + str(Setsize) + " H's occurred: " + str(Hcount))
print("Total number of times " + str(Setsize) + " H's did not occur: " + str(Normalcount))
print("Total number of trials ran: " + str(Totalcount))

print("")

prob=Hcount/Totalcount 
percent = prob*100

print("For " + str(Trialnum) + " trials")

print("The probability of you getting " + str(Setsize) + " heads in a row on a coin toss is approximately: \n" + str(Hcount) + "/" + str(Totalcount) + " or " + str(round(prob,4)) + " (" + str(round(percent,2)) +"%) \n")

input("(Press enter to exit the program) \n")