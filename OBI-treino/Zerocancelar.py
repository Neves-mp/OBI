nums = []
N = int(input())
for i in range(N):
    num = int(input())
    if num != 0:
        nums.append(num)
    elif num == 0:
        nums.pop()
print(sum(nums))
