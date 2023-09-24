from PIL import Image
import os

def resize_images(input_folder, output_folder, target_width, target_height, compression_level):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Check if the file is a PNG image
        if filename.lower().endswith('.png'):
            # Open the image
            img = Image.open(input_path)

            # Resize the image to the target dimensions
            img_resized = img.resize((target_width, target_height))

            # Save the resized image to the output folder as PNG with specified compression level
            output_filename = os.path.splitext(filename)[0] + ".png"
            output_path = os.path.join(output_folder, output_filename)
            img_resized.save(output_path, "PNG", compress_level=compression_level)

def resize_images2(input_folder, output_folder, target_width, target_height, compression_level):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Check if the file is a PNG image
        if filename.lower().endswith('.png'):
            # Open the image
            img = Image.open(input_path)

            # Resize the image to the target dimensions
            img_resized = img.resize((target_width, target_height))

            # Save the resized image to the output folder as PNG with specified compression level
            output_filename = os.path.splitext(filename)[0] + "1.png"
            output_path = os.path.join(output_folder, output_filename)
            img_resized.save(output_path, "PNG", compress_level=compression_level)

if __name__ == "__main__":
    input_folder = "input"  # Replace with the actual path to your input folder
    output_folder = "output"  # Replace with the desired output folder
    target_width = 300
    target_height = 300
    compression_level_40 = 1  # Higher value means lower quality (0-9)
    compression_level_60 = 3  # Higher value means lower quality (0-9)

    # Delete all files from the output folder
    for file in os.listdir(output_folder):
        os.remove(os.path.join(output_folder, file))

    # Resize images with compression level 40
    resize_images(input_folder, output_folder, target_width, target_height, compression_level_40)
    print("Images resized and saved with compression level 40 in the output folder.")

    # Resize images with compression level 60
    resize_images2(input_folder, output_folder, target_width, target_height, compression_level_60)
    print("Images resized and saved with compression level 60 in the output folder.")
