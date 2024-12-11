calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(word: str) -> tuple[int, str, str]:
    count_calls()
    length = len(word)
    upper = word.upper()
    lower = word.lower()
    return (length, upper, lower)


def is_contains(word: str, wordlist: list) -> bool:
    count_calls()
    word = word.casefold()
    for lookup in wordlist:
        if word == lookup.casefold():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
