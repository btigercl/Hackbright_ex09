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
    text = [ ]
    random_text = ""
    key = random.choice(chains.keys())
    text.append(key[0])
    text.append(key[1])
    # starting_value = random.choice(chains[starting_key])
    #text.append(starting_value)
#   previous_key = (starting_key[1], starting_value)
    # text.append(previous_key[0])
    # text.append(previous_key[1])
    while key in chains:
        value = random.choice(chains[key])
        # value = random.choice(chains[previous_key])
        text.append(value)
        key = (key[1], value)
        # text.append(new_key[0])
        # text.append(new_key[1])
        # previous_key = new_key
        # if previous_key not in chains:
        #     stop = False 
    random_text = " ".join(text)
    return random_text

def main():
    #Change this to read input_text from a file
    script, filename = argv
    # input_text = "Would you, could you in"
    chain_dict = make_chains(filename)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()
