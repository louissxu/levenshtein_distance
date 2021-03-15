# Levenshtein Distance

Calculates the levenshtein distance between two strings recursively
```
Usage: python levenshtein_distance.py first_string second_string
```



### Specification
Calculate the difference between two strings where each character change, insertion, or deletion has a cost of one.

### Background
The Levenshtein distance is a measure of the difference between two sequences. Informally it is the number of single character edits (substitution, insertion, deletion) to change from one string to another.

Naive implementation from first principles. Brute force to try all possible options out of substitute/insert/delete recursively and returns the smallest distance. No attempt has been made to make this more efficient. Worst case time complexity is `O(n^3)`.

No sanitisation of input strings has been made. The inputs are assumed to be two valid lowercase strings.