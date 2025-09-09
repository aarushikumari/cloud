import os
from flask import Flask, render_template_string

application = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Flask on Elastic Beanstalk</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body style="font-family: Arial, sans-serif; margin: 40px;">
  <h1>✅ Deployed successfully!</h1>
  <p>This is a minimal Flask app running on AWS Elastic Beanstalk.</p>
  <p>Environment: <strong>{{ env }}</strong></p>
  <p>Try the JSON health check at <a href="/health">/health</a>.</p>
</body>
</html>
"""

@application.route("/")
def index():
    env = os.getenv("APP_ENV", "local")
    return render_template_string(TEMPLATE, env=env)

@application.get("/health")
def health():
    return {"ok": True, "service": "flask-eb", "env": os.getenv("APP_ENV", "local")}, 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    application.run(host="0.0.0.0", port=port)