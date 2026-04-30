# 🎧 Vibe-to-Music : AI Micro-Expression Analyst who recommend song

An AI-driven music recommendation engine that uses Computer Vision and Large Language Models (LLMs) to detect your mood via facial micro-expressions and instantly curate a matching YouTube Music session.

---

## ✨ Features
- **Micro-Expression Analysis:** Uses an evidence-based approach to scan brows, eyes, and jaw tension for high-accuracy emotion detection.
- **Gemini 3 Flash Integration:** Leverages cutting-edge multimodal AI to interpret "vibes" rather than just simple smiles.
- **Smart Logic:** Built-in "Model Pool" with fallback mechanisms and quota-friendly cooldown timers.
- **Professional Terminal UI:** Real-time progress bars (`tqdm`), animated status spinners (`rich`), and clickable hyperlinks.

---

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **AI Model:** Google Gemini 3 Flash / 1.5 Flash
- **Vision:** OpenCV
- **Interface:** Rich (Console UI) & TQDM (Progress Bars)
- **Deployment:** GitHub-ready architecture

---

## 🚀 Quick Start

### 1. Prerequisites
- Python installed on your system.
- A **Gemini API Key** from [Google AI Studio](https://aistudio.google.com/).

### 2. Installation & Auto-Setup
Clone the repository and run the automated setup script. This will create your virtual environment, install all dependencies, and generate your configuration templates.

```bash
# Clone the project
git clone {git repository link}
cd music_recommender

# Run the automated setup (creates environment and .env template)
./setup.bat
```
### 3. Configuration
The `setup.bat` script automatically creates a `.env` file for you in the root directory.

Open the `.env` file with any text editor (Notepad, VS Code, etc.).

Replace the placeholder text with your actual key:

```bash
GEMINI_API_KEY=your_actual_key_here
```

Save the file.


### 4. Run the App
Simply double-click `run_vibe_music.bat` or run:
```bash
python vision_agent.py
```

---

## 🎮 How to Use
1. **Launch the App:** The terminal will show a "Vibe Checker Active" message.
2. **Scan Face:** Press **'V'** on your keyboard while looking at the camera.
3. **Analyze:** Watch the animated spinner as Gemini scans your micro-expressions.
4. **Enjoy:** A YouTube Music search will automatically open with a curated "Vibe."
5. **Cooldown:** A 12-second cooldown bar will appear to respect API quota limits.

---

## 🧠 Architecture & Logic
This project avoids "Black Box" emotion detection. It forces the AI to follow a strict evidence-based protocol:
- **Priority:** Weighted analysis of involuntary signals (eyes/brows) over voluntary signals (mouth).
- **Intensity Mapping:** Confidence-based music selection (e.g., High Confidence Happy → Upbeat Party; Low Confidence Happy → Chill Indie).
- **Resilience:** If one Gemini model is busy (503/429), the system automatically falls back to the next available model in the pool.

---

## 📄 License
This project is for educational purposes as part of an AI Engineering portfolio.
