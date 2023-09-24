import os
import random
from PIL import Image

def overlay_images(background_path, foreground_path, output_path, resize_factor):
    # Open the background and foreground images
    background = Image.open(background_path)
    foreground = Image.open(foreground_path)

    # Randomly resize the foreground image based on the given resize factor
    new_width = int(background.width * resize_factor)
    new_height = int(background.height * resize_factor)
    foreground_resized = foreground.resize((new_width, new_height))

    # Calculate the position to paste the resized foreground image at the center
    x_position = (background.width - foreground_resized.width) // 2
    y_position = (background.height - foreground_resized.height) // 2

    # Ensure the resized foreground image has an alpha channel (transparency)
    foreground_with_alpha = foreground_resized.convert("RGBA")

    # Extract the alpha channel from the foreground image and use it as the mask
    alpha_mask = foreground_with_alpha.split()[3]

    # Paste the resized foreground image onto the background using the alpha mask and centered position
    result = Image.new("RGBA", background.size)
    result.paste(background, (0, 0))
    result.paste(foreground_with_alpha, (x_position, y_position), mask=alpha_mask)

    # Save the resulting image
    result.save(output_path)

def combine_all_images(background_folder, foreground_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of all background and foreground files
    background_files = os.listdir(background_folder)
    foreground_files = os.listdir(foreground_folder)

    # Loop through each background and foreground image
    for background_file in background_files:
        for foreground_file in foreground_files:
            background_path = os.path.join(background_folder, background_file)
            foreground_path = os.path.join(foreground_folder, foreground_file)

            # Generate a random resize factor between 0.3 and 0.9
            resize_factor = random.uniform(0.3, 0.9)

            # Generate the output image file path
            output_file = f"{os.path.splitext(background_file)[0]}_{os.path.splitext(foreground_file)[0]}_{resize_factor:.2f}.png"
            output_path = os.path.join(output_folder, output_file)

            # Overlay the foreground image on the background image with the random resize factor
            overlay_images(background_path, foreground_path, output_path, resize_factor)

if __name__ == "__main__":
    # Paths to the background and foreground folders, and the output folder
    background_folder_path = "background"
    foreground_folder_path = "foreground"
    output_folder_path = "output"

    # remove all files in the output folder
    for file in os.listdir(output_folder_path):
        os.remove(os.path.join(output_folder_path, file))

    # Combine every foreground with every background and save in the output folder
    combine_all_images(background_folder_path, foreground_folder_path, output_folder_path)
    print("Image combination completed. Results saved in the output folder.")
