from collections import Counter

with open("input.txt", "r") as file:
    input = file.read()

input = input.strip().split("\n")
input = [tuple(map(int, line.split())) for line in input]

left, right = zip(*input)

left = sorted(left)
right = sorted(right)
right_counter = Counter(right)

similarity_scores = []
for i in range(len(left)):
    count = right_counter[left[i]]
    if count > 0:
        similarity_scores.append(right_counter[left[i]] * left[i])

print(sum(similarity_scores))
