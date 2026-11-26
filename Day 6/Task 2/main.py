import csv
import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
print(f"API Key Loaded: {api_key is not None}")

employees = []
with open('employees.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file, fieldnames=['ID', 'Name', 'Department', 'Salary'])
    next(reader) # Header line ah skip pannidu
    for row in reader:
        clean_row = {}
        for k, v in row.items():
            if k is None:
                continue
            if isinstance(v, list):
                v = v[0] if v else ""
            if v is None:
                v = ""
            clean_row[k] = v.strip()
        if not clean_row.get('ID'):
            continue
        clean_row['Salary'] = int(clean_row['Salary'])
        clean_row['ID'] = int(clean_row['ID'])
        employees.append(clean_row)

print(f"Rows read: {len(employees)}")
high_earners = [e for e in employees if e['Salary'] > 50000]
print(f"High earners: {len(high_earners)}")

with open('employees.json', 'w') as f:
    json.dump(employees, f, indent=4)

with open('high_earners.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['ID', 'Name', 'Department', 'Salary'])
    writer.writeheader()
    writer.writerows(high_earners)

try:
    res = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
    users = res.json()
    for u in users[:3]:
        print(f"{u['id']} - {u['name']} - {u['email']}")
    saved_users = []
    for u in users:
        saved_users.append({
            "id": u.get("id"),
            "name": u.get("name"),
            "email": u.get("email"),
            "city": u.get("address", {}).get("city"),
            "company": u.get("company", {}).get("name")
        })
    with open('users.json', 'w') as f:
        json.dump(saved_users, f, indent=4)
except requests.exceptions.Timeout:
    print("Request Timed Out!")
except requests.exceptions.ConnectionError:
    print("Connection Error!")

res404 = requests.get("https://jsonplaceholder.typicode.com/users/9999", timeout=5)
if res404.status_code == 404:
    print("/users/9999 -> 404 Not found")