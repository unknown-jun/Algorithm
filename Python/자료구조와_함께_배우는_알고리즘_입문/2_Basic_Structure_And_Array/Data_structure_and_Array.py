#Print sum and average five of student's group

print("Calcultrate sum and average in student group's socore")

score1 = int(input("Enter No.1 student's score: "))
score2 = int(input("Enter No.2 student's score: "))
score3 = int(input("Enter No.3 student's score: "))
score4 = int(input("Enter No.4 student's score: "))
score5 = int(input("Enter No.5 student's score: "))

total=0
total += score1
total += score2
total += score3
total += score4
total += score5

print(f'Sum is {total}')
print(f'Average is {total/5}')


