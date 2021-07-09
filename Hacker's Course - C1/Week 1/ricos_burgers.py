
# total_wage = total_hours * hourly_rate
N = 5

minimum_wage = 14.25
total_hours = 0

for i in range(0, N):
    current_employee_hours = int(input("Enter your hours: "))
    total_hours += current_employee_hours

total_wage = minimum_wage * total_hours
print("$", total_wage)