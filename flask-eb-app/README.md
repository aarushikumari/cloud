# Flask on AWS Elastic Beanstalk

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python application.py
# open http://localhost:5000
```

## Deploy (Elastic Beanstalk Console)
1. Zip this folder (without .venv):
   ```bash
   zip -r flask-eb-app.zip .
   ```
2. Go to AWS Elastic Beanstalk Console → Create Application.
3. Choose platform **Python 3.11**.
4. Upload the `flask-eb-app.zip`.
5. Create environment → wait → open EB URL.