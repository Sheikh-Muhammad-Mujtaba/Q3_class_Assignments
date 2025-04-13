import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from PIL import Image, ImageDraw, ImageOps

def generate_bio_qr():
    """Generate an attractive, auto-redirect QR code for Mujtaba Javed."""

    # Direct URL – opens instantly in most camera apps
    qr = qrcode.QRCode(
        version=8,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Best for logo placement
        box_size=10,
        border=4
    )
    
    qr.add_data("https://linktr.ee/s.m.mujtabajaved")
    qr.make(fit=True)

    # Stylish QR Code with radial color
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=RadialGradiantColorMask(
            center_color=(25, 136, 224),
            edge_color=(9, 91, 156)
        )
    ).convert("RGBA")

    try:
        # Load and resize logo
        logo = Image.open("logo.png").convert("RGBA")
        logo_size = min(img.size) // 5
        logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

        # Create circular mask
        mask = Image.new("L", (logo_size, logo_size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, logo_size, logo_size), fill=255)

        # Make logo circular
        logo.putalpha(mask)

        # Optional: White circle background behind logo
        bg_circle = Image.new("RGBA", (logo_size + 12, logo_size + 12), (255, 255, 255, 255))
        bg_mask = Image.new("L", (logo_size + 12, logo_size + 12), 0)
        draw = ImageDraw.Draw(bg_mask)
        draw.ellipse((0, 0, logo_size + 12, logo_size + 12), fill=255)

        pos = ((img.size[0] - bg_circle.size[0]) // 2, (img.size[1] - bg_circle.size[1]) // 2)
        img.paste(bg_circle, pos, mask=bg_mask)

        # Paste the circular logo on top
        pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
        img.paste(logo, pos, mask=logo)

    except Exception as e:
        print(f"Note: Logo not applied. Error: {e}")

    # Save final QR code
    img.save("mujtaba_bio_qr.png")
    print("✅ QR Code Generated Successfully!")

if __name__ == "__main__":
    generate_bio_qr()
