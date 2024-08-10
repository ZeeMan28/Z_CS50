from fpdf import FPDF


class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 70)
        self._pdf.cell(0, 10, f"CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        self._pdf.ln(20)

        self._pdf.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", w=self._pdf.epw, keep_aspect_ratio=True)

        self._pdf.set_y(80)
        self._pdf.set_font(size=35)
        self._pdf.cell(0, 10, name, new_x="LMARGIN",  align="C")


    def save(self, name):
        self._pdf.output(name)


name = input("Enter name: ")
pdf = PDF(name)

pdf.save("new-tuto3.pdf")