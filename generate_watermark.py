import numpy as np

def generate_watermark(image_shape, seed):
    np.random.seed(seed)  # Set the seed to ensure reproducibility

    # Generate random noise using numpy discrete uniform rand
    watermark = np.random.randint(2, size=image_shape)
    watermark = watermark.astype(np.int16)  # Convert array to int16 to avoid overflow
    watermark[watermark == 0] = -1  # Replace 0 with -1 to make the total distributed energy zero (filled with 1 and -1)

    return watermark
