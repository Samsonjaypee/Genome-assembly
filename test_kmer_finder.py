#!/usr/bin/env python3
# This script is used to test the functions in the kmer_finder.py script
# The script passed all these tests

import sys
from io import StringIO
import pytest
from kmer_finder import find_substrings, find_substrings_from_file, find_smallest_k

# Tests for find_substrings function
class TestFindSubstrings:
    def test_find_substrings_true_1(self):  #true
        sequence = "ATCGATCG"
        k = 3
        result = find_substrings(sequence, k)
        expected_result = {'ATC': ['TCG', 'TCG'], 'TCG': ['CGA', 'CG'], 'CGA': ['GAT'], 'GAT': ['ATC']}
        assert result == expected_result

    def test_find_substrings_true_2(self):  #true
        sequence = "ATCGATCG"
        k = 2
        result = find_substrings(sequence, k)
        assert result == {'AT': ['TC', 'TC'], 'TC': ['CG', 'CG'], 'CG': ['GA', 'G'], 'GA': ['AT']}

    def test_find_substrings_false_1(self):  #false
        sequence = "ATCGATCG"
        k = 3
        result = find_substrings(sequence, k)
        assert result != {'ATC': ['TCG'], 'TCG': ['CGA', 'C']}

    def test_find_substrings_false_2(self):  #false
        sequence = "ATCGATCG"
        k = 2
        result = find_substrings(sequence, k)
        assert result != {'AT': ['TC', 'TC'], 'TC': ['CG', 'CG'], 'CG': ['GA', 'GA']}

# Tests for find_substrings_from_file function
class TestFindSubstringsFromFile:
    def test_find_substrings_from_file_true_1(self):
        filename = "test_files/test_sequences1_true.fasta"  # true
        k = 3
        result = find_substrings_from_file(filename, k)
        expected_result = {'ATCGATCG': {'ATC': ['TCG', 'TCG'], 'CGA': ['GAT'], 'GAT': ['ATC'], 'TCG': ['CGA', 'CG']}}
        assert result == expected_result
    
    def test_find_substrings_from_file_true_2(self):
        filename = "test_files/test_sequences1_true.fasta"  # true
        k = 2
        expected_result = {'ATCGATCG': {'AT': ['TC', 'TC'], 'TC': ['CG', 'CG'], 'CG': ['GA', 'G'], 'GA': ['AT']}}
        result = find_substrings_from_file(filename, k)
        assert result == expected_result

    def test_find_substrings_from_file_false_1(self):
        filename = "test_files/test_sequences3_false.fasta"  # sequence has letters or number
        k = 3
        with pytest.raises(ValueError, match="Invalid character in sequence. Only 'A', 'T', 'C', 'G', and 'N' are allowed."):
            find_substrings_from_file(filename, k)

    def test_find_substrings_from_file_false_2(self):
        filename = "test_files/test_sequences4_false.fasta"  # sequence has letters or number
        k = 2
        with pytest.raises(ValueError, match="Invalid character in sequence. Only 'A', 'T', 'C', 'G', and 'N' are allowed."):
            find_substrings_from_file(filename, k)

    def test_find_substrings_from_file_invalid_file(self):
        filename = "nonexistent_file.txt"  # non-existent file name
        k = 3
        with pytest.raises(FileNotFoundError):
            find_substrings_from_file(filename, k)

# Tests for find_smallest_k function
class TestFindSmallestK:
    def test_find_smallest_k_true_1(self):
        filename = "test_files/test_sequences1_true.fasta"  # true
        result = find_smallest_k(filename)
        assert result == 1

    def test_find_smallest_k_true_2(self):
        filename = "test_files/test_sequences2_true.fasta"  # true
        result = find_smallest_k(filename)
        assert result == 8

    def test_find_smallest_k_invalid_file(self):
        filename = "nonexistent_file.txt"  # non-existent file name
        with pytest.raises(FileNotFoundError):
            find_smallest_k(filename)

