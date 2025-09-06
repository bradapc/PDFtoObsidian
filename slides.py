from pdf2image import convert_from_path

def convert_pdf_to_png(pdf_path):
    try:
        images = convert_from_path(pdf_path, dpi=100, poppler_path=r"C:\Program Files (x86)\poppler-25.07.0\Library\bin")
        pdf_name=pdf_path.split('.')[0]
        output_folder=f"{pdf_name}_Slides"
        import os
        os.makedirs(output_folder, exist_ok=True)

        for i, image in enumerate(images):
            output_filename = os.path.join(output_folder, f"slide_{i+1}.png")
            image.save(output_filename, "PNG")
            print(f"Saved: {output_filename}")
    except Exception as e:
        print(f"Error converting PDF: {e}")

def output_obsidian_markdown(slides_path, pdf_name):
    try:
        import os
        slides = sorted(os.listdir(slides_path))
        output_file = open(f"{pdf_name}.md", "a")
        print(f"Created output file {pdf_name}.md")
        for slide in slides:
            if slide.endswith(".png") or slide.endswith(".jpg"):
                output_file.write(f"![[{slides_path}/{slide}]]\n\n- Notes:\n\n---\n")
        print(f"Output finished. Please use the {pdf_name}.md file for your notes")
    except Exception as e:
        print(f"Error reading and outputting markdown {e}")

convert_pdf_to_png("Lecture 2 - Intro to Networks.pdf")
output_obsidian_markdown("Lecture 2 - Intro to Networks_Slides", "Lecture 2 - Intro to Networks")