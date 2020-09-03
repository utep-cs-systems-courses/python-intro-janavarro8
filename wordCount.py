def main():
    inputFile = "declaration.txt"
    outputFile = ""
    dict = {}

    fillDict(inputFile, dict)
    print(dict)


def fillDict(fileName, dict):
    try:
        with open(fileName, 'r') as file:
            for item in file:
                line = item.split()
                for i in range(len(line)):
                    line[i] = line[i].lower()
                    if(line[i] in dict):
                        dict[line[i]] += 1
                    else:
                        dict[line[i]] = 1
    except IndexError:
        pass




main()