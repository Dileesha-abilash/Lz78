
# "amthisththisinnerthin"
string = input("input the string")
# removing space 😅
string = string.replace(" ", "")

dic = []
index = []
out = []
out_number = []
i = 1

last =[]
checker = string[i]
dic.append(string[0])


while i < len(string):
    while True:

        if checker not in dic:
            dic.append(checker)
            i = i + 1
            if i < len(string):
                checker = string[i]
            break
        else:
            i = i + 1
            checker = checker + string[i]

for i in dic:
    out.append(i[-1])

for i in dic:
    if len(i)> 1:
        last.append(i[:len(i)-1])
    else:
        last.append(None)

for i in last:
    if i == None:
        out_number.append(0)
    else:
        
            if i in dic:
                out_number.append(dic.index(i))


with open("out.txt_index","w")as out_index:
    for i in out_number:
        out_index.write(str(i))

with open("out_text.txt","w")as out_character:
    for i in out:
        out_character.write(str(i))

