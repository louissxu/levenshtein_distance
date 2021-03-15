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

    
    # Probable pseudocode

    # base case
    # if a and b are empty return count

    # else    
    # recursive case
    # return minimum of:
    # match_letter
    # change letter
    # insert_letter
    # delete_letter


    # match_letter(a, b, count):
    #     dog -> dark
    #     return og, ark, count

    # change_letter(a, b, count):
    #     dog -> cat
    #     return og, at, count +=1

    # insert_letter(a, b, count):
    #     dog -> cat
    #     cdog -> cat
    #     return cdog, cat, count += 1 (and let subsequent match remove one) or simplify down and
    #     return dog, at, count += 1

    # delete_letter(a, b, count):
    #     dog -> cat
    #     og -> cat
    #     return og, cat count += 1 


def main():
    # Check command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python levenshtein_distance.py first_string second_string")

    # Run levenshtein distance
    print(levenshtein_distance(sys.argv[1], sys.argv[2]))


if __name__ == "__main__":
    main()