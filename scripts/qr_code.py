import qrcode
import image


async def make_qrcode(content, user_id):
    img = qrcode.make(content)
    img.save(f"images/{user_id}.png")
    return open(f"images/{user_id}.png", "rb")
