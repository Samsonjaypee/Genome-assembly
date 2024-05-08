#!/usr/bin/env python3
#To know more about the functions follow these instructions:
#1. Go to your terminal and open a interactive Python session by running $python3
#2. Import the functions from kmer_finder.py using this code:$from kmer_finder import find_substrings, find_substrings_from_file, find_smallest_k
#3. Using the help(function) will give you more information on each function.
#$help(find_substrings)
#$help(find_substrings_from_file)
#$help(find_smallest_k)

import sys

def find_substrings(sequence, k):
    """
    This function identifies all the substrings of size k and their subsequent substrings for a single sequence.

    Args:
    sequence (str): The input sequence.
    k (int): The size of the substrings.

    Returns:
    dict: A dictionary where keys are k-mers and values are lists of subsequent k-mers.
    """
    # Setting the code to only include specific characters. I added N because some sequences contain N.
    valid_chars = set('ATCGN')
    if not set(sequence).issubset(valid_chars):
        raise ValueError("Invalid character in sequence. Only 'A', 'T', 'C', 'G', and 'N' are allowed.")

    kmers = {}
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        next_kmer = sequence[i+1:i+k+1]
        if kmer not in kmers:
            kmers[kmer] = []
        kmers[kmer].append(next_kmer)
    return kmers  # returning the identified k-mers

def find_substrings_from_file(filename, k):
    """
    This function identifies all possible substrings and their subsequent substrings for all sequences in a file.

    Args:
    filename (str): The name of the file containing sequences.
    k (int): The size of the substrings.

    Returns:
    dict: A dictionary where keys are sequences and values are dictionaries containing substrings and their subsequent substrings.
    """
    all_substrings = {}
    with open(filename, 'r') as file:
        for line in file:
            sequence = line.strip()
            if sequence:
                valid_chars = set('ATCGN')
                if not set(sequence).issubset(valid_chars):
                    raise ValueError("Invalid character in sequence. Only 'A', 'T', 'C', 'G', and 'N' are allowed.") # # Setting the code to only include specific characters. I added N because some sequences contain N

                kmers = {}
                for i in range(len(sequence) - k + 1):
                    kmer = sequence[i:i+k]
                    next_kmer = sequence[i+1:i+k+1]
                    if kmer not in kmers:
                        kmers[kmer] = []
                    kmers[kmer].append(next_kmer)
                all_substrings[sequence] = kmers
    return all_substrings  # returning the substrings identified

def find_smallest_k(filename):
    """
    This function identifies the smallest value of k where every substring has only one possible subsequent substring.
    
    Args:
    - filename (str): The name of the file containing sequence fragments.
    
    Returns:
    - int: The smallest value of k meeting the criteria.
    """
    smallest_k = 1
    while True:
        all_substrings = find_all_substrings_with_next(filename, smallest_k)
        unique_next_substrings_count = sum(len(set(next_substrings)) == 1 for next_substrings in all_substrings.values())
        if unique_next_substrings_count == len(all_substrings):
            return smallest_k
        smallest_k += 1
    
def find_all_substrings_with_next(filename, k):
    """
    Find all substrings of length k in the file and their subsequent substrings.
                    
    Args:
    - filename (str): The name of the file containing sequence fragments.
    - k (int): The length of substrings to find. 
                
    Returns:
    - dict: A dictionary containing substrings as keys and their subsequent substrings as values.
    """
    all_substrings = {}
    with open(filename, 'r') as file: # opening the file with the sequence
        for line in file:
            sequence = line.strip()
            if sequence:
                valid_chars = set('ATCGN')
                if not set(sequence).issubset(valid_chars):
                    raise ValueError("Invalid character in sequence. Only 'A', 'T', 'C', 'G', and 'N' are allowed.") # Setting the code to only include specific characters. I added N because some sequences contain N
                
                for i in range(len(sequence) - k):
                    substring = sequence[i:i + k]
                    next_substring = sequence[i + 1:i + k + 1]
                    if substring not in all_substrings:
                        all_substrings[substring] = [next_substring]
                    else:
                        all_substrings[substring].append(next_substring)
    return all_substrings

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 kmer_finder.py <option> <arguments>") # I added this, so when the input is not correct, this will show up
        sys.exit(1)
    
    option = sys.argv[1]
    if option == "find_substrings":
        if len(sys.argv) != 4:
            print("Usage: python3 kmer_finder.py find_substrings <sequence> <k-value>") # I added this, so when the input is not correct, this will show up
            sys.exit(1)
        
        sequence = sys.argv[2]
        k = int(sys.argv[3])
        try:
            substrings = find_substrings(sequence, k)
            for kmer, next_kmers in substrings.items():
                print("K-mer: {}, Next K-mers: {}".format(kmer, next_kmers))
        except ValueError as e:
            print(e)
            sys.exit(1)
    
    elif option == "find_substrings_from_file":
        if len(sys.argv) != 4:
            print("Usage: python3 kmer_finder.py find_substrings_from_file <filename> <k-value>") # I added this, so when the input is not correct, this will show up
            sys.exit(1)
        
        filename = sys.argv[2]
        k = int(sys.argv[3])
        try:
            all_substrings = find_substrings_from_file(filename, k)
            for sequence, substrings in all_substrings.items():
                print(f"Sequence: {sequence}")
                for kmer, next_kmers in substrings.items():
                    print(f"K-mer: {kmer}, Next K-mers: {next_kmers}")
        except ValueError as e:
            print(e)
            sys.exit(1)
    
    elif option == "find_smallest_k":
        if len(sys.argv) != 3:
            print("Usage: python3 kmer_finder.py find_smallest_k <filename>") # I added this, so when the input is not correct, this will show up
            sys.exit(1)
        
        filename = sys.argv[2]   # printing the result
        result = find_smallest_k(filename)
        print("The smallest value of k meeting the criteria:")
        print(result)
    
    else:
        print("Invalid option. Available options: find_substrings, find_substrings_from_file, find_smallest_k") # If the function name is not correct, this will show up
        sys.exit(1)

