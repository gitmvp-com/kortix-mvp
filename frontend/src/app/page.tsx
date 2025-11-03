export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      <div className="container mx-auto px-4 py-16">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-6xl font-bold text-white mb-6">
            Kortix MVP
          </h1>
          <p className="text-xl text-purple-200 mb-8">
            Open Source Platform to Build, Manage and Train AI Agents
          </p>
          
          <div className="bg-white/10 backdrop-blur-lg rounded-lg p-8 text-left">
            <h2 className="text-2xl font-semibold text-white mb-4">🚀 Welcome to Kortix</h2>
            <p className="text-purple-100 mb-4">
              This is a simplified MVP version of the Kortix AI Agent Platform. To get started:
            </p>
            
            <ol className="list-decimal list-inside space-y-2 text-purple-100 mb-6">
              <li>Configure your environment variables in <code className="bg-black/30 px-2 py-1 rounded">.env.local</code></li>
              <li>Set up your Supabase project and add credentials</li>
              <li>Add at least one LLM provider API key (Anthropic, OpenAI, etc.)</li>
              <li>Start building your AI agents!</li>
            </ol>
            
            <div className="grid md:grid-cols-2 gap-4">
              <div className="bg-black/20 rounded p-4">
                <h3 className="font-semibold text-white mb-2">📚 Features</h3>
                <ul className="text-sm text-purple-100 space-y-1">
                  <li>• Multi-LLM Support</li>
                  <li>• Chat Interface</li>
                  <li>• Agent Management</li>
                  <li>• File Processing</li>
                  <li>• Web Search & Scraping</li>
                </ul>
              </div>
              
              <div className="bg-black/20 rounded p-4">
                <h3 className="font-semibold text-white mb-2">🔗 API Endpoints</h3>
                <ul className="text-sm text-purple-100 space-y-1">
                  <li>• <a href="http://localhost:8000/docs" className="underline">API Docs</a></li>
                  <li>• <code>/api/health</code></li>
                  <li>• <code>/api/agents</code></li>
                  <li>• <code>/api/chat</code></li>
                  <li>• <code>/api/files</code></li>
                </ul>
              </div>
            </div>
            
            <div className="mt-6 p-4 bg-yellow-500/20 border border-yellow-500/50 rounded">
              <p className="text-sm text-yellow-100">
                ⚠️ <strong>Note:</strong> This is an MVP with placeholder implementations. 
                Connect your services and implement the core logic to enable full functionality.
              </p>
            </div>
          </div>
          
          <div className="mt-8 flex justify-center gap-4">
            <a 
              href="https://github.com/gitmvp-com/kortix-mvp" 
              className="bg-purple-600 hover:bg-purple-700 text-white px-6 py-3 rounded-lg font-semibold transition"
              target="_blank"
              rel="noopener noreferrer"
            >
              View on GitHub
            </a>
            <a 
              href="http://localhost:8000/docs" 
              className="bg-white/20 hover:bg-white/30 text-white px-6 py-3 rounded-lg font-semibold transition"
            >
              API Documentation
            </a>
          </div>
        </div>
      </div>
    </div>
  )
}
