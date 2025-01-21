from pdf2image import convert_from_path
import os

def load_images_from_pdf(pdf_path, output_folder="temp_images", dpi=300):
    try:
        images = convert_from_path(pdf_path, dpi=600)
        
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        image_paths = []
        for idx, img in enumerate(images):
            image_path = os.path.join(output_folder, f"page_{idx + 1}.png")
            img.save(image_path)
            image_paths.append(image_path)
        
        print(f"PDF converted to images. Saved to {output_folder}.")
        return image_paths
    except Exception as e:
        print(f"Error loading images from PDF: {e}")
        raise
