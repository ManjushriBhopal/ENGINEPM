FROM python:3.12-slim
#Set working directory
WORKDIR /app
#copy files
COPY . /app
#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
#Expose port HF Spaces uses 7860
EXPOSE 7860
#Run app
CMP ["python", "app.py"]
