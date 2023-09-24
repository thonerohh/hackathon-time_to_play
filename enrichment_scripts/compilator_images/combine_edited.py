from PIL import Image
import os

def overlay_images(background_path, foreground_path, output_path):
    # Open the background and foreground images
    background = Image.open(background_path)
    foreground = Image.open(foreground_path)

    # Resize the foreground image to fit the background
    foreground = foreground.resize((background.width, background.height))

    # Ensure the foreground image has an alpha channel (transparency)
    foreground_with_alpha = foreground.convert("RGBA")

    # Extract the alpha channel from the foreground image and use it as the mask
    alpha_mask = foreground_with_alpha.split()[3]

    # Paste the foreground image onto the background using the alpha mask
    result = Image.new("RGBA", background.size)
    result.paste(background, (0, 0))
    result.paste(foreground_with_alpha, (0, 0), mask=alpha_mask)

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

            # Generate the output image file path
            output_file = f"{os.path.splitext(background_file)[0]}_{os.path.splitext(foreground_file)[0]}.png"
            output_path = os.path.join(output_folder, output_file)

            # Overlay the foreground image on the background image
            overlay_images(background_path, foreground_path, output_path)

if __name__ == "__main__":
    # Paths to the background and foreground folders, and the output folder
    background_folder_path = "background"
    foreground_folder_path = "foreground"
    output_folder_path = "output"

    # Combine every foreground with every background and save in the output folder
    combine_all_images(background_folder_path, foreground_folder_path, output_folder_path)
    print("Image combination completed. Results saved in the output folder.")
