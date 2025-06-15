# train_from_file.py
from app.model import train_from_file

if __name__ == "__main__":
    result = train_from_file("train_data.json")
    print("Model trained with coefficients:", result["coefficients"])

