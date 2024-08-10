from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", w=pdf.epw, keep_aspect_ratio=True)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", border=1, align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-40)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


# Instantiation of inherited class
pdf = PDF()
pdf.add_page()

pdf.set_font("Times", size=12)

pdf.cell(0, 10, f"Zabder Bobander", new_x="LMARGIN", new_y="NEXT")
pdf.output("new-tuto3.pdf")