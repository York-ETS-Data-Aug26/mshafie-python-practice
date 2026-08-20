 #1
print ("##################")
name = input("Enter your name : ")
print ("Hello ,", name)
print ("##################")

#2
var1 = int (input( "The first number is : "))
var2 = int (input("The second number is :  "))
print ("The sum is " , (var1 + var2))
print ("The diff is " ,    var1 - var2 )
print ("The product is " , (var1 * var2))
print ("The quotient is " , (var1 / var2))

print ("##################")

#3

width = float ((input("Enter the width of the rectangle : ")))
height = float ((input ("Enter the height of the rectangle: ")))
print  ("The Area of the rectangle is : " , (width * height))
print   ("The perimeter is : " , 2 * (width + height))

print ("##################")

#4
Temp_in_C = 25
Temp_in_F = (Temp_in_C *(9/5)) +32
print ("The temp inn Fahrenheit is : " , Temp_in_F)

print ("##################")

#5
num = int (input("Enter your nnumber : "))
print (num * 2)

print ("##################")

#6
num1 = int (input("Enter your first number : "))
num2 = int (input("Enter your second number :  "))
avg =  (num1 + num2 )/2
print (" The avg of your two numbers is : " , avg)

print ("##################")

#7
price = 19.99
tax_rate = 8/100
total_cost = price + (price * tax_rate)
print (" The total cost is  : " , round (total_cost,2) )

print ("##################")

#8
sentence = " The sky is blue "
print  (" All uppercase : " , sentence.upper())
print   (" All Lower :  " , sentence.lower())
print  (" Total Character : " , len (sentence))

print ("##################")

#9
first_name = input ("Enter your first name : ")
last_name = input (" Enter your last name :  ")
print ( first_name  + " " + last_name)

print ("##################")

#10
num_of_min = int (input ("Enter the total no.of minutes : "))
hours = num_of_min // 60
leftover_min = num_of_min % 60
print ( hours ,"hours" , leftover_min , " minutes ")

print ("##################")


