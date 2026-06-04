from fpdf import FPDF

def generate_pdf(summary):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        "B",
        16
    )

    pdf.cell(
        200,
        10,
        "Startup Analytics Report",
        ln=True,
        align="C"
    )

    pdf.ln(10)

    for key,value in summary.items():

        pdf.cell(
            200,
            10,
            f"{key}: {value}",
            ln=True
        )

    path = (
        "reports/generated_reports/"
        "startup_report.pdf"
    )

    pdf.output(path)

    return path
