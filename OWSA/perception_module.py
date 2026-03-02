from ultralytics import YOLO

def detect_oilwells(image_path: str, model_path: str = "best.pt"):
    model = YOLO(model_path)
    results = model(image_path)

    detections = []
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            confidence = box.conf[0].item()
            detections.append(
                {
                    "position": {"x1": x1, "y1": y1, "x2": x2, "y2": y2},
                    "confidence": confidence,
                }
            )

    return detections

