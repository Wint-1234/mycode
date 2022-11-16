import random


wordbank= ["indentation", "spaces"] 
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank.append(4)

#num = input("Pick a number between 0 and 20\n>")
num = random.randint(0, len(tlgstudents) - 1)

num = int(num)

student_name = tlgstudents[num]

print(f"{student_name} always uses {wordbank[-1]} {wordbank[1]} to indent.")
