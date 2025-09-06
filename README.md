# PDF to Obsidian Slides Converter

Convert a PDF into a folder of slide images and a companion Markdown note tailored for [Obsidian](https://obsidian.md/).  
Each slide is embedded and followed by a small notes section so you can annotate lectures or decks quickly.

---

## Features

- One PNG per PDF page (slide).
- Images saved to a `<PDF_Name>_Slides` folder.
- Auto-generated `<PDF_Name>.md` with Obsidian-style embeds:
  - `![[<PDF_Name>_Slides/slide_1.png]]`
  - A `- Notes:` area under each slide
  - `---` separators between slides

**Example Markdown output snippet:**

```markdown
![[MyLecture_Slides/slide_1.png]]

- Notes:

---

![[MyLecture_Slides/slide_2.png]]

- Notes:

---
```

---

## Requirements

### Python
- **Python 3.7+**

### Python packages (requirements.txt)
Copy this into a file named **`requirements.txt`**, then install with `pip install -r requirements.txt`:

```txt
pdf2image
natsort
```

> `tkinter` is used for the file picker, but it’s part of standard Python installs on Windows and macOS.  
> On Debian/Ubuntu you may need: `sudo apt install python3-tk`.

### Poppler (required by `pdf2image`)
Install Poppler and ensure its `bin` directory is on your system `PATH`, **or** pass its location to `convert_from_path` via `poppler_path` (as this script does).

- **Windows:**  
  Download a Poppler build (e.g., from a reputable Windows build provider), unzip, and use the path to `...\poppler-XX\Library\bin`.  
  You can also add that `bin` folder to your **PATH**.
- **macOS:**  
  `brew install poppler`
- **Linux (Debian/Ubuntu):**  
  `sudo apt install poppler-utils`

---

## Installation

1. Clone or download this repository.
2. (Recommended) Create and activate a virtual environment.
3. Install Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Install Poppler (see above) and note its `bin` path if you won’t add it to `PATH`.

---

## Usage

Run the script (assuming the filename is `pdf_to_obsidian.py`):

```bash
python pdf_to_obsidian.py
```

1. A file dialog appears; select your `.pdf`.  
2. The script:
   - Creates `<PDF_Name>_Slides/` with `slide_1.png`, `slide_2.png`, …
   - Creates `<PDF_Name>.md` **next to** the selected PDF (or in the chosen file’s folder).
3. Open the generated `.md` in Obsidian and start taking notes under each slide.

---

## Output Structure

If you select `Lecture1.pdf`, you’ll get:

```
Lecture1_Slides/
  ├── slide_1.png
  ├── slide_2.png
  ├── slide_3.png
Lecture1.md
```

And `Lecture1.md` contains Obsidian embeds like:

```markdown
![[Lecture1_Slides/slide_1.png]]

- Notes:

---

![[Lecture1_Slides/slide_2.png]]

- Notes:

---
```

---

## Configuration

- **DPI (image quality & size):**  
  The script uses `dpi=100` in `convert_from_path(...)` for a good size/quality balance.  
  Increase for sharper images; decrease for smaller files.

- **Poppler path (Windows / custom installs):**  
  The script passes an explicit `poppler_path`, e.g.:
  ```python
  convert_from_path(f"{pdf_path}.pdf", dpi=100, poppler_path=r"C:\Program Files (x86)\poppler-25.07.0\Library\bin")
  ```
  Update this string to match your system, or add Poppler’s `bin` to your PATH and remove the parameter.

- **Markdown filename:**  
  You’ll be prompted to confirm or override the default Markdown name (derived from the PDF filename).

---

## Troubleshooting

- **“File must be a PDF. Aborting…”**  
  Make sure you selected a `.pdf` file.

- **Poppler not found / conversion errors:**  
  Verify Poppler is installed and the `poppler_path` points to the correct `bin` directory, or that `bin` is on your PATH.

- **Large output size:**  
  Lower the `dpi` value (e.g., 100 → 75) to shrink PNG sizes.

- **`tkinter` import error on Linux:**  
  Install the Tk package for your distro, e.g., `sudo apt install python3-tk`.

---
