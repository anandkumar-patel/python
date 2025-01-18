import pytube
link = input("Enter Youtube video url")
yt = pytube.YouTube(link)
yt.streams.first().download()
print('Downloaded', link)
