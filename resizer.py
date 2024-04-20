from PIL import Image
import os

def resize_image(input_image_path, output_image_path, target_size_kb):
    quality = 90  # Initial quality setting for JPEG compression
    while True:
        # Open image and resize
        original_image = Image.open(input_image_path)
        resized_image = original_image.resize(original_image.size)

        # Save the resized image with specified quality
        resized_image.save(output_image_path, optimize=True, quality=quality)

        # Check the resulting file size
        file_size_kb = os.path.getsize(output_image_path) / 1024

        # If the resulting file size is within the acceptable range, break the loop
        if file_size_kb <= target_size_kb:
            break

        # Decrease quality and try again
        quality -= 10
        if quality <= 0:
            # If quality becomes too low, break the loop to avoid infinite loop
            break

def main():
    input_image_path = "img.jpg"
    output_image_path = "compressed_img.jpg"
    target_size_kb = 100
    
    resize_image(input_image_path, output_image_path, target_size_kb)
    print("Image resized successfully!")

if __name__ == "__main__":
    main()
