def charCount(string):
    print("string from file :", string)
    freq = [None] * len(string)
    print(type(freq))
    for i in range(0, len(string)):
        freq[i] = 1
        for j in range(i + 1, len(string)):
            if (string[i] == string[j]):
                freq[i] += 1
                string = string[: j] + '0' + string[j + 1:]
        print("string after iteration ",i,string)
    print("after iteration string is :",string)
    print("list is ",freq)
    print("Characters and their frequencies")
    print("--------------------------------")
    for i in range(0, len(freq)):
        if (string[i] != ' ' and string[i] != '0'):
            print(string[i] + "-> " + str(freq[i]))


# opening a file and reading the content
documentText = open('data', 'r')
string = documentText.read().lower()
charCount(string)