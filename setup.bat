@echo off
echo 📦 Starting Project Setup...

:: 1. Create the virtual environment
python -m venv music_env
call music_env\Scripts\activate

:: 2. Install dependencies
echo 📥 Installing libraries...
pip install -r requirements.txt

:: 3. Create the .env file if it doesn't exist
IF NOT EXIST .env (
    echo 📝 Creating .env template...
    echo GEMINI_API_KEY=PASTE_YOUR_KEY_HERE > .env
    echo ✅ Created .env file. Please open it and paste your API key!
) ELSE (
    echo ✅ .env file already exists.
)

echo.
echo ✨ SETUP COMPLETE! 
echo 💡 Remember to paste your Gemini API key in the .env file.
pause