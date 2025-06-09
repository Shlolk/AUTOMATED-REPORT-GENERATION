from fpdf import FPDF

# Function to read and analyze the file
def analyze_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)

    return line_count, word_count, char_count

# Function to generate PDF report
def generate_pdf_report(line_count, word_count, char_count, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)

    pdf.cell(200, 10, txt="Text File Analysis Report", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Total Lines: {line_count}", ln=True)
    pdf.cell(200, 10, txt=f"Total Words: {word_count}", ln=True)
    pdf.cell(200, 10, txt=f"Total Characters: {char_count}", ln=True)

    pdf.output(output_path)
    print(f"PDF report generated: {output_path}")

# Main execution
if __name__ == "__main__":
    input_file = "/sdcard/data.txt"        # Android path
    output_pdf = "/sdcard/report.pdf"      # Android path

    try:
        lines, words, chars = analyze_file(input_file)
        generate_pdf_report(lines, words, chars, output_pdf)
    except FileNotFoundError:
        print("File not found. Make sure data.txt is in internal storage (/sdcard/).")