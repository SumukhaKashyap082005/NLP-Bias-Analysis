# Bias and Fairness Analysis in NLP Models

## 1. Introduction
Natural Language Processing models are increasingly used in real-world applications.
However, these models may exhibit unintended bias when sensitive words such as gender or profession are changed.

This project analyzes bias in a pretrained NLP model by measuring changes in prediction confidence under controlled text variations.



## 2. Problem Statement
NLP models often produce the same prediction label across similar sentences, but the confidence associated with these predictions may change.
Such changes can indicate potential bias or sensitivity to specific terms.

This project investigates whether modifying sensitive attributes in text leads to measurable confidence shifts.



## 3. Methodology
The system follows these steps:
1. Load sentence pairs that differ only in sensitive terms.
2. Use a pretrained sentiment classification model.
3. Record prediction labels and confidence scores.
4. Measure absolute confidence difference between sentence variants.
5. Analyze differences as a potential bias signal.

No model training is performed.



## 4. Model Used
- Model: distilbert-base-uncased-finetuned-sst-2-english
- Task: Sentiment Classification
- Framework: Hugging Face Transformers

The model is used as-is to reflect real-world deployment scenarios.



## 5. Experiments
Controlled sentence pairs involving gender and profession terms were evaluated.
Each pair was tested independently to observe confidence changes.




## 6. Results and Observations
- Prediction labels remained largely consistent across variants.
- Confidence scores showed small but measurable differences.
- These differences suggest potential sensitivity to certain word changes.
- The experiment highlights areas for deeper fairness investigation.



## 7. Limitations
- Small manually curated dataset.
- Bias is inferred from confidence changes, not ground truth labels.
- Only one pretrained model was analyzed.



## 8. Future Work
- Extend analysis to multiple NLP models.
- Include race, age, and socioeconomic indicators.
- Apply statistical significance testing.
- Explore mitigation techniques.



## 9. Conclusion
This project demonstrates a simple and controlled approach to analyzing bias in NLP systems.
It emphasizes evaluation and interpretability over model performance.

The project is intended as a research prototype for fairness exploration.

