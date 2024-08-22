from sys import argv, exit, path
from PIL import Image, ImageOps, ImageDraw, ImageFont
from fpdf import FPDF

def main():
    image_path= Image.open(image_maker())
    width, height= image_path.size
    print(width,height)
    pdf_width = 210* 2.83
    pdf_height = 297 * 3.78

    new_width = 200
    aspect_ratio = image_path.height / image_path.width
    new_height = int(new_width * aspect_ratio)

    # Redimensionar a imagem mantendo a proporção
    resized_image = image_path.resize((new_width, new_height))
    resized_image_path = 'imagem_redimensionada.png'
    resized_image.save(resized_image_path)
    # Calcular a posição da imagem para centralizá-la
    image_x = (pdf_width - new_width) / 2
    image_y = 100
    pdf = FPDF('P','pt','A4')
    pdf.add_page()

    # Adicionar o texto acima da imagem
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 20, 'CS50 Shirtificate', align='C')

    # Adicionar a imagem ao PDF
    pdf.image(resized_image_path,x= image_x, y=image_y)

    # Salvar o PDF
    output_pdf_path = 'shirtificate.pdf'
    pdf.output(output_pdf_path)


def image_maker():
    image= Image.open('shirtificate.png')
    width, height= image.size
    print(width, height)
    draw= ImageDraw.Draw(image)
    text= input("Name: ")
    text= text + ' took CS50'
    font_size = 30
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", font_size)
    position= (150,110)
    draw.text(position, text, (255, 255, 255), font=font)
    image_path= 'shirt.png'
    image.save(image_path)
    return image_path


if __name__ == "__main__":
    main()
