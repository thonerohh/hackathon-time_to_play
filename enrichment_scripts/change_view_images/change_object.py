from PIL import Image
import os

input_folder = "input"
output_folder = "output"

# Function to rotate image 90 degrees
def rotate_image(image):
    return image.rotate(90)

# Function to rotate image 180 degrees
def rotate_image1(image):
    return image.rotate(180)

# Function to rotate image 270 degrees
def rotate_image2(image):
    return image.rotate(270)

# Function to mirror image
def mirror_image(image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)

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

        rotated_image = rotate_image(image)
        rotated_image.save(os.path.join(output_folder, f"rotate_{output_base_name}.png"))

        rotated_image1 = rotate_image1(image)
        rotated_image1.save(os.path.join(output_folder, f"rotate1_{output_base_name}.png"))

        rotated_image2 = rotate_image2(image)
        rotated_image2.save(os.path.join(output_folder, f"rotate2_{output_base_name}.png"))

        # Mirror image and save
        mirrored_image = mirror_image(image)
        mirrored_image.save(os.path.join(output_folder, f"mirror_{output_base_name}.png"))


        print(f"Processed {filename}")

print("Processing complete.")
