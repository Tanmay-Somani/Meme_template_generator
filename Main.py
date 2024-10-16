from PIL import Image,ImageDraw,ImageFont
import textwrap
im=Image.open("I1.jpeg")
draw=ImageDraw.Draw(im)
image_width,image_height=im.size
font=ImageFont.truetype(font="/impact.ttf",size=int(image_height/10))
top_text="When in exam".upper()
bottom_text="Panik".upper()
char_width,char_height=font.getsize("A")
char_per_line=image_width//char_width
top_lines=textwrap.wrap(top_text,width=char_per_line)
bottom_lines=textwrap.wrap(bottom_text,width=char_per_line)
y=10
for line in top_lines:
    line_width,line_height=font.getsize(line)
    x=(image_width-line_width)/2
    draw.text((x,y),line,fill='white',font=font)
    y+=line_height
y=image_height-char_height*len(bottom_lines)
for line in bottom_lines:
    line_width,line_height=font.getsize(line)
    x=(image_width-line_width)/2
    draw.text((x,y),line,fill='white',font=font)
    y+=line_height
im.show()

