# This program determines the probability of getting n heads in a row when flipping a coin
# n times per data set for m trials, n and m is determined by the user
import random
import time
import matplotlib.pyplot as plt

Trialflag=0 # This increments to keep track of the trial we are on
Hcount=0 # This increments to keep track of heads
Normalcount=0 # This increments whenever we dont have all heads
Totalcount=0 # This increments to keep track of the total amount of trials, regardless of all heads or not

RunCount = 0
Trialnum = 100000 # The ammount of trials to test for in 

Setsize = 1 # Must start with one flip 
Setsize_max = 20 # Max amount of heads we are testing for in each size case (amount of flips)

# Lists to plot:
probs_heads = []
probs_normal = []
Setsize_nums = []

while Setsize <= Setsize_max:
    # reset per set size
    #Trialflag = 0
    Hcount = 0
    Normalcount = 0
    Totalcount = 0
    while Totalcount < Trialnum: # Runs the program for n (Trialnum) trials
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
        #Trialflag=Trialflag+1 # The exit condition for the loop, when the desired trial number n is reached, the loop will break

    prob_heads=Hcount/Totalcount # Prob of getting all heads
    prob_normal = Normalcount/Totalcount # Prob of not getting all heads

    percent_heads = prob_heads*100
    percent_normal = prob_normal*100

    probs_heads.append(round(percent_heads, 2))
    probs_normal.append(round(percent_normal, 2))
    
    Setsize_nums.append(Setsize)
    Setsize+=1
    #Trialnum+=1

print(probs_heads)
print("")
print(probs_normal)
print("")
print(Setsize_nums)

# Plotting:
plt.plot(Setsize_nums, probs_heads, label="Probability of All Heads")
plt.plot(Setsize_nums, probs_normal, label="Probability of Not All Heads")
plt.axhline(y=0, color='green', linestyle='--', linewidth=1)
plt.axhline(y=50, color='black', linestyle='--', linewidth=1)
plt.axhline(y=100, color='green', linestyle='--', linewidth=1)
plt.axvline(x=1, color='black', linestyle='--', linewidth=1)

plt.xticks(range(1, 21))
#plt.ylim(0, 100)
plt.yticks(range(0, 110, 10))

plt.xlabel('Number of Coin Flips')
plt.ylabel('Probability (%)')
plt.title(f'Probability vs. Number of Coin Flips \n ({Trialnum} Trials per Number of Coin Flips)')

plt.legend(loc="center right", bbox_to_anchor=(1, 0.2))
plt.savefig("CoinTossProbability.pdf")
plt.show()
