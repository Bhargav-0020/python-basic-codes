print([i for i in range (1,11)])
print([i**2 for i in range (1,11)])
print([i for i in range (1,51) if i%2==0])
print([i for i in range(1,51) if i%2!=0])
words=["apple","banana","cherry"]
print([word.upper() for word in words])
print([len(word) for word in words])
values=[1,2,3,4,5]
print([str(word) for word in values])
print([i**2 for i in range(1,21) if i%2==0])
nums=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
print([i for i in nums if i>=0])
text="artificial intelligence"
print([i for i in text if i in "aeiouAEIOU"])
print([i for i in range(1,101) if i%3==0 and i%5==0])
words=["hello","world","python","programming"]
print([i[0] for i in words])
data=["ai","","ml","dl"]
print([i for i in data if i!=""])
print([i[::-1] for i in words])
sound="i love you"
print([i.strip() for i in sound.split()])
