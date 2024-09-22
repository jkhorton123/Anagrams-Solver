import json
import os
from itertools import combinations, permutations
import re
from pathlib import Path

def getWords():
    """
    Loads in txt file containing list of all english words and returns the words in a set for O(1) lookup
    en.txt must be in the current directory

    Returns:
        engWords (set) : Set containing all English words as keys
    """
    path = str(Path.cwd())
    path += "/en.txt"
    with open(path) as words:
        engWords = set(word.strip().lower() for word in words)
    return engWords

def getLets():
    """
    Asks user for a sequence of between 3 and 8 letters and returns the letters as a string

    Returns:
        lets (string) : Concatenation of the user-entered letters
    """
    validStr = False
    while not validStr:
        validStr = True
        letsMsg = "Please enter between 3 and 8 English letters for the anagram solver: "
        lets = input(letsMsg)
        if len(lets) < 3: 
            validStr = False
            print("Less than 3 letters were entered")
            continue
        if len(lets) > 8:
            validStr = False
            print("More than 8 letters were entered")
            continue
        lets = re.sub(r"\s+", "", lets, flags=re.UNICODE)
        for let in lets:
            if not let.isalpha():
                validStr = False
                print("One or more of the characters entered are not English letters")
                break
    lets = lets.lower()
    return lets

def getMode():
    """
    Asks the user to enter a digit representing the display mode for the anagrams

    Returns:
        mode (int) : 1 represents the mode where the words will be shown in categories based on lengths
                     2 represents the mode where the words will be displayed in order of decreasing length
                     3 allows the user to enter new letters
                     4 quits the program
    """
    isMode = False
    while not isMode:
        isMode = True
        modeMsg = "Enter 1 to display the words categorized by length, 2 to display the words from longest to shortest, 3 to enter new letters, 4 to quit the program\n"
        mode = input(modeMsg)
        if not mode.isdigit():
            isMode = False
            print("Please enter a valid integer")
        
        elif not (int(mode) in (1, 2, 3, 4)):
            isMode = False
            print("Please enter an integer between 1 and 4")

    return int(mode)

def findAnagrams(lets, words):
    """
    Finds and returns all anagrams made up of 3 or more of the user-entered letters

    Parameters:
        lets (string) : The user-entered letters
        words (dict) : Dictionary containing all English words as keys

    Returns:
        anagrams (list) : Contains all the valid anagrams containing only the user-entered letters
    """
    anagrams = []
    for i in range(3, len(lets)+1):
        combs = [j for j in permutations(list(lets), i)] # Computes all possible arrangements of the letters 
        for comb in list(combs): 
            word = "".join(comb)
            if word in words and not word in anagrams:
                anagrams.append(word)
    return anagrams


def catMode(anagrams):
    """
    Displays the anagrams in categories based on length

    Parameters: 
        anagrams (list) : Contains all the valid anagrams containing only the user-entered letters
    """
    if len(anagrams) == 0:
        print("No 3+ letter valid English anagrams were found")
        return
    maxLen = len(anagrams[-1])
    tempList = []
    l = maxLen
    i = 1
    for word in reversed(anagrams):
        if not len(word) == l:
            tempList = sorted(tempList)
            print(l, "Letter Words:", ' '.join(tempList))
            l = len(word)
            tempList = []
            tempList.append(word)
            if i == len(anagrams):
                print(l, "Letter Words:", ' '.join(tempList))
        elif i == len(anagrams):
            tempList.append(word)
            tempList = sorted(tempList)
            print(l, "Letter Words:", ' '.join(tempList))
        else:
            tempList.append(word)
        i += 1
    return 


def rankMode(anagrams):
    """
    Displays the anagrams in decreasing order by length

    Parameters:
        anagrams (list) : Contains all the valid anagrams containing only the user-entered letters
    """
    if len(anagrams) == 0:
        print("No 3+ letter valid English anagrams were found")
        return
    maxLen = len(anagrams[-1])
    tempList = []
    l = maxLen
    i = 1
    j = 1 # Specifies the jth anagram in the sorted list
    for word in reversed(anagrams):
        if not len(word) == l:
            tempList = sorted(tempList)
            for sWord in tempList:
                print(j, ": ", sWord)
                j+=1
            l = len(word)
            tempList = []
            tempList.append(word)
            if i == len(anagrams):
                print(j, ": ", word)
        elif i == len(anagrams):
            tempList.append(word)
            tempList = sorted(tempList)
            for sWord in tempList:
                print(j, ": ", sWord)
                j+=1
        else:
            tempList.append(word)
        i += 1
    return
    
def main():
    """
    Initializes and executes the anagrams solver
    """
    print("Welcome to Anagrams Solver")
    run = True
    while run:
        run = False 
        words = getWords()
        lets = getLets()
        anagrams = findAnagrams(lets, words)
        dRun = True
        while dRun:
            mode = getMode()
            if mode == 1:
                catMode(anagrams)
            elif mode == 2: 
                rankMode(anagrams)
            elif mode == 3:
                run = True
                break
            else: 
                return


if __name__ == "__main__":
    main()
    