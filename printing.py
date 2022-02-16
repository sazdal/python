def printing(msg):
    word=""
    i=0
    while i<len(msg):
        if msg[i]==" ":
            print(word)
        else:
            word=word+msg[i]
        i=i+1
msg=input("Enter a message")
print(printing(msg))