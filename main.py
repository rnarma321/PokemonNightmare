import requests
import urllib.request
from PIL import Image
import os

promptList = []
for i in range(1,152):
    print(i)

    x = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(i))

    imgLink = x.json()['sprites']['other']['official-artwork']['front_default']
    try:
        os.mkdir(r"C:\Users\rosha\Documents\Code\PokemonNightmare\Images2" + "\\"+ str(i))
    except OSError as error:
        print(error)

            # print(error)
    name = x.json()['forms'][0]['name']
    imageLocation = r"C:\\Users\\rosha\\Documents\\Code\\PokemonNightmare\\Images2" + "\\\\" + str(i) + "\\\\"+name +".png"
    urllib.request.urlretrieve(imgLink,imageLocation)

    img = Image.open(imageLocation)
    newImg = img.resize((512,512))
    newImage2 = Image.new("RGBA", (512,512), "WHITE")
    newImage2.paste(newImg, (0, 0), newImg)
    newImage2.convert('RGB').save(imageLocation, "JPEG")
    promptList.append("Mech,futuristic,robot,highly detailed,sharp focus, HD,steampunk, 4K, Ultra realistic, artstation, by greg rutkowski -f0.59 -I" + imageLocation +" -o "+ r"C:\\Users\\rosha\\Documents\\Code\\PokemonNightmare\\Images2" + "\\\\" + str(i) + "\\\\"+name+"\n")

    # promptList.append("Fantasy Mythical Creature, HD, 4K, ultra-realistic, artstation, by greg rutkowski -f0.63 -I" + imageLocation +" -o "+ r"C:\\Users\\rosha\\Documents\\Code\\PokemonNightmare\\Images" + "\\\\" + str(i) + "\\\\"+name+"\n")

with open(r"C:\Users\rosha\Documents\Code\PokemonNightmare\prompt2.txt","w") as f:
    for prompt in promptList:
        f.write(prompt)
