# Kortix MVP - Frontend

Next.js-based frontend for the Kortix AI Agent Platform.

## Setup

### 1. Install Dependencies

```bash
npm install
```

### 2. Configure Environment

```bash
cp .env.example .env.local
# Edit .env.local with your credentials
```

### 3. Run Development Server

```bash
npm run dev
```

Open http://localhost:3000

### 4. Build for Production

```bash
npm run build
npm start
```

## Project Structure

```
frontend/
├── src/
│   ├── app/          # Next.js app router pages
│   ├── components/   # React components
│   └── lib/          # Utilities
├── public/           # Static assets
└── package.json
```

## Docker

```bash
docker build -t kortix-frontend .
docker run -p 3000:3000 kortix-frontend
```
