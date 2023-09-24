from PIL import Image
import os


# Function to lower image quality
def lower_image_quality(image, quality=60):
    return image.convert("RGB").convert("P", palette=Image.ADAPTIVE, colors=quality)

# Function to lower image quality
def lower_image_quality2(image, quality=30):
    return image.convert("RGB").convert("P", palette=Image.ADAPTIVE, colors=quality)

def resize_images(input_folder, output_folder, target_width, target_height):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Check if the file is a PNG image
        if filename.lower().endswith('.png'):
            output_base_name = os.path.splitext(filename)[0]
            # Open the image
            img = Image.open(input_path)

            # Resize the image to the target dimensions
            img_resized = img.resize((target_width, target_height))

            # Lower image quality and save
            lower_quality_image = lower_image_quality(img_resized)
            lower_quality_image.save(os.path.join(output_folder, f"quality_{output_base_name}.png"))

            # Lower image quality and save
            lower_quality_image2 = lower_image_quality2(img_resized)
            lower_quality_image2.save(os.path.join(output_folder, f"quality2_{output_base_name}.png"))

if __name__ == "__main__":
    input_folder = "input"  # Replace with the actual path to your input folder
    output_folder = "output"  # Replace with the desired output folder
    target_width = 300
    target_height = 300
    
    # delete all files from output folder
    for file in os.listdir(output_folder):
        os.remove(os.path.join(output_folder, file))


    resize_images(input_folder, output_folder, target_width, target_height)
    print("Images resized and saved as .png with transparent background in the output folder.")
