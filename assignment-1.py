#Section 1
name= "Batman"
age= 3
height= 2.7
is_student= False

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

#Section 2
name= input("What is your name?")
birth_year= int(input("What year were you born?"))
age= 2026 - birth_year
print("Hi, "+ name + "! You are approximately "+ str(age) + " years old.")

#Section 3
number1= float(input("Please enter the number of days in this year:"))
number2= float(input("Please enter the number of day left in this week:"))
result= number1 * number2
print(f"{number1} x {number2} = {result}")

#Section 4
item = "Batman Action Figures"
price= 52.97
quantity= 7
total= price * quantity
print("~~~~~~~~~~~~~~~~~~~~")
print("      RECEIPT       ")
print("~~~~~~~~~~~~~~~~~~~~")
print("Item:   ", item)
print(f"Price:    ${price:.2f}")
print("Quantity:  ", quantity)
print("====================")
print(f"Total:     ${total:.2f}")
print("~~~~~~~~~~~~~~~~~~~~")

#Section 5
name2= input("What is your name? ")
hometown= input("What town are you from? ")
hobby= input("What is your favorite hobby? ")
fun_fact= input("Tell me a fun fact about yourself! ")
birthday_year= int(input("What year were you born?"))
age= 2026 - birthday_year
print("╔══════════════════════════════╗")
print(f"        PROFILE: {name2}     ")
print("╚══════════════════════════════╝")
print(f"Approx. Age: {age}")
print(f"Hometown:    {hometown}")
print(f"Hobby:       {hobby}")
print(f"Fun Fact:    {fun_fact}")
