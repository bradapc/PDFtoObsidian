from pdf2image import convert_from_path

def convert_pdf_to_png(pdf_path, output_folder="output_images"):
    try:
        images = convert_from_path(pdf_path, dpi=100, poppler_path=r"C:\Program Files (x86)\poppler-25.07.0\Library\bin")
        import os
        os.makedirs(output_folder, exist_ok=True)

        for i, image in enumerate(images):
            output_filename = os.path.join(output_folder, f"page_{i+1}.png")
            image.save(output_filename, "PNG")
            print(f"Saved: {output_filename}")
    except Exception as e:
        print(f"Error converting PDF: {e}")

convert_pdf_to_png("test.pdf")