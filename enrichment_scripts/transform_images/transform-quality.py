from PIL import Image
import os

def resize_images(input_folder, output_folder, target_width, target_height, qualities):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Check if the file is an image
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Open the image
            img = Image.open(input_path)

            for quality in qualities:
                # Resize the image to the target dimensions
                img_resized = img.resize((target_width, target_height))

                # Save the resized image to the output folder with the specified quality
                output_filename = os.path.splitext(filename)[0] + f"_quality_{quality}.jpg"
                output_path = os.path.join(output_folder, output_filename)
                img_resized.save(output_path, "JPEG", quality=quality)

if __name__ == "__main__":
    input_folder = "input_back"  # Replace with the actual path to your input folder
    output_folder = "output_back"  # Replace with the desired output folder
    target_width = 300
    target_height = 300
    qualities = [40, 60]  # List of desired qualities

    # Delete all files from the output folder
    for file in os.listdir(output_folder):
        os.remove(os.path.join(output_folder, file))

    resize_images(input_folder, output_folder, target_width, target_height, qualities)
    print("Images resized and saved as .jpg with specified qualities in the output folder.")
