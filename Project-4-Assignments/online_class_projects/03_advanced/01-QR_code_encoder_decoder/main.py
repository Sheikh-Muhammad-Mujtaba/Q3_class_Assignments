import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
import os


def generate_qr(
    data: str, 
    filename: str = "myqr.png",
    version: int = 8,
    box_size: int = 10,
    fill_color: str = "black",
    back_color: str = "white"
) -> None:
    
    qr = qrcode.QRCode(
        version=version,
        box_size=box_size,
        border=2
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(filename)
    print(f"\n✅ QR code saved as: {filename}\n")


def decode_qr(filename: str = "./myqr.png") -> None:
    
    if not os.path.exists(filename):
        print(f"\n⚠️ File '{filename}' not found.")
        return
    
    img = Image.open(filename)
    results = decode(img)
    
    if results:
        print("\n✅ Decoded data:")
        for obj in results:
            print(f"📦 {obj.data.decode('utf-8')}")
    
    else:
        print("\n❌ No QR code found in the image.")


def main() -> None:
    
    while True:
        print("\n🔷 QR Code Tool 🔷")
        print("1. Encode QR Code")
        print("2. Decode QR Code")
        print("3. Exit")
        choice: str = input("Enter your choice (default: 1): ").strip() or "1"

        if choice == "1":
            data: str = input("Enter the data to encode: ").strip()
            if not data:
                print("❌ Data cannot be empty.")
                continue

            try:
                version_input: str = input("Enter the Version of QR Code (1–40, default: 8): ").strip() or "8"
                version: int = int(version_input)
                if not (1 <= version <= 40):
                    raise ValueError("Version must be between 1 and 40.")

                box_size_input: str = input("Enter the box Size (default: 10): ").strip() or "10"
                box_size: int = int(box_size_input)
                if not (1 <= box_size <= 50):
                    raise ValueError("Box size should be reasonable (e.g., 1–50).")

            except ValueError as e:
                print(f"❌ Error: {e}")
                continue

            fill_color: str = input("Enter the fill color (default: black): ").strip() or "black"
            back_color: str = input("Enter the background color (default: white): ").strip() or "white"
            filename: str = input("Enter filename to save (default: myqr.png): ").strip() or "myqr.png"

            generate_qr(data, filename, version, box_size, fill_color, back_color)

        elif choice == "2":
            filename: str = input("Enter file path with filename to decode (default: myqr.png): ").strip() or "myqr.png"
            decode_qr(filename)

        elif choice == "3":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
