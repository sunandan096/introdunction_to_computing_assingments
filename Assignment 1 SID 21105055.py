#Assignment-1
#Answer 1
print('Answer 1')
#Taking Input of three numbers from the user 
Num1= float(input("Enter the first number = "))
Num2= float(input("Enter the second number = "))
Num3= float(input("Enter the third number = "))
sum= Num1+Num2+Num3 #Sum of three numbers
Average = sum/3 #Defining Average of Three Number
print("The Average Value Of the numbers is = ")
print(Average)




#Answer 2
print("Answer 2")
#To Calculate the Income Tax
income = float(input("Enter Your Gross Income = "))
standard_deduction = 10000
flat_tax_rate = 0.20
dependent_deduction = 3000
dependents = int(input("Enter the number of non earning family members = "))
taxable_income = income-standard_deduction-(dependent_deduction*dependents)
print("Your Taxable income is = ",taxable_income)
tax=taxable_income*flat_tax_rate
if tax<0:
 print("You Don't have to pay any Income Tax.")
else:
 print("Your Final Income Tax is = ",tax)






#Answer 3
print("Answer 3")
#Taking Input From User
SID = int(input("Enter Your SID = "))
Name= input("Enter Your Name = ")
Gender= input("Enter Gender Use (\'M' \'F' \'U') = ")
Course_Name=input("Enter Course Name = ")
CGPA = float(input("Enter Your CGPA = "))
Student = [SID,Name,Gender,Course_Name,CGPA]#Student here is defined as list
print("Your Values Are Given as = "  )
print(Student) 





#Answer 4
print("Answer 4")
#Taking input from student of their marks
std1= int(input("Marks Of Student 1 = "))
std2= int(input("Marks Of Student 2 = "))
std3= int(input("Marks Of Student 3 = "))
std4= int(input("Marks Of Student 4 = "))
std5= int(input("Marks Of Student 5 = "))
Marks =[std1,std2,std3,std4,std5]#Making the list of marks obtained by students
print("Marks of student before Sorting =",end="")
print(Marks)
Marks.sort()
print("Marks of student after Sorting =",end="")
print(Marks)




#Answer 5
print("Answer 5")
Color= ['Red','Green','White','Black','Pink','Yellow']#Making List of Different Colors
print("Colors are = ",Color)
#Answer 5(a)
Color.pop(3)#Removing 4th element from the list of colors
print("Colors after removing 4th element = ",Color)
Color= ['Red','Green','White','Black','Pink','Yellow']
Color[3:5]=["Purple"]#Replacing Black and Pink color with purple in a single line
print("Final Colors Are = ",end="")
print(Color)

