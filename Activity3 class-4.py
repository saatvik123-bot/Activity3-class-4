print("Enter Marks Obtained in 4 Subjects: ")

math=int(input("Maths :"))
english=int(input("English:"))
science=int(input("Science:"))
hindi=int(input("Hindi:"))

sum = math+english+science+hindi
print("sum of math,english,science and hindi")

perc = (sum/400)*100

print(end="Percentage Mark = ")
print(perc)