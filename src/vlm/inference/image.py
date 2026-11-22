from pathlib import Path


def ask_image(image: str, prompt: str, model_id: str = "HuggingFaceTB/SmolVLM-256M-Instruct", device: str = "cpu") -> str:
    """Single-image baseline; optional large dependencies loaded lazily."""
    from PIL import Image
    import torch
    from transformers import AutoProcessor, AutoModelForVision2Seq

    if device.startswith("cuda") and not torch.cuda.is_available():
        raise RuntimeError("CUDA unavailable: choose --device cpu")
    processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=False)
    model = AutoModelForVision2Seq.from_pretrained(model_id, trust_remote_code=False).to(device)
    model.eval()
    pic = Image.open(Path(image)).convert("RGB")
    messages = [{"role": "user", "content": [{"type": "image"}, {"type": "text", "text": prompt}]}]
    text = processor.apply_chat_template(messages, add_generation_prompt=True)
    inputs = processor(text=text, images=[pic], return_tensors="pt").to(device)
    with torch.inference_mode():
        generated = model.generate(**inputs, max_new_tokens=128, do_sample=False)
    return processor.batch_decode(generated[:, inputs["input_ids"].shape[1]:], skip_special_tokens=True)[0]
