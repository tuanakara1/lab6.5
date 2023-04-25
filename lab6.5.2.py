def is_palindrome(word):

    return word == word[::-1]

def palindrome_strings(string_list):

    return [word for word in string_list if is_palindrome(word)]

string_list = ["level", "toot", "python","civic"]
print(palindrome_strings(string_list))
