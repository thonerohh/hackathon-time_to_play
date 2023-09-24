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

# Function Crop and Resize image
def crop_image(image):
    width, height = image.size
    #  crop image for 20%
    left = width * 0.3
    top = height * 0.3
    right = width * 0.7
    bottom = height * 0.7
    return image.crop((left, top, right, bottom)).resize((width, height))

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

        # Crop and resize image and save
        cropped_image = crop_image(image)
        cropped_image.save(os.path.join(output_folder, f"crop_{output_base_name}.png"))


        print(f"Processed {filename}")

print("Processing complete.")
