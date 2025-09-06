from pdf2image import convert_from_path
from tkinter import filedialog as fd
import tkinter as tk
import os
from pathlib import Path

def convert_pdf_to_png(pdf_path):
    try:
        images = convert_from_path(f"{pdf_path}.pdf", dpi=100, poppler_path=r"C:\Program Files (x86)\poppler-25.07.0\Library\bin")
        output_folder=f"{pdf_path}_Slides"
        os.makedirs(output_folder, exist_ok=True)

        for i, image in enumerate(images):
            output_filename = os.path.join(output_folder, f"slide_{i+1}.png")
            image.save(output_filename, "PNG")
            print(f"Saved: {output_filename}")
    except Exception as e:
        print(f"Error converting PDF: {e}")

def output_obsidian_markdown(slides_path, pdf_name):
    try:
        slides = sorted(os.listdir(slides_path))
        initial_path = Path(slides_path)
        output_path = initial_path.parent / f"{pdf_name}.md"
        output_file = open(output_path, "a")
        print(f"Created output file {pdf_name}.md")
        for slide in slides:
            if slide.endswith(".png") or slide.endswith(".jpg"):
                output_file.write(f"![[{slides_path}/{slide}]]\n\n- Notes:\n\n---\n")
        print(f"Output finished. Please use the {pdf_name}.md file for your notes")
    except Exception as e:
        print(f"Error reading and outputting markdown {e}")

def main():
    root = tk.Tk()
    root.withdraw()
    file_path = fd.askopenfilename(
        title="Select a PDF",
    )
    if file_path:
        if (not file_path.endswith(".pdf")):
            print("File must be a PDF. Aborting...")
            exit(1)
        file_name = os.path.basename(file_path)
        markdown_name = file_name.split(".")[0]
        file_path = file_path.split(".")[0]
        print(f"The name of your markdown file will be {markdown_name}")
        user_input = input("Press <Enter> to confirm or enter a new name: ")
        markdown_name = markdown_name if not user_input else user_input
        convert_pdf_to_png(file_path)
        output_obsidian_markdown(f"{file_path}_Slides", markdown_name)
    else:
        print("No file selected. Aborting...")
        exit(2)

if __name__ == "__main__":
    main()