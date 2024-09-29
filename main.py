import cv2
import pytesseract

# Path ke tesseract di sistem Anda (sesuaikan jika perlu)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Fungsi untuk mengubah gambar menjadi tulisan
def gambar_ke_tulisan(gambar_path):
    # Membaca gambar menggunakan OpenCV
    img = cv2.imread(gambar_path)

    # Mengonversi gambar ke dalam skala abu-abu
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Menggunakan pytesseract untuk mendapatkan teks dari gambar
    teks = pytesseract.image_to_string(gray)

    return teks

# Path gambar yang ingin diubah menjadi tulisan
gambar_path = 'img.jpg'  # Gantilah dengan path gambar Anda

# Mendapatkan teks dari gambar
teks = gambar_ke_tulisan(gambar_path)

# Mencetak hasil teks
print("Teks dari gambar:")
print(teks)
