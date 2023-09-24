from PIL import Image
import os

def resize_images(input_folder, output_folder, target_width, target_height):
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

            # Resize the image to the target dimensions
            img_resized = img.resize((target_width, target_height))

            # Save the resized image to the output folder as .jpg
            output_filename = os.path.splitext(filename)[0] + ".jpg"
            output_path = os.path.join(output_folder, output_filename)
            img_resized.save(output_path, "JPEG")

if __name__ == "__main__":
    input_folder = "input_back"  # Replace with the actual path to your input folder
    output_folder = "output_back"  # Replace with the desired output folder
    target_width = 300
    target_height = 300

    # delete all files from output folder
    for file in os.listdir(output_folder):
        os.remove(os.path.join(output_folder, file))

    resize_images(input_folder, output_folder, target_width, target_height)
    print("Images resized and saved as .jpg in the output folder.")


