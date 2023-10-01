def char_count(input_data):
    print("string from file :", input_data)
    freq = [None] * len(input_data)
    print(type(freq))
    for i in range(0, len(input_data)):
        freq[i] = 1
        for j in range(i + 1, len(input_data)):
            if input_data[i] == input_data[j]:
                freq[i] += 1
                input_data = input_data[: j] + '0' + input_data[j + 1:]
        print("string after iteration ", i, input_data)
    print("after iteration string is :", input_data)
    print("list is ", freq)
    print("Characters and their frequencies")
    print("--------------------------------")
    for i in range(0, len(freq)):
        if input_data[i] != ' ' and input_data[i] != '0':
            print(input_data[i] + "-> " + str(freq[i]))


# opening a file and reading the content
documentText = open('data', 'r')
data = documentText.read().lower()
char_count(data)
