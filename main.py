import os
import shutil
import tempfile
from PIL import Image


LOCALAPPDATA = os.getenv('LOCALAPPDATA')
USERPROFILE = os.getenv('USERPROFILE')
splotlight_dir = os.path.join(USERPROFILE, "Pictures\Windows Spotlight")
source_dir = os.path.join(LOCALAPPDATA, "Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets")
file_extension = ".jpg"  # Change this to the desired file extension

if not os.path.exists(splotlight_dir):
    os.makedirs(splotlight_dir)

# Create a temporary directory
temp_dir = tempfile.mkdtemp()

# Iterate through files in the source directory
for filename in os.listdir(source_dir):
  source_file = os.path.join(source_dir, filename)
  destination_file = os.path.join(temp_dir, f"{filename}{file_extension}")

  # Copy the file from the source to the temporary directory
  shutil.copy(source_file, destination_file)
  
  try:
    with Image.open(destination_file) as img:
      width, height = img.size
      if width == 1920 and height == 1080:
        # Copy the image to the specified destination directory
        shutil.copy(destination_file, os.path.join(splotlight_dir, f"{filename}{file_extension}"))
  except Exception as e:
    pass

# Clean up the temporary directory and its contents
shutil.rmtree(temp_dir)
