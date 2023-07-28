from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def inserttext(img:Image, txt:str, prompt="Жириновский предложил "):
    txt=split_input(prompt+txt, 20)
    fnt=ImageFont.truetype('fonts/impact.ttf',23)
    drawer = ImageDraw.Draw(img)
    drawer.text((139,213),txt,font=fnt,fill=(0,0,0),anchor="ma",align="center")
    return img

def split_input(user_string, line_size:int=24):
    if(len(user_string)>=180):
        user_string = "пойти пользователю нахуй с такими длинными запросами."
    output,curline = [],[]
    words = user_string.split(" ")
    counter=0
    for word in words:
        if(len(word)>23):
            output.append(" ".join(curline))
            curline=[]
            output.append(word)            
            counter=0
        elif(len(word)+counter ) <= line_size:
            curline.append(word)
            counter+=len(word)
        else:
            output.append(" ".join(curline))
            curline=[]
            curline.append(word)
            counter=0
    output.append(" ".join(curline))
    return "\n".join(output)
def gen_image(txt:str, img:Image=Image.open('templates/default.png')):
    image=img.copy()
    inserttext(image, split_input(txt, 24)).save("buffer.png")
    image.close()
    