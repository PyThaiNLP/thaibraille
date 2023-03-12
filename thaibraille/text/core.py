# -*- coding: utf-8 -*-
import re
from pythainlp.util import Trie
from pythainlp.tokenize import word_tokenize

thai_braille_mapping_dict = {
    "ก":["1234"],
    "ข":["15"],
    "ฃ":["456", "15"],
    "ค":["156"],
    "ฅ":["56", "156"],
    "ฆ":["6", "156"],
    "ง":["12346"],
    "จ":["234"],
    "ฉ":["25"],
    "ช":["256"],
    "ซ":["2356"],
    "ฌ":["6", "256"],
    "ญ":["6", "12456"],
    "ฎ":["6", "124"],
    "ฏ":["6", "1346"],
    "ฐ":["6", "2345"],
    "ฑ":["6", "23456"],
    "ฒ":["56", "23456"],
    "ณ":["6", "1245"],
    "ด":["124"],
    "ต":["1346"],
    "ถ":["2345"],
    "ท":["23456"],
    "ธ":["456", "23456"],
    "น":["1245"],
    "บ":["1356"],
    "ป":["12356"],
    "ผ":["1235"],
    "ฝ":["1256"],
    "พ":["1246"],
    "ฟ":["1236"],
    "ภ":["6", "1246"],
    "ม":["125"],
    "ย":["12456"],
    "ร":["1345"],
    "ล":["135"],
    "ว":["2346"],
    "ศ":["6", "235"],
    "ษ":["56", "235"],
    "ส":["235"],
    "ห":["134"],
    "ฬ":["6", "135"],
    "อ":["145"],
    "ฮ":["123456"],
    "1":["1"],
    "2":["13"],
    "3":["12"],
    "4":["124"],
    "5":["14"],
    "6":["123"],
    "7":["1234"],
    "8":["134"],
    "9":["23"],
    "0":["234"],
    "๑":["1"],
    "๒":["13"],
    "๓":["12"],
    "๔":["124"],
    "๕":["14"],
    "๖":["123"],
    "๗":["1234"],
    "๘":["134"],
    "๙":["23"],
    "๐":["234"],
    "ะ":['1'],
    "า":['16'],
    "ิ":['13'],
    "ี":['35'],
    "ุ":['12'],
    "ู":['34'],
    "ึ":['236'],
    "ื":['36'],
    "เ":['123'],
    "โ":['23'],
    "ั":['245'],
    "ำ":['1456'],
    "แ":['136'],
    "ไ":['146'],
    "่":['45'],
    "้":['346'],
    "๊":['3456'],
    "๋":['356'],
    "์":['456'],
    "ๆ":['3'],
    " ":['-1'],
    "<N>":['2456']
}

dict_2 = {
    "เ-อ":['126'],
    "เ-ีย":['13456'],
    "เ-ือ":['12345'],
    "-ัว":['14'],
    "เ-า":['345'],
    "เ-าะ":['145', '1']
}

# number start with '2456'

def replace_number(word):
    if word[0] in list("1234567890๐๑๒๓๔๕๖๗๘๙"):
        return '<N>'+word
    return word

thai_braille_mapping_dict = dict(thai_braille_mapping_dict, **dict_2)

_v1=["เ-tอ", "เ-ีtย", "เ-ืtอ", "-ัtว", "เ-tา", "เ-tาะ"]

char_trie = Trie(list(thai_braille_mapping_dict.keys())+_v1+[" ","<N>"])


_vowel_patterns =[i.replace("-","([ก-ฮ])").replace("t","([่้๊๋])")+",\\1"+i.replace("t","")+"\\2" for i in _v1]
_vowel_patterns += [i.replace("-","([ก-ฮ])")+",\\1"+i for i in dict_2.keys()]
_VOWELS = [x.split(",") for x in _vowel_patterns]

def _replace_vowels(word: str) -> str:
    for vowel in _VOWELS:
        word = re.sub(vowel[0], vowel[1], word)

    return word

def thai_word_braille(word: str) -> str:
    word = _replace_vowels(word)
    word = replace_number(word)
    _temp = []
    for i in word_tokenize(word,custom_dict=char_trie, engine="mm"):
       if i.isspace() and len(i)>1:
        for k in list(i):
            _temp.append(thai_braille_mapping_dict[k])
       else:
        _temp.append(thai_braille_mapping_dict[i])
    _b = Braille(_temp)
    return _b.tobraille()


def thai_text_braille(text: str) -> list:
    _list_braille = []
    for word in word_tokenize(text):
        _list_braille.append(thai_word_braille(word))
    return _list_braille


class Braille:
	'''
    List Braille to Braille
	'''
	def __init__(self,data):
		self.inputdata=data
		if isinstance(data, list): # หากข้อมูลเป็นชนิด list
			if len(data)>1: # หากมี list มากกว่าหนึ่ง
				self.data =['']*len(data) # สร้าง list ซ้อน list ตามจำนวนที่มี
				self.i=0
				while self.i<len(data): # ทำการลูปตามจำนวน list ที่ซ้อนใน data
					self.data[self.i] = sorted(list(data[self.i])) #  ทำการแปลงข้อมูลใน list ให้เป็น list
					self.i+=1
			else: # หากมี ['12'] อันเดียว
				self.data =sorted(list(data[0]))
		else:
			self.data = sorted(list(data)) # แปลงเป็น list พร้อมเรียงจากน้อยไปมาก
		self.db = {
            "-1":" ",
            '0':'⠀',
            '1':'⠁',
            '3':'⠂',
            '13':'⠃',
            '5':'⠄',
            '15':'⠅',
            '35':'⠆',
            '135':'⠇',
            '2':'⠈',
            '12':'⠉',
            '23':'⠊',
            '123':'⠋',
            '25':'⠌',
            '125':'⠍',
            '235':'⠎',
            '1235':'⠏',
            '⠐':'4',
            '14':'⠑',
            '34':'⠒',
            '134':'⠓',
            '45':'⠔',
            '145':'⠕',
            '1345':'⠗',
            '24':'⠘',
            '124':'⠙',
            '234':'⠚',
            '1234':'⠛',
            '245':'⠜',
            '1245':'⠝',
            '2345':'⠞',
            '12345':'⠟',
            '6':'⠠',
            '16':'⠡',
            '36':'⠢',
            '136':'⠣',
            '56':'⠤',
            '156':'⠥',
            '356':'⠦',
            '1356':'⠧',
            '26':'⠨',
            '126':'⠩',
            '236':'⠪',
            '1236':'⠫',
            '256':'⠬',
            '1256':'⠭',
            '2356':'⠮',
            '12356':'⠯',
            '46':'⠰',
            '146':'⠱',
            '346':'⠲',
            '1346':'⠳',
            '456':'⠴',
            '1456':'⠵',
            '3456':'⠶',
            '13456':'⠷',
            '246':'⠸',
            '1246':'⠹',
            '2346':'⠺',
            '12346':'⠻',
            '2456':'⠼',
            '12456':'⠽',
            '23456':'⠾',
            '123456':'⠿',
            '7':'⡀',
            '17':'⡁',
            '37':'⡂',
            '137':'⡃',
            '57':'⡄',
            '157':'⡅',
            '357':'⡆',
            '1357':'⡇',
            '27':'⡈',
            '127':'⡉',
            '237':'⡊',
            '1237':'⡋',
            '257':'⡌',
            '1257':'⡍',
            '2357':'⡎',
            '12357':'⡏',
            '47':'⡐',
            '147':'⡑',
            '1257':'⡍',
            '2357':'⡎',
            '12357':'⡏',
            '47':'⡐',
            '147':'⡑',
            '347':'⡒',
            '1347':'⡓',
            '457':'⡔',
            '1457':'⡕',
            '3457':'⡖',
            '13457':'⡗',
            '247':'⡘',
            '1247':'⡙',
            '2347':'⡚',
            '12347':'⡛',
            '2457':'⡜',
            '12457':'⡝',
            '23457':'⡞',
            '123457':'⡟',
            '67':'⡠',
            '167':'⡡',
            '367':'⡢',
            '1367':'⡣',
            '567':'⡤',
            '1567':'⡥',
            '3567':'⡦',
            '13567':'⡧',
            '267':'⡨',
            '1267':'⡩',
            '2367':'⡪',
            '12367':'⡫',
            '2567':'⡬',
            '12567':'⡭',
            '23567':'⡮',
            '123567':'⡯',
            '467':'⡰',
            '1467':'⡱',
            '3467':'⡲',
            '13467':'⡳',
            '4567':'⡴',
            '14567':'⡵',
            '34567':'⡶',
            '134567':'⡷',
            '2467':'⡸',
            '12467':'⡹',
            '23467':'⡺',
            '123467':'⡻',
            '24567':'⡼',
            '124567':'⡽',
            '234567':'⡾',
            '1234567':'⡿',
            '8':'⢀',
            '18':'⢁',
            '38':'⢂',
            '138':'⢃',
            '58':'⢄',
            '158':'⢅',
            '358':'⢆',
            '1358':'⢇',
            '28':'⢈',
            '128':'⢉',
            '238':'⢊',
            '1238':'⢋',
            '258':'⢌',
            '1258':'⢍',
            '2358':'⢎',
            '12358':'⢏',
            '48':'⢐',
            '148':'⢑',
            '348':'⢒',
            '1348':'⢓',
            '458':'⢔',
            '1458':'⢕',
            '3458':'⢖',
            '13458':'⢗',
            '248':'⢘',
            '1248':'⢙',
            '2348':'⢚',
            '12348':'⢛',
            '2458':'⢜',
            '12458':'⢝',
            '23458':'⢞',
            '123458':'⢟',
            '68':'⢠',
            '168':'⢡',
            '368':'⢢',
            '1368':'⢣',
            '568':'⢤',
            '1568':'⢥',
            '3568':'⢦',
            '13568':'⢧',
            '268':'⢨',
            '1268':'⢩',
            '2368':'⢪',
            '12368':'⢫',
            '2568':'⢬',
            '12568':'⢭',
            '23568':'⢮',
            '123568':'⢯',
            '468':'⢰',
            '1468':'⢱',
            '3468':'⢲',
            '13468':'⢳',
            '4568':'⢴',
            '14568':'⢵',
            '34568':'⢶',
            '134568':'⢷',
            '2468':'⢸',
            '12468':'⢹',
            '23468':'⢺',
            '123468':'⢻',
            '24568':'⢼',
            '124568':'⢽',
            '234568':'⢾',
            '1234568':'⢿',
            '78':'⣀',
            '178':'⣁',
            '378':'⣂',
            '1378':'⣃',
            '578':'⣄',
            '1578':'⣅',
            '3578':'⣆',
            '13578':'⣇',
            '278':'⣈',
            '1278':'⣉',
            '2378':'⣊',
            '12378':'⣋',
            '2578':'⣌',
            '12578':'⣍',
            '23578':'⣎',
            '123578':'⣏',
            '478':'⣐',
            '1478':'⣑',
            '3478':'⣒',
            '13478':'⣓',
            '4578':'⣔',
            '14578':'⣕',
            '34578':'⣖',
            '134578':'⣗',
            '2478':'⣘',
            '12478':'⣙',
            '23478':'⣚',
            '123478':'⣛',
            '24578':'⣜',
            '124578':'⣝',
            '234578':'⣞',
            '1234578':'⣟',
            '678':'⣠',
            '1678':'⣡',
            '3678':'⣢',
            '13678':'⣣',
            '5678':'⣤',
            '15678':'⣥',
            '35678':'⣦',
            '135678':'⣧',
            '2678':'⣨',
            '12678':'⣩',
            '23678':'⣪',
            '123678':'⣫',
            '25678':'⣬',
            '125678':'⣭',
            '235678':'⣮',
            '1235678':'⣯',
            '4678':'⣰',
            '14678':'⣱',
            '34678':'⣲',
            '134678':'⣳',
            '45678':'⣴',
            '145678':'⣵',
            '345678':'⣶',
            '1345678':'⣷',
            '24678':'⣸',
            '124678':'⣹',
            '234678':'⣺',
            '1234678':'⣻',
            '245678':'⣼',
            '1245678':'⣽',
            '2345678':'⣾',
            '12345678':'⣿',
            '345':'⠖',
        }
	def tobraille(self):
		'''
		เอา [1,2,3,4] มาเป็น 1234 เรียงจากน้อยไปมาก
		'''
		if len(self.data) > 1 and isinstance(self.inputdata, list):
			self.data1 =''
			for o in self.data:
				self.data1 += self.db[''.join(str(''.join(o)))]
			return self.data1
		else:
			self.data1 = ''.join(self.data) # แปลง list to str
			return self.db[self.data1]
	def printbraille(self):
		'''
		กลับด้านตัวเลข
		'''
		self.chage={'1':'2','2':'1','3':'4','4':'3','5':'6','6':'5','7':'8','8':'7'}
		self.i=0
		self.aa=[]*len(self.data)
		if len(self.data) > 1 and isinstance(self.inputdata, list):
			self.data2=['']*len(self.data)
			while self.i < len(self.data):
				for a in self.data[self.i]:
					self.data2[self.i] += self.chage[a]
				self.data2[self.i]=sorted(self.data2[self.i])
				self.data2[self.i]=self.db[''.join(self.data2[self.i])]
				self.i+=1
			self.data2.reverse() # ทำการเรียงจากหลังไปหน้า
			return ''.join(self.data2)
		else:
			self.data2=['']
			for a in self.data:
				self.data2.append(self.chage[a])
			return self.db[''.join(sorted(self.data2))]
