print("Occurrence of each word in a line\n")
line = input("Enter the line: ")
print(line)
words = line.split()
print(words)

from collections import Counter
word_count = Counter(words)
print(word_count)

