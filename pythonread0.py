file1 = open('spoersmaal33.js','r',encoding="utf8")
i = 0
question = []
data = {}
list = []

for line in file1:
    if i%5 == 0:
        data = {}
        data["Q"] = line[3:].strip('\n').strip().replace('\t',' ')
    elif i%5 == 1 or i%5 == 2 or i%5 == 3:
        question.append(line.strip('\n').replace('\t',' '))
    elif i%5 == 4:
        question.append(line.strip('\n').replace('\t',' '))
        data["A"] = question
        data["R"] = ""
        question = []
        list.append(data)
        print(list)
    i += 1
file1.close()
file2 = open('spoersmaal3.txt','w')
file2.write(str(list))
file2.close()
