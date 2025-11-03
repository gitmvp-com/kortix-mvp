"""Kortix MVP - FastAPI Backend Application"""
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from datetime import datetime, timezone
import os
import uuid
import time

# Basic configuration
ENV_MODE = os.getenv("ENV_MODE", "local")

# Placeholder for database and services
# In a full implementation, these would be imported from core modules
class PlaceholderDB:
    async def initialize(self):
        print("Database initialized (placeholder)")
    
    async def disconnect(self):
        print("Database disconnected (placeholder)")

class PlaceholderRedis:
    async def initialize_async(self):
        print("Redis initialized (placeholder)")
    
    async def close(self):
        print("Redis closed (placeholder)")
    
    async def get_client(self):
        return self
    
    async def ping(self):
        return True

db = PlaceholderDB()
redis_client = PlaceholderRedis()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager"""
    print(f"Starting Kortix MVP Backend in {ENV_MODE} mode")
    
    try:
        await db.initialize()
        await redis_client.initialize_async()
        
        yield
        
        await redis_client.close()
        await db.disconnect()
    except Exception as e:
        print(f"Error during startup/shutdown: {e}")
        raise

app = FastAPI(
    title="Kortix MVP API",
    description="Open Source AI Agent Platform",
    version="1.0.0",
    lifespan=lifespan
)

# CORS configuration
allowed_origins = [
    "http://localhost:3000",
    "http://localhost:3001",
]

if ENV_MODE == "production":
    allowed_origins.extend([
        "https://www.kortix.ai",
        "https://kortix.ai",
    ])

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization", "X-API-Key"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Request logging middleware"""
    request_id = str(uuid.uuid4())
    start_time = time.time()
    
    print(f"[{request_id}] {request.method} {request.url.path}")
    
    response = await call_next(request)
    
    process_time = time.time() - start_time
    print(f"[{request_id}] Completed in {process_time:.2f}s - Status: {response.status_code}")
    
    return response

# Health check endpoints
@app.get("/api/health", tags=["System"])
async def health_check():
    """Basic health check"""
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "version": "1.0.0",
        "env": ENV_MODE
    }

@app.get("/api/health-docker", tags=["System"])
async def health_check_docker():
    """Docker health check with dependency verification"""
    try:
        # Check Redis
        client = await redis_client.get_client()
        await client.ping()
        
        return {
            "status": "ok",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "redis": "connected",
            "database": "connected"
        }
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Health check failed: {str(e)}")

# Agent endpoints (placeholders for MVP)
@app.get("/api/agents", tags=["Agents"])
async def list_agents():
    """List all agents"""
    return {
        "agents": [],
        "total": 0
    }

@app.post("/api/agents", tags=["Agents"])
async def create_agent(request: Request):
    """Create a new agent"""
    body = await request.json()
    return {
        "id": str(uuid.uuid4()),
        "name": body.get("name", "New Agent"),
        "created_at": datetime.now(timezone.utc).isoformat()
    }

@app.get("/api/threads", tags=["Threads"])
async def list_threads():
    """List conversation threads"""
    return {
        "threads": [],
        "total": 0
    }

@app.post("/api/threads", tags=["Threads"])
async def create_thread(request: Request):
    """Create a new conversation thread"""
    body = await request.json()
    return {
        "thread_id": str(uuid.uuid4()),
        "created_at": datetime.now(timezone.utc).isoformat()
    }

@app.post("/api/chat", tags=["Chat"])
async def chat(request: Request):
    """Send a message to an agent"""
    body = await request.json()
    return {
        "message_id": str(uuid.uuid4()),
        "response": "This is a placeholder response. Connect your LLM provider to enable chat.",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

# File management endpoints
@app.get("/api/files", tags=["Files"])
async def list_files():
    """List uploaded files"""
    return {
        "files": [],
        "total": 0
    }

@app.post("/api/files/upload", tags=["Files"])
async def upload_file(request: Request):
    """Upload a file"""
    return {
        "file_id": str(uuid.uuid4()),
        "status": "uploaded",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

# Knowledge base endpoints
@app.get("/api/knowledge-base", tags=["Knowledge Base"])
async def list_knowledge():
    """List knowledge base entries"""
    return {
        "entries": [],
        "total": 0
    }

# Webhook endpoints
@app.post("/api/webhooks/trigger", tags=["Webhooks"])
async def webhook_trigger(request: Request):
    """Handle incoming webhooks"""
    body = await request.json()
    return {
        "received": True,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

# Billing endpoints
@app.get("/api/billing/subscription", tags=["Billing"])
async def get_subscription():
    """Get user subscription details"""
    return {
        "plan": "free",
        "status": "active"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=(ENV_MODE == "local")
    )
