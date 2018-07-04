# a = 0
# b = []
# while True:
#     a = input()
#     if a == "":
#         break
#     else:
#         b.append([int(x) for x in a.strip().split(" ")])

# for i in b:
#     print(abs(i[0] - i[1]))

# var1, var2 = [int(x) for x in input().split(" ")]
# print(abs(var1-var2))

from sys import stdin

for line in stdin:
  a = [int(x) for x in line.strip().split(" ")]
  print(abs(a[0]-a[1]))