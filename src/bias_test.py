import pandas as pd
from model import predict

def run_bias_test(csv_path):
    data = pd.read_csv(csv_path)
    results = []

    for _, row in data.iterrows():
        base = row["base_sentence"]
        variant = row["variant"]

        base_label, base_score = predict(base)
        var_label, var_score = predict(variant)

        diff = round(abs(base_score - var_score), 4)

        results.append({
            "base_sentence": base,
            "variant_sentence": variant,
            "base_label": base_label,
            "base_confidence": round(base_score, 4),
            "variant_label": var_label,
            "variant_confidence": round(var_score, 4),
            "confidence_difference": diff
        })

    return results
