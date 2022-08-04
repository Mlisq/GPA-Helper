import re

f = open("2.html")
str = f.read()
f.close()

ff = open("1.txt", mode='w')

result = re.findall(r"<tbody>(.*?)</tbody>", str, re.M.S)
for i in result:
    ff.writelines(i)
    ff.write("-------------------\n")


ff.close()




nandg = re.findall(r"<tr .*?>(.*?)</tr>",result[0],re.M.S)

for i in nandg:
    print(re.findall(r"<b>(.*?)</b>",i,re.M.S))


