# Cloud-Native College Event Registration System

## Project Overview
This project is a simple and functional cloud-native web application for student registration in university events such as Tech Fest, Cultural Events, Workshops, and seminars.

The project is implemented in two parts:

1. **Working Prototype (Implemented & Deployed)**
   - Local Prototype: Flask + SQLite
   - Cloud Demo: Flask + SQLite deployed on Render
   - Purpose: Demonstrates end-to-end functionality with a public URL

2. **Proposed GCP Cloud-Native Serverless Version**
   - Backend: Google Cloud Functions (Python)
   - Database: Google Cloud Firestore
   - Frontend: HTML/CSS/JavaScript calling Cloud Function
   - Purpose: Matches faculty requirement for a serverless Google Cloud solution

---

## Features
- Student event registration through a web form
- Fields:
  - Full Name
  - Department
  - Batch
  - KU ID
  - Enrollment Number
  - Event Name
- Attractive and user-friendly UI
- Registration success confirmation
- View all registrations page (local prototype)
- Cloud-native architecture ready for future integration

---

## Tech Stack

### Local Prototype
- Python
- Flask
- SQLite

### Cloud Demo (Current Live Version)
- Flask
- SQLite
- Render (public hosting)
- GitHub

### Proposed Official Cloud-Native GCP Version
- Google Cloud Functions
- Google Cloud Firestore
- HTML/CSS/JavaScript frontend

---

## Project Structure

```text
College_Event_Registration/
│
├── README.md
├── .gitignore
│
├── local-prototype/
│   ├── app.py
│   ├── requirements.txt
│   └── registrations.db
│
├── gcp-cloud-function/
│   ├── main.py
│   ├── requirements.txt
│   └── sample_frontend.html
│
├── docs/
│   ├── architecture-diagram.txt
│   └── ppt-content.txt
