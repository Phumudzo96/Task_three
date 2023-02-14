#Ask user to enter times for the three trianthlon event
swimming = int(input("Enter the time for swimming: "))
cycling = int(input("Enter the time for cycling: "))
running = int(input("Enter the time for running: "))

#Create a variable that will calculate the times of the trianthlon event
triathlon = swimming + cycling + running

#determine where the user falls for the awards after calculating the times
if triathlon <= 100:
    print("Provincial colours")
elif (triathlon > 100) and (triathlon <= 105):
    print("Provincial  half colours")
elif (triathlon > 105) and (triathlon <= 110):
    print("Provincial scroll")
else:
    print("No award")