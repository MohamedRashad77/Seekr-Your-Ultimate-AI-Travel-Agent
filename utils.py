from fpdf import FPDF

def create_travel_prompt(destination, departure_city, duration, budget):
    """Create the appropriate travel prompt based on budget type."""
    base_prompt = f"""
Overview
Provide a brief overview of {destination}, highlighting its unique features, cultural significance, and what makes it a desirable location for {budget} travel.

Create a detailed travel itinerary for a {budget}-style experience in {destination} for {duration} days.

Include:
1. Accommodation recommendations
2. Flight options from {departure_city}
3. Day-by-day itinerary
4. Culinary experiences
5. Practical travel tips
6. Budget breakdown
"""
    return base_prompt

def generate_pdf(content, departure_city, destination):
    """Generate a PDF document from the travel itinerary."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add title and content
    pdf.cell(200, 10, txt="Seekr: Your Ultimate AI Travel Agent", ln=True, align='C')
    pdf.cell(200, 10, txt="Travel Itinerary", ln=True, align='C')
    pdf.cell(200, 10, txt=f"From {departure_city} to {destination}", ln=True, align='C')

    # Add content with proper encoding
    for line in content.splitlines():
        pdf.multi_cell(0, 10, line.encode('latin1', 'ignore').decode('latin1'))

    return pdf.output(dest='S').encode('latin1')
