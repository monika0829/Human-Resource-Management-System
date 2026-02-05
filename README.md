🧑‍💼 HRMS Lite – Employee & Attendance Management System

HRMS Lite is a full-stack HR management application built using FastAPI (Backend) and React (Frontend).
It allows organizations to manage employees and track daily attendance through a clean, production-ready UI.

🚀 Features
✅ Employee Management

Add new employees

View employee list

Delete employees

Prevent duplicate employee ID or email

✅ Attendance Management

Mark attendance (Present / Absent)

Automatically records attendance for the current day

Prevents duplicate attendance for the same employee on the same day

View attendance records with employee names

✅ Dashboard

Total Employees count

Present Today count

(Extendable for Absent Today & analytics)

✅ Reports & Summary

Display Total Present Days per Employee

Live UI updates (no refresh required)

🛠️ Tech Stack
Backend

FastAPI

PostgreSQL

SQLAlchemy

Pydantic

Frontend

React (Vite)

Axios

CSS (Custom Layout)

📂 Project Structure
hrms-lite/
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   │   ├── employees.py
│   │   │   └── attendance.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   └── database.py
│   └── main.py
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Employees.jsx
│   │   │   └── Attendance.jsx
│   │   ├── components/
│   │   │   ├── EmployeeForm.jsx
│   │   │   ├── EmployeeTable.jsx
│   │   │   └── AttendanceForm.jsx
│   │   ├── api/api.js
│   │   └── styles/layout.css
│
└── README.md

⚙️ Backend Setup
1️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

2️⃣ Install Dependencies
pip install fastapi uvicorn sqlalchemy psycopg2 pydantic

3️⃣ Run Backend Server
uvicorn app.main:app --reload


Backend runs at:

http://127.0.0.1:8000


Swagger Docs:

http://127.0.0.1:8000/docs

💻 Frontend Setup
1️⃣ Install Dependencies
npm install

2️⃣ Run Frontend
npm run dev


Frontend runs at:

http://localhost:5173

🔗 API Endpoints
Employees
Method	Endpoint	Description
GET	/employees/	Get all employees
POST	/employees/	Add employee
DELETE	/employees/{id}	Delete employee
Attendance
Method	Endpoint	Description
POST	/attendance/mark	Mark attendance
GET	/attendance/	List attendance
🎨 UI Highlights

Professional navbar (full width)

Responsive layout

Status badges (Present = 🟢 Green, Absent = 🔴 Red)

Clean cards and tables

Real-time updates without page refresh

❌ Out of Scope (As Per Assignment)

Leave Management

Payroll System

Advanced HR analytics

Role-based authentication

📌 Future Enhancements

Attendance filtering by date

Attendance percentage per employee

Export reports (CSV / PDF)

Monthly attendance calendar

👤 Author

Developed by:
MONIKA MAURYA
(HRMS Lite – Assignment Project)# Human-Resource-Management-System
Human Resource Management System
