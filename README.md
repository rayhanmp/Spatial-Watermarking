# Spatial Watermarking with Correlation Based Detection

A simple program to embed and detect spatial watermark using Python.

## 💭 Introductory
Watermarking can be achieved through various methods, but the most straightforward approach involves **imbedding the original image using white noise** generated in a controlled manner. The white noise is created with a specific seed for reproducibility, and this seed serves as a user-defined key of sorts. Subsequently, comparing the watermarked image to the noise allows us to ascertain the correlation value. If the correlation surpasses a designated threshold, it indicates the presence of the watermark.

## 🔥 Features
1. Embedding watermark
2. Detecting watermark
3. Writing watermarked image to a file

## ⚙ How to Run
1. Clone the repository:

    ```bash
    git clone https://github.com/rayhanmp/Spatial-Watermarking.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Spatial-Watermarking
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Python program:

    ```bash
    python main.py
    ```

5. Enter "0" to exit, "1" to embed watermark to an image, and "2" to detect watermark


By default, watermarked image will be stored on `/results` using .jpg format. The program will automatically append information regarding the seed and k-value used.
Target image (whether it's for detecting watermark/embedding watermark) must be placed on `/target-images`.
