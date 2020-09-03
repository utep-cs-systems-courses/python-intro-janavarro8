def main():
    inputFile = "declaration.txt"
    outputFile = "myOutput.txt"
    dict = {}
    wordList = []

    fillDict(inputFile, dict, wordList)

    wordList = sorted(wordList, reverse=True)

    writeToFile(outputFile, dict, wordList)




def fillDict(fileName, dict, wordList):
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
                        wordList.append(line[i])
                        dict[line[i]] = 1
    except IndexError:
        pass

def writeToFile(outputFile, dict, wordList):
    #file = open(outputFile, 'w')
    with open(outputFile, 'w') as file:
        for i in range(len(wordList)):
            file.write("%s %d\n" % (wordList[i], dict[wordList[i]]))




main()