from fpdf import FPDF

def image_to_pdf(image_path, pdf_path):
    pdf = FPDF()
    pdf.add_page()

    # Set image size to fit the page
    pdf.image(image_path, x=0, y=0, w=210, h=297)

    pdf.output(pdf_path, "F")

# Example usage:
image_to_pdf("img.jpg", "output_pdf.pdf")
