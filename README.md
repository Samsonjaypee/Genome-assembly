# Genome-assembly

This repository contains the kmer_finder.py script which has functions that can be used as starting point to assemble a genome.
To learn more about the functions follow these instruction:
1. Go to your terminal and open a interactive Python session by running ```python3```. 
2. Import the functions from kmer_finder.py using this code:
   
```from kmer_finder import find_substrings, find_substrings_from_file, find_smallest_k```

3. Using the help(function) will give you more information on each function.

```help(find_substrings)```

```help(find_substrings_from_file)```

```help(find_smallest_k)```

## USAGE

### find_substrings

This function identifies the substrings of a given sequence (as argument) and the subsequent substring based on the k-value (also argument). To run this scipt, copy this command:

```python3 kmer_finder.py find_substrings <sequence> <k-value>```

Change <sequence> with the sequence you want to use (e.g. ATGTCTGTCTGAA) and the <k-value>. For example:

```python3 kmer_finder.py find_substrings ATGTCTGTCTGAA 2```

Output:
```
K-mer: AT, Next K-mers: ['TG']
K-mer: TG, Next K-mers: ['GT', 'GT', 'GA']
K-mer: GT, Next K-mers: ['TC', 'TC']
K-mer: TC, Next K-mers: ['CT', 'CT']
K-mer: CT, Next K-mers: ['TG', 'TG']
K-mer: GA, Next K-mers: ['AA']
K-mer: AA, Next K-mers: ['A']
```
### find_substrings_from_file

This function identifies the substrings of a given sequence in a file and the subsequent substring based on the k-value (as argument). To run this scipt, copy this command:

```python3 kmer_finder.py find_substrings_from_file <filename> <k-value>```

Change <filename> with the filename you want to use (e.g. sequence.seq) and the <k-value>. For example:

```python3 kmer_finder.py find_substrings_from_file sequence.seq 40```

Output:

```
Sequence: CATGCAGTCGAGCGGAACGAGAATAGCTTGCTATTCGGCGTCGAGCGGCGGACGGGTGAGTAATGC
K-mer: CATGCAGTCGAGCGGAACGAGAATAGCTTGCTATTCGGCG, Next K-mers: ['ATGCAGTCGAGCGGAACGAGAATAGCTTGCTATTCGGCGT']
K-mer: ATGCAGTCGAGCGGAACGAGAATAGCTTGCTATTCGGCGT, Next K-mers: ['TGCAGTCGAGCGGAACGAGAATAGCTTGCTATTCGGCGTC']
K-mer: TGCAGTCGAGCGGAACGAGAATAGCTTGCTATTCGGCGTC, Next K-mers: ['GCAGTCGAGCGGAACGAGAATAGCTTGCTATTCGGCGTCG']
K-mer: GCAGTCGAGCGGAACGAGAATAGCTTGCTATTCGGCGTCG, Next K-mers: ['CAGTCGAGCGGAACGAGAATAGCTTGCTATTCGGCGTCGA']
K-mer: CAGTCGAGCGGAACGAGAATAGCTTGCTATTCGGCGTCGA, Next K-mers: ['AGTCGAGCGGAACGAGAATAGCTTGCTATTCGGCGTCGAG']
K-mer: AGTCGAGCGGAACGAGAATAGCTTGCTATTCGGCGTCGAG, Next K-mers: ['GTCGAGCGGAACGAGAATAGCTTGCTATTCGGCGTCGAGC']
K-mer: GTCGAGCGGAACGAGAATAGCTTGCTATTCGGCGTCGAGC, Next K-mers: ['TCGAGCGGAACGAGAATAGCTTGCTATTCGGCGTCGAGCG']
K-mer: TCGAGCGGAACGAGAATAGCTTGCTATTCGGCGTCGAGCG, Next K-mers: ['CGAGCGGAACGAGAATAGCTTGCTATTCGGCGTCGAGCGG']
K-mer: CGAGCGGAACGAGAATAGCTTGCTATTCGGCGTCGAGCGG, Next K-mers: ['GAGCGGAACGAGAATAGCTTGCTATTCGGCGTCGAGCGGC']
K-mer: GAGCGGAACGAGAATAGCTTGCTATTCGGCGTCGAGCGGC, Next K-mers: ['AGCGGAACGAGAATAGCTTGCTATTCGGCGTCGAGCGGCG']
K-mer: AGCGGAACGAGAATAGCTTGCTATTCGGCGTCGAGCGGCG, Next K-mers: ['GCGGAACGAGAATAGCTTGCTATTCGGCGTCGAGCGGCGG']
...
```

### find_smallest_k

This function identifies the smallest k-value for a given sequence file. To run this scipt, copy this command:

```python3 kmer_finder.py find_smallest_k <filename>```

Replace <filename> with the filename of the sequence file

```python3 kmer_finder.py find_smallest_k reads.fa```

Output:

```
The smallest value of k meeting the criteria:
10
```
For the [reads.fa](Genome-assembly/reads.fa), the identified smallest k-value using the find_smallest_k function is 10.
