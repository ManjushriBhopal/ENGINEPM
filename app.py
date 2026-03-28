from fastapi import FastAPI
import pandas as pd
from huggingface_hub import hf_hub_download
import joblib

# Define the load_model function to fetch from Hugging Face Hub
def load_model_from_hub():
  model_path = hf_hub_download(
      repo_id="ManjushriBhopal/ENGINEPMmodel",
      filename="engine_model.pkl"
  )
  model = joblib.load(model_path)
  return model

app = FastAPI()

# Load model once using the updated function
model = load_model_from_hub()

@app.get("/")
def home():
  return {"message": "Engine Condition Prediction API"}

@app.post("/predict")
def predict(data: dict):
  try:
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]

    return {
        "prediction": int(prediction),
        "status": "success"
    }
  except Exception as e:
     return {"error": str(e)}
