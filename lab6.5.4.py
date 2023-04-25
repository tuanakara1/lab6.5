def is_anagram(word1, word2):

    return sorted(word1.lower().replace(" ", "")) == sorted(word2.lower().replace(" ", ""))

def anagrams(word, word_list):

    return [w for w in word_list if is_anagram(w, word)]

word = "listen"
word_list = ["enlists", "google", "inlets", "banana"]
print(anagrams(word, word_list))
