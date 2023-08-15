import os
from image_processing_pipeline import ImageProcessingPipeline

if __name__ == "__main__":
    user_documents = os.path.expanduser("~/Documents")
    input_image_path = os.path.join(user_documents, "pics")
    output_image_path_noText = os.path.join(user_documents, "output_images")
    output_text_path = os.path.join(user_documents, "output_text")
    output_image_path_noBackground = os.path.join(user_documents, "PreprocessedImages")
    output_csv_path = os.path.join(user_documents, "output_csv")

    pipeline = ImageProcessingPipeline()
    pipeline.process_images(input_image_path, output_image_path_noText, output_text_path, output_image_path_noBackground, output_csv_path)
