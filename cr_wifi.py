
words = "1234567890qwertyuiopasdfghjklzxcvbnm"

r = its.product(words,repeat=8)

dic = open(r"C:\Users\water\Desktop\mi.txt","a")

for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))
    print(i)
dic.close()
print("密码本已经生成")