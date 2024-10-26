import fitz  # PyMuPDF
from reportlab.lib.pagesizes import A4

# Constants for A4 dimensions in points (1 point = 1/72 inch)
A4_WIDTH, A4_HEIGHT = A4  # Width, Height in points

# Input and output PDF paths
input_pdf_path = "example.pdf"
output_pdf_path = "split_scaled_a4_document.pdf"

# Open the original PDF document
doc = fitz.open(input_pdf_path)

# Create a new PDF to store the split and scaled pages
output_doc = fitz.open()  # New PDF to store the output

# Loop through each page in the original document
for page_num in range(len(doc)):
    page = doc[page_num]
    original_width, original_height = page.rect.width, page.rect.height
    current_y = 0

    # Calculate the scale factor based on width (to fit within A4 width)
    scale_factor = A4_WIDTH / original_width

    # Adjusted dimensions for scaling to fit A4 width
    scaled_height = original_height * scale_factor

    # Split the page vertically into A4-sized sections based on the scaled height
    while current_y < scaled_height:
        # Create a new A4-sized page in the output document
        new_page = output_doc.new_page(width=A4_WIDTH, height=A4_HEIGHT)

        # Define the portion of the content to copy based on the A4 height
        # but scaled to fit within A4 dimensions.
        clip_rect = fitz.Rect(0, current_y / scale_factor, original_width, (current_y + A4_HEIGHT) / scale_factor)

        # Copy content within the clip rectangle to the new A4-sized page with scaling
        new_page.show_pdf_page(
            rect=fitz.Rect(0, 0, A4_WIDTH, A4_HEIGHT),  # Fit within A4 dimensions
            src=doc,                                    # Source document
            pno=page_num,                               # Page number in source document
            clip=clip_rect
        )

        # Move down for the next section, scaled for A4 height
        current_y += A4_HEIGHT

# Save the new PDF with A4-sized pages
output_doc.save(output_pdf_path)
output_doc.close()
doc.close()

print(f"PDF successfully split and scaled to A4 pages and saved as {output_pdf_path}.")
