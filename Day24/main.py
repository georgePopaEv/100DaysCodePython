# file = open("my_file.txt") #I have read the file
from sys import getsizeof

# contents = file.read()
# print(contents)
# file.close()
# C:\Users\George\Desktop\python\Mail Merge Project Start\Input\Letters
names = ["George", "Alina", "Evelyn", "Ada", "Alin", "Mihai"]
lines_from_letters = []
# with open("C:\\Users\\George\\Desktop\\python\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt", mode='r') as file:
#     myline = file.readline()
#     while myline:
#         lines_from_letters.append(myline)
#         myline = file.readline()
f = open("C:\\Users\\George\\Desktop\\python\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt")
lines_from_letters = f.readlines()
# print(f"{getsizeof(lines_from_letters[0])}  vs  {len(lines_from_letters[0])}")
f.close()

for line_id in range(len(lines_from_letters)):
    print(line_id)
    for name in names:
        if line_id ==0:
            with open(f"C:\\Users\\George\\Desktop\\python\\Mail Merge Project Start\\Input\\Letters\\letters_{name}.txt",mode="w") as out:
                line_replaced = lines_from_letters[line_id].replace("[name]", name)
                out.write(line_replaced)
        else:
            with open(f"C:\\Users\\George\\Desktop\\python\\Mail Merge Project Start\\Input\\Letters\\letters_{name}.txt",mode="a") as out:
                line_replaced = lines_from_letters[line_id].replace("[name]", name)
                out.write(line_replaced)
