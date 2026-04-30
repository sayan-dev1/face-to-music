@echo off
echo 🎧 Starting Vibe-to-Music...
:: Activate the virtual environment
call music_env\Scripts\activate
:: Run the python script
python vision_agent.py
pause