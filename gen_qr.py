import qrcode
from PIL import Image, ImageDraw, ImageFont
import uuid

def generate_qr_with_text(name, output_file):
    # Generate a unique citizen ID
    citizen_id = str(uuid.uuid4())
    qr_data = {"citizenId": citizen_id}  # Data to encode in QR Code

    # Create QR Code
    qr = qrcode.QRCode(version=1, box_size=10, border=4)  # Larger box_size ensures clarity
    qr.add_data(qr_data)  # Encode JSON data in QR Code
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Create a canvas to add text below the QR code
    canvas_width = qr_img.width
    canvas_height = qr_img.height + 100  # Extra space for text
    canvas = Image.new('RGB', (canvas_width, canvas_height), 'white')
    canvas.paste(qr_img, (0, 0))

    # Add text below QR Code
    draw = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.truetype("arial.ttf", 18)  # Adjust font size as needed
    except IOError:
        font = ImageFont.load_default()

    # Text formatting
    message = (
        f"{name}\n"
        "Maine kiya hai sankalp swasthya ka,\n"
        "jiska hai aadhaar Ayurveda ka."
    )
    lines = message.split("\n")
    y_text = qr_img.height + 10

    for line in lines:
        text_width, text_height = draw.textsize(line, font=font)
        draw.text(((canvas.width - text_width) / 2, y_text), line, fill="black", font=font)
        y_text += text_height + 5  # Add spacing between lines

    # Save the final image
    canvas.save(output_file)

    print(f"QR Code saved to {output_file}")
    print(f"Generated Citizen ID: {citizen_id}")

# Example Usage
names = ["Nagendra U S", "Rahul Sharma", "Anjali Verma"]

for name in names:
    output_file = f"{name.replace(' ', '_')}_qr.png"
    generate_qr_with_text(name, output_file)
