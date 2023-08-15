
class ImageProcessingPipeline:
    def __init__(self):
        self.image_processor = ImageProcessor()
        self.csv_writer = CSVWriter()

    def process_images(self, input_image_path, output_image_path_noText, output_text_path, output_image_path_noBackground, output_csv_path):
        # Validate directory paths
        input_image_path = validate_directory_path(input_image_path)
        output_image_path_noText = validate_directory_path(output_image_path_noText)
        output_text_path = validate_directory_path(output_text_path)
        output_image_path_noBackground = validate_directory_path(output_image_path_noBackground)

        # Step 1: Remove background and keep only text
        self.image_processor.remove_background(input_image_path, output_image_path_noBackground)

        # Step 2: Extract text from the output image
        self.image_processor.text_extract(output_image_path_noBackground, output_text_path)

        # Step 3: Remove text from the original input image
        self.image_processor.remove_text(input_image_path, output_image_path_noText)

        # Step 4: CSV with key words
        self.csv_writer.output_csv(output_csv_path, output_text_path)

        print("Aggregated CSV file created.")
