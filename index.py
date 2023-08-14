employees = [
  { "name": "John", "salary": 3000, "designation": "developer" },
  { "name": "Emma", "salary": 4000, "designation": "manager" },
  { "name": "Kelly", "salary": 3500, "designation": "tester" },
]


def maxSalary(employees):
  maximum = float("-infinity")
  max_emp = None
  for employee in employees:
    salary = employee.get("salary",0)
    if salary > maximum:
      maximum=salary
      max_emp=employee
  return max_emp
    
    
max_emp = maxSalary(employees)
print(max_emp)
  
