def main():
    dict = {}       #keeps track of instances
    wordList = []   #keeps track of words

    inputFile = input('Enter the name of the input file: ')
    outputFile = input('Enter the name of the output file: ')

    fillDict(inputFile, dict, wordList)

    wordList = sorted(wordList)     #sorts words in descending order

    writeToFile(outputFile, dict, wordList)




def fillDict(fileName, dict, wordList):
    try:
        with open(fileName, 'r') as file:
            for item in file:
                item = item.replace("\n", " ")      #replace to help remove punctuation
                item = item.replace("; ", " ")
                item = item.replace(".", " ")
                item = item.replace(", ", " ")
                item = item.replace(": ", " ")
                item = item.replace("-", " ")
                item = item.replace("'", " ")

                line = item.split()
                for i in range(len(line)):          #loops through each word in the line
                    line[i] = line[i].lower()       #lower for case insensitivity
                    if(line[i] in dict):            #adds 1 if word already in dict
                        dict[line[i]] += 1
                    else:                           #equal to 1 if first instance of word
                        wordList.append(line[i])
                        dict[line[i]] = 1
    except IndexError:
        pass

def writeToFile(outputFile, dict, wordList):
    with open(outputFile, 'w') as file:
        for i in range(len(wordList)):      #writes name and instances to a new file
            file.write("%s %d\n" % (wordList[i], dict[wordList[i]]))


main()