# FastAPI + Neon Postgres

## Local development

1. **Create venv and activate venv**  
python -m venv .venv  
source .venv/Scripts/activate  

2. **Install dependencies**  
pip install -r requirements.txt  

3. **Configure DB**  
In /app create a .env file, set DATABASE_URL  

4. **Run locally**  
In /app:  
uvicorn main:app --reload  
Navigate to provided url