import cv2
import json
import os
import time
import sys
import webbrowser
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load Environment
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Quota & Model Settings
MODEL_POOL = ["gemini-3-flash-preview", "gemini-2.5-flash", "gemini-1.5-flash"]
last_call_time = 0
COOLDOWN = 12 

def get_vibe_analysis(frame):
    global last_call_time
    
    # 1. High-Quality Pre-processing
    frame_small = cv2.resize(frame, (512, 512))
    _, buffer = cv2.imencode('.jpg', frame_small, [cv2.IMWRITE_JPEG_QUALITY, 90])
    image_part = types.Part.from_bytes(data=buffer.tobytes(), mime_type="image/jpeg")

    # 2. Precise Micro-Expression Prompt
    # This specifically targets the areas where "Bored" and "Angry" differ from "Focused"
    prompt = """
Analyze the user's facial micro-expressions with high granularity.
 1.DETECTION RULES:
  - If eyebrows are pulled down and together + eyes narrowed: Label 'Angry' (NOT Focused).
  - If eyelids are drooping + jaw is relaxed + gaze is dull: Label 'Bored' or 'Tired'.
  - If mouth corners are slightly down + eyes lack crinkle: Label 'Sad' or 'Melancholy'.
  - If there is a genuine Duchenne smile (eyes crinkling): Label 'Happy' or 'Joyful'.
  - Detect moods too like 'Funny', 'Chill', 'Confused', 'Thoughtful' etc. based on specific cues.
 2.Based on this, return JSON:
  - mood: The raw emotion found.
  - short explanation: Mention the specific facial cue (e.g., 'brow tension detected'). 
  - search_query: A YouTube Music search for this specific energy
    EXAMPLES:
     Happy (High Confidence) -> e.g., "Upbeat Party Hits" or "High-energy Funk"
     Happy (Low Confidence) -> e.g., "Chill Happy Indie" or "Soft Sunny Acoustic"
     Sad (High) -> e.g., "Deep Emotional Ballads" or "Melancholic Piano"
     Angry -> e.g., "Aggressive Phonk" or "Industrial Dark Trap"
     Neutral -> e.g., "Lofi Beats" or "Ambient Coffee Shop"
"""


    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema={
            "type": "OBJECT",
            "properties": {
                "mood": {"type": "STRING"},
                "search_query": {"type": "STRING"},
                "explanation": {"type": "STRING"}
            },
            "required": ["mood", "search_query", "explanation"]
        }
    )

    # 3. The Fallback Loop
    for model_id in MODEL_POOL:
        try:
            console.print(f"🚀 Attempting analysis with [green]{model_id}[/green]...")
            response = client.models.generate_content(
                model=model_id,
                contents=[prompt, image_part],
                config=config
            )
            last_call_time = time.time()
            return json.loads(response.text)
            
        except Exception as e:
            if "503" in str(e) or "429" in str(e):
                console.print(f"⚠️ [yellow]{model_id}[/yellow] busy. Moving to fallback...")
                continue
            else:
                console.print(f"❌ Error: [red]{e}[/red]")
                return None
    print("💀 All models are currently at capacity.")        
    return None

def play_on_youtube(query):
    search_url = f"https://music.youtube.com/search?q={query.replace(' ', '+')}"
    console.print(f"🎵 Recommended Vibe: [cyan][link={search_url}]{query}[/link][/cyan]")
    webbrowser.open(search_url)

# --- Main Loop ---
from rich.console import Console
from tqdm import tqdm

console = Console()

# --- Main Loop ---

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW) 

console.print("\n[bold cyan]✨ Vibe Checker 2.0 (Micro-Expression Mode) Active![/bold cyan]")
console.print("[italic]Press [bold]V[/bold] to scan face, [bold]Q[/bold] to quit.[/italic]\n")

while True:
    ret, frame = cap.read()
    if not ret: continue
    
    cv2.imshow('Vibe Checker', frame)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('v'):
        elapsed = time.time() - last_call_time
        
        if elapsed < COOLDOWN:
            remaining = int(COOLDOWN - elapsed)
            # 1. Pretty Countdown Progress Bar
            for _ in tqdm(range(remaining), 
                          desc="⏳ Cooling down", 
                          bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}s",
                          leave=False):
                time.sleep(1)
            console.print("[bold green]✅ Ready for next check![/bold green]")
            
        else:
            # 2. Animated "Thinking" Status using Rich
            with console.status("[bold yellow]🤖 Gemini is scanning your micro-expressions...", spinner="dots12"):
                vibe = get_vibe_analysis(frame)
            
            if vibe:
                console.print("\n[bold green]📊 ANALYSIS COMPLETE[/bold green]")
                console.print(f"[bold]Mood:[/bold] {vibe['mood']}")
                console.print(f"[bold]Details:[/bold] [italic]{vibe['explanation']}[/italic]")
                
                # Trigger Music
                play_on_youtube(vibe['search_query'])

    elif key == ord('q'):
        console.print("[bold red]Shutting down... Goodbye![/bold red]")
        break

cap.release()
cv2.destroyAllWindows()

