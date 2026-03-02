file = open("song.txt")
words = []
word_count = {}
for line in file:
    line = line.rstrip()
    words.extend(line.split())
file.close()
for word in words:
    if word_count.__contains__(word):
        word_count[word]+=1
    else:
        word_count[word] = 1

total = 0
for word, count in word_count.items():
    if word_count[word] == 1:
        total+=1

print(total)