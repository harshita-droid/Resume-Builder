from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import sqlite3 as db
sqlcon = db.connect('resume.sqlite')
cursor= sqlcon.cursor()
file=open("resid.txt","r")
resid = file.read()
file.close()

find_res = ("SELECT * FROM details where resid=?")
cursor.execute(find_res, [resid])
details_results = cursor.fetchall()
print(details_results)
# name 857 157
img = Image.open(f"images/1.png")
file=open("imagefile.txt","r")
path = file.read()
file.close()
imgtoinsert = Image.open(path)

imgtoinsert=imgtoinsert.resize((398,376))
I1 = ImageDraw.Draw(img)
find_res = ("SELECT * FROM info where resid=?")
cursor.execute(find_res, [resid])
info_results = cursor.fetchall()
print(info_results)
info_split=info_results[0][1].split()
print(info_split)
fnt = ImageFont.truetype("font2.ttf", 25)
if len(info_split)>=0 and len(info_split)<=7:
    I1.text((130, 1610), info_results[0][1], font=fnt, fill=(0,0,0))
xpos=594
ypos=411
if len(info_split)>7 and len(info_split)<15:
    first=' '.join(info_split[0:8])
    second=' '.join(info_split[8:len(info_split)])
    I1.text((xpos, ypos), first, font=fnt, fill=(0,0,0))
    I1.text((xpos,ypos+40), second, font=fnt, fill=(0,0,0))
if len(info_split)>15 and len(info_split)<30:
    first=' '.join(info_split[0:8])
    second=' '.join(info_split[7:15])
    third=' '.join(info_split[15:22])
    fourth = ' '.join(info_split[22:len(info_split)])
    I1.text((xpos, ypos), first, font=fnt, fill=(0,0,0))
    I1.text((xpos,ypos+40), second, font=fnt, fill=(0,0,0))
    I1.text((xpos,ypos+80), third, font=fnt, fill=(0,0,0))
    I1.text((xpos,ypos+120), fourth, font=fnt, fill=(0,0,0))

insert_name = details_results[0][1]
split_name=insert_name.split()

print(split_name)
fnt = ImageFont.truetype("font.otf", 80)
xpos=592
ypos=130
if len(split_name)>2:
    first_name = ' '.join(split_name[0:2])
    last_name=' '.join(split_name[2:len(split_name)])
    I1.text((xpos, ypos), first_name, font=fnt, fill=(51,83,132))
    I1.text((xpos, ypos+80), last_name, font=fnt, fill=(51, 83, 132))
else:
    I1.text((592, 170), insert_name, font=fnt, fill=(51, 83, 132))
insert_address = details_results[0][4]
fnt = ImageFont.truetype("font2.ttf", 20)

address_split = insert_address.split()
print(address_split)
ypos=631
xpos=150
first=' '.join(address_split[0:4])
I1.text((xpos, ypos), first, font=fnt, fill=(255, 255, 255))
second=' '.join(address_split[4:len(address_split)])
I1.text((xpos, ypos+30), second, font=fnt, fill=(255, 255, 255))
insert_num = str(details_results[0][3])
fnt = ImageFont.truetype("font2.ttf", 20)
I1.text((150, 750), insert_num, font=fnt, fill=(255, 255, 255))
insert_email= str(details_results[0][2])
fnt = ImageFont.truetype("font2.ttf", 20)
I1.text((140, 812), insert_email, font=fnt, fill=(255, 255, 255))
find_res = ("SELECT * FROM skills where resid=?")
cursor.execute(find_res, [resid])
skills_results = cursor.fetchall()
print(skills_results)
xpos=107
ypos=1067
for i in range(0,len(skills_results)):
    insert_skill=skills_results[i][1]
    I1.text((xpos, ypos), insert_skill, font=fnt, fill=(255, 255, 255))
    ypos+=40
# I1.text((107, 1367), insert_skill6, font=fnt, fill=(255, 255, 255))
find_res = ("SELECT * FROM extra_details where resid=?")
cursor.execute(find_res, [resid])
achievement_results = cursor.fetchall()
achievement_split=achievement_results[0][1].split()
if len(achievement_split)>=0 and len(achievement_split)<7:
    I1.text((130, 1610), achievement_results[0][1], font=fnt, fill=(255, 255, 255))
xpos=130
ypos=1610
if len(achievement_split)>7 and len(achievement_split)<15:
    first=' '.join(achievement_split[0:8])
    second=' '.join(achievement_split[8:len(achievement_split)])
    I1.text((xpos, ypos), first, font=fnt, fill=(255, 255, 255))
    I1.text((xpos,ypos+40), second, font=fnt, fill=(255, 255, 255))
if len(achievement_split)>15 and len(achievement_split)<30:
    first=' '.join(achievement_split[0:8])
    second=' '.join(achievement_split[7:15])
    third=' '.join(achievement_split[15:22])
    fourth = ' '.join(achievement_split[22:len(achievement_split)])
    I1.text((xpos, ypos), first, font=fnt, fill=(255, 255, 255))
    I1.text((xpos,ypos+40), second, font=fnt, fill=(255, 255, 255))
    I1.text((xpos,ypos+80), third, font=fnt, fill=(255, 255, 255))
    I1.text((xpos,ypos+120), fourth, font=fnt, fill=(255, 255, 255))
print(achievement_results)
fnt = ImageFont.truetype("font2.ttf", 20)


find_res = ("SELECT * FROM internship_details where resid=?")
cursor.execute(find_res, [resid])
insternship_results = cursor.fetchall()
print(insternship_results)
fnt = ImageFont.truetype("font2.ttf", 25)
I1.text((583, 746), insternship_results[0][1], font=fnt, fill=(0, 0, 0))
I1.text((583, 786), insternship_results[0][3]+ "  | ", font=fnt, fill=(0, 0, 0))
I1.text((950, 786), insternship_results[0][2], font=fnt, fill=(0, 0, 0))
I1.text((583, 826), insternship_results[0][4]+"  |  ", font=fnt, fill=(0, 0, 0))
I1.text((683, 826), insternship_results[0][5], font=fnt, fill=(0, 0, 0))
intdes_split = insternship_results[0][6].split()
# I1.text((583, 866), insternship_results[0][6], font=fnt, fill=(0, 0, 0)))
xpos=583
ypos=866
if len(intdes_split)<=25:
    first = ' '.join(intdes_split[0:13])
    I1.text((xpos, ypos), first, font=fnt, fill=(0, 0, 0))
    second=' '.join(intdes_split[13:len(intdes_split)])
    I1.text((xpos, ypos+40), second, font=fnt, fill=(0, 0, 0))
elif len(intdes_split)>25 and len(intdes_split)<=35:
    first = ' '.join(intdes_split[0:13])
    I1.text((xpos, ypos), first, font=fnt, fill=(0, 0, 0))
    second = ' '.join(intdes_split[13:25])
    I1.text((xpos, ypos + 40), second, font=fnt, fill=(0, 0, 0))
    third = ' '.join(intdes_split[25:len(intdes_split)])
    I1.text((xpos, ypos + 80), third, font=fnt, fill=(0, 0, 0))
elif len(intdes_split)>35 and len(intdes_split)<=45:
    first = ' '.join(intdes_split[0:13])
    I1.text((xpos, ypos), first, font=fnt, fill=(0, 0, 0))
    second = ' '.join(intdes_split[13:25])
    I1.text((xpos, ypos + 40), second, font=fnt, fill=(0, 0, 0))
    third = ' '.join(intdes_split[25:35])
    I1.text((xpos, ypos + 80), third, font=fnt, fill=(0, 0, 0))
    fourth = ' '.join(intdes_split[25:len(intdes_split)])
    I1.text((xpos, ypos + 120), fourth, font=fnt, fill=(0, 0, 0))
find_res = ("SELECT * FROM secondry_details where resid=?")
cursor.execute(find_res, [resid])
secondry_results = cursor.fetchall()
print(secondry_results)
I1.text((585,1315), secondry_results[0][1], font=fnt, fill=(0, 0, 0))
I1.text((585,1355), str(secondry_results[0][2])+"  |  ", font=fnt, fill=(0, 0, 0))
I1.text((680,1355), str(secondry_results[0][3]), font=fnt, fill=(0, 0, 0))
I1.text((585,1395), str(secondry_results[0][4]), font=fnt, fill=(0, 0, 0))
find_res = ("SELECT * FROM senior_secondry_details where resid=?")
cursor.execute(find_res, [resid])
senior_secondry_results = cursor.fetchall()
print(senior_secondry_results)
I1.text((585,1515), senior_secondry_results[0][1], font=fnt, fill=(0, 0, 0))
I1.text((585,1555), str(senior_secondry_results[0][2])+"  |  ", font=fnt, fill=(0, 0, 0))
I1.text((680,1555), str(senior_secondry_results[0][3])+"  |  ", font=fnt, fill=(0, 0, 0))
I1.text((800,1555), str(senior_secondry_results[0][4]), font=fnt, fill=(0, 0, 0))
I1.text((585,1595), str(senior_secondry_results[0][5]), font=fnt, fill=(0, 0, 0))
find_res = ("SELECT * FROM graduation_details where resid=?")
cursor.execute(find_res, [resid])
graduation_results = cursor.fetchall()
print(graduation_results)
I1.text((585,1730), graduation_results[0][1], font=fnt, fill=(0, 0, 0))
I1.text((585,1770), str(graduation_results[0][2])+"  |  ", font=fnt, fill=(0, 0, 0))
I1.text((680,1770), str(graduation_results[0][3]), font=fnt, fill=(0, 0, 0))
I1.text((585,1810), graduation_results[0][4]+"  |  ", font=fnt, fill=(0, 0, 0))
I1.text((680,1810), graduation_results[0][5], font=fnt, fill=(0, 0, 0))
I1.text((585,1850), str(graduation_results[0][6]), font=fnt, fill=(0, 0, 0))
back_im =img.copy()
back_im.paste(imgtoinsert, (37, 129))

find_res = ("SELECT * FROM info where resid=?")
cursor.execute(find_res, [resid])
info_results = cursor.fetchall()
print(info_results)

img2 = Image.open(f"images/2.png")

I2 = ImageDraw.Draw(img2)
find_res = ("SELECT * FROM project_details where resid=?")
cursor.execute(find_res, [resid])

project_results = cursor.fetchall()
print(project_results)
I2.text((585,173), project_results[0][1], font=fnt, fill=(0, 0, 0))
I2.text((585,243), project_results[0][2], font=fnt, fill=(0, 0, 0))
I2.text((585,283), project_results[0][3]+"  |  ", font=fnt, fill=(0, 0, 0))
I2.text((690,283), project_results[0][4], font=fnt, fill=(0, 0, 0))
prodes_split=project_results[0][5].split()
xpos=585
ypos=323
if len(prodes_split)<=25:
    first = ' '.join(prodes_split[0:13])
    I2.text((xpos, ypos), first, font=fnt, fill=(0, 0, 0))
    second=' '.join(prodes_split[13:len(prodes_split)])
    I2.text((xpos, ypos+40), second, font=fnt, fill=(0, 0, 0))
elif len(prodes_split)>25 and len(prodes_split)<=35:
    first = ' '.join(prodes_split[0:13])
    I2.text((xpos, ypos), first, font=fnt, fill=(0, 0, 0))
    second = ' '.join(prodes_split[13:25])
    I2.text((xpos, ypos + 40), second, font=fnt, fill=(0, 0, 0))
    third = ' '.join(prodes_split[25:len(prodes_split)])
    I2.text((xpos, ypos + 80), third, font=fnt, fill=(0, 0, 0))
elif len(prodes_split)>35 and len(prodes_split)<=45:
    first = ' '.join(prodes_split[0:13])
    I2.text((xpos, ypos), first, font=fnt, fill=(0, 0, 0))
    second = ' '.join(prodes_split[13:25])
    I2.text((xpos, ypos + 40), second, font=fnt, fill=(0, 0, 0))
    third = ' '.join(prodes_split[25:35])
    I2.text((xpos, ypos + 80), third, font=fnt, fill=(0, 0, 0))
    fourth = ' '.join(prodes_split[25:len(prodes_split)])
    I2.text((xpos, ypos + 120), fourth, font=fnt, fill=(0, 0, 0))
find_res = ("SELECT * FROM training_details where resid=?")
cursor.execute(find_res, [resid])
training_results = cursor.fetchall()
print(training_results)
I2.text((585,793), training_results[0][1], font=fnt, fill=(0, 0, 0))
I2.text((585,833), training_results[0][2]+"  |  ", font=fnt, fill=(0, 0, 0))
I2.text((690,833), training_results[0][3], font=fnt, fill=(0, 0, 0))
I2.text((585,873), training_results[0][4]+"  |  ", font=fnt, fill=(0, 0, 0))
I2.text((680,873), training_results[0][5], font=fnt, fill=(0, 0, 0))
traindes_split=training_results[0][6].split()
xpos=585
ypos=913
if len(traindes_split)<=25:
    first = ' '.join(traindes_split[0:13])
    I2.text((xpos, ypos), first, font=fnt, fill=(0, 0, 0))
    second=' '.join(traindes_split[13:len(traindes_split)])
    I2.text((xpos, ypos+40), second, font=fnt, fill=(0, 0, 0))
elif len(traindes_split)>25 and len(traindes_split)<=35:
    first = ' '.join(traindes_split[0:13])
    I2.text((xpos, ypos), first, font=fnt, fill=(0, 0, 0))
    second = ' '.join(traindes_split[13:25])
    I2.text((xpos, ypos + 40), second, font=fnt, fill=(0, 0, 0))
    third = ' '.join(traindes_split[25:len(traindes_split)])
    I2.text((xpos, ypos + 80), third, font=fnt, fill=(0, 0, 0))
elif len(traindes_split)>35 and len(traindes_split)<=45:
    first = ' '.join(traindes_split[0:13])
    I2.text((xpos, ypos), first, font=fnt, fill=(0, 0, 0))
    second = ' '.join(traindes_split[13:25])
    I2.text((xpos, ypos + 40), second, font=fnt, fill=(0, 0, 0))
    third = ' '.join(traindes_split[25:35])
    I2.text((xpos, ypos + 80), third, font=fnt, fill=(0, 0, 0))
    fourth = ' '.join(traindes_split[25:len(traindes_split)])
    I2.text((xpos, ypos + 120), fourth, font=fnt, fill=(0, 0, 0))


def png_to_jpg(png):
    background = Image.new("RGB", png.size, (255, 255, 255))
    background.paste(png, mask=png.split()[3])
    return background
back_im=png_to_jpg(back_im)
img2=png_to_jpg(img2)
im_list=[img2]
pdf1_filename = "my_resume.pdf"

back_im.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)
