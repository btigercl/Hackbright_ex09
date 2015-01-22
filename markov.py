#!/usr/bin/env python

from sys import argv

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_dictionary = {}
    filename = open(corpus, 'r')
    read_file = filename.read()
    words = read_file.split()
    for word_index in range(0, len(words) - 2):
        key = (words[word_index], words[word_index + 1])
        value = words[word_index + 2]
       # markov_dictionary[(words[word_index], words[word_index + 1])] = markov_dictionary.((words[word_index], words[word_index + 1]))  [words[word_index + 2]]
        if key not in markov_dictionary:
            markov_dictionary[key] = [value]
        else:
            markov_dictionary[key].append(value)
    return markov_dictionary


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    import random
    
    starting_point = random.choice(chains.keys())
    
    print 
    #pick a random value based on random key
    #intiate a list or string
    #new key = index 1 from tuple + value 
    #in a while loop
    # break if key = none
    #return string or list
    return "Here's some random text."

def main():
    #Change this to read input_text from a file
    script, filename = argv
    input_text = "Would you, could you in"
    chain_dict = make_chains(filename)
    crandom_text = make_text(chain_dict)
    # print random_text

if __name__ == "__main__":
    main()
