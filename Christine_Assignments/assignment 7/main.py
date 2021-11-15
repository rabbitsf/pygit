cont = True
searchList = []
while cont:
    text = input("Enter a text to analyze: ")
    searchList.append(text)
    ch = input("Do you want to enter another text?(y/n) ")
    if ch == 'n' or ch == 'N':
        cont = False
print("\n")
print(searchList)

input_text = input("Enter paragraphs for analysis: ")
paragraph = input_text.replace("\n", " ")
print(paragraph.upper())
print("\n")

for text in searchList:
    if text.upper() in paragraph.upper():
        tcount = paragraph.upper().count(text.upper())
        print(f"There are {tcount} {text}")
    else:
        print(f"{text} not found in the paragraphs")





