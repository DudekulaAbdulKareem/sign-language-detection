from ultralytics import YOLO
import cv2
import os

# Load your YOLO model (supports .pt format)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "best.pt")
model = YOLO(MODEL_PATH)

import cv2
import numpy as np
from ultralytics.utils import is_docker, is_colab  # Ensure you have the right imports

def check_imshow():
    try:
        assert not is_docker(), 'cv2.imshow() is disabled in Docker Environments'
        assert not is_colab(), 'cv2.imshow() is disabled in Google Colab Environments'
        
        # Create a dummy image
        cv2.imshow('test', np.zeros((1, 1, 3), dtype=np.uint8))
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        return True
    except Exception as e:
        print(f'Warning: Environment does not support cv2.imshow() - {e}')
        return False


model.predict(source="0", show=True, conf=0.3)