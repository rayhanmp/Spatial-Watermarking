import cv2
import os
from generate_watermark import generate_watermark
from embed_watermark import embed_watermark
from detect_watermark import detect_watermark

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def select_image():
    target_images_folder = 'target-images'
    create_folder_if_not_exists(target_images_folder)
    
    print("\nSelect the target image:")
    files = os.listdir(target_images_folder)
    
    if not files: # If no file found
        print("No images found in /target-images folder.")
        return None
    
    for i, file in enumerate(files): # Enumerate items in the folder
        print(f"{i + 1}. {file}")
    
    while True:
        choice = input("Enter the number of the target image: ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(files):
                return os.path.join(target_images_folder, files[choice - 1])
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def write_result(image, filename, seed, k):
    # Check whether the folder exists
    results_folder = 'results'
    create_folder_if_not_exists(results_folder)

    filename += f'_seed{seed}_k{k}'
    # Append '.jpg' extension if not provided by the user
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        filename += '.jpg'

    # Write the image to the folder
    result_path = os.path.join(results_folder, filename)
    cv2.imwrite(result_path, image)
    print(f"Result written to: {result_path}")

def detect_watermark_menu():
    image_path = select_image()
    
    if image_path:
        while True:
            try:
                seed = int(input("Enter the seed value: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        target_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        watermark = generate_watermark(target_image.shape, seed)
        watermark_detected = detect_watermark(target_image, watermark)
        
        print("Watermark Detection Result:", watermark_detected)

def embed_watermark_menu():
    image_path = select_image()
    
    if image_path:
        original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        while True:
            try:
                seed = int(input("Enter the seed value: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        while True:
            try:
                k = int(input("Enter the k value: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        watermark = generate_watermark(original_image.shape, seed)
        watermarked_image = embed_watermark(original_image, watermark, k)

        write_option = input("Do you want to write the result to a folder? (yes/no): ")
        if write_option.lower() == "yes":
            filename = input("Enter the filename for the result image: ")
            write_result(watermarked_image, filename, seed, k)
    
        print(f"Watermarked image with k of {k}.")
        cv2.imshow(f"Watermarked Image (k={k})", watermarked_image)
        cv2.waitKey(0)

def main():
    while True:
        print("\nMenu:")
        print("0. Quit")
        print("1. Detect Watermark")
        print("2. Embed Watermark")

        choice = input("Enter your choice (0, 1, or 2): ")

        if choice == "0":
            print("\nBye!")
            break
        elif choice == "1":
            detect_watermark_menu()
        elif choice == "2":
            embed_watermark_menu()
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
