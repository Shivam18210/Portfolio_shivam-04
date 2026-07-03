import os
import sys

def build_pdf():
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.lib import colors
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
    except ImportError:
        print("ReportLab is not installed. Installing it now...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
        from reportlab.lib.pagesizes import letter
        from reportlab.lib import colors
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

    pdf_filename = "Shivam_Rajput_Resume.pdf"
    
    # 0.75 in margins (54 points)
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        rightMargin=54,
        leftMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Define custom styles
    primary_color = colors.HexColor("#060913")
    accent_color = colors.HexColor("#00f2fe")
    dark_gray = colors.HexColor("#1e293b")
    light_gray = colors.HexColor("#475569")
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=primary_color,
        alignment=TA_LEFT,
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=15,
        textColor=light_gray,
        alignment=TA_LEFT,
        spaceAfter=10
    )
    
    contact_style = ParagraphStyle(
        'ContactText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=dark_gray,
        alignment=TA_LEFT
    )
    
    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=primary_color,
        spaceBefore=12,
        spaceAfter=4,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=dark_gray,
        spaceAfter=6
    )
    
    bullet_style = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=dark_gray,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=4
    )
    
    bold_sub = ParagraphStyle(
        'BoldSub',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=dark_gray
    )
    
    story = []
    
    # 1. Header (Name, Title, Contact Info)
    story.append(Paragraph("SHIVAM RAJPUT", title_style))
    story.append(Paragraph("Web Developer", subtitle_style))
    
    contact_info = (
        "<b>Phone:</b> +91 6392846902 &nbsp;&nbsp;|&nbsp;&nbsp; "
        "<b>Email:</b> rshivam2204@gmail.com &nbsp;&nbsp;|&nbsp;&nbsp; "
        "<b>Location:</b> Rae Bareli, Uttar Pradesh, India<br/>"
        "<b>GitHub:</b> github.com/Shivam18210 &nbsp;&nbsp;|&nbsp;&nbsp; "
        "<b>LinkedIn:</b> linkedin.com/in/shivam-rajput-7b8616292"
    )
    story.append(Paragraph(contact_info, contact_style))
    story.append(Spacer(1, 10))
    
    # Divider Line
    d_table = Table([[""]], colWidths=[504], rowHeights=[1.5])
    d_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), primary_color),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(d_table)
    story.append(Spacer(1, 10))
    
    # 2. Professional Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_heading))
    summary_text = (
        "Results-driven Web Developer specializing in HTML, CSS, JavaScript, React.js, Python, "
        "Flask, and FastAPI. Passionate about building responsive, user-friendly, and scalable web "
        "applications. Focused on responsive design, performance optimization, and premium user experiences."
    )
    story.append(Paragraph(summary_text, body_style))
    
    # 3. Technical Skills
    story.append(Paragraph("TECHNICAL SKILLS", section_heading))
    skills_data = [
        [Paragraph("<b>Frontend:</b>", bold_sub), Paragraph("HTML5, CSS3, JavaScript (ES6+), React.js, Bootstrap, Tailwind CSS", body_style)],
        [Paragraph("<b>Backend:</b>", bold_sub), Paragraph("Python, Flask, FastAPI", body_style)],
        [Paragraph("<b>Tools & Tech:</b>", bold_sub), Paragraph("Git, GitHub, Docker, AWS, Vercel, Netlify, CI/CD", body_style)]
    ]
    skills_table = Table(skills_data, colWidths=[90, 414])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 8))
    
    # 4. Work Experience
    story.append(Paragraph("WORK EXPERIENCE", section_heading))
    
    # Date paragraph style
    date_style = ParagraphStyle(
        'DateStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        textColor=light_gray,
        alignment=TA_RIGHT
    )
    
    # Job 1: Web Developer
    job1_table = Table([
        [Paragraph("<b>Web Developer</b> &nbsp;|&nbsp; Freelance & Tech Consultant", bold_sub),
         Paragraph("Dec 2025 – March 2026", date_style)]
    ], colWidths=[360, 144])
    job1_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'BOTTOM'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(job1_table)
    story.append(Spacer(1, 4))
    story.append(Paragraph("&bull; Developed high-performance, mobile-responsive business and e-commerce websites.", bullet_style))
    story.append(Paragraph("&bull; Implemented SEO best practices to increase online search visibility and organic traffic.", bullet_style))
    story.append(Paragraph("&bull; Improved website accessibility, UI/UX aesthetics, and overall user engagement metrics.", bullet_style))
    story.append(Spacer(1, 6))
    
    # Job 2: Junior Web Developer
    job2_table = Table([
        [Paragraph("<b>Junior Web Developer</b> &nbsp;|&nbsp; Software Solutions Lab", bold_sub),
         Paragraph("July 2024 – Dec 2025", date_style)]
    ], colWidths=[360, 144])
    job2_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'BOTTOM'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(job2_table)
    story.append(Spacer(1, 4))
    story.append(Paragraph("&bull; Built and maintained highly responsive web applications utilizing HTML, CSS, JavaScript, and React.", bullet_style))
    story.append(Paragraph("&bull; Optimized assets, code delivery, and server responses to significantly improve page load performance.", bullet_style))
    story.append(Paragraph("&bull; Integrated custom REST APIs with frontend templates for real-time visual client interactions.", bullet_style))
    story.append(Spacer(1, 6))
    
    # Job 3: Freelance Web Developer
    job3_table = Table([
        [Paragraph("<b>Freelance Web Developer</b> &nbsp;|&nbsp; Self-Employed", bold_sub),
         Paragraph("2021 – 2024", date_style)]
    ], colWidths=[360, 144])
    job3_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'BOTTOM'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(job3_table)
    story.append(Spacer(1, 4))
    story.append(Paragraph("&bull; Built responsive and modern websites for clients.", bullet_style))
    story.append(Paragraph("&bull; Developed custom web applications using HTML, CSS, JavaScript, React.js, Python, Flask, and FastAPI.", bullet_style))
    story.append(Paragraph("&bull; Communicated directly with clients and delivered projects on time.", bullet_style))
    story.append(Paragraph("&bull; Worked with international clients from Dubai, Canada, the UK, and Africa.", bullet_style))
    story.append(Paragraph("&bull; Focused on responsive design, performance optimization, and client satisfaction.", bullet_style))
    story.append(Spacer(1, 8))
    
    # 5. Education
    story.append(Paragraph("EDUCATION", section_heading))
    story.append(Paragraph("<b>Diploma in Electrical and Electronics Engineering</b> &nbsp;|&nbsp; 2021 – 2024", bold_sub))
    story.append(Paragraph("Board of Technical Education, Uttar Pradesh, India", body_style))
    story.append(Spacer(1, 8))
    
    # 6. Projects
    story.append(Paragraph("FEATURED PROJECTS", section_heading))
    
    story.append(Paragraph("<b>E-Commerce Website</b>", bold_sub))
    story.append(Paragraph("Built a full-featured online store layout utilizing React and Python backends. Implemented a secure authentication system, dynamic product catalog search, a persistent shopping cart, and mock API payment gateways.", body_style))
    
    story.append(Paragraph("<b>Personal Developer Portfolio</b>", bold_sub))
    story.append(Paragraph("Created a premium, modern developer portfolio website utilizing custom CSS animations, scroll reveals, dynamic category filters, and an interactive contact validation system. Optimized for SEO and ATS readability.", body_style))
    
    # Build Document
    doc.build(story)
    print(f"Successfully generated {pdf_filename}!")

if __name__ == '__main__':
    build_pdf()
