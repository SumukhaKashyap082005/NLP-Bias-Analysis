from bias_test import run_bias_test

results = run_bias_test("../data/sentences.csv")

for r in results:
    print("\nBase Sentence:", r["base_sentence"])
    print("Variant Sentence:", r["variant_sentence"])
    print("Base Prediction:", r["base_label"], r["base_confidence"])
    print("Variant Prediction:", r["variant_label"], r["variant_confidence"])
    print("Confidence Difference:", r["confidence_difference"])
