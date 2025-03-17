# text = input("Enter a string: ")
# print(f"The text is {len(text)} characters")

# text = input("Enter a string: ")
# text = text.replace(" ","")
# print(f"The text has {len(text)} characters")


array = []
z = 0
while z < 5:
    text = input("Enter a text: ").replace(" ", "")
    array.append(f"{text} => {len(text)}")
    z += 1
print(array) 
