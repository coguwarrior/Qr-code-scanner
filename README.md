Here is a clean, professional README.md you can directly copy-paste.
It’s written clearly for first-time users, offline environments, and defence / shipboard use.

📦 Excel Sheet to QR Code Generator (Offline)

This project generates one QR code per Excel sheet, where:

Each sheet’s data is embedded directly inside the QR code

The QR image file name = sheet name

The sheet name is printed below the QR code

Works 100% offline after setup

Ideal for checklists, inventories, servicing schedules, and shipboard documentation.

🚀 Features

📊 Reads Excel files with multiple sheets

🔳 Generates one QR code per sheet

🏷 Sheet name printed below each QR

📁 Automatically creates output folder

🔐 No cloud, no URLs, no internet dependency

⚙ Compatible with modern Pillow versions (10+)

🗂 Project Structure
project/
│── generate_qr.py        # Main Python script
│── input.xlsx            # Excel file with multiple sheets
│── requirements.txt      # Python dependencies
│── qr_codes/             # Auto-generated QR images

🛠 Requirements

Python 3.8 or higher

Works on Windows / Linux / macOS

Suitable for offline & restricted environments

📦 Installation

Install dependencies using:

python -m pip install -r requirements.txt


⚠ If pip is not available directly, this command always works on Windows.

▶️ How to Run

Place your Excel file as input.xlsx in the project folder

Run the script:

python generate_qr.py

📤 Output

A folder named qr_codes/ is created automatically

One PNG QR image is generated for each Excel sheet

Example:

qr_codes/
│── LSA_Inventory.png
│── FFA_Checklist.png
│── Safety_Equipment.png


Each QR code:

Contains the full sheet data (CSV format)

Displays the sheet name below the QR

Can be scanned offline using any QR scanner

📖 QR Content Format

When scanned, the QR code shows sheet data as text:

Equipment,Serial,Last Service,Next Due
Life Jacket,LJ001,12-08-2024,12-08-2025
Life Buoy,LB014,20-09-2024,20-09-2025

⚠ Important Notes

QR codes have a data size limit

Best suited for:

Checklists

Inventories

Registers

Maintenance logs

Avoid very large sheets (hundreds of rows)

🔐 Offline & Security

Excel file stays on local system

QR codes contain embedded data only

No cloud services or APIs used

Suitable for defence, shipboard, and secure environments

🧩 Customisation Ideas (Future Enhancements)

JSON-encoded QR data

Colour-coded QR borders (Due / Overdue)

QR encryption

Automatic sheet splitting for large data

Export as standalone .exe

📄 License

This project is provided for educational and operational use.
You are free to modify and extend it as required.

👤 Author

Developed using Python for offline documentation and operational efficiency.
