# 🧑‍💼 MongoDB Employees & Departments – Manual Join Example

This project demonstrates how to simulate a relational structure in MongoDB using two collections: `employees` and `departments`. It shows how to insert sample data and perform a manual LEFT JOIN in Python using `pymongo`.

MongoDB does not support traditional SQL-style joins, but we can achieve similar results by referencing `ObjectId`s and querying related documents manually.

## 🔧 Technologies Used

- 🐍 Python 3.x  
- 🗃️ MongoDB (local instance)  
- 📦 pymongo (`pip install pymongo`)

## 🗂️ Project Structure

- `main.py` – Contains all logic: connection, data insertion, and manual join
- No schema definition required (MongoDB is schema-less)

## 📥 Data Model

### Departments Collection
```json
{
  "_id": ObjectId,
  "name": "HR"
}
```

### Employees Collection
```json
{
  "_id": ObjectId,
  "name": "Alice",
  "department_id": ObjectId  // optional
}
```

## 🚀 How to Run

1. Make sure MongoDB is running locally on port `27017`
2. Install dependencies:
   ```bash
   pip install pymongo
   ```
3. Run the script:
   ```bash
   python main.py
   ```

## 📌 What the Script Does

- Connects to MongoDB and creates a database `company_db`
- Inserts sample departments and employees
- Simulates a LEFT JOIN: for each employee, fetches the department name (if available)
- Prints all employees with their department or `"No department"` if missing

## 🧠 Example Output

```
📋 Employees with department names:
- Alice → HR
- Bob → IT
- Charlie → No department
```

## 📝 Author

**Adrian** – Exploring data modeling in MongoDB with Python.
```



If you'd like to expand this into a more advanced project — maybe using `$lookup` aggregation or building a small API — I’d be happy to help you take it further.
