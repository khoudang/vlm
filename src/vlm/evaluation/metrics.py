from collections.abc import Iterable


def binary_metrics(truth: Iterable[int], prediction: Iterable[int]) -> dict:
    t, p = list(truth), list(prediction)
    if not t or len(t) != len(p):
        raise ValueError("Expected non-empty equal-length label sequences")
    if any(v not in (0, 1) for v in t + p):
        raise ValueError("Only binary labels 0 or 1 supported")
    tp = sum(a == 1 and b == 1 for a, b in zip(t, p))
    tn = sum(a == 0 and b == 0 for a, b in zip(t, p))
    fp = sum(a == 0 and b == 1 for a, b in zip(t, p))
    fn = sum(a == 1 and b == 0 for a, b in zip(t, p))
    safe = lambda a, b: a / b if b else 0.0
    precision = safe(tp, tp + fp)
    recall = safe(tp, tp + fn)
    return {"tp": tp, "tn": tn, "fp": fp, "fn": fn,
            "precision": precision, "recall": recall,
            "f1": safe(2 * precision * recall, precision + recall),
            "accuracy": safe(tp + tn, len(t))}
