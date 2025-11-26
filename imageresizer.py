import os
from PIL import Image

input_folder = "images"
output_folder = "resized_images"

os.makedirs(output_folder, exist_ok=True)

def resize_images(width, height):
    print("Starting batch image resizing...\n")

    for filename in os.listdir(input_folder):
        try:
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                img_path = os.path.join(input_folder, filename)

                img = Image.open(img_path)
                resized_img = img.resize((width, height))

                output_path = os.path.join(output_folder, filename)
                resized_img.save(output_path)

                print(f"✔ Resized: {filename} → saved to {output_path}")
        except Exception as e:
            print(f"✖ Error processing {filename}: {e}")

    print("\nAll images resized successfully!")

resize_images(300, 300)
