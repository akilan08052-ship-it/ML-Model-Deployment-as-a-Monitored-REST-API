from prometheus_client import Counter

prediction_counter = Counter(
    "predictions_total",
    "Total successful predictions",
    ["predicted_class"]
)