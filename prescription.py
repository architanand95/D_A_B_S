import easyocr

def extract_text_from_image(image):
    # Create an OCR reader
    reader = easyocr.Reader(['en'])  # Specify the language(s) you expect to encounter
    
    # Read the text from the image
    result = reader.readtext(image)
    
    # Extract and concatenate the text detected by EasyOCR
    extracted_text = '\n'.join([entry[1] for entry in result])
    
    return extracted_text

# Replace 'image_path.jpg' with the path to your image file
image_text = extract_text_from_image('image.jpg')
print(image_text)
