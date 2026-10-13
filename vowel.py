f=open("vowel.txt","r")
content=f.read()
count=0
for ch in content:
    if ch.lower() in "aeiou":
        count+=1
print("Total vowels:",count)
f.close()

     