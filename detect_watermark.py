import numpy as np

def detect_watermark(watermarked_image, watermark):
    # Calculate correlation between noise and the watermarked image
    correlation = np.sum(watermark * watermarked_image) / np.sqrt(
        np.sum(watermark**2) * np.sum(watermarked_image**2))

    # Set a threshold for detection, you can change the value
    threshold = 2

    # Check if watermark is detected
    if correlation > threshold:
        return True, correlation
    else:
        return False, correlation
