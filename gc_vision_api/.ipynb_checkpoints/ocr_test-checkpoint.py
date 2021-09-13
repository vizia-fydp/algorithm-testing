import io
import os
import time

# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = '/home/martin/projects/fydp/test_images/kindle.jpg'

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
        
        t_start = time.time()
        image = vision.Image(content=content)

        # Performs label detection on the image file
        response = client.document_text_detection(image=image)
        labels = response.text_annotations

        print(f"Inference time: {time.time() - t_start:.2f} sec")

        print(response)

