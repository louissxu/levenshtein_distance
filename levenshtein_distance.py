import sys

def levenshtein_distance(string_a, string_b, count = 0):
    '''Returns the levenshtein distance between two strings
    Args:
        string_a (str): first string to be compared
        string_b (str): second string to be compared

    Returns:
        result (int): the calculated levenshtein distance
    '''

    # Base case - one or more of the strings are empty. Return the total count
    if string_a == "" and string_b == "":
        return count
    if string_a == "":
        return count + len(string_b)
    if string_b == "":
        return count + len(string_a)

    # Recursive cases
    # Try to match letter for free
    if string_a[0] == string_b[0]:
        return match_letter(string_a, string_b, count)

    # Otherwise, do task with cost
    else:
        return min(
            change_letter(string_a, string_b, count),
            insert_letter(string_a, string_b, count),
            delete_letter(string_a, string_b, count),
        )

def match_letter(a, b, count):
    return levenshtein_distance(a[1:], b[1:], count) # Count does not increment. "Free letter"

def change_letter(a, b, count):
    return levenshtein_distance(a[1:], b[1:], count + 1)

def insert_letter(a, b, count):
    return levenshtein_distance(a, b[1:], count + 1)

def delete_letter(a, b, count):
    return levenshtein_distance(a[1:], b, count + 1)


def main():
    # Check command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python levenshtein_distance.py first_string second_string")

    # Run levenshtein distance
    print(levenshtein_distance(sys.argv[1], sys.argv[2]))


if __name__ == "__main__":
    main()