# Analysing Sentiments for Low-resource African Languages using Afrisenti and Sesotho News Headlines Datasets

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-380/)

## Overview
This repository contains the implementation and experiments for sentiment analysis on low-resource African languages (Mozambican Portuguese, Swahili, and Sesotho) using the AfriSenti and Sesotho News Headlines datasets. 
The project explores various approaches including traditional Long Short-Term Memory (LSTM) networks, transformer-based BERT models, data augmentation, and different fine-tuning strategies (full fine-tuning vs. adapters).


## Key Results

Full fine-tuning was found to be resource intensive, although it did show significant improvements against the baseline.

Adapters were found to be a viable alternative to full fine-tuning for cross-lingual transfer and sentiment analysis.

## Objectives

- Evaluate sentiment analysis performance on low-resource African languages
- Compare traditional neural networks (LSTM) with transformer-based models (mBERT, XLM-R, AfroXLMR)
- Assess the effectiveness of Adapters compared to full fine-tuning strategies
- Investigate data augmentation techniques for improving model performance with low-resource African languages

## Datasets

### AfriSenti Dataset
- **Description**: Multilingual sentiment analysis dataset for African languages
- **Languages**: [**Mozambican Portuguese** and **Swahili**](https://github.com/afrisenti-semeval/afrisent-semeval-2023?tab=readme-ov-file#-)
- **Classes**: [Negative, Neutral, Positive]

### Sesotho News Headlines Dataset
- **Description**: Domain-specific sentiment dataset from Sesotho news sources
- **Domain**: [News headlines and articles](https://zenodo.org/records/10531959)
- **Classes**: [Negative, Neutral, Positive]

## Project Structure

```
├── datasets/
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
├── training_results/
│   ├── afroxlmr_results_por.csv
│   ├── mbert_baseline.txt
│   ├── swahili_lstm_results.csv
│   └── ...
├── main.ipynb
├── data_preparation.ipynb
├── requirements.txt
└── readme.md
```

## Configuration

### Training Parameters

- **Batch Size**: 16
- **Learning Rate**: 2e-5
- **Epochs**: 3
- **Warm-up Steps**: 0


### Detailed Results

For comprehensive results and analysis, see our submitted Project Report.


### Areas for Contribution

- Research into NLP in African languages
- Optimization of training procedures
- Cross-lingual transfer learning experiments

[//]: # (Dataset documentation is here:)

[//]: # (- **Mozambican Portuguese** and **Swahili**: https://huggingface.co/datasets/masakhane/afrisenti)

[//]: # (- **Sesotho**: https://zenodo.org/records/10531959)

[//]: # ()
[//]: # (## Setup)

[//]: # ()
[//]: # (1. Create a venv)

[//]: # (2. Activate venv)

[//]: # (3. pip install -r requirements.txt)

[//]: # ()
[//]: # (Add dependencies to requirements.txt as we go.)
