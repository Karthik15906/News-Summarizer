# AI News Summarizer

An AI-powered news summarization application built using FastAPI, NewsAPI, Gemini, and a simple HTML/CSS/JavaScript frontend.

The application fetches the latest news articles based on a user-provided topic and generates a concise executive summary using Google's Gemini model.

## Features

- Search news by topic
- Fetch latest news articles using NewsAPI
- Generate AI-powered summaries using Gemini
- FastAPI backend with asynchronous requests
- Interactive frontend built with HTML, CSS, and JavaScript
- Loading animation during summary generation
- Error handling for API failures and invalid requests

## Tech Stack

### Backend

- Python
- FastAPI
- HTTPX
- Python Dotenv
- Google Gemini API

### Frontend

- HTML
- CSS
- JavaScript

### APIs

- NewsAPI
- Gemini API

## Project Structure

```text
News-Summarizer/
│
├── app/
│   ├── main.py
│   │
│   ├── services/
│   │   ├── news_service.py
│   │   └── gemini_service.py
│   │
│   └── schemas/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .env
├── README.md
└── pyproject.toml
```

## How It Works

```text
User Input
     ↓
Frontend (HTML/CSS/JS)
     ↓
FastAPI Backend
     ↓
NewsAPI
     ↓
Latest News Headlines
     ↓
Gemini
     ↓
Executive Summary
     ↓
Frontend Display
```

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/news-summarizer.git
cd news-summarizer
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
uv sync
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
News_api_key=YOUR_NEWS_API_KEY
Gemini_api_key=YOUR_GEMINI_API_KEY
```

## Running the Application

Start FastAPI:

```bash
uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

Launch the frontend using VS Code Live Server or any static server.

## Example

Input:

```text
Quantum Computing
```

Output:

```text
Global advancements in quantum computing continue to accelerate...
```

## Concepts Learned

This project helped me learn:

- FastAPI fundamentals
- REST APIs
- Async and Await
- HTTP Requests with HTTPX
- Environment Variables
- API Integration
- Prompt Engineering
- Frontend and Backend Communication
- DOM Manipulation
- Fetch API
- CORS Handling
- Error Handling

## Future Improvements

- Search history
- User authentication
- Local LLM support with Ollama
- Vector database integration
- RAG-based news assistant
- Deployment with Docker
- Better UI/UX

## Author

Karthik Chukka

Computer Science Undergraduate | Aspiring AI/ML Engineer
