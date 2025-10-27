#Roger Blake
#Find fbi in multiple lines of text and print which line it is on.
text = []
for i in range(5):
    lines = input()
    text.append(lines)

def fbi(text):
    fbis = []
    for here in range(len(text)):
        if "fbi" in text[here].lower():
            fbis.append(here + 1)
            
    if fbis:
        for line in fbis:
            print(line)
    else:
        print("He got away!")

fbi(text)