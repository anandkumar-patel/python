def wordCount(string):
    count = dict()
    words =string.split()

    for word in words:
        if word in count:
            count[word] =count[word]+1
        else:
            count[word] =1
    return count


# opening a file and reading the content
documentText = open('data','r')
textString = documentText.read().lower()
print("Distinct Words and their frequency")
print(wordCount(textString))