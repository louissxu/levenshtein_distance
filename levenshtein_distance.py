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
    if string_a == "" and string_b == "":
        return count

    # Need to explicitly handle one string empty otherwise insert/delete recursion tries to slice empty strings
    if string_a == "":
        return count + len(string_b)
    if string_b == "":
        return count + len(string_a)

    # Try to match letter
    if string_a[0] == string_b[0]:
        return match_letter(string_a, string_b, count)

    else:
        return min(
            change_letter(string_a, string_b, count),
            insert_letter(string_a, string_b, count),
            delete_letter(string_a, string_b, count),
        )

def match_letter(a, b, count):
    return levenshtein_distance(a[1:], b[1:], count)

def change_letter(a, b, count):
    return levenshtein_distance(a[1:], b[1:], count+1)

def insert_letter(a, b, count):
    return levenshtein_distance(a, b[1:], count+1)

def delete_letter(a, b, count):
    return levenshtein_distance(a[1:], b, count+1)

    # Better pseudocode

    # base case
    # if a and b are the same return count

    # else recursive case 
    # recursive case
    # return ld of minimum of:
    # match_letter
    # change letter
    # insert_letter
    # delete_letter


    # match_letter(a, b, count):
    #     dog -> dark
    #     return ld(og, ark, count)

    # change_letter(a, b, count):
    #     dog -> cat
    #     return ld(og, at, count +=1)

    # insert_letter(a, b, count):
    #     dog -> cat
    #     cdog -> cat
    #     return ld(cdog, cat, count += 1) (and let subsequent match remove one) or simplify down and
    #     return ld(dog, at, count += 1)

    # delete_letter(a, b, count):
    #     dog -> cat
    #     og -> cat
    #     return ld(og, cat count += 1)


def main():
    # Check command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python levenshtein_distance.py first_string second_string")

    # Run levenshtein distance
    print(levenshtein_distance(sys.argv[1], sys.argv[2]))


if __name__ == "__main__":
    main()