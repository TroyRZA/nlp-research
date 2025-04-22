import os
from datasets import load_dataset

def setup_project():
    os.makedirs("./datasets/afrisenti", exist_ok=True)
    
    print("Downloading Swahili (swa) dataset...")
    swa_dataset = load_dataset("masakhane/afrisenti", "swa")
    print("Swahili dataset downloaded!")
    
    print("Downloading Portuguese (por) dataset...")
    por_dataset = load_dataset("masakhane/afrisenti", "por")
    print("Portuguese dataset downloaded!")
    
    print("Downloading Tsonga (tso) dataset...")
    tso_dataset = load_dataset("masakhane/afrisenti", "tso")
    print("Tsonga dataset downloaded!")
    
    print("Saving datasets to disk...")
    swa_dataset.save_to_disk("./datasets/afrisenti/swa")
    por_dataset.save_to_disk("./datasets/afrisenti/por")
    tso_dataset.save_to_disk("./datasets/afrisenti/tso")
    print("All datasets saved successfully to ./datasets/afrisenti/")

if __name__ == "__main__":
    setup_project()