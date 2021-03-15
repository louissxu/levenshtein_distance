import sys

def levenshtein_distance(string_a, string_b):
    '''Returns the levenshtein distance between two strings
    Args:
        string_a (str): first string to be compared
        string_b (str): second string to be compared

    Returns:
        result (int): the calculated levenshtein distance
    '''

    raise NotImplementedError


def main():
    # Check command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python levenshtein_distance.py first_string second_string")

    # Run levenshtein distance
    print(levenshtein_distance(sys.argv[1], sys.argv[2]))


if __name__ == "__main__":
    main()