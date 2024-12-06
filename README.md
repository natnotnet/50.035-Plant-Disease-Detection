# 50.035 Plant Disease Detection Project
## Introduction
This folder contains all the relevant files for our Plant Disease Detection project, as well as the runnable source code for our prototype. 

Refer to this video for a quick demonstration of the prototype:


## Datasets and Models used
**Image Classification**: 
EfficientNetB0, ShuffleNet v2, ... were trained on the [PlantVillage dataset](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset).

**Image Segmentation**:
UNet, UNet++ and DeepLabV3 were trained on the [Leaf segmentation dataset](https://www.kaggle.com/datasets/fakhrealam9537/leaf-disease-segmentation-dataset).

## Folder contents
- `notebooks/Data_preparation.ipynb`: All data pre-processing steps for the *PlantVillage* dataset.
- 
- 


## Instructions to run prototype code
### 1. Downloading folder
Download the **user_interface** folder in this repository to your local storage, and navigate to its directory (e.g. `cd Downloads/user_interface`).


### 2. Creating a virtual environment
Within the folder, create a virtual environment with [**Python 3.11.1**](https://www.python.org/downloads/release/python-3111/)
```
python3.11 -m venv venv2
```

...and activate it (re-activate for every session).

- MacOS:
    ```
    source venv2/bin/activate
    ```

- Windows:
    ```
    venv2/Scripts/activate
    ```


### 3. Installing dependencies
Install all required libraries and dependencies within the environment.
```
pip install -r requirements.txt
```


### 4. Running the webpage
Run the following command to start the Streamlit app.
```
streamlit run Frontend.py
```
If the execution is successful, you should be automatically directed to the running application on your default web browser 👍