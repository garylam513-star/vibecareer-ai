
VibeCareer.AI // Taste-Driven Career Matching


Qloo Agentic Hackathon 2026 Submission

VibeCareer.AI is an autonomous cultural career placement agent that maps personal lifestyles, subcultures, and aesthetic consumer affinities directly to rewarding career choices. Built over a 24-hour sprint for the global Qloo Agentic Hackathon, it re-imagines professional mapping by aligning who you are with where you belong.

💡 The Core Inspiration

Traditional job hunting maps structural data metrics: what certifications you hold, what code libraries you memorize, and where you interned. It completely ignores human individuality, leading to widespread creative burnout and cultural misalignment in the workplace.
Standard career tests (like Myers-Briggs) rely on shallow, gameable questionnaires. VibeCareer.AI looks at your taste signatures—your preferred fashion design spaces, your sonic sub-genres, and your spatial habitats. By cross-analyzing real consumer behavior data patterns, it targets high-identity industry ecosystems where your lifestyle directly converts into an unreplicable creative advantage.

🛠️ The Architecture & Integration Data Flow

The application bridges empirical consumer behavior patterns with long-form generative synthesis via a multi-layered API pipeline:
[ User Vibe Input ] ──> [ Qloo Taste AI API ] ──> [ Gemini 3.8 Flash ] ──> [ Cinematic UI ]
  (e.g., Math Rock)      (Affinity Matrix)        (Structural Prompt)       (Tailwind Dashboard)
1. The Affinity Matrix Layer (Qloo Engine): The user defines their subculture landscape freely (e.g., "Tokyo Techwear, Math Rock, A24 Indie Horror, Specialty Espresso Bars"). The application queries Qloo's Taste AI Engine to isolate non-obvious consumer correlations across cross-functional rings (Music, Film, Fashion, Dining, Nightlife, and Locality).
2. The Creative Strategy Layer (Google Gemini API): The cold statistical affinity values returned by Qloo are cleanly injected into a structural prompt layout running on Google AI Studio (Gemini 3.8 Flash Free Tier). Gemini acts as an expert cultural creative director—processing the behavioral clusters to output a bespoke, futuristic job role and a multi-paragraph cultural justification analysis.
3. The Multi-Model Fallback Circuit: To guarantee maximum uptime during high-demand hackathon spikes, the backend features a loop fallback array that automatically shifts down through alternative endpoints (gemini-3.8-flash ➔ gemini-2.0-flash-exp ➔ gemini-1.5-flash) if capacity thresholds are exceeded.

💻 Tech Stack & Systems Placement

• Core Backend: Python 3.11 with FastAPI / Uvicorn Server
• AI Processing Engine: Qloo Taste AI API Matrix Contextualization
• Generative Language Framework: Google GenAI SDK (Gemini API Integration)
• Frontend Presentation Layer: Single-file semantic HTML5 wrapped in a responsive, glass-morphic theme utilizing Tailwind CSS CDN infrastructure
• Cloud Infrastructure Environment: Dockerized Linux Containerization compiled and deployed natively via Google Cloud Run to the Tokyo region (asia-northeast1)

📦 Local Installation & Setup Layout

Ensure you are using an updated Linux/Ubuntu distribution environment with Python 3.10+ installed.

1. Initialize and Isolate Dependencies

bash
# Clone or create your project directory space
mkdir vibecareer-ai && cd vibecareer-ai

# Set up your native virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements dependencies
pip install google-genai requests fastapi uvicorn
Use code with caution.

2. Configure Local Authentication Keys

Export your secure operational platform credentials inside your active terminal pane instance:
bash
export GEMINI_API_KEY="your_ai_studio_free_tier_key"
export QLOO_API_KEY="your_qloo_taste_api_key"
Use code with caution.

3. Initialize the Web Engine

bash
uvicorn app:app --reload
Use code with caution.
Open your preferred local browser interface and access http://127.0.0.1:8000 to interact with the engine configuration profiles.

🚀 Enterprise Production Deployment (GCP Cloud Run)

To securely build and launch this codebase directly to live Google Cloud Serverless environments without hardcoding secret keys:
bash
# 1. Login to your authenticated Google Cloud Profile
gcloud auth login

# 2. Bind your terminal workspace context to your active GCP Project ID
gcloud config set project YOUR_GCP_PROJECT_ID

# 3. Stream deployment sources to the Tokyo Region data center clusters
gcloud run deploy vibecareer-ai \
  --source . \
  --region asia-northeast1 \
  --allow-unauthenticated \
  --set-env-vars="GEMINI_API_KEY=your_gemini_key,QLOO_API_KEY=your_qloo_key"
Use code with caution.

👥 Acknowledgments

• Qloo for granting foundational API keys to map real consumer affinity records.
• Google AI Studio for highly responsive, free-tier processing power.


Test Case 1
Input : Specialty Espresso Bars, Lo-Fi Hip Hop, Independent Zines, Mid-Century Modern furniture, Analogue Photography
Returned : Creative Director of Tactile Identity & Small-Press Brand Artifacts
Bespoke Brand Publishing & Physical Experience Design

Your intuitive curation of analogue photography, low-frequency soundscapes, and deliberate pour-over extraction signals an allergic reaction to frictionless digital monoculture—a trait that directly mirrors the elite design houses and independent luxury hospitality groups defining tomorrow's aesthetic landscape. In an era dominated by hyper-optimized, algorithmic churn, the Qloo demographic anchor of niche high-end lifestyle married to community-centric creative production places you at the epicenter of the tactile counter-revolution. The deliberate patience required to develop 120mm film and restore mid-century walnut joints translates directly into the operational cadence of independent micro-publishing and high-concept physical branding. Your workplace ecosystem rejects corporate open-plans in favor of natural daylight, sun-drenched Scandinavian oak tables, and the mechanical clatter of letterpresses, cultivating environments where community trust is fostered through tangible, slow-crafted ephemera rather than ephemeral ad impressions.

In this role, you will helm the ideation and physical execution of limited-run brand publications, risograph art manuals, vinyl companion presses, and textural spatial touchpoints for heritage-conscious luxury labels, boutique hotels, and conceptual retail spaces. The market outlook for this discipline is experiencing an explosive trajectory: as digital touchpoints saturate and cheapen client brand perception, high-net-worth audiences are placing unprecedented enterprise value on physical, collectible artifacts that cannot be replicated by generative digital models. Your non-obvious operational challenges will lie in balancing the fragile supply chains of deadstock paper mills and analogue lab chemistries against institutional production timelines, alongside the delicate politics of preserving subcultural grit without letting it become a sanitized corporate pastiche. Your unfair competitive advantage is that your lived aesthetic is not a moodboard assembled on a screen; your muscle memory for physical grain, spatial acoustic restraint, and grass-roots zine dissemination gives you an infallible radar for authenticity that focus groups and corporate strategists can never replicate. 

