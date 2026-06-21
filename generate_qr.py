import qrcode

# The text you want encoded in the QR
data = "Hello Copilot!"

# Create QR image
img = qrcode.make(data)

# Save into your data/raw folder
img.save("data/raw/test_qr.png")

print("✅ QR code saved as data/raw/test_qr.png")
