from PIL import Image
import os

input_folder = "input"
output_folder = "output"

# delete all from output


# Function to lower image quality
def lower_image_quality(image, quality=50):
    return image.convert("RGB").convert("P", palette=Image.ADAPTIVE, colors=quality)

# Function to lower image quality
def lower_image_quality2(image, quality=20):
    return image.convert("RGB").convert("P", palette=Image.ADAPTIVE, colors=quality)

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through images in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Check if the file is an image
        input_path = os.path.join(input_folder, filename)
        output_base_name = os.path.splitext(filename)[0]

        # Load the image
        image = Image.open(input_path)

        # Lower image quality and save
        lower_quality_image = lower_image_quality(image)
        lower_quality_image.save(os.path.join(output_folder, f"quality_{output_base_name}.png"))

        # Lower image quality and save
        lower_quality_image2 = lower_image_quality2(image)
        lower_quality_image2.save(os.path.join(output_folder, f"quality2_{output_base_name}.png"))

        print(f"Processed {filename}")

print("Processing complete.")
