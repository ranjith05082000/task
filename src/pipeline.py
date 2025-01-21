import os
from PIL import Image
import numpy as np
import easyocr
from utils import load_images_from_pdf
from preprocess import preprocess_image
from spellchecker import SpellChecker

reader = easyocr.Reader(['en'], gpu=False)

def ocr_recognition(image):
    try:
        result = reader.readtext(np.array(image))
        text = " ".join([entry[1] for entry in result])
        return text
    except Exception as e:
        print(f"Error during OCR recognition: {e}")
        raise

def save_text_to_file(text, output_txt, append_mode=True):
    try:
        mode = 'a' if append_mode else 'w'
        with open(output_txt, mode, encoding="utf-8") as f:
            f.write(text)
        print(f"Text successfully saved to {output_txt}")
    except Exception as e:
        print(f"Error saving text to file: {e}")
        raise

def process_pdf_to_text(pdf_path, output_txt, clear_file=True):
    if clear_file:
        with open(output_txt, "w", encoding="utf-8") as f:
            pass
        print(f"Cleared the file: {output_txt}")

    try:
        image_paths = load_images_from_pdf(pdf_path)
        full_text = ""

        for page_num, image_path in enumerate(image_paths):
            try:
                print(f"Processing page {page_num + 1}...")
                image = Image.open(image_path)
                preprocessed_image = preprocess_image(image)
                preprocessed_image.save(f"temp_preprocessed_images/page_{page_num + 1}.png")

                text = ocr_recognition(preprocessed_image)
                print(f"OCR result for page {page_num + 1}: {text}")

                page_text = f"Page {page_num + 1}:\n{text}\n\n"
                full_text += page_text
                save_text_to_file(page_text, output_txt, append_mode=True)
            except Exception as e:
                print(f"Error processing page {page_num + 1}: {e}")

        print("Processing completed!")
    except Exception as e:
        print(f"Error during PDF processing: {e}")
        raise

def preprocess_image(image):
    if isinstance(image, str):
        image = Image.open(image)

    image = image.convert("L")
    image = image.resize((1024, 1024))

    image_array = np.array(image)
    processed_image = Image.fromarray(image_array)
    return processed_image

if __name__ == "__main__":
    pdf_path = "D:/Handwritten_Text_OCR/data/Kaggle/new.pdf"
    output_txt = "D:/Handwritten_Text_OCR/results/output.txt"

    process_pdf_to_text(pdf_path, output_txt)
