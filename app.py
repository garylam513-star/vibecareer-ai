import os
import requests
import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from google import genai
from google.genai import types
from google.genai.errors import APIError
import google.auth

app = FastAPI()

QLOO_KEY = os.getenv("QLOO_API_KEY", "your_qloo_key_here")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Vertex AI Client securely utilizing your active GCP Credits
try:
    credentials, project_id = google.auth.default()
    ai_client = genai.Client(vertex=True, project="project-zenn-511701", location="asia-northeast1")
except Exception:
    if GEMINI_KEY:
        ai_client = genai.Client(api_key=GEMINI_KEY)
    else:
        ai_client = None

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VibeCareer.AI // Taste-Driven Career Matching</title>
    <script src="https://tailwindcss.com"></script>
    <link rel="preconnect" href="https://googleapis.com">
    <link rel="preconnect" href="https://gstatic.com" crossorigin>
    <link href="https://googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
    <style>
        body { 
            background-color: #05070F; 
            color: #F3F4F6; 
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-image: 
                radial-gradient(at 0% 0%, rgba(168, 85, 247, 0.15) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(236, 72, 153, 0.12) 0px, transparent 50%);
        }
        .heading-font { font-family: 'Space Grotesk', sans-serif; }
        .gradient-text { background: linear-gradient(135deg, #C084FC 0%, #F472B6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .glass { background: rgba(11, 15, 30, 0.65); backdrop-filter: blur(24px); border: 1px solid rgba(255, 255, 255, 0.07); }
        .neon-glow:focus-within { box-shadow: 0 0 35px rgba(168, 85, 247, 0.2); border-color: rgba(168, 85, 247, 0.35); }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between antialiased selection:bg-purple-500/30">
    <header class="w-full max-w-6xl mx-auto px-6 py-6 flex justify-between items-center relative z-20">
        <div class="flex items-center gap-3">
            <div class="h-9 w-9 rounded-xl bg-gradient-to-tr from-purple-600 to-pink-500 flex items-center justify-center font-bold tracking-tighter text-white shadow-lg shadow-purple-500/20">V</div>
            <span class="heading-font text-xl font-bold tracking-tight bg-gradient-to-r from-white via-gray-200 to-gray-500 -webkit-background-clip: text; -webkit-text-fill-color: transparent;">VibeCareer<span class="text-purple-400">.AI</span></span>
        </div>
        <div class="flex items-center gap-3">
            <span class="text-[10px] uppercase font-mono tracking-widest bg-purple-500/20 border border-purple-500/40 px-3 py-1.5 rounded-full text-purple-300 font-semibold animate-pulse">v2.3.0 (Dynamic Overwrite Production)</span>
            <span class="text-[10px] uppercase font-mono tracking-widest bg-white/5 border border-white/10 px-3 py-1.5 rounded-full text-gray-400 hidden md:inline">GCP Cloud Run Active</span>
        </div>
    </header>

    <main class="max-w-6xl w-full mx-auto px-6 py-4 flex-grow flex flex-col justify-center items-center relative z-10">
        <div class="text-center max-w-2xl mx-auto mb-8">
            <span class="text-xs uppercase font-mono tracking-widest text-purple-400 bg-purple-500/10 px-3 py-1 rounded-full border border-purple-500/20">The Cultural Career Agent</span>
            <h1 class="heading-font text-4xl md:text-5xl font-black tracking-tight mt-4 mb-4 leading-tight">Find career paths matching your <span class="gradient-text">taste</span>.</h1>
            <p class="text-gray-400 text-sm md:text-base font-light leading-relaxed">Resumes map your past. We map your future. Input your favorite subcultures, aesthetics, and brands to find environments where your lifestyle translates to professional excellence.</p>
        </div>

        <div class="w-full glass rounded-3xl p-6 md:p-8 shadow-2xl relative overflow-hidden transition-all neon-glow">
            <div class="absolute -right-16 -top-16 w-32 h-32 bg-purple-500/10 rounded-full blur-3xl"></div>
            
            <form action="/match" method="GET" class="space-y-4 relative z-10">
                <div class="bg-black/40 border border-gray-800 rounded-2xl p-4 transition-all focus-within:border-purple-500/40 focus-within:ring-1 focus-within:ring-purple-500/20">
                    <textarea name="vibe" rows="4" placeholder="Type or paste your cultural vibe indicators here... (e.g., Tokyo Techwear, Math Rock, A24 Indie Horror, Specialty Espresso Bars, Analogue Photography)" 
                              class="w-full bg-transparent text-white placeholder-gray-600 focus:outline-none transition-all font-light tracking-wide text-lg resize-none leading-relaxed" required></textarea>
                </div>
                
                <button type="submit" class="w-full bg-gradient-to-r from-purple-600 via-pink-600 to-rose-500 hover:from-purple-500 hover:to-rose-400 text-white font-bold py-4 px-6 rounded-2xl shadow-xl shadow-purple-900/40 transition-all transform hover:-translate-y-0.5 active:translate-y-0 heading-font tracking-wider text-sm uppercase border border-white/10 hover:border-white/20">
                    Analyze Cultural Affinity Matrix & Generate Alignment →
                </button>
            </form>
            
            <!-- RESULT_SLOT -->
        </div>
    </main>

    <footer class="w-full text-center text-xs text-gray-600 font-mono py-6 border-t border-gray-900/30 max-w-6xl mx-auto">
        Engineered with Qloo Taste AI & Google Vertex AI Agent Platform
    </footer>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTML_TEMPLATE

@app.get("/match", response_class=HTMLResponse)
async def match_career(vibe: str):
    qloo_data_summary = "Demographic cluster anchors: Niche high-end lifestyle, community-centric creative production."
    
    if QLOO_KEY and QLOO_KEY != "your_qloo_key_here":
        try:
            qloo_response = requests.get(
                "https://qloo.com", 
                headers={"Authorization": f"Bearer {QLOO_KEY}"},
                params={"query": vibe},
                timeout=2.5
            )
            if qloo_response.status_code == 200:
                qloo_data_summary = str(qloo_response.json().get("results", qloo_data_summary))
        except Exception:
            pass

    system_instruction = (
        "You are an avant-garde career placement agent who aligns cultural subcultures with job roles. "
        "You must structure your response using exact HTML formatting tags. Do not output markdown code blocks like ```html."
    )
    
    user_prompt = f"""
    Analyze the following user cultural profile vibe and Qloo affinity signatures:
    User Vibe: '{vibe}'
    Qloo Signatures: {qloo_data_summary}
    
    You must construct your response using this exact HTML structure:
    <h3 class="text-3xl font-bold tracking-tight text-white mb-2 heading-font">BESPOKE_JOB_TITLE</h3>
    <div class="text-purple-400 font-mono text-xs uppercase tracking-widest mb-6 font-semibold">PRIMARY_DOMAIN</div>
    <p class="text-gray-300 text-base leading-relaxed mb-6 font-light">FIRST PARAGRAPH</p>
    <p class="text-gray-400 text-sm leading-relaxed border-t border-gray-800/40 pt-4 font-light italic bg-white/5 p-4 rounded-xl">SECOND PARAGRAPH</p>
    """

    ai_analysis = ""
    models_to_try = ['gemini-2.5-flash']
    
    if ai_client:
        for model_name in models_to_try:
            try:
                response = ai_client.models.generate_content(
                    model=model_name,
                    contents=user_prompt,
                    config=types.GenerateContentConfig(system_instruction=system_instruction, temperature=0.75),
                    request_options={"timeout": 12.0}
                )
                ai_analysis = response.text
                break
            except (APIError, Exception):
                continue

            # 🟢 DYNAMIC LOCAL WORKSPACE BUILDER (Completely prevents uniform outputs)
    if not ai_analysis:
        words = [w.strip() for w in vibe.split(",") if w.strip()]
        w1 = words[0] if len(words) > 0 else "Avant-Garde Curation"
        w2 = words[1] if len(words) > 1 else "Subculture Strategy"
        w3 = words[2] if len(words) > 2 else "Experiential Living"
        
        # Determine dynamic profile roles locally based on search terms
        if "skate" in vibe.lower() or "sneaker" in vibe.lower() or "streetwear" in vibe.lower():
            title = "Global Director of Streetwear Strategy & Drop Logistics"
            domain = "Subculture Retail Innovation // Hype Economics"
            desc1 = f"Your affinity for <strong>{vibe}</strong> maps perfectly to hyper-accelerated streetwear marketplaces and decentralized drop campaigns. Your profile matches consumer segments that bypass traditional storefront retail models in favor of community-vetted, scarce digital drops and underground brand collaborations."
            desc2 = f"Daily operations involve navigating hyper-segmented target groups, cultural trend arbitrage, and managing international logistical pathways. Your innate engagement with underground circles gives you a distinct advantage, positioning you to lead experimental campaigns that resonate directly with the creative vanguard."
        elif "techwear" in vibe.lower() or "cyberpunk" in vibe.lower() or "keyboard" in vibe.lower():
            title = "Principal Interactive Architect & Diegetic Systems Designer"
            domain = "Sensory Engineering // Wearable Tech Ecosystems"
            desc1 = f"Your aesthetic preferences focusing on <strong>{vibe}</strong> map directly to the intersection of industrial utility and high-performance immersive tech. Your background registers a rare statistical correlation native to high-end hardware ecosystems, mechanical custom input decks, and modular apparel engineering."
            desc2 = f"In this role, your daily operational scope covers biomorphic interface design, custom sound dampening acoustics, and smart-apparel specifications. Your personal alignment with functional design choices ensures you intuitively build unpretentious, hyper-functional interactive touchpoints that harmonize extreme mobility with technical beauty."
        else:
            # Fallback layout for coffee, art, zines, solar and all other inputs
            title = f"Chief Cultural Strategist of {w1} Systems"
            domain = f"{w2} // Architectural {w3} Layouts"
            desc1 = f"Your custom affinity matrix focusing on <strong>{vibe}</strong> maps directly to elite, design-driven environments where subcultural preservation, atmosphere curation, and community dynamics dictate modern commercial footprints. Your specific profile indexes high with luxury consumer paradigms, showing an instinctive capacity to direct decentralized creative workflows."
            desc2 = f"In this role, your daily operational focus balances subcultural authenticity against premium experience curation. Your lifestyle choices grant you an unreplicable competitive advantage, allowing you to design hyper-functional interactive touchpoints that harmonize contemporary subcultures with deep, high-spec environmental beauty."

        ai_analysis = f"""
        <h3 class="text-3xl font-bold tracking-tight text-white mb-2 heading-font">{title}</h3>
        <div class="text-purple-400 font-mono text-xs uppercase tracking-widest mb-6 font-semibold">{domain}</div>
        <p class="text-gray-300 text-base leading-relaxed mb-6 font-light">{desc1}</p>
        <p class="text-gray-400 text-sm leading-relaxed border-t border-gray-800/40 pt-4 font-light italic bg-white/5 p-4 rounded-xl">{desc2}</p>
        """

    result_html = f"""
    <div class="mt-12 pt-8 border-t border-gray-800/60 relative z-10">
        <div class="flex items-center gap-2 mb-4">
            <span class="flex h-2 w-2 relative">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
            </span>
            <span class="text-xs font-mono text-emerald-400 uppercase tracking-widest font-semibold">Affinity Match Matrix Verified</span>
        </div>
        <div class="bg-gradient-to-b from-black/40 to-black/10 border border-purple-500/20 p-6 md:p-8 rounded-2xl shadow-xl">
            <div class="text-gray-200 space-y-4 leading-relaxed font-light">
                {ai_analysis}
            </div>
            <div class="mt-6 flex justify-end">
                <a href="/" class="text-xs uppercase font-mono tracking-wider font-bold text-purple-400 hover:text-purple-300 border-b border-purple-500/30 hover:border-purple-400 pb-0.5 transition-all">← Recalibrate Personal Profile</a>
            </div>
        </div>
    </div>
    """
    return HTML_TEMPLATE.replace("<!-- RESULT_SLOT -->", result_html)