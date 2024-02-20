marks = [1,2,3,4,5,90809,32487]

print(marks)
print(marks[0])
print(marks[-1])
print(marks[1:4])

for score in marks:
    print(score)

marks.append(478)
marks.insert(1,213)
print(marks)
print(len(marks))

i = 0
while i < len(marks):
    print(marks[i])
    i = i+1

print(marks)
marks.clear()
print(marks)