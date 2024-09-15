#from english_words import get_english_words_set 

def insert_trie(root, word):
    temp = root
    for char in word:
        if char not in temp:
            temp[char] = {}
        temp = temp[char]
    temp['isEnd'] = True

def build_trie(words):
    trie_root = {}
    for word in words:
        insert_trie(trie_root, word)
    return trie_root

'''def print_suggestions(root, res,prefix):
    if 'isEnd' in root:
        print(res, end=' ')
    for char in root:
        if char != 'isEnd':
            res += char
            print_suggestions(root[char], res)
            res = res[:-1]'''
def levenshtein_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        new_distances = [index2 + 1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                new_distances.append(distances[index1])
            else:
                new_distances.append(1 + min((distances[index1], distances[index1 + 1], new_distances[-1])))
        distances = new_distances
    return distances[-1]

def print_suggestions(root, res, prefix, input_word):
    if 'isEnd' in root and levenshtein_distance(res, input_word) <= 1:
        print(prefix + res)
    for char in root:
        if char != 'isEnd':
            print_suggestions(root[char], res + char, prefix, input_word)

"""def check_spelling(trie_root, word):
    temp = trie_root
    for char in word:
        if char not in temp:
            print("Suggestions for correct spellings:")
            print_suggestions(trie_root, word)
            return False
        temp = temp[char]
    if 'isEnd' in temp:
        return True
    print("Suggestions for correct spellings:")
    print_suggestions(trie_root, word)
    return False"""

def check_spelling(trie_root, word):
    temp = trie_root
    prefix = ""
    for char in word:
        if char not in temp:
            print("Suggestions for correct spellings:")
            print_suggestions(trie_root, "", prefix, word)
            return False
        temp = temp[char]
        prefix += char

    if 'isEnd' in temp:
        return True

    print("Suggestions for correct spellings:")
    print_suggestions(temp, "", prefix[:-1], word)  # Adjusted this line
    return False

def main():
    # Get a set of English words from the "web2" word list (lowercase only)
    #english_words = get_english_words_set(['web2'], lower=True)
    english_words=["banana","apple","super"]
    trie = build_trie(english_words)
    #print(trie)

    input_word = input("Enter a word: ").lower()
    if check_spelling(trie, input_word):
        print("The word is spelled correctly.")
    else:
        print("The word is misspelled.")


main()