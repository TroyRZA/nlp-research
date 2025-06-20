
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-380/)
# Overview
This folder contains the source code and a report produced as a result of conducting experiments exploring sentiment analysis on low-resource African languages (Mozambican Portuguese, Swahili, and Sesotho) using the AfriSenti and Sesotho News Headlines datasets.

 This research aims to aid in aligning technology with the unique linguistic diversity and cultural value of African languages. This work has immediate relevance for social media monitoring, customer feedback analysis, and public opinion tracking in African language contexts.

The approach taken will make use of several pre-trained language models (PLMs) such as mBERT, XLM-Roberta and Afro-XLMR to establish baseline measures for model performance. The project will then explore how two types of fine-tuning will improve performance on sentiment analysis.

This research will also evaluate how data augmentation strategies such as undersampling, oversampling and back-translation affect model performance; which highlights the significant effect of the structure of the corpora.  Lastly, the use of adapters as an alternative to full fine-tuning will be explored, to determine its viability in low-resource environments. 

# Contents of the Zip File
```  
├── datasets/   //folder where Both datasets are stored
│   ├── afrisenti/  
│   │   ├──por  
│   │   │   ├──train  
│   │   │   ├──test  
│   │   │   ├──validate  
│   │   ├──por_balanced_augmented  
│   │   │   ├──train  
│   │   │   ├──test  
│   │   │   ├──validate  
│   │   ├──swa  
│   │   │   ├──train  
│   │   │   ├──test  
│   │   │   ├──validate  
│   │   ├──tso  
│   │   │   ├──train  
│   │   │   ├──test  
│   │   │   ├──validate  
│   ├── sesotho_news_dataset/  
│   │   ├──train  
│   │   ├──test  
│   │   ├──validate  
│   ├── explanations  
├── training_results/  //Folder for all training results
│   ├── afroxlmr_results_por.csv  
│   ├── mbert_baseline.txt  
│   ├── swahili_lstm_results.csv  
│   └── ...  //other result files (.csv or .txt)
├── main.ipynb  //Notebook where all training, testing, fine-tuning, augmentation
├── data_preparation.ipynb  //Notebook for converting Sesotho .txt to dataset
├── requirements.txt  //Concise list of all the packages and their versions
└── readme.md  
```

# Setup Instructions
## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Jupyter Notebook or JupyterLab

1) Create a virtual environment

```bash
python -m venv nlp-env
```
2) Activate the virtual environment
```bash
nlp-env\Scripts\activate # for windows

source nlp-env/bin/activate # for macOS/Linux
```
3)  Install required packages
```bash
pip install -r requirements.txt
```

If you did not install Jupyter, run the following command:
```bash
pip install jupyter
```


# Running the Code
1. **Start Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

2. **Open the main notebook**:
   - Navigate to `main.ipynb` in the Jupyter UI
   - Open the notebook

3. **Run the cells**:
   - Execute cells sequentially using Shift+Enter
   - Or run all cells using Cell → Run All
# Data information
The datasets must be placed within a folder labelled `datasets`. Each language in afrisenti will be placed in its own folder. The data within the folders will be split into three sets (train, test and validate).
### AfriSenti Dataset  
- **Description**: A sentiment analysis benchmark that contains more than 110,000 tweets in 14 African languages (Amharic, Algerian Arabic, Hausa, Igbo, Kinyarwanda, Moroccan Arabic, Mozambican Portuguese, Nigerian Pidgin, Oromo, Swahili, Tigrinya, Twi, Xitsonga, and Yoruba) from four language families.
- **Languages**: [**Mozambican Portuguese** and **Swahili**](https://github.com/afrisenti-semeval/afrisent-semeval-2023?tab=readme-ov-file#-)  
- Download: [Here](https://github.com/afrisenti-semeval/afrisent-semeval-2023)
- **Classes**: [Negative, Neutral, Positive]  
  
### Sesotho News Headlines Dataset  
- **Description**: A dataset containing Sesotho news headlines, which have been annotated for the Sentiment Analysis and the Aspect Based Sentiment Analysis Task.
- **Domain**: [News headlines and articles](https://zenodo.org/records/10531959)  
- Download: [Here](https://zenodo.org/records/10531959)
- **Classes**: [Negative, Neutral, Positive]

## Key Results  
  
Full fine-tuning was found to be resource intensive, although it did show significant improvements against the baseline.  
  
Adapters were found to be a viable alternative to full fine-tuning for cross-lingual transfer and sentiment analysis.

### Areas for Contribution  
  
- Research into NLP in African languages  
- Optimization of training procedures  
- Cross-lingual transfer learning experiments
