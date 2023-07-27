import qrcode

# Data to be represented
data = "Hello, World!"

# Create qr code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data to qr code
qr.add_data(data)

# Compile the data into a QR code array
qr.make(fit=True)

# Print the image to the console (requires pillow)
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("hello_world_qr.png")
