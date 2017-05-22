# Tinashe M. Tapera
# CS520
# Homework 3 Part 1: Selection Sort Algorithm
# Notes: I acknowledge that there are very few sanity checks and checks for valid user input 

#--------------------------------------#
# imports up here #
import random #for random numbers
import time #for timing the algorithm
import os #for reading and writing to file
#--------------------------------------#
#first lets build an array of integers,
#allowing the user to determine how many to use

print("Welcome to a demo of the selection sort algorithm. Here, we'll sort an array of integers [ranging from 0 to 10000] and time the algorithm performance.")
exSize = int(input("How many integers should the array be?: "))


print("Here's an unsorted list...")
myArray = random.sample(range(10000),exSize)
print(myArray)

#--- implement and time algorithm ----#
t0 = time.clock()
#iterate from left to right, keeping the left as sorted and the right as unsorted
for i in range(exSize):
    minValue = myArray[i]

    #find the minimum value in the unsorted portion
    for j in range(i,exSize):
        if myArray[j] < minValue:
            minValue = myArray[j]
    
    #swap the minimum value and the first item in the unsorted portion
    pos1, pos2 = i, myArray.index(minValue)
    myArray[pos1], myArray[pos2] = myArray[pos2], myArray[pos1]

t1 = time.clock()
final = t1-t0

print("And now, it's sorted:")
print(myArray)
print("And it only took " + str(final) + " seconds.")

#-------------------------------------#
# now, implement the algorithm in function  # 

def Sel_Sort(arraySize):
    theArray = random.sample(range(10000),arraySize)

    t0 = time.clock()
    #iterate from left to right, keeping the left as sorted and the right as unsorted
    for i in range(arraySize):
        minValue = theArray[i]

        #find the minimum value in the unsorted portion
        for j in range(i,arraySize):
            if theArray[j] < minValue:
                minValue = theArray[j]
    
        #swap the minimum value and the first item in the unsorted portion
        pos1, pos2 = i, theArray.index(minValue)
        theArray[pos1], theArray[pos2] = theArray[pos2], theArray[pos1]

    t1 = time.clock()
    final = t1-t0

    return((arraySize,final))
#--------------done---------------#

#-----collect data on performance-----#

continuation = input("\nWe can run and collect data on this algorithm's performance. Would you like to do that now? (y/n): ") 

if continuation == "y" or continuation == "Y":
    nRuns = int(input("How many iterations do you want to do?"))
    largest = int(input("How many integers should the largest list have?"))
    smallest = int(input("How many integers should the smallest list have?"))

    arrays = [random.randint(smallest,largest) for x in range(nRuns)]
    print("Computing...")
    
    results = [Sel_Sort(n) for n in arrays]

    #----------------------------------#
    # to finish off, we write
    # the results to a file which we
    # append each time this script runs

    fname = "SelSortResults.csv"
    if os.path.isfile(fname):
        print("A previous dataset already exists! Appending a new set of results...")
        f = open(fname, "a")
        f.write("\n")
        f.write('\n'.join('%s,%s' % x for x in results))
        f.close()
    else:
        print("Writing out the results to a new file...")
        f = open(fname, "w+")
        f.write("Length of List,Time(s)\n")
        f.write('\n'.join('%s,%s' % x for x in results))
        f.close()
    print("Done! Exiting...")

else:
    print("Exiting...")
