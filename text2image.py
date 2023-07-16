from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def inserttext(img:Image , txt:str, prompt="Жириновский предложил "):
    #w,h=230,230
    txt=split_input(prompt+txt, 20)
    fnt=ImageFont.truetype('fonts/impact.ttf',23)
    drawer = ImageDraw.Draw(img)
    drawer.text((139,213),txt,font=fnt,fill=(0,0,0),anchor="ma",align="center")
    #drawer.textbbox((30,215),txt,font=fnt,fill=(0,0,0))
    img.show()

def split_input(user_string, line_size):
    if(len(user_string)>=180):
        user_string = "пойти пользователю нахуй с такими длинными запросами."
    output,curline = [],[]
    words = user_string.split(" ")
    counter=0
    for word in words:
        #print(curline)
        if(len(word)>23):
            print("finished line:",curline)
            output.append(" ".join(curline))
            curline=[]
            print("finished line:",word)
            output.append(word)
            
            counter=0
        elif(len(word)+counter ) <= line_size:
            curline.append(word)
            counter+=len(word)
        else:
            print("finished line:",curline)
            output.append(" ".join(curline))
            curline=[]
            curline.append(word)
            counter=0
    output.append(" ".join(curline))
    return "\n".join(output)
#inserttext(Image.open('templates/default.png'), "пыне сдохнуть от спида")