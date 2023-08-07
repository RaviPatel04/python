import qrcode 

# # simple
# image = qrcode.make("https://github.com/RaviPatel04")
# image.save("github_profile.png")

# color qrcode
from PIL import Image

qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=30,
        border=5,
    )
qr.add_data("https://github.com/RaviPatel04?tab=repositories")
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="black")
img.save("github_profile_repo.png")