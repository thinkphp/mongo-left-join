from pymongo import MongoClient
from bson.objectid import ObjectId

# 1. Conectare la MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["company_db"]

departments = db["departments"]
employees = db["employees"]

# 2. Curățare colecții (doar pentru test)
departments.delete_many({})
employees.delete_many({})

# 3. Inserare departamente
hr_id = departments.insert_one({"name": "HR"}).inserted_id
it_id = departments.insert_one({"name": "IT"}).inserted_id

# 4. Inserare angajați (cu și fără departament)
employees.insert_many([
    {"name": "Alice", "department_id": hr_id},
    {"name": "Bob", "department_id": it_id},
    {"name": "Charlie"}  # fără departament
])

# 5. LEFT JOIN manual: angajați + departamente
print("\n📋 Employees with department names:")
for emp in employees.find():
    dept_name = "No department"
    if "department_id" in emp:
        dept = departments.find_one({"_id": emp["department_id"]})
        if dept:
            dept_name = dept["name"]
    print(f"- {emp['name']} → {dept_name}")

