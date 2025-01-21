Handwritten Text OCR Pipeline

This project implements a Handwritten Text OCR Pipeline that extracts text from images in PDF documents and applies various preprocessing and error correction techniques. The pipeline utilizes EasyOCR for optical character recognition and SpellChecker for spelling correction. The results are evaluated using Character Error Rate (CER) and Word Error Rate (WER) metrics.

Project Structure
graphql
Copy
Edit
Handwritten_Text_OCR/
│
├── src/
│   ├── evaluate.py           # Evaluate the OCR results (CER, WER)
│   ├── pipeline.py           # Main OCR pipeline
│   ├── preprocess.py         # Image preprocessing functions
│   ├── train_model.py        # (Optional) Training the OCR model
│   ├── utils.py              # Utility functions                 # Input PDF files
│
├── results/
│   └── output.txt            # OCR output text
│
├── requirements.txt          # List of dependencies
└── README.md                 # This file
Overview of the Pipeline
The pipeline follows the steps below:

PDF to Images: Converts each page of a PDF document into individual images using the pdf2image library.
Image Preprocessing: Each image is processed to enhance quality for OCR. This step involves:
Converting images to grayscale
Resizing images for consistency
OCR Recognition: The preprocessed images are passed to EasyOCR to extract text.
Text Correction: The recognized text is passed through the SpellChecker to correct spelling errors.
Text Formatting: The corrected text is formatted for better readability.
Save to Output File: The final output is saved to a text file.
Evaluation: The output text is evaluated using CER and WER metrics.
Requirements
You can install all the necessary dependencies listed in requirements.txt using the following command:

Copy
Edit
pip install -r requirements.txt
The requirements.txt file includes the following libraries:

numpy: For numerical operations.
pandas: Data manipulation and analysis.
matplotlib: For plotting results (if needed).
tensorflow: For machine learning and deep learning tasks.
keras: Deep learning API for TensorFlow.
torch: PyTorch framework for machine learning.
opencv-python: For image processing.
pillow: Python Imaging Library (PIL) for image manipulation.
jupyter: For running Jupyter notebooks.
pdf2image: To convert PDF pages to images.
Levenshtein: For calculating string similarity.
easyocr: OCR library for recognizing text.
spellchecker: For spell correction.
Setup and Running the Code
Step 1: Clone the Repository
Clone the repository or download the project files.

Step 2: Install Dependencies
Use the requirements.txt file to install the required libraries:

bash
Copy
Edit
pip install -r requirements.txt
Step 3: Prepare Your PDF File
Place the PDF file from which you want to extract text in the data/ folder.

Step 4: Run the Pipeline
Run the pipeline.py script to process the PDF and extract text:

bash
Copy
Edit
python src/pipeline.py
This will:

Convert the PDF into images.
Process each image through OCR.
Correct the extracted text.
Save the output to results/output.txt.
Step 5: Evaluate the Results
To evaluate the accuracy of the OCR output, run the evaluate.py script:

bash
Copy
Edit
python src/evaluate.py
This will calculate the Character Error Rate (CER) and Word Error Rate (WER) metrics for the OCR results and display them.

How to Use the Code
1. pipeline.py
This is the main script for processing the PDF and extracting the text. It includes the following steps:

Loading PDF images: The PDF is converted into images, and each image is processed.
Preprocessing images: Images are resized and converted to grayscale to improve OCR accuracy.
OCR recognition: EasyOCR is used to recognize text from each image.
Spell correction: After OCR, the text is corrected using the SpellChecker library to fix common OCR errors.
Formatting: The final output is formatted, including proper capitalization.
Saving output: The processed text is saved into a text file.
2. evaluate.py
After running pipeline.py, you can evaluate the accuracy of the OCR results using this script. It calculates:

Character Error Rate (CER): A measure of the number of incorrect characters in the OCR result.
Word Error Rate (WER): A measure of the number of incorrect words in the OCR result.
3. preprocess.py
This script contains functions to preprocess the images before performing OCR. It includes:

Converting images to grayscale.
Resizing the images for consistency.
4. train_model.py
(Optional) If you want to train a custom OCR model, you can modify or use this script to train on your dataset.

5. utils.py
Contains utility functions like loading images from a PDF or other helper functions used in the pipeline.

Example Output
When running the pipeline.py script, the expected output will be:

bash
Copy
Edit
PDF converted to images. Saved to temp_images.
Processing page 1...
OCR result for page 1: AND Am Data ScientiST MY Name 1S RanjitH
Text successfully saved to D:/Handwritten_Text_OCR/results/output.txt
Processing completed!
After running evaluate.py, the output might look like:

bash
Copy
Edit
CER: 95.24%
WER: 444.44%
Evaluation completed successfully.
This indicates the Character Error Rate (CER) and Word Error Rate (WER) of the extracted text compared to the ground truth.

Future Enhancements
Improve OCR accuracy by training a custom model.
Fine-tune preprocessing steps to better handle noisy or low-quality images.
Add additional text correction techniques beyond spell checking.
Troubleshooting
Error: "Unsupported depth of input image"
This error may occur if the image format is incompatible. Ensure the images are properly converted to a NumPy array and preprocessed correctly.

Error: "Invalid input type"
Ensure that the input passed to the OCR function is a valid NumPy array or image object, not a file path or string."# Handwritten_Text_OCR" 
