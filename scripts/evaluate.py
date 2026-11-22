import argparse, csv, json
from vlm.evaluation.metrics import binary_metrics

def load(path):
    with open(path,newline="",encoding="utf8") as f:
        return {r["video_id"]:int(r["label"]) for r in csv.DictReader(f)}

p=argparse.ArgumentParser()
p.add_argument("--truth",required=True)
p.add_argument("--predictions",required=True)
a=p.parse_args()
t,pred=load(a.truth),load(a.predictions)
if t.keys()!=pred.keys():
    raise SystemExit(f"Mismatched video IDs: truth_only={sorted(t.keys()-pred.keys())}; pred_only={sorted(pred.keys()-t.keys())}")
ids=sorted(t)
print(json.dumps(binary_metrics([t[i] for i in ids],[pred[i] for i in ids]),indent=2))
