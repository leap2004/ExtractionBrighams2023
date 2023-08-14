## Installation

To run this project, you'll need to have Python installed on your system. You can follow the steps below to set up and run the project:

1. Clone the repository to your local machine:
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. Install the required Python libraries and dependencies using `pip`:
    pip install -r requirements.txt

   This will install the necessary packages specified in the `requirements.txt` file.

4. Download the spaCy language model by running:

   python -m spacy download en_core_web_sm

## Usage

To process images and extract information using this tool, follow these steps:

1. Place your input images in the `input_images` directory.

2. Run the main processing script:
   python process_images.py

   This script performs the following steps:
   
   - Removes the background and keeps only text from the images.
   - Extracts text from the processed images.
   - Removes text from the original input images.
   - Aggregates extracted information into a CSV file.

3. After running the script, you'll find the results in the following directories:
   - Processed images with removed text: `output_images_noText`
   - Extracted text files: `output_text`
   - Preprocessed images with removed background: `output_images_noBackground`
   - Aggregated CSV file: `output_csv/aggregated_data.csv`

## Acknowledgments

This project uses the following libraries and tools:
- spaCy for named entity recognition
- OpenCV for image processing
- pytesseract for text extraction from images
- mmocr for text detection
- extcolors for color extraction
- autocorrect for text spell checking
