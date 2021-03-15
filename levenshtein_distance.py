import sys

def levenshtein_distance(string_a, string_b, count = None):
    '''Returns the levenshtein distance between two strings
    Args:
        string_a (str): first string to be compared
        string_b (str): second string to be compared

    Returns:
        result (int): the calculated levenshtein distance
    '''

    # Initialise count so same function can be used for the recursion
    if not count:
        count = 0

    # Base case
    # One or more of the strings are empty. Return the total count
    if string_a == "" and string_b == "":
        return count

    # Need to explicitly handle one string empty otherwise insert/delete recursion tries to slice empty strings
    if string_a == "":
        return count + len(string_b)
    if string_b == "":
        return count + len(string_a)

    # Recursive cases

    # Try to match letter for free
    if string_a[0] == string_b[0]:
        return match_letter(string_a, string_b, count)

    # Otherwise, do spendy task
    else:
        return min(
            change_letter(string_a, string_b, count),
            insert_letter(string_a, string_b, count),
            delete_letter(string_a, string_b, count),
        )

def match_letter(a, b, count):
    # pig -> pat
    # ig -> at
    # Count does not increment. "Free letter"
    return levenshtein_distance(a[1:], b[1:], count)

def change_letter(a, b, count):
    # dog -> cat
    # cog -> cat
    # og -> at (includes the step done by match letter)
    # Count increments since this is a costly action
    return levenshtein_distance(a[1:], b[1:], count+1)

def insert_letter(a, b, count):
    # dog -> cat
    # cdog -> cat
    # dog -> at (including the step done by match letter)
    # Count increments
    return levenshtein_distance(a, b[1:], count+1)

def delete_letter(a, b, count):
    # dog -> cat
    # og -> cat
    # Count increments
    return levenshtein_distance(a[1:], b, count+1)


def main():
    # Check command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python levenshtein_distance.py first_string second_string")

    # Run levenshtein distance
    print(levenshtein_distance(sys.argv[1], sys.argv[2]))


if __name__ == "__main__":
    main()