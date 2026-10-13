sentence=input("Enter a sentence:")
word=sentence.split()
longest=max(word,key=len)
print("Longest word:",longest)