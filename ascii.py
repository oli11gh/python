import PIL.Image
import requests
import os, glob, time
from pyfiglet import figlet_format
import fcntl, termios, struct



th, tw, hp, wp = struct.unpack('HHHH',
fcntl.ioctl(0, termios.TIOCGWINSZ,
struct.pack('HHHH', 0, 0, 0, 0)))





SYMBOLS = ["@", "#", "S", "%", "!", "*", "+", ";", ":", ",", "."]

UNICODE = ["█", "█", "▓", "▓", "▒", "▒", "░", "░", "┉", "┉", " "]



def delt():
  files = glob.glob('images/*')
  for f in files:
    os.remove(f)

def gen_id():
    global uid
    res = requests.get("https://idgen.i-api.repl.co/uid?length=5").json()["id"]
    uid = res

def download(img_name, url):
    res = requests.get(url)
    f = open(f"images/{img_name}.png", "wb")
    f.write(res.content)
    f.close()
    PIL.Image.open(f"images/{img_name}.png").convert("RGBA").save(f"images/{img_name}.png")




def resize_image(image, new_width=100):
  width, height = image.size
  ratio = height / width / 1.65
  new_height = int(new_width * ratio)
  resized_image = image.resize((new_width, new_height))
  return(resized_image)

def grayify(image):
  grayscale_image = image.convert("L")
  return(grayscale_image)

def symbols_to_ascii(image):
  pixels = image.getdata()
  characters = "".join([SYMBOLS[pixel//25] for pixel in pixels])
  return(characters)

def unicode_to_ascii(image):
  pixels = image.getdata()
  characters = "".join([UNICODE[pixel//25] for pixel in pixels])
  return(characters)

  
def imageAscii(new_width=100):
  os.system("cls||clear")
  print("Prosze wlaczyc pelny ekran")
  type = input("[1]: SYMBOLE ASCII ART\n[2]: UNICODE ASCII ART\n>>> ")
  if type == "1":
    url = input("URL zdjecia\n>>> ")
    gen_id()
    try:
      download(uid, url)
      image = PIL.Image.open(f"images/{uid}.png")
    except Exception as e:
      print(f"\033[93m{e}\nNieprawidlowy link.")
  
    new_image_data = symbols_to_ascii(grayify(resize_image(image)))
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
    os.system("cls||clear")
    print(ascii_image)
    ft = open(f"ascii/{uid}.txt", "wb")
    ft.write(bytes(ascii_image, "UTF-8"))
    ft.close()
    delt()
  elif type == "2":
    url = input("URL  zdjecia\n>>> ")
    gen_id()
    try:
      download(uid, url)
      image = PIL.Image.open(f"images/{uid}.png")
    except Exception as e:
      print(f"\033[93m{e}\nPodany obraz nie jest wspierany.")
  
    new_image_data = unicode_to_ascii(grayify(resize_image(image)))
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
    os.system("cls||clear")
    print(ascii_image)
    ft = open(f"ascii/{uid}.txt", "wb")
    ft.write(bytes(ascii_image, "UTF-8"))
    ft.close()
    delt()
  else:
    imageAscii()


def textAscii():
  os.system("cls||clear")
  gen_id()
  type = input("[1]: Standardowy Font\n[2]: Custom Font\n>>> ")
  if type == "1":
    text = input("Twoj tekst\n>>> ")
    data = figlet_format(str(text), font="standard")
    os.system("cls||clear")
    print(data)
    fta = open(f"ascii/text-{uid}.txt", "wb")
    fta.write(bytes(data, "UTF-8"))
    fta.close()
  elif type == "2":
    styl = input("Nazwa fontu\n(Odwiedz 'http://www.figlet.org/examples.html' aby wybrac font!)\n>>> ")
    text = input("Twoj tekst\n>>> ")
    try:
      data = figlet_format(str(text), font=styl)
      os.system("cls||clear")
      print(data)
      fta = open(f"ascii/text-{styl}-{uid}.txt", "wb")
      fta.write(bytes(data, "UTF-8"))
      fta.close()
    except:
      print(f"\33[31mError: {styl} nie znaleziono takiego fontu!\33[37m")
      time.sleep(2)
      textAscii()
  else:
    textAscii()
    

def main():
  os.system("cls||clear")
  print("Wybierz typ:\n[1]: Zdjecie do Ascii\n[2]: Tekst do Ascii")
  con = input(">>> ")
  if con == "1":
    imageAscii()
  elif con == "2":
    print("Prosze wlaczyc pelny ekran")
    textAscii()
  else:
    main()

main()
