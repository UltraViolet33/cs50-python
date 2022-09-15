from fpdf import FPDF


class Shirt_PDF():

    def __init__(self, name):
        self._shirt_pdf = FPDF()
        self._shirt_pdf.add_page()
        self._shirt_pdf.set_font("helvetica", "B", 40)
        self._shirt_pdf.cell(0, 60, "CS50 Shirtificate",
                             new_x="LMARGIN", new_y="NEXT", align="C")
        self._shirt_pdf.image("shirtificate.png", w=self._shirt_pdf.epw)
        self._shirt_pdf.set_font_size(35)
        self._shirt_pdf.set_text_color(255, 255, 255)
        self._shirt_pdf.text(x=48, y=140, txt=f"{name} took CS50")

    def save_pdf(self, name):
        self._shirt_pdf.output(name)


name = input("Name: ")
shirt_pdf = Shirt_PDF(name)
shirt_pdf.save_pdf("shirtificate.pdf")
