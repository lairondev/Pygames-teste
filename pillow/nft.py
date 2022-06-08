from PIL import Image

def img_create():
    largura, altura = 100, 100
    verde = (0,255,0)
    
    img = Image.new("RGB", (largura, altura), verde)
    img.save("img_teste.png")

if __name__ == "__main__":
    img_create()