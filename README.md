# QR-Code-Generator

## QR Code Generator with Unique Citizen ID

This project generates QR codes that, when scanned, display a unique JSON object containing a `citizenId`. Additionally, the QR code image includes a custom message and name below it.

---

## Features
- Generates a unique `citizenId` for each QR code using Python's `uuid` module.
- Embeds the `citizenId` into the QR code in JSON format.
- Adds a custom name and message below the QR code.
- Outputs the final QR code as an image file.

---

## Requirements
Before you start, make sure you have the following installed:

1. **Python 3.7+**  
2. Required Python libraries:
   - `qrcode`
   - `Pillow` (PIL)

---

## Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/qr-code-generator.git
   cd qr-code-generator
   
2. **Create and Activate a Virtual Environment (Optional but recommended)**
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies**
bash
pip install qrcode[pil]

**File Structure**
qr-code-generator/
│
├── gen_qr.py          # Main script to generate QR codes
├── README.md          # Project documentation
└── output/            # Folder to store generated QR code images

**Execution Steps**
1. *Run the Python Script* Use the following command to execute the script and generate QR codes:
bash
python gen_qr.py

2. *Output*
QR code images will be saved in the output/ folder (ensure it exists).
Each image will have the corresponding name as its filename.

3. *Example QR Code Output* When scanned, the QR code will display:
json
{"citizenId": "77bd66a4-c84f-48f1-97c5-5e42c7c766d0"}
Below the QR code, the name and custom message will appear:
Anjali Verma
Maine kiya hai sankalp swasthya ka,
jiska hai aadhaar Ayurveda ka.

**Customization**
1. Change Names
Modify the names list in the script to include the desired names.

2. Custom Message
Update the message variable in the script to personalize the message.

3. QR Code Dimensions
Adjust box_size and border in the qrcode.QRCode() initialization for resizing.

**Troubleshooting**
1. Module Not Found Error
Ensure you’ve installed the required libraries with:
bash
pip install qrcode[pil]

2. Text Misalignment
If the text appears misaligned, ensure the arial.ttf font is correctly installed. Alternatively, use the default font:
python
font = ImageFont.load_default()

3. QR Code Not Scanning
Increase box_size to a higher value (e.g., box_size=15) to make the QR code more scannable.

**Contributing**
Feel free to fork this repository and submit pull requests. Contributions are welcome!
