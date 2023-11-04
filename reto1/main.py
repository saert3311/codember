def readFile(filename: str) -> str:
    file = open(filename, "r")
    data = file.read()
    clean_data=data.replace('\n', '')
    file.close()
    return clean_data

def processLines(raw_lines: str) -> dict:
    result = {}
    word_list = list(raw_lines.split(' '))
    for word in word_list:
        if word in result.keys():
            result[word] += 1
        else:
            result[word] = 1
    return result

def decodeDict(word_dict: dict) -> str:
    result = ''
    for key, value in word_dict.items():
        result = result + f'{key}{value}'
    return result    

def main() -> None:
    lines = readFile('message_01.txt')
    grouped_words =  processLines(lines)
    print(decodeDict(grouped_words))

if __name__ == '__main__':
    main()