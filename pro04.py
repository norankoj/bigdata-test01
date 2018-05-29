
s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

list = s.upper()
list = list.split()
list[6] = list[6][:6]
list[18] = list[18][:5]
list[33] = list[33][:7]
nlist = set([])

# 중복제거 결과
for i in list:
    count = list.count(i)
    nlist.add(i+":%d" %count)

# 셋-->리스트 변환
Llist=[]
for n in nlist:
    Llist.append(n)

# 오름차순 출력
Llist.sort()
for L in Llist:
    print(L)


























