import os
import requests
import urllib.parse

# Your Pixabay API key is plugged in here!
API_KEY = '54900703-f111d9c7573a028ef3824558f'
SAVE_DIR = r'C:\Users\eran\Desktop\Claude project\Fruits\images'

# Create the target directory if it doesn't exist
os.makedirs(SAVE_DIR, exist_ok=True)

# The shopping list
fruits = [
    {"q": "mango fruit", "filename": "mango.jpg"},
    {"q": "dragon fruit cut", "filename": "dragonfruit.jpg"},
    {"q": "rambutan", "filename": "rambutan.jpg"},
    {"q": "lychee fruit", "filename": "lychee.jpg"},
    {"q": "starfruit carambola", "filename": "starfruit.jpg"},
    {"q": "papaya cut", "filename": "papaya.jpg"},
    {"q": "guava fruit", "filename": "guava.jpg"},
    {"q": "passion fruit open", "filename": "passionfruit.jpg"},
    {"q": "mangosteen", "filename": "mangosteen.jpg"},
    {"q": "longan fruit", "filename": "longan.jpg"},
    {"q": "jackfruit", "filename": "jackfruit.jpg"},
    {"q": "durian fruit", "filename": "durian.jpg"},
    {"q": "feijoa", "filename": "feijoa.jpg"},
    {"q": "persimmon fruit", "filename": "persimmon.jpg"},
    {"q": "nashi pear", "filename": "nashi.jpg"},
    {"q": "kumquat", "filename": "kumquat.jpg"},
    {"q": "pomelo fruit", "filename": "pomelo.jpg"},
    {"q": "etrog citron", "filename": "etrog.jpg"},
    {"q": "prickly pear cactus fruit", "filename": "pricklypear.jpg"},
    {"q": "date fruit palm", "filename": "date.jpg"},
    {"q": "fig fruit cut", "filename": "fig.jpg"},
    {"q": "pomegranate open", "filename": "pomegranate.jpg"},
    {"q": "quince fruit", "filename": "quince.jpg"},
    {"q": "acai berry", "filename": "acai.jpg"},
    {"q": "pineapple cut", "filename": "pineapple.jpg"},
    {"q": "coconut open", "filename": "coconut.jpg"},
    {"q": "kiwi fruit sliced", "filename": "kiwi.jpg"},
    {"q": "avocado cut open", "filename": "avocado.jpg"},
    {"q": "lucuma fruit", "filename": "lucuma.jpg"},
    {"q": "sapodilla fruit", "filename": "sapodilla.jpg"},
    {"q": "loquat fruit", "filename": "loquat.jpg"},
    {"q": "banana fruit", "filename": "banana.jpg"},
    {"q": "raspberry", "filename": "raspberry.jpg"},
    {"q": "blueberry", "filename": "blueberry.jpg"},
    {"q": "cherry fruit", "filename": "cherry.jpg"}
]

for fruit in fruits:
    query = urllib.parse.quote(fruit['q'])
    url = f"https://pixabay.com/api/?key={API_KEY}&q={query}&image_type=photo&orientation=horizontal"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data.get('hits'):
            # webformatURL usually provides a ~640px image
            img_url = data['hits'][0]['webformatURL'] 
            img_data = requests.get(img_url).content
            
            filepath = os.path.join(SAVE_DIR, fruit['filename'])
            with open(filepath, 'wb') as handler:
                handler.write(img_data)
            print(f"OK Downloaded: {fruit['filename']}")
        else:
            print(f"X No results found for: {fruit['q']}")
    except Exception as e:
        print(f"Error downloading {fruit['filename']}: {e}")

print("\nTask Complete!")