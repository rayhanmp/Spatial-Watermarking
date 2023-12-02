import numpy as np

def embed_watermark(image, watermark, k):
    # Embed watermark by adding noise multiplied by a factor k
    watermarked_image = image + k * watermark

    # Clip pixel values to ensure they stay in the [0, 255] range to ensure imshow can display it
    watermarked_image = np.clip(watermarked_image, 0, 255)

    return watermarked_image.astype(np.uint8)
