
# N employees
N = 5

employees_work_hours = []
for i in range(0, N):
    employee_hour = int(input("Enter your hours: "))
    employees_work_hours.append(employee_hour)

total_pay = 0
for i in range(0, N):
    total_pay += employees_work_hours[i] * 14.25

# Final product: total pay
print("Total pay: ", total_pay)