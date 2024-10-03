import cv2 as cv
import os

# Load the image
input_image_path = 'kino.jpg'
output_image_path = 'output.jpg'

def apply_clahe(input_image_path: str, output_image_path: str):
    # Check if the input image file exists
    if not os.path.isfile(input_image_path):
        print(f"Error: The file {input_image_path} does not exist.")
        exit()

    # Read the image using OpenCV
    image = cv.imread(input_image_path, 1)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Could not read the image.")
        exit()

    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    lab_image = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)  # Convert to LAB
    y, cr, cb = cv.split(lab_image)  # Split to 3 channels
    y = clahe.apply(y)  # Apply CLAHE to the L channel

    # Merge the channels back correctly
    lab_image = cv.merge([y, cr, cb])  # Pass as a list
    applied_image = cv.cvtColor(lab_image, cv.COLOR_YCrCb2BGR)  # Convert back to BGR

    # Save the processed image using Pillow
    _ = cv.imwrite(output_image_path, applied_image)
    print(f"Processed image saved as {output_image_path}")

if __name__ == '__main__':
    try:
        apply_clahe(input_image_path, output_image_path)
    except Exception as e:
        print('Error: %s' % e)
