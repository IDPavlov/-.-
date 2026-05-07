import sys

with open(sys.argv[1], 'r') as file:
    nums = list(map(
        int,
        file.read().strip().split()
    ))

median_index = len(nums) // 2
median = sorted(nums)[median_index]

steps = 0
for n in nums:
    steps += abs(median - n)

if steps <= 20:
    print(steps)
else:
    print('20 ходов недостаточно для приведения всех элементов массива к одному числу')
