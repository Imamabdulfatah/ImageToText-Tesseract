# ImageToText-Tesseract

## 📖 Project Overview

`ImageToText-Tesseract` is a simple Python utility that converts images (jpg, png, etc.) to plain text using **OpenCV** for image preprocessing and **Tesseract OCR** via the `pytesseract` wrapper. It demonstrates a minimal end‑to‑end OCR pipeline:

1. Load an image with OpenCV.
2. Convert it to grayscale (optional preprocessing can be added later).
3. Feed the processed image to Tesseract.
4. Print the extracted text to the console.

The repository is intentionally lightweight, making it a great starting point for developers who want to experiment with OCR or integrate text extraction into larger Python projects.

---

## 🛠️ Technologies & Dependencies

| Category      | Technology / Library               |
|--------------|------------------------------------|
| Language     | Python 3.8+                        |
| Image I/O    | `opencv-python` (cv2)              |
| OCR Engine   | Tesseract OCR (installed separately) |
| Python Wrapper| `pytesseract`                      |

> **Note**: Tesseract itself is **not** a Python package; you must install the binary on your system (see *Prerequisites* below).

---

## 📦 Prerequisites

1. **Tesseract OCR binary**
   - **Windows**: Download the installer from the official repo – https://github.com/UB-Mannheim/tesseract/wiki
   - During installation, note the install folder (e.g., `C:\Program Files\Tesseract-OCR`).
   - Add the folder to your `PATH` **or** update `pytesseract.pytesseract.tesseract_cmd` in `main.py` to point to the executable (already configured in the script).
2. **Python 3.8+** – Use your favourite environment manager (venv, conda, etc.).

---

## 🚀 Installation

```bash
# Clone the repository (already done)
# cd into the project folder
cd "C:/Users/admin/Desktop/Gitclone/ImageToText-Tesseract"

# (Optional) create a virtual environment
python -m venv venv
source venv/Scripts/activate  # PowerShell: .\venv\Scripts\Activate.ps1

# Install Python dependencies
pip install -r requirements.txt
```

---

## 🖥️ Usage

1. Place the image you want to process in the project folder (or provide an absolute path).
2. Edit `main.py` – change the `gambar_path` variable to point to your image file.
3. Run the script:

```bash
python main.py
```

You should see output similar to:

```
Teks dari gambar:
Hello World!
```

---

## 📂 Repository Structure

```
ImageToText-Tesseract/
├─ .git/                # Git metadata (auto‑generated)
├─ .gitignore          # Ignored files (currently empty)
├─ main.py             # Core OCR script (already explained)
├─ mainBlob.py         # Variant that reads from a video stream (optional)
├─ requirements.txt    # Python dependencies
├─ README.md           # You are reading it right now!
├─ doc.txt             # Original documentation from upstream author
├─ gambar.png / img.jpg # Sample images (feel free to replace)
├─ tesseract.exe       # Windows build of Tesseract (optional, you can use system install)
└─ videoStream.py      # Example of realtime OCR from webcam/video
```

---

## 🧩 Extending the Project

- **Pre‑processing** – Apply thresholding, noise removal, or deskewing before OCR to improve accuracy.
- **Batch processing** – Loop over a directory of images and write results to a CSV.
- **GUI** – Wrap the script with a lightweight web UI (e.g., Streamlit) for drag‑and‑drop image conversion.

---

## 📜 License

The original repository is licensed under the MIT License. Feel free to modify, distribute, and use it in commercial projects.

---

## 🙏 Acknowledgements

- **Tesseract OCR** – Open‑source OCR engine maintained by Google.
- **OpenCV** – Powerful computer‑vision library.
- **pytesseract** – Convenient Python wrapper around Tesseract.

---

Happy coding! 🎉
