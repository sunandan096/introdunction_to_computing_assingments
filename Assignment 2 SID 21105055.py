print("Answer 1")
statement="Python is a case sensitive language"
print("Given statement is:",statement)

# a Part
print("Length of the statement is",len(statement))

# b Part
print("Reversed statement will be printed as:",statement[::-1])

# c Part. To assign new variable to "a case sensitive"
new_string = statement[10:27]#Stroring "a case sensitive" in new string  
print("New String will be:",new_string)

# d Part
replacing =statement.replace("a case sensitive","object oriented")
print("After Replacing [a case sensitive] with [object oriented] the final output is:",replacing)

# e part
a_index = statement.find("a")
print("The index of substring a in the given string is:",a_index)

# d Part
final_result= statement.replace(" ","")#Replacing the blank space with no element
print("The statement after removing space is:",final_result)



print("Answer 2")

Name="Sunandan Aggarwal"
SID= 21105055
Department_name = "Electronics and Communication Engineering"
CGPA=9.9
# With the help of string formatting
print("Hey %s Here!"%Name)
print("My SID is %d"%SID)
print("I am from %s department and my CGPA is %f"%(Department_name,CGPA))



print("Answer 3")
a=56
b=10
print("a=",a,"b=",b)

# a Part
print("Performing &(and) operation will provide us:",a&b)

#b Part
print("Performing |(or) operation will give us:",a|b)

#c Part
print("Output after using ^(XOR) operator wil be:",a^b)

#d Part
print("Left shifting a with 2 will result in:",a<<2,"while Left shifting b with 2 will result in",b<<2)

#e Part
print("Right shifting a with 2 will result in:",a>>2,"while right shifting b with 4 will result in",b>>4)




print("Answer 4")
#Assigning x,y,z as input from user
x=float(input("Enter your 1st Number(X):"))
y=float(input("Enter your 2nd Number(Y):"))
z=float(input("Enter your 3rd Number(Z):"))
if x>y and x>z:
  print("X is the greatest number")
elif y>x and y>z:
  print("Y is the greatest number")
else:
  print("Z is the greatest number")
   
   
   
   
print("Answer 5")#To write a program to print yes if input contains name otherwise no. 

statement= input("Write something here:")
if "name" in statement:
  print("Yes")
else:
  print("No")
  
  
  
print("Answer 6")
#To find if triangle is possible for the length provided by the user
length1=int(input("Enter the 1st length of the triangle:"))
length2=int(input("Enter the 2nd length of the triangle:"))
length3=int(input("Enter the 3rd length of the triangle:"))
if length1+length2>length3 and length1+length3>length2 and length2+length3>length1:
  print("Yes")
else:
  print("No")