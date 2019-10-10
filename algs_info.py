



ALGS = {


    'Levenshtein distance': 'The Levenshtein distance between two words is the minimum number of single-character edits \n(insertions, deletions or substitutions) required to change one word into the other.',
    
    'Damerau-Levenshtein Distance': 'The Damerau–Levenshtein distance between two words is the minimum number of operations \n(consisting of insertions, deletions or substitutions of a single character, \nor transposition of two adjacent characters) required to change one word into the other. \nIt differs from the classical Levenshtein distance by including transpositions among its allowable operations in addition \nto the three classical single-character edit operations',

    'Jaro Distance': 'The Jaro algorithm is a measure of characters in common, being no more than half the length of the longer \nstring in distance, with consideration for transpositions.',

    'Jaro-Winkler Distance': 'Winkler modified the Jaro algorithm to support the idea that differences near the start of the string \nare more significant than differences near the end of the string.',

    'Match Rating Approach Comparison': 'The match rating approach (MRA) is a phonetic algorithm, for indication and comparison of \nhomophonous names (a word pronounced the same as another but differing in meaning)',

    'Hamming Distance': 'the Hamming distance between two strings of equal length is the number of positions at which the corresponding \nsymbols are different. In other words, it measures the minimum number \nof substitutions required to change one string into the other, or the minimum number of errors that could have transformed one string into the other.',


}



def algs_names():
    
    print("\n"*2)

    for name, definition in ALGS.items():
        print( f"|{name}| ==> {definition}\n")

    print("\n")

algs_names()