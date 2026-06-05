# AI Interview Platform

> AI-powered mock interview platform built with FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication, and OpenAI.

---

# Table of Contents

- Overview
- Problem
- Solution
- Features
- System Architecture
- Request Flow
- Database Design
- Authentication Flow
- SQLAlchemy Design
- API Endpoints
- Project Structure
- Environment Variables
- Getting Started
- Future Roadmap
- What I Learned

---

# Overview

AI Interview Platform helps students and job seekers practice technical and behavioral interviews.

The system generates interview questions, records answers, evaluates responses using AI, and provides detailed feedback reports.

The goal is to simulate a real interview experience while giving users actionable feedback.

---

# Problem

Most students prepare DSA and theory but rarely practice actual interviews.

Common issues:

- No realistic interview environment
- Lack of feedback
- Expensive mock interviews
- Poor communication skills
- No performance tracking

---

# Solution

This platform acts as an AI interviewer.

It can:

- Generate interview questions
- Conduct interview sessions
- Evaluate answers
- Track performance
- Suggest improvements

---

# Features

## Authentication

- Registration
- Login
- JWT Access Tokens
- Password Hashing
- Protected Routes

## Interview Engine

- AI Generated Questions
- Technical Interviews
- Behavioral Interviews
- Session Tracking

## Feedback System

- Technical Score
- Communication Score
- Strengths
- Weaknesses
- Suggestions

## Dashboard

- Interview History
- Performance Analytics
- Feedback Reports

---

# System Architecture

```text
User
 │
 ▼
React Frontend
 │
 ▼
FastAPI Backend
 │
 ├── JWT Authentication
 ├── Interview Service
 ├── Feedback Service
 │
 ▼
PostgreSQL Database
 │
 ▼
OpenAI API
```
---

# Request Flow

## Registration

User → FastAPI → Hash Password → PostgreSQL

## Login

User → FastAPI → Verify Password → Generate JWT

## Interview

User → Create Session → Generate Questions → Submit Answers → AI Evaluation

---

# Database Design

## User

| Field | Type |
|---------|---------|
| id | UUID |
| name | String |
| email | String |
| hashed_password | String |
| created_at | DateTime |

Relationship:

One User → Many Interview Sessions

## Interview Session

| Field | Type |
|---------|---------|
| id | UUID |
| user_id | UUID |
| interview_type | String |
| started_at | DateTime |
| completed_at | DateTime |

## Question

| Field | Type |
|---------|---------|
| id | UUID |
| session_id | UUID |
| question | Text |
| answer | Text |
| score | Integer |

## Feedback

| Field | Type |
|---------|---------|
| id | UUID |
| session_id | UUID |
| strengths | Text |
| weaknesses | Text |
| suggestions | Text |
| overall_score | Integer |

---

# Authentication Flow

1. User registers.
2. Password hashed with bcrypt.
3. Data stored in PostgreSQL.
4. User logs in.
5. JWT token generated.
6. Protected routes verify JWT.
7. Access granted.

---

# Why SQLAlchemy

SQLAlchemy is an ORM.

Instead of writing:

```sql
SELECT * FROM users;
```

You write:

```python
db.query(User).all()
```

Benefits:

- Cleaner code
- Relationships
- Type safety
- Easier maintenance
- Database abstraction

---

# API Endpoints

## Auth

POST /auth/register

POST /auth/login

GET /auth/me

## Interviews

POST /interview/start

POST /interview/{id}/answer

POST /interview/{id}/finish

GET /interview/{id}

## Feedback

GET /feedback/{session_id}

GET /feedback/history

---

# Project Structure

```text
backend/
│
├── auth/
│   ├── models.py
│   ├── schemas.py
│   ├── service.py
│   ├── security.py
│   └── router.py
│
├── interview/
│   ├── models.py
│   ├── schemas.py
│   ├── service.py
│   └── router.py
│
├── feedback/
│   ├── service.py
│   └── router.py
│
├── database.py
├── dependencies.py
└── main.py
```

---

# Environment Variables

```env
DATABASE_URL=postgresql://user:password@localhost/interview_db

SECRET_KEY=super_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

OPENAI_API_KEY=your_key
```

---

# Getting Started

```bash
git clone <repo>

cd backend

python -m venv venv

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

# Future Roadmap

## Phase 1

- Registration
- Login
- JWT

## Phase 2

- Interview Sessions
- Question Storage

## Phase 3

- AI Evaluation
- Analytics

## Phase 4

- Voice Interviews
- Video Interviews

## Phase 5

- Resume Analysis
- Company Specific Interviews

---

# What I Learned

This project demonstrates:

- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT Authentication
- Password Hashing
- API Design
- AI Integration
- Backend Architecture

---

# License

MIT
