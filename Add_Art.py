import os
from bs4 import BeautifulSoup

def get_user_input():
    art_name = input("Enter the name of the art item: ")
    artist_name = input("Enter the name of the artist: ")
    creation_date = input("Enter the date the art was created: ")
    description = input("Enter a description of the art item: ")
    image_path = input("Enter the path to the image file of the art item: ")
    
    return art_name, artist_name, creation_date, description, image_path

def create_art_item_page(art_name, artist_name, creation_date, description, image_path):
    art_filename = art_name.lower().replace(" ", "_") + ".html"
    with open(art_filename, "w") as file:
        file.write(f'''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{art_name} - Withers Art Collection</title>
                <link rel="stylesheet" href="WAM.css">
            </head>
            <body>
                <header>
                    <h1><a href="LandingPage.html" style="text-decoration: none; color: inherit;">The George Withers Collection</a></h1>
                </header>
                <main>
                    <section id="art-details">
                        <div class="art-image">
                            <img src="{image_path}" alt="{art_name}">
                        </div>
                        <div class="art-info">
                            <h2>{art_name}</h2>
                            <p class="artist-name">{artist_name}</p>
                            <p>{creation_date}</p>
                            <p class="art-description">{description}</p>
                        </div>
                    </section>
                </main>
            </body>
            </html>
        ''')
    return art_filename

def update_landing_page(art_name, art_filename, image_path):
    with open("LandingPage.html", "r") as file:
        soup = BeautifulSoup(file, "html.parser")

    new_art_div = soup.new_tag("a", href=art_filename, **{'class': 'art-item'})
    
    img_tag = soup.new_tag("img", src=image_path, alt=art_name)
    new_art_div.append(img_tag)
    
    title_tag = soup.new_tag("p", **{'class': 'landing-art-title'})  # Here's the change
    title_tag.string = art_name
    new_art_div.append(title_tag)
    
    gallery_section = soup.find("section", {"id": "gallery"})
    gallery_section.append(new_art_div)

    with open("LandingPage.html", "w") as file:
        file.write(str(soup))

def main():
    art_name, artist_name, creation_date, description, image_path = get_user_input()
    
    art_filename = create_art_item_page(art_name, artist_name, creation_date, description, image_path)
    
    update_landing_page(art_name, art_filename, image_path)

if __name__ == "__main__":
    main()
