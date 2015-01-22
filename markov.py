#!/usr/bin/env python

import sys

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""


    for each_line in corpus: 
        stripped_line = corpus.rstrip()
        words = stripped_line.split(" ")
    print words


    #markov_dictionary = {}
    #strip = 
    # tuples = corpus.split(' ', 2)
    # print tuples

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."

def main():
    #args = sys.argv

    # Change this to read input_text from a file
    #script, args = sys.argv
    input_text = "Would you, could you in a house Would you, could you with a mouse Would you, could you in a box Would you, could you with a fox Would you like green eggs and ham? Would you like them, Sam I Am?"

    markov_dictionary = make_chains(input_text)
    # random_text = make_text(chain_dict)
    # print random_text

if __name__ == "__main__":
    main()
