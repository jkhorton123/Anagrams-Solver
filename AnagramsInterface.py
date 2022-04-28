import os
from itertools import combinations, permutations
import re

def getWords():
    pathMsg = "Please enter the path to the Collins Scrabble Words txt File: "
    path = input(pathMsg)
    with open(path) as words:
        engWords = set(word.strip().lower() for word in words)
    #print(engWords)
    return engWords

def getLets():
    letsMsg = "Please enter up to 8 letters for the anagram solver: "
    lets = input(letsMsg)
    lets = re.sub(r"\s+", "", lets, flags=re.UNICODE)
    lets = lets.lower()
    return lets

def getMode():
    modeMsg = "Please enter 1 to display the words organized by length and 2 to display the words from longest to shortest: "
    mode = int(input(modeMsg))
    return mode

def findAnagrams(lets, words):
    anagrams = []
    for i in range(1, len(lets)+1):
        combs = [j for j in permutations(list(lets), i)]
        for comb in list(combs): 
            word = "".join(comb)
            if word in words and not word in anagrams:
                anagrams.append(word)
    return anagrams


def orgMode(anagrams):
    #Program utilizes the Collins List of Scrabble Words (2019) to verify words
    
    return 
        
    


def rankMode(validWords):
    return
    
def main():
    """
    Initializes and executes the game 
    """
    print("Welcome to Anagrams Solver")
    words = getWords()
    lets = getLets()
    anagrams = findAnagrams(lets, words)
    print(anagrams)
    mode = getMode()
    if mode == 1:
        orgMode(anagrams)
    else: 
        rankMode(anagrams)



if __name__ == "__main__":
    main()
    