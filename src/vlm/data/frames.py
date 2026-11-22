from pathlib import Path
import cv2


def extract_frames(video: str, output: str, sample_fps: float = 1.0, max_frames: int = 30, resize_width: int = 512) -> list[str]:
    """Sample approximately uniformly in time, capped to a maximum number of frames."""
    if sample_fps <= 0 or max_frames < 1 or resize_width < 1:
        raise ValueError("sample_fps, max_frames, resize_width must be positive")
    cap = cv2.VideoCapture(str(video))
    if not cap.isOpened():
        raise FileNotFoundError(f"Cannot open video: {video}")
    out_dir = Path(output)
    out_dir.mkdir(parents=True, exist_ok=True)
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        cap.release()
        raise ValueError("Invalid video FPS; inspect source")
    stride = max(1, round(fps / sample_fps))
    saved = []
    frame_index = 0
    try:
        while len(saved) < max_frames:
            ok, frame = cap.read()
            if not ok:
                break
            if frame_index % stride == 0:
                height, width = frame.shape[:2]
                if width > resize_width:
                    frame = cv2.resize(frame, (resize_width, round(height * resize_width / width)))
                target = out_dir / f"frame_{frame_index:08d}.jpg"
                if not cv2.imwrite(str(target), frame):
                    raise OSError(f"Failed to save {target}")
                saved.append(str(target))
            frame_index += 1
    finally:
        cap.release()
    return saved
