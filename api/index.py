from flask import Flask,render_template


info = [
    "if you need only Img Chracters = http://127.0.0.1:5050/img",
    "if you need only Img character name = http://127.0.0.1:5050/char",
    "if you need only Img p tag = http://127.0.0.1:5050/des",
]
img = [
   "https://cdn.shopify.com/s/files/1/0665/3404/7973/files/Naruto_Uzumaki_600x600.png?v=1707667895", 
   "https://cdn.shopify.com/s/files/1/0665/3404/7973/files/Sasuke_Uchiha_600x600.png?v=1707668073",
   "https://cdn.shopify.com/s/files/1/0665/3404/7973/files/Sakura_Haruno_600x600.png?v=1707668258",
   "https://wallpapers.com/images/high/itachi-sharingan-look-down-bouso6qi0g04jykz.webp",
   "https://cdn.shopify.com/s/files/1/0665/3404/7973/files/Madara_Uchiha_600x600.png?v=1707669068",
   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrrgNPUq7b2q3rPBJTXEm5fEgVrY8CcIvyDA&s",
   "https://rukminim2.flixcart.com/image/850/1000/poster/j/b/6/hinata-hyuga-with-purple-eyes-naruto-athah-fine-quality-poster-original-imaejyd6ygzztyjt.jpeg?q=90&crop=false",
   "https://bleachmx.fr/wp-content/uploads/Boruto-Naruto-Next-Generations-episode-132.jpg",
   "https://w0.peakpx.com/wallpaper/527/107/HD-wallpaper-minato-namikaze-shinobi-minato-naruto-guy-manga-blonde-4th-mesy-hokage-anime-wink-kunai-fourth-namikaze-ninja.jpg",
   "https://cdn.shopify.com/s/files/1/0046/2779/1960/files/rock_lee.jpg?v=1584716762    ",
   "https://2img.net/h/i615.photobucket.com/albums/tt231/altea_Peqee/NaraShikamaru.jpg",
   "https://i.pinimg.com/736x/3a/a1/26/3aa126707b05da90920542592acb6e8d.jpg",
   "https://cdn.staticneo.com/w/naruto/thumb/Killerbee.png/300px-Killerbee.png",
   "https://cdn.shopify.com/s/files/1/0665/3404/7973/files/Orochimaru_600x600.png?v=1707668885",
   "https://i.pinimg.com/736x/38/b8/cf/38b8cf47f832d51eb8f9890e0249b835.jpg",
   "https://preview.redd.it/jpwfs25lqhh91.jpg?width=640&crop=smart&auto=webp&s=a9a1835988fbbdf10de7c0875b3af779d17f9215",
   "https://i.ytimg.com/vi/k6avkwpNpLc/maxresdefault.jpg",
   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiIdqeBK1k51la-kATLt-mcjP65NbwAEQq7A&s",
   "https://cdn.dekudeals.com/images/53c4752504a286adc9463f0a3f8845960db9ce14/w500.jpg",
]
characters = [
    "uzumaki naruto", 
    "sasuke uchiha",
    "sakura haruno",
    "uchiha itachi",
    "madara uchiha",
    "Senju Tsunade",
    "Hinata Hyuga",
    "Ogata Jiraiya",
    "Minato Namikaze",
    "Rock Lee",
    "Shikamaru Nara",
    "Tenten",
    "Killer Bee",
    "Orochimaru",
    "Asuma Sarutobi",
    "Choji Akimichi",
    "shino",
    "hoku"
   "Konohamaru Sarutobi",
]
description = [
    "The protagonist of the series, Naruto is an energetic and determined ninja who seeks , recognition and dreams of becoming the Hokage to protect his village.",
    "A skilled and brooding ninja, Sasuke is Naruto's rival and friend. He is driven by revenge after  the massacre of his clan by his older brother, Itachi.",
    "A member of Team 7, Sakura is a skilled medical ninja with superhuman strength and a deep  love for Sasuke. Her character evolves throughout the series",
    "A prodigious ninja and Sasuke’s older brother, Itachi is initially believed to be a villain for  massacring the Uchiha clan, though his true motivations are far more complex.",
    "One of the founders of Konoha, Madara is a legendary and powerful Uchiha who seeks to create  an ideal world by using the power of the Ten Tails.",
    "A legendary Sannin and the Fifth Hokage, Tsunade is an expert medical ninja and possesses immense strength.",
    "A shy and kind-hearted member of the Hyuga clan, Hinata has a deep admiration for Naruto. She later becomes a key character in Naruto’s life.",
    "One of the legendary Sannin, Jiraiya is Naruto’s mentor and a wise, powerful ninja with a playful,  perverted personality.  ",
    "The Fourth Hokage and Naruto’s father, Minato is a hero of the village who sacrificed himself to seal the Nine-Tails inside his newborn son.",
    "A taijutsu master who cannot use ninjutsu or genjutsu, Lee’s determination and perseverance to  become a great ninja despite his limitations make him an inspiring character",
    "A tactical genius and master of shadow-based jutsu, Shikamaru is often seen as lazy, but his  intelligence and strategic mind make him an essential asset to his team.",
    "A weapons expert and member of Team Guy, Tenten’s strength lies in her mastery of various  ninja tools, though she often gets overshadowed by her teammates.",
    "The jinchuriki of the Eight-Tails, Killer Bee is a powerful and eccentric shinobi from the Hidden  Cloud Village who teaches Naruto about the connection between jinchuriki and their tailed beasts.",
    "A former member of the Legendary Sannin, Orochimaru seeks immortality and power by  experimenting with forbidden jutsu, leading him to become one of the series' main antagonists.",
    "A member of the Sarutobi clan and a jonin leader of Team 10, Asuma is a calm and caring  mentor who has a deep bond with his students.",
    "A member of Team 10, Choji is known for his ability to expand his body size in combat, using the unique jutsu of his clan in powerful ways.",
    "A quiet and enigmatic member of Team 8, Shino is a master of insect-based jutsu, using bugs as both weapons and spies."
    "A young and tragic character, Haku is a skilled ice user and Zabuza’s loyal companion. His backstory is a key element of Zabuza’s redemption.",
    "The grandson of the Third Hokage, Konohamaru is a young ninja with aspirations of becoming Hokage and looks up to Naruto as a role model.",
]

app = Flask(__name__,template_folder="temp")

@app.route("/")
def a():
    return info+img + characters +description
@app.route("/img")
def b():
    return img
@app.route("/char")
def c():
    return characters
@app.route("/des")
def d():
    return description
if __name__ == "__main__":
    app.run(debug=True,port=5050)
