# Tinashe M. Tapera
# CS520
# Homework 3 Part 2: Merge Sort Algorithm
# Notes: I acknowledge that there are very few sanity checks and checks for valid user input 

#--------------------------------------#
# imports up here #
import random #for random numbers
import time #for timing the algorithm
import os #for reading and writing to file
#--------------------------------------#
#first lets build an array of integers,
#allowing the user to determine how many to use

print("Welcome to a demo of the merge sort algorithm. Here, we'll sort an array of integers [ranging from 0 to 10000] and time the algorithm performance.")
exSize = int(input("How many integers should the array be?: "))


print("Here's an unsorted list...")
myArray = random.sample(range(10000),exSize)
print(myArray)

#-------------------------------------#
# now, define the algorithm in function  # 

def Merge(leftSide,rightSide):
    toReturn = []

    while len(leftSide) != 0  and len(rightSide) != 0:
        if leftSide[0] > rightSide[0]:
            toReturn.append(rightSide.pop(0))
        else:
            toReturn.append(leftSide.pop(0))

    while leftSide:
        toReturn.append(leftSide.pop(0))
    while rightSide:
        toReturn.append(rightSide.pop(0))

    #print("Here is what we merged: ")
    #print(toReturn)
    return(toReturn)
        

def M_Sort(theArray):
    
    # first, recurse through the array, splitting it in half each time;
    # if the array is singular, return it
    if(len(theArray) == 1 or len(theArray) == 0):
        return(theArray)
    else:
        mid = int(len(theArray)/2)
        #print("Midpoint: " + str(mid))
        left = theArray[:mid]
        right = theArray[mid:]

        #print(left)
        #print(right)
        left = M_Sort(left)
        right = M_Sort(right)

        #print("This is the left side: ")
        #print(left)
        #print("This is the right side: ")
        #print(right)

        #then, merge the two halves
        return(Merge(left,right))


#--------------done---------------#
t0 = time.clock()
sortedArray = M_Sort(myArray)
t1 = time.clock()
final = t1-t0
print("And here, it's sorted: ")
print(sortedArray)
print("And it only took " + str(final) + " seconds.")
#--------------------------------#
# incorporate a timer  and a return#

def MergeSort(arraySize):
    theArray = random.sample(range(10000),arraySize)

    t0 = time.clock()
    result = M_Sort(theArray)
    t1 = time.clock()

    final = t1-t0

    # i know we don't see or return the results here; trust me, it works
    return((arraySize,final))
#---------------done---------------#



#-----collect data on performance-----#

continuation = input("\nWe can run and collect data on this algorithm's performance. Would you like to do that now? (y/n): ") 

if continuation == "y" or continuation == "Y":
    nRuns = int(input("How many iterations do you want to do?"))
    largest = int(input("How many integers should the largest list have?"))
    smallest = int(input("How many integers should the smallest list have?"))

    arrays = [random.randint(smallest,largest) for x in range(nRuns)]
    print("Computing...")

    
    results = [MergeSort(n) for n in arrays]

    #----------------------------------#
    # to finish off, we write
    # the results to a file which we
    # append each time this script runs

    fname = "MergeSortResults.csv"
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
    exit
