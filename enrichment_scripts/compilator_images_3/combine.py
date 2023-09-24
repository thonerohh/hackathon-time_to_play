from PIL import Image
import os

def calculate_max_dimensions(background_width, background_height):
    # Calculate the maximum width and height for the foreground image (80% of background width or height)
    max_width = int(background_width * 0.72)
    max_height = int(background_height * 0.72)
    return max_width, max_height

def resize_image(image, max_width, max_height):
    # Resize the image while maintaining its aspect ratio
    image.thumbnail((max_width, max_height))
    return image

def overlay_images(background_path, foreground_path, output_path):
    # Open the background (JPG) image
    background = Image.open(background_path)

    # Calculate maximum dimensions for the foreground image
    max_width, max_height = calculate_max_dimensions(background.width, background.height)

    # Open the foreground (PNG) image with an alpha channel and resize it
    foreground = Image.open(foreground_path).convert('RGBA')
    foreground_resized = resize_image(foreground, max_width, max_height)

    # Calculate position to center the resized foreground image
    x_position = (background.width - foreground_resized.width) // 2
    y_position = (background.height - foreground_resized.height) // 2

    # Paste the resized foreground image onto the background image
    background.paste(foreground_resized, (x_position, y_position), foreground_resized)

    # Save the resulting image
    background.save(output_path)

if __name__ == "__main__":
    # Path to the folders
    foreground_folder = "foreground"
    background_folder = "background"
    output_folder = "output"

    # Iterate through foreground images
    for foreground_filename in os.listdir(foreground_folder):
        foreground_path = os.path.join(foreground_folder, foreground_filename)

        # Check if the file is an image (PNG format)
        if foreground_filename.lower().endswith(('.png')):
            # Iterate through background images
            for background_filename in os.listdir(background_folder):
                background_path = os.path.join(background_folder, background_filename)

                # Generate output filename based on the foreground and background filenames
                output_filename = f"{os.path.splitext(foreground_filename)[0]}_{os.path.splitext(background_filename)[0]}.png"
                output_path = os.path.join(output_folder, output_filename)

                # Overlay foreground and background images and save the output
                overlay_images(background_path, foreground_path, output_path)
                # print(f"Combined {foreground_filename} with {background_filename} and saved to {output_filename}")