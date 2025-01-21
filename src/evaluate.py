import Levenshtein

def calculate_cer(ground_truth, ocr_output):
    if len(ground_truth) == 0:
        raise ValueError("Ground truth is empty. Cannot calculate CER.")
    distance = Levenshtein.distance(ground_truth, ocr_output)
    cer = distance / len(ground_truth) * 100
    return cer

def calculate_wer(ground_truth, ocr_output):
    ground_truth_words = ground_truth.split()
    ocr_output_words = ocr_output.split()
    if len(ground_truth_words) == 0:
        raise ValueError("Ground truth is empty. Cannot calculate WER.")
    distance = Levenshtein.distance(" ".join(ground_truth_words), " ".join(ocr_output_words))
    wer = distance / len(ground_truth_words) * 100
    return wer

def evaluate_ocr(ground_truth, ocr_output):
    try:
        cer = calculate_cer(ground_truth, ocr_output)
        wer = calculate_wer(ground_truth, ocr_output)
        print(f"CER: {cer:.2f}%")
        print(f"WER: {wer:.2f}%")
        return cer, wer
    except ValueError as e:
        print(f"Error during evaluation: {e}")
        return None, None

if __name__ == "__main__":
    ground_truth_file = "D:/Handwritten_Text_OCR/data/ground_truth.txt"
    ocr_output_file = "D:/Handwritten_Text_OCR/results/output.txt"
    
    with open(ground_truth_file, "r", encoding="utf-8") as gt_file:
        ground_truth = gt_file.read().strip()
    
    with open(ocr_output_file, "r", encoding="utf-8") as ocr_file:
        ocr_output = ocr_file.read().strip()

    cer, wer = evaluate_ocr(ground_truth, ocr_output)
    
    if cer is not None and wer is not None:
        print("Evaluation completed successfully.")
    else:
        print("Evaluation failed due to missing or empty ground truth.")
