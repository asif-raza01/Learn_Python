name="Zeeshan"
age=32
gender="male"
is_student=True

print("hello",name,"your age is",age)
print(name,age,gender)
print(name,age,gender,sep="##")  #now this sep is by default space but we can change it to any character
#by default a single print statement takes an entire line and then moves to the next line but we can change this by using end parameter
print(name,age,gender,end=" ")  #now this end is by default new line
print(name)
print(age)
print(gender)

#F-strings
print(f"hello {name} your age is {age} and your gender is {gender}")