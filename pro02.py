
nlist = []

num = input("숫자 5개를 ,로 구분하세요:")
nlist = num.split(",")
print(nlist)
sum1 =0
for no in nlist:
    sum1 += int(no)

avg = sum1/len(nlist)

print("평균은 %1.1f입니다." %avg)