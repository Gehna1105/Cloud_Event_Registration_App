# 🎓 College Event Registration System

## 📌 Project Overview

This project is a web-based College Event Registration System that allows students to register for various events. The application provides a user-friendly interface for submitting registration details and viewing all registrations.

The project demonstrates both a **local prototype** and a **cloud-deployed application**, along with a **cloud-ready architecture for Google Cloud Platform (GCP)**.

---

## 🚀 Features

* 🎨 Attractive pastel-themed user interface
* 📝 Student registration form
* 📋 View all registrations page
* 🗂️ Multiple input fields (Name, Department, Batch, KU ID, Enrollment Number)
* 🌐 Publicly accessible web application

---

## 🛠️ Technologies Used

### Frontend

* HTML
* CSS (Pastel UI design)

### Backend

* Python (Flask)

### Database

* SQLite (local database for prototype and deployment)

### Deployment

* Cloud platform: Render

### Cloud-Ready Configuration

* Docker
* Google Cloud Build
* Google Cloud Run (proposed)

---

## 💻 Local Setup Instructions

### Step 1: Clone the repository

```
git clone <your-repo-link>
cd Local-App
```

### Step 2: Install dependencies

```
pip install -r requirements.txt
```

### Step 3: Run the application

```
python app.py
```

### Step 4: Open in browser

```
http://127.0.0.1:5000
```

---

## ☁️ Live Deployment

The application is deployed on Render and is publicly accessible.

🔗 **Live URL:**
https://cloud-event-registration-app-gehna7.onrender.com

---

## 🧱 Project Structure

```
Local-App/
│
├── app.py
├── init_db.py
├── requirements.txt
├── Dockerfile
├── cloudbuild.yaml
├── gcp_setup_guide.md
├── .gitignore
└── README.md
```

---

## ☁️ Proposed Google Cloud Architecture

Although the current deployment is on Render, the application is designed to be deployed on Google Cloud Platform using serverless technologies.

### Proposed Services:

* Google Cloud Run → for hosting the web application (serverless)
* Google Cloud Build → for building container images
* Firestore / Cloud SQL → for cloud database storage

---

## 🔄 Migration to Google Cloud (Concept)

To migrate this application to GCP:

1. Containerize the application using Dockerfile
2. Use Cloud Build to build and push the container image
3. Deploy the container to Cloud Run
4. Replace SQLite with Firestore or Cloud SQL for persistent cloud storage

---

## 📊 Cloud Concepts Demonstrated

* 🌍 Public accessibility through cloud deployment
* 📈 Scalability using serverless architecture (Cloud Run)
* 🔄 Reliability through managed cloud services
* 📦 Containerization using Docker

---

## ⚠️ Current Limitations

* SQLite database is not suitable for long-term cloud persistence
* Current deployment is not fully serverless
* Cloud database integration is proposed but not implemented

---

## 📚 Future Improvements

* Integration with Firestore or Cloud SQL
* Authentication system (login/signup)
* Admin dashboard
* Export data (CSV/Excel)

---

## 👩‍💻 Author

* Name: Gehna Upadhyay
* Course: B.Tech. CSE - DS (Hons.)
* Semester: 2nd Semester

---

## 📌 Conclusion

This project successfully demonstrates a working web application with cloud deployment and a clear migration path to Google Cloud Platform, fulfilling both functional and conceptual cloud computing requirements.
