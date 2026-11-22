import argparse
from vlm.data.frames import extract_frames

p = argparse.ArgumentParser(description="Sample JPEG frames from a source video")
p.add_argument("--video", required=True)
p.add_argument("--output", required=True)
p.add_argument("--fps", type=float, default=1.0)
p.add_argument("--max-frames", type=int, default=30)
p.add_argument("--width", type=int, default=512)
a = p.parse_args()
paths = extract_frames(a.video, a.output, a.fps, a.max_frames, a.width)
print(f"Saved {len(paths)} frames to {a.output}")
