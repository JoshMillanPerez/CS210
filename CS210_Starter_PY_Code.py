import re
import string


def Menu():
    print()
    print("------------------------------------------------------------------------------------------------------------------------")
    print("1: Produce a list of all items purchased in a given day along with the number of times each item was purchased.")
    print("2: Produce a number representing how many times a specific item was purchased in a given day.")
    print("3: Produce a text-based histogram listing all items purchased in a given day, along with a representation of the number of times each item was purchased.")
    print("4: Exit")
    print("Enter your selection as a number 1, 2, 3 or 4.")
    print("------------------------------------------------------------------------------------------------------------------------")

def CountFile(v):
    # Open the file in read mode
    text = open("frequency.dat.txt", "r")  
    # Create an empty dictionary
    d = dict()
    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()
  
        # Convert the characters in line to 
        # lowercase to avoid case mismatch
        line = line.lower()
  
        # Split the line into words
        words = line.split(" ")
  
        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1
    # Print the contents of dictionary
    for key in list(d.keys()):
        print(key, d[key])
    return 0
    
def CountFileWord(v):
    # Open the file in read mode
    text = open("frequency.dat.txt", "r")  
    # Create an empty dictionary
    d = dict()
    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()
  
        # Convert the characters in line to 
        # lowercase to avoid case mismatch
        line = line.lower()
  
        # Split the line into words
        words = line.split(" ")
  
        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1
    # Print the contents of dictionary
    v=v.lower()
    if v in d: #v is the word youre looking for
        print(v, d[v])
    else:
        print("Not an option")
    return 0

def Histogram(v):
# Open the file in read mode
    text = open("frequency.dat.txt", "r")  
    # Create an empty dictionary
    d = dict()
    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()
  
        # Convert the characters in line to 
        # lowercase to avoid case mismatch
        line = line.lower()
  
        # Split the line into words
        words = line.split(" ")
  
        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1
    # Print the contents of dictionary
    for key in list(d.keys()):
        print(key, v*d[key]) # v is the symbol
    return 0