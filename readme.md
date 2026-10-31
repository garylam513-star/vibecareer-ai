# VibeCareer.AI // Taste-Driven Career Matching
### Qloo Agentic Hackathon 2026 Submission

**VibeCareer.AI** is an autonomous cultural career placement agent that maps personal lifestyles, subcultures, and aesthetic consumer affinities directly to rewarding career choices. Powered by **Qloo’s Taste AI API Engine** and **Google Vertex AI (`gemini-2.5-flash`)**, it bridges the gap between workforce identity and workplace culture.

---

## 💼 Business Case & HR Disruption Matrix

### The Problem
Traditional HR talent management systems and career platforms are deeply broken. They rely entirely on structural data metrics: what certifications a candidate holds, what keywords are on their resume, and where they went to school. This cold, mechanical approach completely ignores the human element, resulting in severe workplace cultural misalignment, rapid employee burnout, and multi-billion-dollar corporate turnover costs.

### The Human-Centric Solution
**VibeCareer.AI** introduces a paradigm shift by building a truly **human-centric matching engine**. Resumes map where a candidate has been; taste maps who a candidate *is*. By analyzing a user's organic lifestyle preferences—their sonic choices, design spaces, media consumption, and daily environments—the agent targets high-identity industry ecosystems where their existing subcultural fluency naturally translates into an unreplicable creative advantage and long-term workplace happiness.

### The Qloo Advantage
Standard Large Language Models (LLMs) fail at this task because they can only generate surface-level text cliches based on generic training parameters. **Qloo bridges this gap.** By querying Qloo’s deep, multi-domain preference data, our platform uncovers real-world, statistically sound behavioral correlations across completely separate rings (Music, Film, Fashion, Dining, and Locality). Qloo gives the agent empirical "taste" data, transforming speculative guessing into verified affinity intelligence.

---

## 🏗️ Technical Architecture & Infrastructure Blueprint

The application is engineered as a secure, stateless, decoupled microservice built entirely inside dockerized containers and hosted on enterprise cloud networks:

[ User Vibe Input ] ──> [ Qloo Taste AI API ] ──> [ Google Vertex AI ] ──> [ Google Cloud Run ]
(Multiline Text)       (Empirical Affinities)    (Gemini 2.5 Flash)       (Serverless Tokyo Hub)

### 1. Compute & Deployment Layer (Google Cloud Run)
* **Serverless Execution:** The system is compiled into a lightweight Linux container (`python:3.11-slim`) and deployed natively to **Google Cloud Run** in the Tokyo region (`asia-northeast1`) to guarantee ultra-low latency for APAC users.
* **Stateless Scaling:** Cloud Run securely isolates our environment, scales down to zero when idle to conserve project resources, and securely injects backend environmental secrets without hardcoding keys into the source directory.

### 2. Analytical Layer (Qloo Engine)
* Processes multi-line textual subculture queries and passes them to Qloo endpoints with a strict `2.5-second` gateway execution safety timeout to eliminate container freezes.

### 3. Reasoning Layer (Google Vertex AI & IAM)
* **Secure Enterprise IAM Authentication:** The backend leverages Google Cloud's **Identity and Access Management (IAM)** protocols. Requests to the highly cost-efficient **`gemini-2.5-flash`** model are signed internally via local service accounts, completely removing the security vulnerability of standard API keys.
* **Fallback Circuit:** Features an 8-second processing execution cap backed by an autonomous local variable-driven HTML generator to shield the interface if network spikes occur.

---

## 📈 Future Strategic Improvements Roadmap

* **Dynamic Icon People List Integration:** Build an asynchronous reasoning layer to dynamically cross-analyze generated career paths and query real-world cultural pioneers and icons who live that exact subculture.
* **Direct ATS Integrations:** Connect directly with enterprise Applicant Tracking Systems (ATS) to let corporate talent teams match candidate affinity matrices with active team subcultures.

---

## 🧪 Verified Test Cases & Validation Samples

### Test Case 1: Curation & Analogue Lifestyle
* **Input String:** `Specialty Espresso Bars, Lo-Fi Hip Hop, Independent Zines, Mid-Century Modern furniture, Analogue Photography`
* **System Return Output:**
```text
[PASTE YOUR SYSTEM LIVE OUTPUT CARD CONTENT HERE]
```

### Test Case 2: High-Performance Cyber-Aesthetic
* **Input String:** `Tokyo Techwear, Synthwave music, Retro-arcade design, Cyberpunk media, Mechanical keyboards`
* **System Return Output:**
```text
[PASTE YOUR SYSTEM LIVE OUTPUT CARD CONTENT HERE]
```

### Test Case 3: High-End Outdoor Utility & Eco-Minimalism
* **Input String:** `Gorpcore fashion, Ambient Drone music, Glamping & Eco-Travel, Organic architecture, Functional design`
* **System Return Output:**
```text
[PASTE YOUR SYSTEM LIVE OUTPUT CARD CONTENT HERE]
```
