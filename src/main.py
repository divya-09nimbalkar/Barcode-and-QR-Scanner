from scanner import scan_image

def main():
    print("🚀 Starting Barcode_and_QR_Scanner")
    # Use a proper path string
    sample_file = r"data/raw/test_qr.png"
    result = scan_image(sample_file)
    print(f"Scan result: {result}")

if __name__ == "__main__":
    main()
