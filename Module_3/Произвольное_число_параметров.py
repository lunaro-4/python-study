def single_root_words(root_word: str, *other_words):
    same_words: list = []
    for word in other_words:
        casefold_word = word.casefold()
        casefold_root = root_word.casefold()
        root_in_word = casefold_word.find(casefold_root) != -1
        word_in_root = casefold_root.find(casefold_word) != -1
        if root_in_word or word_in_root:
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
