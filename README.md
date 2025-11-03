# Kortix MVP – Open Source Platform to Build AI Agents

![License](https://img.shields.io/badge/License-Apache--2.0-blue)

**A simplified MVP of Kortix - A complete platform for creating autonomous AI agents**

This is a minimal viable product version of Kortix (formerly Suna), demonstrating the core capabilities of building, managing, and deploying AI agents.

## 🌟 Features

This MVP includes:

- ✅ **Chat Interface** - Conversational AI with thread management
- ✅ **Multi-LLM Support** - Anthropic, OpenAI, Gemini, Groq via LiteLLM
- ✅ **Authentication** - Supabase-based user management
- ✅ **Agent Sandbox** - Daytona Docker execution environments
- ✅ **Web Intelligence** - Tavily search & Firecrawl scraping
- ✅ **File Management** - PDF, DOCX, XLSX, PPTX handling
- ✅ **Knowledge Base** - Vector storage for context
- ✅ **Background Jobs** - Redis + Dramatiq task queue
- ✅ **Integrations** - MCP, Composio, Google Workspace
- ✅ **Billing** - Stripe subscription management
- ✅ **Webhooks & Triggers** - Event-driven automation
- ✅ **Observability** - Langfuse & Sentry monitoring

## 🏗️ Architecture

```
kortix-mvp/
├── backend/          # FastAPI Python backend
├── frontend/         # Next.js React frontend
└── docker-compose.yaml
```

### Tech Stack

**Backend:**
- Python 3.11 with FastAPI
- Supabase (PostgreSQL + Auth)
- Redis for caching & queues
- Dramatiq for background jobs
- LiteLLM for unified LLM access

**Frontend:**
- Next.js 15.3.1
- React 18
- Tailwind CSS 4
- Radix UI components
- Zustand for state management

## 🚀 Quick Start

### Prerequisites

- Docker & Docker Compose
- Python 3.11+
- Node.js 22+

### 1. Clone the Repository

```bash
git clone https://github.com/gitmvp-com/kortix-mvp.git
cd kortix-mvp
```

### 2. Configure Backend

```bash
cd backend
cp .env.example .env
# Edit .env with your API keys
```

**Required Environment Variables:**

```env
# Database
SUPABASE_URL=your_supabase_url
SUPABASE_ANON_KEY=your_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key

# Redis (use defaults for docker-compose)
REDIS_HOST=redis
REDIS_PORT=6379

# At least one LLM provider
ANTHROPIC_API_KEY=your_key
# or OPENAI_API_KEY=your_key

# Search & Scraping
TAVILY_API_KEY=your_key
FIRECRAWL_API_KEY=your_key

# Agent Sandbox
DAYTONA_API_KEY=your_key
DAYTONA_SERVER_URL=https://app.daytona.io/api
```

### 3. Configure Frontend

```bash
cd ../frontend
cp .env.example .env.local
# Edit .env.local
```

```env
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_anon_key
NEXT_PUBLIC_BACKEND_URL=http://localhost:8000/api
NEXT_PUBLIC_URL=http://localhost:3000
```

### 4. Start with Docker Compose

```bash
cd ..
docker-compose up --build
```

The platform will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

### 5. Development Mode (Optional)

**Backend:**
```bash
cd backend
pip install uv
uv sync
uv run uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

**Worker (for background jobs):**
```bash
cd backend
uv run dramatiq --skip-logging --processes 2 --threads 4 run_agent_background
```

## 📁 Project Structure

### Backend (`/backend`)

```
backend/
├── core/                    # Core business logic
│   ├── agentpress/         # Agent management & threads
│   ├── services/           # External services (Redis, Supabase)
│   ├── sandbox/            # Daytona sandbox integration
│   ├── billing/            # Stripe billing
│   ├── admin/              # Admin endpoints
│   ├── mcp_module/         # MCP protocol
│   ├── credentials/        # Secure credential storage
│   ├── templates/          # Agent templates
│   ├── knowledge_base/     # Vector storage
│   ├── triggers/           # Webhooks & automation
│   ├── composio_integration/ # Composio apps
│   └── google/             # Google Workspace
├── api.py                   # FastAPI application
├── run_agent_background.py  # Dramatiq worker
├── pyproject.toml          # Python dependencies
└── Dockerfile
```

### Frontend (`/frontend`)

```
frontend/
├── src/
│   ├── app/                # Next.js app router
│   ├── components/         # React components
│   ├── lib/                # Utilities & helpers
│   └── hooks/              # Custom React hooks
├── public/                 # Static assets
├── package.json
└── Dockerfile
```

## 🔧 Configuration

### Environment Modes

Set `ENV_MODE` in backend/.env:
- `local` - Development
- `staging` - Staging environment
- `production` - Production deployment

### LLM Providers

The platform supports multiple LLM providers via LiteLLM:
- Anthropic (Claude)
- OpenAI (GPT-4, GPT-3.5)
- Google (Gemini)
- Groq
- OpenRouter
- xAI (Grok)
- AWS Bedrock
- Custom OpenAI-compatible APIs

### Database Setup

1. Create a Supabase project at https://supabase.com
2. Copy the project URL and keys to your `.env`
3. The application will handle schema initialization

### Redis Setup

For production, configure an external Redis:

```env
REDIS_HOST=your-redis-host.com
REDIS_PORT=6379
REDIS_PASSWORD=your_password
REDIS_SSL=true
```

## 📚 API Documentation

Once running, visit http://localhost:8000/docs for interactive API documentation (Swagger UI).

## 🧪 Testing

```bash
cd backend
uv run pytest
```

## 🐳 Docker Production Deployment

```bash
# Build production images
docker-compose -f docker-compose.yaml build

# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## 🔐 Security Notes

- Never commit `.env` files
- Use strong encryption keys for `MCP_CREDENTIAL_ENCRYPTION_KEY`
- Enable REDIS_SSL in production
- Configure CORS origins appropriately
- Use Supabase RLS policies for data security

## 📊 Monitoring

### Langfuse (Optional)

For LLM observability:

```env
LANGFUSE_PUBLIC_KEY=your_key
LANGFUSE_SECRET_KEY=your_secret
LANGFUSE_HOST=https://cloud.langfuse.com
```

### Sentry (Optional)

For error tracking, configure Sentry DSN in the code.

## 🤝 Contributing

This is an MVP version. Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

Apache License 2.0 - See LICENSE file for details

## 🔗 Links

- **Parent Project:** [Kortix (Suna)](https://github.com/kortix-ai/suna)
- **Website:** https://www.suna.so
- **Documentation:** See parent repository

## ⚠️ MVP Limitations

This MVP is a simplified version. For production use, consider:

- Implementing proper error boundaries
- Adding comprehensive test coverage
- Setting up CI/CD pipelines
- Configuring proper logging & monitoring
- Implementing rate limiting
- Adding data backup strategies
- Reviewing security best practices

---

**Ready to build AI agents?** Start the platform and explore! 🚀
