print("Mahmoud")
number1=6
print(number1)
number2=3
print(number2)
sum=0	
start_list=[3,6,9]
for i in range(3):
	print(start_list[i])

	sum+=start_list[i]
for j in range(3):
	print(start_list[j]*2)

print(sum)	
import turtle
turtle.begin_fill()
turtle.goto(0,100)
turtle.goto(100,100)
turtle.goto(100,0)
turtle.goto(0,0)
turtle.end_fill()
turtle.circle(100)
turtle.mainloop()