def check_palindrome(sentence):
    """
    This function takes a word or a sentence and
    determines whereather is it palindrome or not.
    Case and any special characters should be ignored.
    """
    import string
    not_special = string.ascii_uppercase + string.ascii_lowercase
    c_list = [x for x in list(sentence.lower()) if x in not_special]
    n = 0
    m = len(c_list) - 1
    while n <= m:
        if c_list[n] != c_list[m]:
            return "no"
        n += 1
        m -= 1
    return "yes"


if __name__ == "__main__":
    import sys

    sentence = sys.argv[1]
    print(check_palindrome(sentence))
