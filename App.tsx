import React, { useState, useEffect } from 'react';

const App: React.FC = () => {
  const [activeTab, setActiveTab] = useState('install');
  const [copied, setCopied] = useState(false);

  const repoUrl = "https://github.com/aaayafuj51-AYFJ/Aaayafuja_CyberSecurity7.py.git";
  
  const installSteps = [
    { label: "Clone Repository", cmd: `git clone ${repoUrl}` },
    { label: "Navigate Directory", cmd: "cd Aaayafuja_CyberSecurity7.py" },
    { label: "Fix Windows Pip", cmd: "python -m pip install --upgrade pip" },
    { label: "Install Requirements", cmd: "python -m pip install -r requirements.txt" },
    { label: "Install Aaayafuj", cmd: "python -m pip install ." }
  ];

  const handleCopy = (text: string) => {
    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="flex flex-col min-h-screen">
      {/* Header */}
      <header className="border-b border-gray-800 p-6 flex justify-between items-center bg-black/50 backdrop-blur-md sticky top-0 z-10">
        <div className="flex items-center space-x-4">
          <div className="w-10 h-10 bg-red-600 rounded flex items-center justify-center font-bold text-xl">AF</div>
          <div>
            <h1 className="text-xl font-bold text-white tracking-tighter">AAAYAFUJ <span className="text-red-500">v7.0.4</span></h1>
            <p className="text-xs text-gray-500">Cybersecurity Command Center</p>
          </div>
        </div>
        <div className="flex space-x-6 text-sm font-medium">
          <button 
            onClick={() => setActiveTab('install')}
            className={`${activeTab === 'install' ? 'text-red-500' : 'text-gray-400 hover:text-white'} transition-colors`}
          >
            Installation
          </button>
          <button 
            onClick={() => setActiveTab('docs')}
            className={`${activeTab === 'docs' ? 'text-red-500' : 'text-gray-400 hover:text-white'} transition-colors`}
          >
            Documentation
          </button>
          <a href={repoUrl} target="_blank" rel="noreferrer" className="text-gray-400 hover:text-white flex items-center">
            GitHub <span className="ml-1 text-[10px]">↗</span>
          </a>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-grow p-8 max-w-5xl mx-auto w-full">
        {activeTab === 'install' && (
          <div className="space-y-8 animate-in fade-in duration-500">
            <section className="bg-red-900/10 border border-red-500/30 rounded-xl p-6 relative overflow-hidden">
              <div className="absolute top-0 right-0 p-4 opacity-10">
                <svg width="100" height="100" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m21 21-6-6m6 6v-4.8m0 4.8h-4.8M3 16.2V21m0 0h4.8M3 21v-4.8M21 3v4.8M21 3h-4.8M21 3l-6 6M3 3l6 6M3 3v4.8M3 3h4.8"/></svg>
              </div>
              <h2 className="text-red-500 font-bold mb-2 flex items-center">
                <span className="mr-2">⚠️</span> CRITICAL INSTALLATION UPDATE
              </h2>
              <p className="text-sm text-gray-300 mb-4">
                The official repository has moved to a new address. Use the following steps to ensure a successful installation and bypass "Fatal Error" pip launcher issues on Windows.
              </p>
              <div className="p-3 bg-black/40 rounded border border-red-500/20 text-xs text-gray-400">
                Repository: <span className="text-red-400 font-mono">{repoUrl}</span>
              </div>
            </section>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div className="space-y-4">
                <h3 className="text-lg font-bold text-white border-l-4 border-red-500 pl-3">Standard Installation</h3>
                <div className="space-y-3">
                  {installSteps.map((step, idx) => (
                    <div key={idx} className="group relative">
                      <div className="text-[10px] text-gray-500 mb-1 uppercase tracking-widest">{step.label}</div>
                      <div className="flex items-center space-x-2 bg-[#121218] p-3 rounded border border-gray-800 group-hover:border-gray-700 transition-all">
                        <span className="text-red-500 text-xs">$</span>
                        <code className="text-xs text-gray-300 flex-grow font-mono">{step.cmd}</code>
                        <button 
                          onClick={() => handleCopy(step.cmd)}
                          className="opacity-0 group-hover:opacity-100 p-1 hover:bg-gray-800 rounded transition-all"
                        >
                          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></svg>
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              <div className="space-y-4">
                <h3 className="text-lg font-bold text-white border-l-4 border-blue-500 pl-3">System Doctor</h3>
                <div className="bg-[#121218] p-6 rounded-xl border border-gray-800 h-full">
                  <p className="text-sm text-gray-400 mb-6">
                    If the tool fails to launch, run the built-in diagnostic module to identify environment corruption.
                  </p>
                  <div className="flex flex-col space-y-4">
                    <button 
                      onClick={() => handleCopy("python aaayafuj/utils/env_check.py")}
                      className="w-full btn-primary text-white font-bold py-3 rounded text-sm uppercase tracking-tighter"
                    >
                      Copy Diagnostic Cmd
                    </button>
                    <div className="pt-6 border-t border-gray-800">
                      <h4 className="text-xs font-bold text-gray-500 mb-2 uppercase">Status Monitors</h4>
                      <div className="grid grid-cols-2 gap-2">
                        <div className="p-3 bg-black/30 rounded border border-gray-800/50">
                          <div className="text-[10px] text-gray-500 uppercase">Engine</div>
                          <div className="text-green-500 text-xs">Ready</div>
                        </div>
                        <div className="p-3 bg-black/30 rounded border border-gray-800/50">
                          <div className="text-[10px] text-gray-500 uppercase">Integrity</div>
                          <div className="text-green-500 text-xs">99.9%</div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'docs' && (
          <div className="space-y-6 animate-in slide-in-from-bottom-4 duration-500">
             <h2 className="text-2xl font-bold text-white">System Architecture</h2>
             <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                {['Core Engine', 'Scan Modules', 'Network Hub'].map(mod => (
                  <div key={mod} className="p-6 bg-[#121218] rounded border border-gray-800 hover:border-red-500/50 transition-colors cursor-default">
                    <h3 className="text-red-500 font-bold mb-2">{mod}</h3>
                    <p className="text-xs text-gray-500">Low-level integration for v7 framework operations.</p>
                  </div>
                ))}
             </div>
             <div className="p-8 bg-black border border-gray-800 rounded-xl">
                <p className="text-gray-400 leading-relaxed text-sm">
                  Aaayafuj is designed to be fully modular. Every command corresponds to a specific sub-process that runs in isolation to prevent system-wide crashes during intense scanning operations.
                </p>
             </div>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="p-6 border-t border-gray-800 text-[10px] text-gray-600 text-center uppercase tracking-[0.2em]">
        © {new Date().getFullYear()} Aaayafuj Cybersecurity | Professional Grade Framework
      </footer>

      {/* Copy Toast */}
      {copied && (
        <div className="fixed bottom-8 right-8 bg-green-600 text-white px-4 py-2 rounded shadow-lg text-sm animate-bounce">
          Command Copied!
        </div>
      )}
    </div>
  );
};

export default App;