import cv2
import pytesseract
from textblob import TextBlob

# Path ke tesseract di sistem Anda (sesuaikan jika perlu)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Fungsi untuk mengubah gambar menjadi tulisan
def gambar_ke_tulisan(gambar_path):
    # Membaca gambar menggunakan OpenCV
    img = cv2.imread(gambar_path)

    # Preprocessing: mengubah ke skala abu-abu
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Preprocessing: menghilangkan noise menggunakan Gaussian Blur
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Preprocessing: meningkatkan kontras menggunakan adaptive thresholding
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Preprocessing: resizing gambar untuk meningkatkan akurasi OCR
    resized = cv2.resize(thresh, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Menggunakan pytesseract untuk mendapatkan teks dari gambar
    custom_config = r'--oem 3 --psm 6'  # Menggunakan OEM 3 untuk mode default dan PSM 6 untuk block of text
    teks = pytesseract.image_to_string(resized, config=custom_config)

    return teks

# Fungsi untuk memperbaiki typo pada teks menggunakan TextBlob
def perbaiki_typo(teks):
    blob = TextBlob(teks)
    teks_diperbaiki = blob.correct()
    return str(teks_diperbaiki)

# Path gambar yang ingin diubah menjadi tulisan
gambar_path = 'medis.jpeg'  # Gantilah dengan path gambar Anda

# Mendapatkan teks dari gambar
teks = gambar_ke_tulisan(gambar_path)

# Memperbaiki typo dari hasil OCR
teks_diperbaiki = perbaiki_typo(teks)

# Mencetak hasil teks yang sudah diperbaiki
print("Teks dari gambar setelah perbaikan typo:")
print(teks_diperbaiki)
