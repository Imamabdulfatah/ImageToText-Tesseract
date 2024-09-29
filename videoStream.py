import cv2
import pytesseract

# Path ke tesseract di sistem Anda (sesuaikan jika perlu)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Mengaktifkan video stream dari webcam
cap = cv2.VideoCapture(0)  # 0 untuk kamera default

# Loop untuk membaca setiap frame dari video stream
while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    # Mengonversi frame ke dalam skala abu-abu
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Menggunakan pytesseract untuk mendapatkan teks dari frame
    teks = pytesseract.image_to_string(gray)

    # Menampilkan teks yang terdeteksi di console
    print("Teks dari frame:")
    print(teks)

    # Menampilkan frame dengan OpenCV
    cv2.imshow('Video Stream', frame)

    # Menunggu 1 ms dan keluar jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Melepaskan kamera dan menutup semua jendela
cap.release()
cv2.destroyAllWindows()
