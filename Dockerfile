# 1. Base Image (Official Python environment)
FROM python:3.10-slim

# 2. Container ke andar working directory set karna
WORKDIR /app

# 3. Sirf requirements file copy karna aur libraries install karna
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Baaki ka saara code (main.py waghera) container mein copy karna
COPY . .

# 5. Port open karna (taake container bahar se network receive kar sake)
EXPOSE 8000

# 6. Server start karne ki aakhri command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]