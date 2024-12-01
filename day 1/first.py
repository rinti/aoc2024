with open("input.txt", "r") as file:
    input = file.read()

input = input.strip().split("\n")
input = [tuple(map(int, line.split())) for line in input]

left, right = zip(*input)

left = sorted(left)
right = sorted(right)

diffs = []
for i in range(len(left)):
    diffs.append(abs(right[i] - left[i]))

print(sum(diffs))
