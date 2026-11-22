import argparse
from vlm.inference.image import ask_image
p=argparse.ArgumentParser()
p.add_argument("--image",required=True)
p.add_argument("--model",default="HuggingFaceTB/SmolVLM-256M-Instruct")
p.add_argument("--device",default="cpu")
p.add_argument("--prompt",default="Describe what is visibly happening. Do not invent unseen causes.")
a=p.parse_args()
print(ask_image(a.image,a.prompt,a.model,a.device))
