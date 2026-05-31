import argparse
import re
import logging
from pathlib import Path
from PIL import Image

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def natural_sort_key(s: str) -> list:
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', str(s))]

def images_to_pdf_and_clean(folder_path: str, output_filename: str = "compiled.pdf") -> None:
    target_dir = Path(folder_path)
    if not target_dir.is_dir():
        logging.error(f"Folder not found: {target_dir}")
        return
    valid_extensions = {".png", ".jpg", ".jpeg"}
    image_files = sorted(
        [f for f in target_dir.iterdir() if f.is_file() and f.suffix.lower() in valid_extensions],
        key=lambda x: natural_sort_key(x.name)
    )
    if not image_files:
        logging.warning("No valid image files found in the folder.")
        return
    output_pdf_path = target_dir / output_filename
    opened_images = []
    try:
        for img_path in image_files:
            img = Image.open(img_path).convert('RGB')
            opened_images.append((img_path, img))
            
        first_img = opened_images[0][1]
        remaining_imgs = [img for _, img in opened_images[1:]]
        first_img.save(output_pdf_path, save_all=True, append_images=remaining_imgs)
        logging.info(f"Successfully exported PDF file at: {output_pdf_path}")
        for _, img in opened_images:
            img.close()
        for img_path, _ in opened_images:
            img_path.unlink()
            
        logging.info("Successfully cleaned up the original image files!")
        
    except Exception as e:
        logging.error(f"An error occurred during processing: {e}")
        for _, img in opened_images:
            img.close()
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to combine images into a PDF file and clean up the folder.")
    parser.add_argument("folder", help="Path to the folder containing images to process")
    parser.add_argument("-o", "--output", default="compiled.pdf", help="Output PDF file name (default: compiled.pdf)")
    
    args = parser.parse_args()
    
    images_to_pdf_and_clean(args.folder, args.output)