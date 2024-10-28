# streamlit-rq-example

A demonstration of how to integrate Streamlit with Redis Queue (RQ) for handling long-running tasks in a distributed manner. This application shows how to implement a background job processing system with a user-friendly web interface.

## Architecture

The application consists of four main components:

- **Frontend**: A Streamlit web application that handles user input and displays results
- **Worker**: A Python RQ worker that processes background jobs
- **Redis**: Message broker and result backend for job queue management
- **Dashboard**: RQ dashboard for monitoring job queues and worker status

## Prerequisites

- Docker and Docker Compose

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/DaniilBoiko/streamlit-rq-example.git
cd streamlit-rq-example
```

2. Start the application:
```bash
docker compose up --build
```

This will start all services:
- Streamlit frontend: http://localhost:8501
- RQ Dashboard: http://localhost:9181
- Redis: localhost:6379 (internal use)

## Project Structure

```
.
├── docker-compose.yml       # Docker Compose configuration
├── frontend/                # Streamlit frontend application
│   ├── Dockerfile
│   ├── app.py               # Main Streamlit application
│   ├── pages/
│   │   ├── 1_Submit.py      # Search submission page
│   │   └── 2_Results.py     # Results display page
│   └── requirements.txt
└── worker/                  # RQ worker
    ├── Dockerfile
    └── worker.py            # Worker implementation
```

## How It Works

1. Users enter a param string in the web interface
2. The frontend submits the job to Redis Queue
3. A worker picks up the job and processes it
4. The frontend polls for job status and displays results when complete

## Component Details

### Frontend (Streamlit)
- Built with Streamlit for interactive web interface
- Handles job submission and result display
- Implements real-time status updates

### Worker
- Processes background jobs using RQ
- Updates job status throughout processing
- Demonstrates task progress tracking

### Redis Queue
- Manages job queue and state
- Enables communication between frontend and workers
- Provides job status persistence

### RQ Dashboard
- Provides visual monitoring of queues
- Shows active, failed, and completed jobs
- Useful for debugging and monitoring
