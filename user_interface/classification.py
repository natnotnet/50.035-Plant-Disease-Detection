import torch
from process_image import classification_preprocess

def predict_disease(image, model, device):
    disease_to_idx = {
        "Apple_scab": 0,
        "Bacterial_spot": 1,
        "Black_rot": 2,
        "Cedar_apple_rust": 3,
        "Cercospora_leaf_spot Gray_leaf_spot": 4,
        "Common_rust": 5,
        "Early_blight": 6,
        "Esca_(Black_Measles)": 7,
        "Haunglongbing_(Citrus_greening)": 8,
        "Late_blight": 9,
        "Leaf_Mold": 10,
        "Leaf_blight_(Isariopsis_Leaf_Spot)": 11,
        "Leaf_scorch": 12,
        "Northern_Leaf_Blight": 13,
        "Powdery_mildew": 14,
        "Septoria_leaf_spot": 15,
        "Spider_mites Two-spotted_spider_mite": 16,
        "Target_Spot": 17,
        "Tomato_Yellow_Leaf_Curl_Virus": 18,
        "Tomato_mosaic_virus": 19,
        "healthy": 20,
    }

    idx_to_disease = {v: k for k, v in disease_to_idx.items()}
    
    input_tensor = classification_preprocess(image).unsqueeze(0)  # Add batch dimension
    model = model.to(device)
    input_tensor = input_tensor.to(device)

    # Predict the disease
    with torch.no_grad():
        logits = model(input_tensor)  # Forward pass

    predicted_idx = torch.argmax(logits, dim=1).item()

    # Map the index to the disease name
    predicted_class = idx_to_disease[predicted_idx]
    
    return predicted_class