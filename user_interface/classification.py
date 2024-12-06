import torch
from process_image import classification_preprocess

def predict_disease(image, model, device):
    disease_to_idx = {
        "healthy": 0,
        "Haunglongbing_(Citrus_greening)": 1,
        "Bacterial_spot": 2,
        "Tomato_Yellow_Leaf_Curl_Virus": 3,
        "Late_blight": 4,
        "Powdery_mildew": 5,
        "Early_blight": 6,
        "Black_rot": 7,
        "Septoria_leaf_spot": 8,
        "Spider_mites Two-spotted_spider_mite": 9,
        "Target_Spot": 10,
        "Esca_(Black_Measles)": 11,
        "Common_rust": 12,
        "Leaf_scorch": 13,
        "Leaf_blight_(Isariopsis_Leaf_Spot)": 14,
        "Northern_Leaf_Blight": 15,
        "Leaf_Mold": 16,
        "Apple_scab": 17,
        "Cercospora_leaf_spot Gray_leaf_spot": 18,
        "Tomato_mosaic_virus": 19,
        "Cedar_apple_rust": 20,
    }
    idx_to_disease = {v: k for k, v in disease_to_idx.items()}
    
    input_tensor = classification_preprocess(image).unsqueeze(0)  # Add batch dimension

    model = model.to(device)
    input_tensor = input_tensor.to(device)

    # Predict the disease
    # model.eval()  # Set the model to evaluation mode
    with torch.no_grad():
        logits = model(input_tensor)  # Forward pass

    predicted_idx = torch.argmax(logits, dim=1).item()

    # Map the index to the disease name
    predicted_class = idx_to_disease[predicted_idx]
    
    return predicted_class