import pandas as pd
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

# -------- CONFIG --------
EXCEL_FILE = "input.xlsx"
OUTPUT_DIR = "qr_codes"
QR_SIZE = 400
FONT_SIZE = 24
# ------------------------

os.makedirs(OUTPUT_DIR, exist_ok=True)

excel = pd.ExcelFile(EXCEL_FILE)

for sheet_name in excel.sheet_names:
    df = excel.parse(sheet_name)

    qr_data = df.to_csv(index=False)

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    qr_img = qr_img.resize((QR_SIZE, QR_SIZE))

    total_height = QR_SIZE + 50
    final_img = Image.new("RGB", (QR_SIZE, total_height), "white")
    final_img.paste(qr_img, (0, 0))

    draw = ImageDraw.Draw(final_img)

    try:
        font = ImageFont.truetype("arial.ttf", FONT_SIZE)
    except:
        font = ImageFont.load_default()

    # Pillow 10+ compatible text sizing
    bbox = draw.textbbox((0, 0), sheet_name, font=font)
    text_width = bbox[2] - bbox[0]
    text_x = (QR_SIZE - text_width) // 2
    text_y = QR_SIZE + 10

    draw.text((text_x, text_y), sheet_name, fill="black", font=font)

    output_path = os.path.join(OUTPUT_DIR, f"{sheet_name}.png")
    final_img.save(output_path)

    print(f"QR generated for sheet: {sheet_name}")

print("All QR codes generated successfully.")
