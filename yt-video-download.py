import pytube
link = input("link: ")
yt = pytube.YouTube(link)
yt.streams.get_highest_resolution().download()
print("Gotowe!")
