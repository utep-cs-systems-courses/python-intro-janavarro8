def main():
    inputFile = "declaration.txt"
    outputFile = ""
    dict = {}

    fillDict(inputFile, dict)
    dict = sorted(dict, reverse=True)
    print(dict)


def fillDict(fileName, dict):
    try:
        with open(fileName, 'r') as file:
            for item in file:
                item = item.replace("\n", " ")
                item = item.replace("; ", " ")
                item = item.replace(". ", " ")
                item = item.replace(", ", " ")
                item = item.replace(": ", " ")

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