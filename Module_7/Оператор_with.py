class WordsFinder:
    def __init__(self, *files) -> None:
        self.file_names = list(files)

    def __clean_line(self, line: str) -> list[str]:
        clean_line: str = line
        for symbol in [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']:
            clean_line = clean_line.replace(symbol, '')
        word_list: list[str] = clean_line.casefold().split(' ')
        while word_list.count('') != 0:
            word_list.remove('')
        return word_list

    def get_all_words(self) -> dict[str, list[str]]:
        all_words_dict: dict[str, list[str]] = {}
        for file_name in self.file_names:
            word_list: list[str] = []
            with open(file_name, 'r') as file:
                for line in file.readlines():
                    word_list.extend(self.__clean_line(line))
            all_words_dict[file_name] = word_list
        return all_words_dict
    
    def find(self, word: str) -> dict[str, int]:
        file_to_words: dict[str, int] = {}
        all_words: dict[str, list[str]] = self.get_all_words()
        for file, word_list in all_words.items():
            word_index: int = word_list.index(word.casefold())
            if word_index != -1:
                file_to_words[file] = word_index +1
        return file_to_words

    def count(self, word: str) -> dict[str, int]:
        file_to_words: dict[str, int] = {}
        all_words: dict[str, list[str]] = self.get_all_words()
        for file, word_list in all_words.items():
            word_count: int = word_list.count(word.casefold())
            if word_count != -1:
                file_to_words[file] = word_count
        return file_to_words



def main():
    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                          'Rudyard Kipling - If.txt',
                          'Mother Goose - Monday’s Child.txt')
    print(finder1.get_all_words())
    print(finder1.find('the'))
    print(finder1.count('the'))


if __name__ == "__main__":
    main()
