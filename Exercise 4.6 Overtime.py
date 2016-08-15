hours_worked = float(input ("Enter number of hours worked:"))
hourly_rate = float(input ("Enter hourly rate:"))
compute = hours_worked * hourly_rate

overtime = hours_worked - 40
overtime_rate = 1.5*hourly_rate

Total = overtime * overtime_rate + 40*hourly_rate

if hours_worked <= 40:
	print ('You worked' + str(hours_worked) + 'and your pay is' + str(compute))
	#print("You worked", hours_worked, "and your pay is", compute)
	#No need to cast strings all the time
else:
	print ('You worked' + str(hours_worked) + 'and your pay is' + str(Total))