from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_exif_data(image_path):
    # Open the image file
    image = Image.open(image_path)
    
    # Retrieve the EXIF data
    exif_data = image.getexif()
    
    if not exif_data:
        print("No EXIF metadata found.")
        return None

    # Create a dictionary to hold the decoded EXIF data
    decoded_exif = {}
    
    for tag_id, value in exif_data.items():
        # Decode the tag ID
        tag = TAGS.get(tag_id, tag_id)
        decoded_exif[tag] = value

    return decoded_exif

# Example usage
image_path = 'mount.jpg'
exif_data = get_exif_data(image_path)

if exif_data:
    for tag, value in exif_data.items():
        print(f"{tag}: {value}")
