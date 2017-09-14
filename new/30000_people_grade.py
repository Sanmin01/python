'''创造3万人的虚拟成绩名单
	create by Ian in 2017-9-6 17:38:14
	创造3万人的excel成绩表，用于测试数据库性能
'''
from openpyxl import Workbook
import random
import re


class Student(object):
	def __init__(self):
	    self.last_name = '''赵钱孙李　周吴郑王　冯陈褚卫　蒋沈韩杨　朱秦尤许　何吕施张　孔曹严华　金魏陶姜
	戚谢邹喻　柏水窦章　云苏潘葛　奚范彭郎　鲁韦昌马　苗凤花方　俞任袁柳　酆鲍史唐
	费廉岑薛　雷贺倪汤　滕殷罗毕　郝邬安常　乐于时傅　皮卞齐康　伍余元卜　顾孟平黄
	和穆萧尹　姚邵湛汪　祁毛禹狄　米贝明臧　计伏成戴　谈宋茅庞　熊纪舒屈　项祝董梁
	杜阮蓝闵　席季麻强　贾路娄危　江童颜郭　梅盛林刁　钟徐邱骆　高夏蔡田　樊胡凌霍
	虞万支柯　咎管卢莫　经房裘缪　干解应宗　宣丁贲邓　郁单杭洪　包诸左石　崔吉钮龚
	程嵇邢滑　裴陆荣翁　荀羊於惠　甄魏加封　芮羿储靳　汲邴糜松　井段富巫　乌焦巴弓
	牧隗山谷　车侯宓蓬　全郗班仰　秋仲伊宫　宁仇栾暴　甘钭厉戎　祖武符刘　姜詹束龙
	叶幸司韶　郜黎蓟薄　印宿白怀　蒲台从鄂　索咸籍赖　卓蔺屠蒙　池乔阴郁　胥能苍双
	闻莘党翟　谭贡劳逄　姬申扶堵　冉宰郦雍　却璩桑桂　濮牛寿通　边扈燕冀　郏浦尚农
	温别庄晏　柴瞿阎充　慕连茹习　宦艾鱼容　向古易慎　戈廖庚终　暨居衡步　都耿满弘
	匡国文寇　广禄阙东　殴殳沃利　蔚越夔隆　师巩厍聂　晁勾敖融　冷訾辛阚　那简饶空
	曾毋沙乜　养鞠须丰　巢关蒯相　查后江红　游竺权逯　盖益桓公　万俟司马　上官欧阳
	夏侯诸葛　闻人东方　赫连皇甫　尉迟公羊　澹台公冶　宗政濮阳　淳于仲孙　太叔申屠
	公孙乐正　轩辕令狐　钟离闾丘　长孙慕容　鲜于宇文　司徒司空　亓官司寇　仉督子车
	颛孙端木　巫马公西　漆雕乐正　壤驷公良　拓拔夹谷　宰父谷粱　晋楚阎法　汝鄢涂钦
	段干百里　东郭南门　呼延归海　羊舌微生　岳帅缑亢　况后有琴　梁丘左丘　东门西门
	商牟佘佴　伯赏南宫　墨哈谯笪　年爱阳佟　第五言福　百家姓续'''.replace("　","").replace("\n","").replace("	",'') # 姓
	    self.first_name = '''筠、柔、竹、霭、凝、晓、欢、霄、枫、芸、菲、寒、伊、亚、宜、可、姬、舒、影、荔、枝、思、丽、秀、娟、英、华、慧、
	    巧、美、娜、静、淑、惠、珠、翠、雅、芝、玉、萍、红、娥、玲、芬、芳、燕、彩、春、菊、勤、珍、贞、莉、兰、凤、洁、梅、琳、素、云、莲、真、
	    环、雪、荣、爱、妹、霞、香、月、莺、媛、 艳、瑞、凡、佳、嘉、琼、桂、娣、叶、璧、璐、娅、琦、晶、妍、茜、秋、珊、莎、锦、黛、青、倩、婷、
	    姣、婉、娴、瑾、颖、露、瑶、怡、婵、雁、蓓、纨、仪、荷、丹、蓉、眉、君、琴、蕊、薇、菁、梦、岚、 苑、婕、馨、瑗、琰、韵、融、园、艺、咏、
	    卿、聪、澜、纯、毓、悦、昭、冰、爽、琬、茗、羽、希、宁、欣、飘、育、滢、馥世、舜、丞、主、产、仁、仇、仓、仕、仞、任、伋、众、伸、佐、佺、
	    侃、侪、促、俟、信、俣、修、倝、倡、倧、偿、储、僖、僧、僳、儒、俊、伟、列、则、刚、创、前、剑、助、劭、势、勘、参、叔、吏、嗣、士、壮、孺、
	    守、宽、宾、宋、宗、宙、宣、实、宰、尊、峙、峻、崇、崇、川、州、巡、帅、庚、战、才、承、拯、操、斋、昌、晁、皓、曹、曾、珺、玮、珹、琒、琛、
	    琩、琮、琸、瑎、玚、璟、璥、瑜、生、畴、矗、矢、石、磊、砂、碫、示、社、祖、祚、祥、禅、稹、穆、竣、竦、综、缜、绪、舱、舷、船、蚩、襦、轼、辑、
	    轩、子、杰、榜、碧、葆、莱、蒲、天、乐、东、钢、铎、铖、铠、铸、铿、锋、镇、键、镰、馗、旭、骏、骢、骥、驹、驾、骄、诚、诤、赐、慕、端、征、坚、
	    建、弓、强、彦、御、悍、擎、攀、旷、昂、晷、健、冀、凯、劻、啸、柴、木、林、森、朴、骞、寒、函、高、魁、魏、鲛、鲲、鹰、丕、乒、候、冕、勰、备、
	    宪、宾、密、封、山、峰、弼、彪、彭、旁、日、明、昪、昴、胜、汉、涵、汗、浩、涛、淏、清、澜、浦、澉、澎、澔、濮、濯、瀚、瀛、灏、沧、虚、豪、豹、
	    辅、辈、迈、邶、合、部、阔、雄、霆、震、韩、俯、颁、颇、频、颔、风、飒、飙、飚、马、亮、仑、仝、代、儋、利、力、劼、勒、卓、哲、喆、展、帝、弛、
	    弢、弩、彰、征、律、德、志、忠、思、振、挺、掣、旲、旻、昊、昮、晋、晟、晸、朕、朗、段、殿、泰、滕、炅、炜、煜、煊、炎、选、玄、勇、君、稼、黎、
	    利、贤、谊、金、鑫、辉、墨、欧、有、友、闻、问'''.replace("、",'').replace("\n",'') # 名

	    self.first_name = 


def main():

    # 初始化
    path = ''
    wb = Workbook()  # 创建文件对象
    ws_1 = wb.create_sheet('grade')  # 创建一个表

a = Student()
print(a.first_name)
