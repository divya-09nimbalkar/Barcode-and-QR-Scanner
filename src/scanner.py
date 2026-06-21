import cv2
import os

def scan_image(image_path: str) -> str:
    """Scan a QR code or barcode from an image file."""
    if not os.path.exists(image_path):
        return "❌ File not found"

    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)

    if data:
        return f"✅ QR/Barcode detected: {data}"
    else:
        return "⚠️ No QR/Barcode found"
