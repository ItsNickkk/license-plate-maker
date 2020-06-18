from PIL import Image, ImageDraw, ImageFont
#------------
#| 横浜200	|
#|か　10-74	|
#------------
#横浜　= plate_lto_abbr
#200 = plate_class
#か　= plate_hira
#10-74 = plate_number

class Plate:

	PLATE_TYPE = {
		1: "resource/template/normal.png",
		2: "resource/template/kei.png",
		3: "resource/template/comm.png",
		4: "resource/template/kei-comm.png"
	}

	FONT_COLOR = {
		1: (25,79,56),
		2: (50,50,50),
		3: (255,255,255),
		4: (243,194,4)
	}

	#List of Hiragana by Font
	FONT_TRM_HIRA = list("あいうかきくけこせを")
	FONT_FZ_HIRA = list("えさすそたちつてとなにぬねのはひふほまみむめもやゆよらりるれろわ")

	def __init__(self, p_lto_abbr, p_class_num, p_hira, p_number, p_type: int=1):
		self.lto_abbr = p_lto_abbr
		self.class_num = p_class_num
		self.type = self.PLATE_TYPE[p_type]
		self.hira = p_hira
		self.hira_font = "resource/font/trm.ttf" if self.hira in self.FONT_TRM_HIRA else "resource/font/fz.otf"
		self.hira_font_size = 450 if self.hira in self.FONT_TRM_HIRA else 500
		self.font_color = self.FONT_COLOR[p_type]
		self.number = p_number

	def __str__(self):
		return f"""
		LTO Abbreviation: {self.lto_abbr}
		Class Number: {self.class_num}
		Hiragana Character: {self.hira}
		Number: {self.number}
		Path: {self.type}
		"""

	def generatePlate(self):
		img = Image.open(self.type)
		draw = ImageDraw.Draw(img)
		font_lto_abbr = ImageFont.truetype(self.hira_font, self.hira_font_size)
		draw.text((340, 70),self.lto_abbr+"＠"+self.class_num,fill=self.font_color, font=font_lto_abbr)
		img.save("test.png")

if __name__ == "__main__":
    p = Plate("横浜", "200", "か", "11-74", 4)
    print(p)
    p.generatePlate()
# plate_info = Plate("横浜", "200", "か", "11-74", 3)
# plate_info.PLATE_TYPE
# Plate.PLATE_TYPE
# # Get Template
# img = Image.open("resource/template/comm.png")

# # Get Font
# font_area = ImageFont.truetype("resource/font/trm.ttf", 155)
# font_main = ImageFont.truetype("resource/font/trm.ttf", 453)

# # Draw
# draw = ImageDraw.Draw(img)
# draw.text((340, 70),"横浜＠２００",fill=(36,255,165), font=font_area)
# draw.text((55, 250),"か10-74",fill=(36,255,165), font=font_main)

