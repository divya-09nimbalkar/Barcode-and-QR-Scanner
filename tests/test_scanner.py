import pytest
from src.scanner import scan_image

def test_invalid_file():
    assert "File not found" in scan_image("nonexistent.png")

def test_valid_qr(tmp_path):
    # Placeholder: add a sample QR image for testing
    test_file = tmp_path / "qr.png"
    test_file.write_text("fake image")  # Replace with real image
    result = scan_image(str(test_file))
    assert isinstance(result, str)
