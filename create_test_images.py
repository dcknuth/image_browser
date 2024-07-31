from subprocess import run

IM = r'C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe'
# Create an image with a number
def create_image(number):
    filename = f"image{number}.jpg"
    command = [
        IM, 
        "-size", "150x150", 
        "xc:white", 
        "-gravity", "center", 
        "-pointsize", "80", 
        "-annotate", "0", str(number), 
        filename
    ]
    run(command)
    print(f"Created {filename}")

for i in range(1, 10):
    create_image(i)
