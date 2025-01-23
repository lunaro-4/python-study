def custom_write(file_name: str, strings: list[str]) -> dict:
    position_to_string: dict = {}
    
    file = open(file_name, 'w')
    for i, string in enumerate(strings):
        byte_pos: int = file.tell()
        index_tuple: tuple = (i, byte_pos)
        file.write(string + '\n')
        position_to_string[index_tuple] = string
    file.close()
    return position_to_string

def main():
    info = [
            'Text for tell.',
            'Используйте кодировку utf-8.',
            'Because there are 2 languages!',
            'Спасибо!'
            ]
    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)

if __name__ == "__main__":
    main()
