#!/usr/bin/env python

import sys

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
#    markov_dictionary = {}
#    stop = len(words)
    for each_line in corpus: 
        stripped_line = corpus.rstrip()
        words = stripped_line.split(" ")
    print words
#for word_index in range(0, stop - 2):
       #markov_dictionary[(words[word_index], words[word_index + 1])] = words.get((words[word_index], words[word_index + 1]), 0) + words[word_index + 2]
 #   print markov_dictionary


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."

def main():
    #args = sys.argv

    # Change this to read input_text from a file
    #script, args = sys.argv
    input_text = "Would you, could you in"
    chain_dict = make_chains(input_text)
    #random_text = make_text(chain_dict)
    # print random_text

if __name__ == "__main__":
    main()
