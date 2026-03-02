file = open("SMSSpamCollection.txt")
spam = []
ham = []
hamWordCount = 0
spamWordCount = 0

for line in file:
    line = line.rstrip()
    if line.startswith("ham"):
        ham.append(line)
        hamWordCount += len(line.split()) - 1
    else:
        spam.append(line)
        spamWordCount += len(line.split()) - 1
file.close()
print("Average ham word count",hamWordCount/len(ham))
print("Average spam word count",spamWordCount/len(spam))

questionMarkCounter = 0
for line in spam:
    if line.endswith("?"):
        questionMarkCounter+=1

print("Ends with ?",questionMarkCounter)