from PIL import Image, ImageDraw, ImageFont

# Get Template
img = Image.open("resource/template/white.png")

# Get Font
font_area = ImageFont.truetype("resource/font/frm.ttf", 155)
font_main = ImageFont.truetype("resource/font/frm.ttf", 453)

# Draw
draw = ImageDraw.Draw(img)
draw.text((340, 70),"横浜＠２００",(25,79,56), font=font_area)
draw.text((55, 250),"か10-74",(25,79,56), font=font_main)

img.save("test.png")