num = int(input())
len_num = len(str(num))
sum = 0

for j in range(num):
    for i in str(j):
        a = pow(int(i), len_num)
        sum = sum + a
    if sum == num:
        print("This is armstrong number ", sum)
    else:
        print("This is not an armstrong number ", num)