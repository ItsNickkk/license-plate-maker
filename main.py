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

	#List of plate type
	PLATE_TYPE = {
		1: "resource/template/normal.png",
		2: "resource/template/kei.png",
		3: "resource/template/comm.png",
		4: "resource/template/kei-comm.png"
	}

	#List of font color
	FONT_COLOR = {
		1: (25,79,56),
		2: (50,50,50),
		3: (255,255,255),
		4: (243,194,4)
	}

	#List of font directories
	LIST_FONT = {
		"TRM": "resource/font/trm.ttf",
		"FZ": "resource/font/fz.otf"
	}

	#List of Hiragana by Font
	FONT_TRM_HIRA = list("あいうかきくけこせを")
	FONT_FZ_HIRA = list("えさすそたちつてとなにぬねのはひふほまみむめもやゆよらりるれろわ")

	#List of LTO Abbreviations
	LIST_TRM_LTO_ABBR = ["ナニワ", "山口", "岐阜", "石川", "浜松", "島根", "横浜", "Ｏ", "Ｉ"]
	LIST_FZ_LTO_ABBR = ["ツクバ", "福島", "北九州", "奈良", "徳島", "金沢", "山口", "富士山", "高知"]

	

	def __init__(self, p_lto_abbr, p_class_num, p_hira, p_number, p_type: int=1):
		self.type = self.PLATE_TYPE[p_type]
		self.font_color = self.FONT_COLOR[p_type]
		#Hiragana Character Setting
		self.hira = p_hira
		self.hira_font = self._hira_font(p_hira)
		self.hira_font_size = 650 if self.hira in self.FONT_TRM_HIRA else 200
		self.hira_position = (60, 180) if self.hira in self.FONT_TRM_HIRA else (85, 380)
		#LTO abbreviation Setting
		self.lto_abbr = p_lto_abbr
		self.lto_abbr_font = self._lto_abbr_font(self.lto_abbr)
		self.lto_abbr_font_size = 200 if self.lto_abbr in self.LIST_TRM_LTO_ABBR else 175
		self.lto_abbr_position = (340, 70) if self.lto_abbr in self.LIST_TRM_LTO_ABBR else (365, 70)
		#Class Number Setting
		self.class_num = p_class_num
		self.class_num_font = self.LIST_FONT["TRM"]
		#Plate Number Setting	
		self.number = p_number
		self.number_font = self.LIST_FONT["TRM"]

	def __str__(self):
		return f"""
		LTO Abbreviation: {self.lto_abbr}, Font used: {self.lto_abbr_font}
		Class Number: {self.class_num}
		Hiragana Character: {self.hira}, Font used: {self.hira_font}
		Number: {self.number}
		Path: {self.type}
		"""

	def _hira_font(self, letter):
		if letter in self.FONT_TRM_HIRA:
			return self.LIST_FONT["TRM"]
		elif letter in self.FONT_FZ_HIRA:
			return self.LIST_FONT["FZ"]
		else:
			raise HiraganaNotFoundError
			return "null"

	def _lto_abbr_font(self, lto_abbr):
		if lto_abbr in self.LIST_TRM_LTO_ABBR:
			return self.LIST_FONT["TRM"]
		elif lto_abbr in self.LIST_FZ_LTO_ABBR:
			return self.LIST_FONT["FZ"]
		else:
			raise LTOAbbreviationNotFoundError
			return "null"

	def generatePlate(self):
		img = Image.open(self.type)
		draw = ImageDraw.Draw(img)
		#Draw LTO Abbreviation
		font_lto_abbr = ImageFont.truetype(self.lto_abbr_font, self.lto_abbr_font_size)
		draw.text(self.lto_abbr_position,self.lto_abbr,fill=self.font_color, font=font_lto_abbr)
		#Draw Hiragana Character
		font_hira = ImageFont.truetype(self.hira_font, self.hira_font_size)
		draw.text(self.hira_position,self.hira,fill=self.font_color, font=font_hira)
		#Draw Class Number
		font_class_num = ImageFont.truetype(self.class_num_font, 200)
		draw.text((770, 70), self.class_num, fill=self.font_color, font=font_class_num)
		#Draw Number
		font_number = ImageFont.truetype(self.number_font, 400)
		draw.text((335, 300), self.number, fill=self.font_color, font=font_number)
		img.save("test.png")

class Error(Exception):
	pass #Base Exception

class HiraganaNotFoundError(Error):
	pass #Exception when plate_hira is not in the list

class LTOAbbreviationNotFoundError(Error):
	pass #Exception when plate_hira is not in the list

if __name__ == "__main__":
	try:
		p = Plate("横浜", "330", "す", "10-74", 1)
		print(p)
		p.generatePlate()
	except HiraganaNotFoundError:
		print("Hiragana not supported")
	except LTOAbbreviationNotFoundError:
		print("LTO Abbreviation not supported")
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

