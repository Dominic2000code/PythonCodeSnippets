from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_image_metadata(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Extract the EXIF metadata
    exif_data = image._getexif()

    if exif_data is not None:
        # Create a dictionary to store the metadata
        metadata = {}

        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            
            # Extract DateTimeOriginal tag
            if tag_name == 'DateTimeOriginal':
                metadata[tag_name] = value
            
            # Extract GPSInfo tag
            if tag_name == 'GPSInfo':
                gps_data = {}
                for gps_tag_id in value:
                    gps_tag_name = GPSTAGS.get(gps_tag_id, gps_tag_id)
                    gps_data[gps_tag_name] = value[gps_tag_id]
                metadata[tag_name] = gps_data
        
        return metadata
    else:
        return None

# Provide the path to your image file
image_path = "testImg.jpg"

# Call the function to extract metadata
metadata = get_image_metadata(image_path)

# Print the extracted metadata
if metadata is not None:
    if 'DateTimeOriginal' in metadata:
        print(f"DateTimeOriginal: {metadata['DateTimeOriginal']}")
    else:
        print("DateTimeOriginal tag not found.")
    
    if 'GPSInfo' in metadata:
        gps_data = metadata['GPSInfo']
        if 'GPSLatitude' in gps_data and 'GPSLongitude' in gps_data:
            latitude = gps_data['GPSLatitude']
            longitude = gps_data['GPSLongitude']
            print(f"GPS Latitude: {latitude}")
            print(f"GPS Longitude: {longitude}")
        else:
            print("GPS coordinates not found.")
    else:
        print("GPSInfo tag not found.")
else:
    print("No metadata found.")
