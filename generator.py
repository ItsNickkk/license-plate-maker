from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
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
		2: 'resources/template/kei.png',
		1: 'resources/template/normal.png',
		3: 'resources/template/comm.png',
		4: 'resources/template/kei-comm.png',
		5: 'resources/template/kari-white.png'
	}

	#List of font color
	FONT_COLOR = {
		1: (25,79,56),
		2: (50,50,50),
		3: (255,255,255),
		4: (243,194,4),
		5: (0, 0, 0)
	}

	#List of font directories
	LIST_FONT = {
		"TRM": 'resources/font/trm.ttf',
		"FZ": 'resources/font/fz.otf'
	}
	
	#List of Hiragana by Font
	FONT_TRM_HIRA = list("あいうかきくけこせを")
	FONT_FZ_HIRA = list("えさすそたちつてとなにぬねのはひふほまみむめもやゆよらりるれろわ")

	#List of LTO Abbreviations
	LIST_TRM_LTO_ABBR = ["ナニワ", "山口", "岐阜", "石川", "浜松", "島根", "横浜", "Ｏ", "Ｉ"]
	LIST_FZ_LTO_ABBR = ["ツクバ", "福島", "北九州", "奈良", "徳島", "金沢", "山口", "富士山", "高知"]

	BOLT_SOURCE = 'resources/template/bolt.png'
	SCREW_SOURCE = 'resources/template/screw.png'

	SCREW_POS = {
		1: ((205, 80), (1130, 80)),
		2: ((205, 50), (1130, 50))
	}

	BOLT_POS = {
		1: (200, 75),
		2: (200, 45)
	}

	def __init__(self, p_lto_abbr, p_class_num, p_hira, p_number, p_bolt, p_screw, p_type: int=1):
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
		self.class_num = self._class_num_format(p_class_num)
		self.class_num_font = self.LIST_FONT["TRM"]
		#Plate Number Setting	
		self.number = self._plate_format(p_number)
		self.number_font = self.LIST_FONT["TRM"]
		#Bolt and Screw Setting
		self.bolt = p_bolt
		self.bolt_position = self._bolt_position(p_type)
		self.bolt_source = self.BOLT_SOURCE
		self.screw = p_screw
		self.screw_position = self._screw_positon(p_type)
		self.screw_source = self.SCREW_SOURCE
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

	def _lto_abbr_font(self, lto_abbr):
		if lto_abbr in self.LIST_TRM_LTO_ABBR:
			return self.LIST_FONT["TRM"]
		elif lto_abbr in self.LIST_FZ_LTO_ABBR:
			return self.LIST_FONT["FZ"]
		else:
			raise LTOAbbreviationNotFoundError

	def _plate_format(self, number):
		if len(number) <= 4:
			if len(number) == 4:
				return f"{number[:2]}-{number[2:]}"
			elif len(number) == 3:
				return f".{number[:1]} {number[1:]}"
			elif len(number) == 2:
				return f".. {number}"
			elif len(number) == 1:
				return f".. .{number}"
		else:
			raise PlateNumberOutOfBoundError
	
	def _class_num_format(self, number):
		if len(number) in (2,3):
			return number
		else:
			raise ClassNumberOutOfBoundError("ClassNumberOutOfBoundError")
	
	def _screw_positon(self, type):
		if type != 5:
			return self.SCREW_POS[1]
		else:
			return self.SCREW_POS[2]
	
	def _bolt_position(self, type):
		if type != 5:
			return self.BOLT_POS[1]
		else:
			return self.BOLT_POS[2]

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
		#Draw screw
		if self.screw:
			screw = Image.open(self.screw_source)
			resized_screw = screw.resize((round(screw.size[0]*0.15), round(screw.size[1]*0.15)))
			img.paste(resized_screw, self.screw_position[0], resized_screw)
			img.paste(resized_screw, self.screw_position[1], resized_screw)
		#Draw Bolt
		if self.bolt:
			bolt = Image.open(self.bolt_source)
			resized_bolt = bolt.resize((round(bolt.size[0]*0.18), round(bolt.size[1]*0.18)))
			img.paste(resized_bolt, self.bolt_position, resized_bolt)
		#generate plate name to be sent back to client
		now = datetime.now()
		date_time = now.strftime("%m%d%Y%H%M%S")
		filename = date_time + "_plate.png"
		img.save(filename)
		return filename
class Error(Exception):
	pass #Base Exception

class HiraganaNotFoundError(Error):
	pass #Exception when plate_hira is not in the list

class LTOAbbreviationNotFoundError(Error):
	pass #Exception when LTO Abbreviation is not in the list

class PlateNumberOutOfBoundError(Error):
	pass #Exception when plate number is not provided//more than 4 characters

class ClassNumberOutOfBoundError(Error):
	pass #Exception when plate number is not provided//more than 3/less than 2 characters

if __name__ == "__main__":
	p = Plate("浜松", "333", "す", "461", False, False, 1)
	print(p)
	p.generatePlate()