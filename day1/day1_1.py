with open("day1_input.txt", "r") as f:
    x = f.read().split("\n")

nums = [str(i) for i in range(10)]
sum_list = []
for i in x:
    _out = ""
    for j in i:
        if j in nums:
            _out += j
            break
    for j in reversed(i):
        if j in nums:
            _out += j
            break
    sum_list.append(int(_out))
print(sum(sum_list))