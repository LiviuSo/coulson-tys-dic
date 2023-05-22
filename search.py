ALPHABET = ['a', 'ā', 'i', 'ī', 'u', 'ū', 'ṛ', 'ṝ', 'ḷ', 'ḹ', 'e', 'ai', 'o', 'au', 'ṃ', 'ḥ', 'k', 'kh',
            'g', 'gh', 'ṅ', 'c', 'ch', 'j', 'jh', 'ñ', 'ṭ', 'ṭh', 'ḍ', 'ḍh', 'ṇ', 't', 'th', 'd', 'dh', 'n', 'p', 'ph',
            'b', 'bh', 'm', 'y', 'r', 'l', 'v', 'ś', 'ṣ', 's', 'h']


def index_of(letter):
    try:
        index_of_letter = ALPHABET.index(letter)
    except ValueError:
        index_of_letter = 9999
    return index_of_letter


def separate_in_letters(word):
    word_len = len(word)
    letters = []
    li = 0
    while li < word_len:
        letter = word[li]
        if letter == 'a':
            if li < word_len - 1 and word[li + 1] in ['i', 'u']:
                letters.append(f"a{word[li + 1]}")
                li = li + 1
            else:
                letters.append(word[li])
        elif letter in ['k', 'g', 'c', 'j', 'ṭ', 'ḍ', 't', 'd', 'p', 'b']:
            if li < word_len - 1 and word[li + 1] == 'h':
                letters.append(f"{letter}h")
                li = li + 1
            else:
                letters.append(word[li])
        else:
            letters.append(word[li])
        li = li + 1
    return letters


# todo override operator
def less_than_or_equal(word1, word2):
    letters1 = separate_in_letters(word1)
    letters2 = separate_in_letters(word2)

    len1 = len(letters1)
    len2 = len(letters2)
    no_of_letters = min(len1, len2)

    il = 0
    while il < no_of_letters:
        ind1 = index_of(letters1[il])
        ind2 = index_of(letters2[il])
        if ind1 > ind2:
            return False
        elif ind1 < ind2:
            return True
        il = il + 1

    # the part of common length is equal
    if len1 <= len2:
        return True
    elif len1 > len2:
        return False


def is_in_range(string, lower_bound, upper_bound):
    if string == "":
        return False

    word = string.lower()
    in_range = less_than_or_equal(lower_bound, word) and less_than_or_equal(word, upper_bound)
    return in_range


def get_index_as_string(i):
    string = ""
    if 1 <= i <= 9:
        string = f"00{i}"
    elif 10 <= i <= 99:
        string = f"0{i}"
    else:
        string = f"{i}"
    return string
