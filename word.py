import string
import os
from collections import defaultdict

class WordforWord:

 

#method 1 
    def printDoc(self, filename):
        file = open(filename, "r") # Opens the file in read mode.
        words = ""
        for line in file:
            words = words + line
        print(words)

    #printDoc('/Users/sjahan/Desktop/PythonProjects/PyWordForWord/testdata/testdata2.txt')
    
#method 2
    def wordCount(first, countDoc):
        numOfwords = 0
        numOfcharc = 0
        numOflines = 0
        with open(countDoc, 'r') as f: #open the file and call f (f is the name of the variable)
            for line in f:
                line = line.strip(os.linesep) #separating a line from \n(new line) character and storing again in line
                wordslist = line.split() #splitting the line
                numOflines = numOflines +1 # incrementing value of num_lines
                numOfwords = numOfwords + len(wordslist) #incrementing value of a num_word. 
                numOfcharc = numOfcharc + sum(1 for c in line if c not in (os.linesep, ' '))  # incrementing the value of num_charc. if os.linesep is not a space
        print("Number of words in text file: ",numOfwords)
        print("Number of lines in text file: ",numOflines)
        print("Number of characters in text file: ", numOfcharc)
        my_tuple = (numOflines, numOfwords, numOfcharc)
        return my_tuple  
    
    #wordCount('/Users/sjahan/Desktop/PythonProjects/PyWordForWord/testdata/testdata2.txt')

    def word_frequency(first, filename):
            frequency = {}  # Initialize an empty dictionary to hold word frequencies
            with open(filename, 'r') as f:
                for line in f:
                    words = line.split()  # Split the line into words
                    for word in words:
                        word = word.lower()  # Make the word lowercase to avoid case sensitivity
                        if word in frequency:
                            frequency[word] += 1  # If the word is already in the dictionary, increment its count
                        else:
                            frequency[word] = 1  # If it's a new word, add it to the dictionary with a count of 1
            print("Word Frequency:", frequency)
            return frequency

    #   words = input_string.split()
     #   wordCount = {}
      #  for word in words:
      #      wordCount[word] = wordCount.get(word, 0) + 1
       # return wordCount
    
    #word_frequency('/Users/sjahan/Desktop/PythonProjects/PyWordForWord/testdata/testdata2.txt')

WordforWord = WordforWord()
WordforWord.printDoc('/Users/sjahan/Desktop/PythonProjects/PyWordForWord/testdata/testdata3.txt')
WordforWord.wordCount('/Users/sjahan/Desktop/PythonProjects/PyWordForWord/testdata/testdata3.txt')
WordforWord.word_frequency('/Users/sjahan/Desktop/PythonProjects/PyWordForWord/testdata/testdata3.txt')    