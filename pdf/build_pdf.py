"""
Optimum Water Solutions - Sales Training Cheat Sheet
Printable PDF for instructor handout
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfgen import canvas

# ===== COLORS =====
NAVY = HexColor('#0F1B2D')
GOLD = HexColor('#B8862E')
INK = HexColor('#1A1A1A')
DIM = HexColor('#5A5A5A')
LIGHT = HexColor('#E8E4DA')
CREAM = HexColor('#F8F5EE')
RED = HexColor('#A02929')
GREEN = HexColor('#2D5F3F')

OUTPUT_PATH = '/mnt/user-data/outputs/optimum-cheat-sheet.pdf'


# ===== STYLES =====
def make_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name='TitleBig', parent=styles['Title'],
        fontName='Helvetica-Bold', fontSize=32, leading=36,
        textColor=NAVY, spaceAfter=4, alignment=TA_LEFT,
    ))
    styles.add(ParagraphStyle(
        name='Subtitle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=11, leading=14,
        textColor=DIM, spaceAfter=20, alignment=TA_LEFT,
        letterSpacing=2,
    ))
    styles.add(ParagraphStyle(
        name='SectionHead', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=18, leading=22,
        textColor=NAVY, spaceBefore=14, spaceAfter=8,
        borderPadding=0,
    ))
    styles.add(ParagraphStyle(
        name='SubHead', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=12, leading=15,
        textColor=GOLD, spaceBefore=12, spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name='Body', parent=styles['Normal'],
        fontName='Helvetica', fontSize=10, leading=14,
        textColor=INK, spaceAfter=6, alignment=TA_LEFT,
    ))
    styles.add(ParagraphStyle(
        name='Script', parent=styles['Normal'],
        fontName='Helvetica-Oblique', fontSize=10, leading=14,
        textColor=NAVY, spaceAfter=6, leftIndent=10,
    ))
    styles.add(ParagraphStyle(
        name='Tiny', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8, leading=10,
        textColor=DIM, spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        name='Lesson', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=10, leading=14,
        textColor=RED, spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name='Caption', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8, leading=10,
        textColor=DIM, spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name='Step', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=10, leading=14,
        textColor=NAVY, spaceAfter=2,
    ))
    return styles


s = make_styles()


# ===== PAGE DECORATIONS =====
def page_decorations(canvas_obj, doc):
    """Header/footer for every page"""
    canvas_obj.saveState()
    width, height = letter

    # Top gold line
    canvas_obj.setFillColor(GOLD)
    canvas_obj.rect(0.5 * inch, height - 0.45 * inch, width - 1 * inch, 1.5, fill=1, stroke=0)

    # Top right brand
    canvas_obj.setFont('Helvetica-Bold', 7)
    canvas_obj.setFillColor(NAVY)
    canvas_obj.drawRightString(width - 0.5 * inch, height - 0.35 * inch,
                                'OPTIMUM WATER SOLUTIONS · SALES TRAINING')

    # Top left page number
    canvas_obj.setFont('Helvetica', 7)
    canvas_obj.setFillColor(DIM)
    canvas_obj.drawString(0.5 * inch, height - 0.35 * inch, f'PAGE {doc.page:02d}')

    # Bottom line
    canvas_obj.setFillColor(LIGHT)
    canvas_obj.rect(0.5 * inch, 0.5 * inch, width - 1 * inch, 0.5, fill=1, stroke=0)

    # Bottom right
    canvas_obj.setFont('Helvetica-Oblique', 7)
    canvas_obj.setFillColor(DIM)
    canvas_obj.drawRightString(width - 0.5 * inch, 0.35 * inch,
                                'INSTRUCTOR HANDOUT · DRILL DAILY')

    canvas_obj.restoreState()


def cover_decorations(canvas_obj, doc):
    """Special decoration for cover page only"""
    width, height = letter
    canvas_obj.saveState()

    # Big gold accent block top
    canvas_obj.setFillColor(NAVY)
    canvas_obj.rect(0, height - 2.5 * inch, width, 2.5 * inch, fill=1, stroke=0)

    # Gold accent stripe
    canvas_obj.setFillColor(GOLD)
    canvas_obj.rect(0, height - 2.55 * inch, width, 6, fill=1, stroke=0)

    # Bottom navy block
    canvas_obj.setFillColor(NAVY)
    canvas_obj.rect(0, 0, width, 0.6 * inch, fill=1, stroke=0)

    # Bottom gold stripe
    canvas_obj.setFillColor(GOLD)
    canvas_obj.rect(0, 0.6 * inch, width, 4, fill=1, stroke=0)

    # Title in white on navy
    canvas_obj.setFillColor(white)
    canvas_obj.setFont('Helvetica-Bold', 48)
    canvas_obj.drawString(0.6 * inch, height - 1.5 * inch, 'THE OPTIMUM')
    canvas_obj.setFont('Helvetica-Bold', 48)
    canvas_obj.drawString(0.6 * inch, height - 2.05 * inch, 'PLAYBOOK')

    # Tagline
    canvas_obj.setFont('Helvetica', 9)
    canvas_obj.setFillColor(GOLD)
    canvas_obj.drawString(0.6 * inch, height - 2.3 * inch,
                          'EVERY SCRIPT  ·  EVERY PROCESS  ·  EVERY OBJECTION  ·  EVERY DOLLAR')

    # Bottom text
    canvas_obj.setFillColor(white)
    canvas_obj.setFont('Helvetica-Bold', 8)
    canvas_obj.drawString(0.6 * inch, 0.27 * inch, 'OPTIMUM WATER SOLUTIONS')
    canvas_obj.setFont('Helvetica', 8)
    canvas_obj.drawRightString(width - 0.6 * inch, 0.27 * inch, 'SALES TRAINING · INSTRUCTOR EDITION')

    canvas_obj.restoreState()


# ===== HELPERS =====
def hr():
    return HRFlowable(width='100%', thickness=0.5, color=LIGHT, spaceBefore=4, spaceAfter=8)


def gold_hr():
    return HRFlowable(width='100%', thickness=1.5, color=GOLD, spaceBefore=2, spaceAfter=10)


def boxed_script(text, width=6.5*inch):
    """A script box - italic with gold left border"""
    p = Paragraph(text, s['Script'])
    t = Table([[p]], colWidths=[width])
    t.setStyle(TableStyle([
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('BACKGROUND', (0,0), (-1,-1), CREAM),
        ('LINEBEFORE', (0,0), (0,-1), 2.5, GOLD),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    return t


def lesson_box(text, width=6.5*inch):
    """A red 'lesson' callout box"""
    p = Paragraph(f"<b>WHY:</b> {text}", s['Body'])
    t = Table([[p]], colWidths=[width])
    t.setStyle(TableStyle([
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('BACKGROUND', (0,0), (-1,-1), HexColor('#FBF1F1')),
        ('LINEBEFORE', (0,0), (0,-1), 2, RED),
    ]))
    return t


# ===== BUILD PAGES =====
def build():
    doc = SimpleDocTemplate(
        OUTPUT_PATH, pagesize=letter,
        leftMargin=0.55*inch, rightMargin=0.55*inch,
        topMargin=0.65*inch, bottomMargin=0.65*inch,
        title='Optimum Water Solutions - Sales Cheat Sheet',
        author='Optimum Water Solutions Sales Training',
    )

    story = []

    # ==========================================================
    # PAGE 1 — COVER
    # ==========================================================
    # Cover is mostly drawn on canvas. Just push some space.
    story.append(Spacer(1, 5.5 * inch))

    # Course at-a-glance table
    overview = [
        ['1', 'THE PROCESS', '15 steps from cold door to closed deal'],
        ['2', 'COLD CALL', 'How to walk in and walk out with a card in 2 minutes'],
        ['3', 'PHONE', 'The 4-step, 30-second appointment-setting call'],
        ['4', 'THE PITCH', '10 steps that turn a meeting into a free trial'],
        ['5', 'CLOSING', '"Follow the Pen" - the ritual close'],
        ['6', 'COMP PLAN', 'How term, price, and bonus tiers make you wealthy'],
        ['7', 'PRODUCTS', 'Five machines, two pitches, every spec you need'],
        ['8', 'OBJECTIONS', 'Every "no" they\'ll throw and how to flip it'],
    ]
    overview_table = Table(overview, colWidths=[0.4*inch, 1.6*inch, 5.0*inch])
    overview_table.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (0,-1), 14),
        ('TEXTCOLOR', (0,0), (0,-1), GOLD),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (1,0), (1,-1), 10),
        ('TEXTCOLOR', (1,0), (1,-1), NAVY),
        ('FONTNAME', (2,0), (2,-1), 'Helvetica'),
        ('FONTSIZE', (2,0), (2,-1), 10),
        ('TEXTCOLOR', (2,0), (2,-1), INK),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LINEBELOW', (0,0), (-1,-2), 0.25, LIGHT),
    ]))
    story.append(Paragraph('<font color="#0F1B2D"><b>EIGHT MODULES</b></font>', s['SubHead']))
    story.append(overview_table)
    story.append(PageBreak())

    # ==========================================================
    # PAGE 2 — THE COMPLETE SALES PROCESS
    # ==========================================================
    story.append(Paragraph('THE COMPLETE SALES PROCESS', s['SectionHead']))
    story.append(gold_hr())
    story.append(Paragraph(
        'Every deal you ever close at Optimum follows the same 15-step path. '
        'Master the order. Skip a step and the deal dies.', s['Body']))
    story.append(Spacer(1, 8))

    process = [
        ['STAGE', 'STEP', 'ACTION', 'TOOL'],
        ['PROSPECT', '1', 'Hit the door — collect business card with magic question', 'Pen'],
        ['', '2', 'Phone the decision-maker — set the appointment', 'Phone'],
        ['SETUP', '3', 'Create Company in Water Desk', 'Water Desk'],
        ['', '4', 'Add Contact under that company', 'Water Desk'],
        ['', '5', 'Create Meeting (type: Self-Generated Appointment)', 'Water Desk'],
        ['PITCH', '6', 'Run the 10-step pitch — get the free trial', 'Brochures, TDS, Precipitator'],
        ['INSTALL', '7', 'Create Opportunity (✓ check credit requested)', 'Water Desk'],
        ['', '8', 'Create Work Order — attach 3 photos', 'Water Desk'],
        ['', '9', 'Email scheduling@drinkoptimum.com — "Install Date Request"', 'Email'],
        ['', '10', 'Send customer the install confirmation template', 'Email'],
        ['', '11', '— INSTALL HAPPENS —', '—'],
        ['CLOSE', '12', 'Two-day follow-up — IN PERSON, UNANNOUNCED', 'Pre-filled agreement'],
        ['', '13', 'If no close: schedule a PCM (Physical Closing Meeting)', 'Calendar'],
        ['', '14', 'Close → scan → email admin@drinkoptimum.com', 'TurboScan + email'],
        ['', '15', 'Mark Opportunity "Closed Won" in Water Desk', 'Water Desk'],
    ]
    proc_table = Table(process, colWidths=[0.9*inch, 0.4*inch, 4.0*inch, 1.7*inch])
    proc_table.setStyle(TableStyle([
        # Header row
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 8),
        # Body
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 9),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (0,1), (0,-1), GOLD),
        ('FONTSIZE', (0,1), (0,-1), 8),
        ('FONTNAME', (1,1), (1,-1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (1,1), (1,-1), NAVY),
        ('ALIGN', (1,0), (1,-1), 'CENTER'),
        # Padding
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        # Lines
        ('LINEBELOW', (0,0), (-1,0), 1, GOLD),
        ('LINEBELOW', (0,1), (-1,-2), 0.25, LIGHT),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        # Stage shading
        ('BACKGROUND', (0,1), (-1,2), CREAM),  # PROSPECT
        ('BACKGROUND', (0,6), (-1,10), CREAM),  # INSTALL
    ]))
    story.append(proc_table)

    story.append(Spacer(1, 14))
    story.append(Paragraph('THREE THINGS THE PROCESS TEACHES', s['SubHead']))
    story.append(Paragraph(
        '<b>1. NEVER PITCH AT THE DOOR.</b> Your close rate drops 75% if the customer hasn\'t '
        'INVITED you in. Get the card, set the appointment, pitch on their schedule.', s['Body']))
    story.append(Paragraph(
        '<b>2. THE 2-DAY FOLLOW-UP IS WHERE DEALS CLOSE.</b> Most reps phone instead of '
        'visiting. Don\'t. The face-to-face triples your close rate.', s['Body']))
    story.append(Paragraph(
        '<b>3. WATER DESK IS NOT OPTIONAL.</b> If it\'s not in the system, it doesn\'t exist. '
        'Update same-day, every day.', s['Body']))

    story.append(PageBreak())

    # ==========================================================
    # PAGE 3 — COLD CALL + PHONE
    # ==========================================================
    story.append(Paragraph('COLD CALLING THE DOOR', s['SectionHead']))
    story.append(gold_hr())
    story.append(Paragraph(
        '<b>Goal:</b> walk in, get the decision-maker\'s name and card, walk out. '
        'Total time: under 2 minutes.', s['Body']))
    story.append(Paragraph(
        '<b>What you bring:</b> a pen and a smile. <i>Nothing else.</i>', s['Body']))

    story.append(Paragraph('THE 7-STEP DOOR', s['SubHead']))
    door_steps = [
        ['1', 'GREETING', '"Lovely place. How are you today?"'],
        ['2', 'PLACE YOURSELF IN THE AREA', '"I have an appointment next door at ABC. I figured I\'d stop in since I had a few minutes."'],
        ['3', 'THE MAGIC QUESTION', '"Who can I contact about what you do for drinking water and ice for your employees?"'],
        ['4', 'GET THE CARD', '"Does Bobby have a business card I could grab?"'],
        ['5', 'GATHER INFO', '"Real quick — what do you do for water? 5-gallon jugs? Any issues? How many coolers? Anything for ice?"'],
        ['6', "GATEKEEPER'S NAME", '"What was your name?"'],
        ['7', 'GET OUT', '"Awesome. Thanks for your help. I\'ll give Bobby a call. Have a great day."'],
    ]
    dt = Table(door_steps, colWidths=[0.3*inch, 1.7*inch, 4.5*inch])
    dt.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (0,-1), 14),
        ('TEXTCOLOR', (0,0), (0,-1), GOLD),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (1,0), (1,-1), 9),
        ('TEXTCOLOR', (1,0), (1,-1), NAVY),
        ('FONTNAME', (2,0), (2,-1), 'Helvetica-Oblique'),
        ('FONTSIZE', (2,0), (2,-1), 9),
        ('TEXTCOLOR', (2,0), (2,-1), INK),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LINEBELOW', (0,0), (-1,-2), 0.25, LIGHT),
    ]))
    story.append(dt)

    story.append(Spacer(1, 4))
    story.append(lesson_box(
        '"Who can I CONTACT" — the word "contact" is FUTURE TENSE. It signals you\'re '
        'leaving immediately. Disarms the gatekeeper instantly.'))

    story.append(Paragraph('THE 4-STEP PHONE CALL', s['SectionHead']))
    story.append(gold_hr())
    story.append(Paragraph(
        '<b>Goal:</b> set the appointment in 30 seconds. Get to the point in 15-20.', s['Body']))

    phone_steps = [
        ['1', 'GREETING / CLEAR THE TIME', 'Set expectation that this is fast.'],
        ['2', 'RELEVANCE', 'Reference what you learned at the door.'],
        ['3', 'VALUE PROPOSITION', 'Solve the problem you uncovered.'],
        ['4', 'ASSUMPTIVE CLOSE', 'Two-option close: NEVER yes/no.'],
    ]
    pt = Table(phone_steps, colWidths=[0.3*inch, 2.0*inch, 4.2*inch])
    pt.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (0,-1), 14),
        ('TEXTCOLOR', (0,0), (0,-1), GOLD),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (1,0), (1,-1), 9),
        ('TEXTCOLOR', (1,0), (1,-1), NAVY),
        ('FONTNAME', (2,0), (2,-1), 'Helvetica'),
        ('FONTSIZE', (2,0), (2,-1), 9),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LINEBELOW', (0,0), (-1,-2), 0.25, LIGHT),
    ]))
    story.append(pt)

    story.append(Spacer(1, 6))
    story.append(Paragraph('FULL EXAMPLE CALL', s['SubHead']))
    story.append(boxed_script(
        '"Hey JP, this is Paul with Optimum. Glad I caught you — I\'ll be quick. '
        'I stopped by yesterday and talked to Selina up front. She mentioned you\'re using '
        '5-gallon jugs and running out, and the machines are getting nasty. Is that right?<br/><br/>'
        'We have systems that give you a never-ending supply of purified water — usually cost '
        'less than the jugs, and they\'re the most sanitary on the market. We work with a bunch '
        'of your neighbors.<br/><br/>'
        'I\'m gonna be next door Tuesday and Thursday — does Tuesday at 2 work, or is Thursday better?"'
    ))

    story.append(Spacer(1, 4))
    story.append(lesson_box(
        'NEVER ask "Is now a good time?" — it\'s a yes/no that invites a no. '
        'CLEAR the time with a statement. ASSUME with two-option closes.'))

    story.append(PageBreak())

    # ==========================================================
    # PAGE 4 — THE 10-STEP PITCH
    # ==========================================================
    story.append(Paragraph('THE 10-STEP PITCH', s['SectionHead']))
    story.append(gold_hr())
    story.append(Paragraph(
        'This is the spine of every appointment. Memorize the order, drill the lines.', s['Body']))

    pitch_steps = [
        ['1', 'GREETING', '"Beautiful office. Somewhere we can sit and chat?"'],
        ['2', 'BUILD RAPPORT', 'How long here? Where from? Family pictures? Find common ground.'],
        ['3', 'GATHER INFO', '"Before I show you anything, let me ask a few questions."'],
        ['4', 'GO TO THE COOLER', '"Mind if we take a quick look at your system?"'],
        ['5', 'DESTROY WHAT THEY HAVE', 'Open system, dog bowl, 60% workman\'s comp, hands-on-spigot.'],
        ['6', 'DESCRIBE OUR UNITS', 'I-14 first, then PW-90. Two machines only.'],
        ['7', 'PURIFICATION', 'RO + boost filter + activated oxygen.'],
        ['8', 'INSTALLATION', '"Like a fridge ice maker. Lines run like cable."'],
        ['9', 'SERVICE', '"Maintenance schedule we manage for you."'],
        ['10', 'CLOSE FOR THE DEMO', 'Free trial → "If you were to do a free trial..." → "Which machine?"'],
    ]
    pst = Table(pitch_steps, colWidths=[0.3*inch, 1.9*inch, 4.3*inch])
    pst.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (0,-1), 13),
        ('TEXTCOLOR', (0,0), (0,-1), GOLD),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (1,0), (1,-1), 9),
        ('TEXTCOLOR', (1,0), (1,-1), NAVY),
        ('FONTNAME', (2,0), (2,-1), 'Helvetica'),
        ('FONTSIZE', (2,0), (2,-1), 9),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LINEBELOW', (0,0), (-1,-2), 0.25, LIGHT),
        # Highlight the destroy and close steps
        ('BACKGROUND', (0,4), (-1,4), CREAM),
        ('BACKGROUND', (0,9), (-1,9), CREAM),
    ]))
    story.append(pst)

    story.append(Spacer(1, 12))
    story.append(Paragraph('THE FOUR LINES YOU MEMORIZE COLD', s['SubHead']))

    sacred_lines = [
        ('THE RO LINE',
         '"Are you familiar with reverse osmosis? Known worldwide as the best way to purify drinking water."'),
        ('THE SMART WATER LINE',
         '"Have you ever had Smart Water? Our machines make Smart Water — that\'s electrolyte-enhanced, pH-balanced water."'),
        ('THE SERVICE LINE',
         '"We put you on a maintenance schedule that we manage for you."'),
        ('THE 5-DAY GUARANTEE',
         '"If we don\'t fix an issue within 5 days, you don\'t pay for your machine that month."'),
    ]
    for label, line in sacred_lines:
        story.append(Paragraph(f'<font color="#B8862E"><b>{label}</b></font>', s['Caption']))
        story.append(boxed_script(line))
        story.append(Spacer(1, 4))

    story.append(PageBreak())

    # ==========================================================
    # PAGE 5 — DESTROYING THE COMPETITION
    # ==========================================================
    story.append(Paragraph('DESTROYING WHAT THEY HAVE', s['SectionHead']))
    story.append(gold_hr())
    story.append(Paragraph(
        'Step 5 of the pitch. You\'re at their cooler. You point out every problem.', s['Body']))

    story.append(Paragraph('IF THEY HAVE 5-GALLON JUGS', s['SubHead']))
    story.append(boxed_script(
        '"This is what we call an OPEN SYSTEM. Hear that <i>glug-glug</i>? That\'s outside air being pulled '
        'into the tank through the opposite spigot. Whatever\'s in the air, on people\'s hands, on the '
        'bottle — gets pulled right into your water."<br/><br/>'
        '"Do you have a dog at home? You fill the bowl, two days later it\'s slimy. That\'s organic '
        'compounds reacting with plastic — same thing in this tank, except people drink out of yours."<br/><br/>'
        '"International Bottled Water Association says clean every 6 weeks. Nobody ever does."<br/><br/>'
        '"And cross-contamination — people\'s sport bottles jammed against the spigot they\'ve been '
        'drinking from for days. Viruses live on plastic 3-5 days. <b>This is how workplace epidemics happen.</b>"<br/><br/>'
        '"Who\'s the lucky person changing 42-pound bottles? Did you know <b>60% of all workman\'s comp '
        'claims in an office come from these jugs?</b> Average non-surgical back claim is around $100,000."'))

    story.append(Spacer(1, 8))
    story.append(Paragraph('IF THEY HAVE A FILTER COOLER (CARBON ONLY)', s['SubHead']))
    story.append(boxed_script(
        '"Carbon filtration only removes gases — chlorine, sulfur. Same as your fridge or a Brita. '
        'Lead, mercury, arsenic, chromium 6 — all stay in your water."<br/><br/>'
        '"Let me run a TDS test. <i>[Test their water — usually 150+ PPM]</i> '
        'And purified water? Should be under 20 PPM."<br/><br/>'
        '"Plus your carbon filter <b>removes the chlorine</b>. Chlorine is a poison — but it\'s the only thing '
        'keeping bacteria from growing in the tank. Once it\'s gone, the tank is a Petri dish."<br/><br/>'
        '<b>[Run the precipitator demo]</b> "Watch this. I added nothing to your water — I just ran '
        'an electrical current through it. Now look at what came out of solution. <i>Cheers.</i> '
        'Which would you rather drink?"'))

    story.append(Spacer(1, 8))
    story.append(Paragraph('THE FOUR SCARY METALS TO NAME', s['SubHead']))
    metals = Table([
        ['LEAD', 'MERCURY', 'ARSENIC', 'CHROMIUM 6'],
    ], colWidths=[1.6*inch]*4)
    metals.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 12),
        ('TEXTCOLOR', (0,0), (-1,-1), RED),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.25, LIGHT),
        ('BACKGROUND', (0,0), (-1,-1), HexColor('#FBF1F1')),
    ]))
    story.append(metals)
    story.append(Paragraph(
        '<i>These four roll off the tongue and instantly disgust the customer. Memorize them.</i>',
        s['Tiny']))

    story.append(PageBreak())

    # ==========================================================
    # PAGE 6 — CLOSING & FOLLOW THE PEN
    # ==========================================================
    story.append(Paragraph('THE TWO-DAY FOLLOW-UP & THE CLOSE', s['SectionHead']))
    story.append(gold_hr())

    story.append(Paragraph('THE OPENING LINE', s['SubHead']))
    story.append(boxed_script(
        '"Hey, I was right next door for another appointment. We put a machine in a couple days ago — '
        'figured I\'d pop in. How\'d my technician do? Did he keep it clean in here?"'))

    story.append(Spacer(1, 6))
    story.append(Paragraph('THE TRANSITION TO THE CLOSE', s['SubHead']))
    story.append(boxed_script(
        '"Sounds like you\'re gonna keep it. As the next step, I just need to grab a signature to '
        'set up your account. You have a couple minutes to sit down?"'))

    story.append(Spacer(1, 4))
    story.append(lesson_box(
        'NOT "I need you to sign my contract." Not "Can I get you signed up?" — '
        'You\'re just <b>setting up their account</b>. Reframes the close as a friendly formality.'))

    story.append(Spacer(1, 10))
    story.append(Paragraph('"FOLLOW THE PEN" — THE PAGE 2 RITUAL', s['SectionHead']))
    story.append(gold_hr())
    story.append(Paragraph(
        'Page 1 (satisfaction guarantee) and Page 3 (delivery acceptance) are easy. '
        'Page 2 is where the deal lives or dies. Point to each thing as you say it. '
        'IN THIS ORDER:', s['Body']))

    follow_pen = [
        ['1', 'CUSTOMER INFO', '"Here\'s your info."'],
        ['2', 'PRICE', '"Your price is $115 a month."'],
        ['3', 'BILLING FREQUENCY', '"We\'ll bill you monthly."'],
        ['4', 'TERM (sandwich)', '"We guarantee your price for 60 months."'],
        ['5', 'INSTALL FEE', '"And a one-time $275 install fee. <b>Sign there. Flip the page when you\'re done.</b>"'],
    ]
    fp = Table(follow_pen, colWidths=[0.3*inch, 1.6*inch, 4.6*inch])
    fp.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (0,-1), 14),
        ('TEXTCOLOR', (0,0), (0,-1), GOLD),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (1,0), (1,-1), 9),
        ('TEXTCOLOR', (1,0), (1,-1), NAVY),
        ('FONTNAME', (2,0), (2,-1), 'Helvetica-Oblique'),
        ('FONTSIZE', (2,0), (2,-1), 9),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LINEBELOW', (0,0), (-1,-2), 0.25, LIGHT),
        ('BACKGROUND', (0,3), (-1,3), CREAM),
    ]))
    story.append(fp)

    story.append(Spacer(1, 4))
    story.append(lesson_box(
        'TERM IS SANDWICHED on purpose. If they push back, it\'ll be on the install fee '
        '(the LAST thing you said) — way easier to handle than fighting term.'))

    story.append(Paragraph('NEGOTIATION LEVERS — IN ORDER', s['SubHead']))
    levers = [
        ['1', 'WAIVE INSTALL FEE', 'Costs you ~$75. Use first.'],
        ['2', 'FREE MONTH REBATE', '$0 cost. Only on credit-approved 36+ month deals.'],
        ['3', 'DROP TERM TO 36', 'Costs 2x multiplier. Last resort.'],
        ['4', 'DROP PRICE', 'Kills bonus eligibility. Avoid.'],
    ]
    lt = Table(levers, colWidths=[0.3*inch, 2.0*inch, 4.2*inch])
    lt.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (0,0), (0,-1), GOLD),
        ('FONTSIZE', (0,0), (0,-1), 12),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (1,0), (1,-1), 9),
        ('TEXTCOLOR', (1,0), (1,-1), NAVY),
        ('FONTNAME', (2,0), (2,-1), 'Helvetica'),
        ('FONTSIZE', (2,0), (2,-1), 9),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(lt)

    story.append(Paragraph('CRITICAL: TERMS & CONDITIONS', s['SubHead']))
    story.append(Paragraph(
        '<b><font color="#A02929">LINE 8 (Early Termination): NEVER let them strike this.</font></b> '
        'Striking it makes the contract month-to-month and breaks the deal economics. '
        'You will be charged 2x commission AND 2x bonus back.', s['Body']))
    story.append(Paragraph(
        '<b>Line 9 (Auto-Renewal): They CAN strike.</b> No big deal — goes month-to-month after term.', s['Body']))

    story.append(PageBreak())

    # ==========================================================
    # PAGE 7 — COMP PLAN
    # ==========================================================
    story.append(Paragraph('THE COMP PLAN — HOW YOU GET PAID', s['SectionHead']))
    story.append(gold_hr())

    story.append(Paragraph('TERM MULTIPLIERS (THE MAGIC NUMBERS)', s['SubHead']))
    mults = [
        ['TERM', '60 mo', '48 mo', '36 mo', '24 mo', '12 / Mo-to-mo / Declined'],
        ['MULTIPLIER', '5x', '4x', '3x', '2x', '1x'],
    ]
    mt = Table(mults, colWidths=[1.0*inch, 0.85*inch, 0.85*inch, 0.85*inch, 0.85*inch, 1.7*inch])
    mt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('FONTNAME', (0,1), (0,1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,1), (0,1), 9),
        ('FONTNAME', (1,1), (-1,1), 'Helvetica-Bold'),
        ('FONTSIZE', (1,1), (4,1), 16),
        ('FONTSIZE', (5,1), (5,1), 11),
        ('TEXTCOLOR', (1,1), (1,1), GOLD),
        ('TEXTCOLOR', (2,1), (4,1), NAVY),
        ('TEXTCOLOR', (5,1), (5,1), DIM),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, LIGHT),
    ]))
    story.append(mt)

    story.append(Spacer(1, 12))
    story.append(Paragraph('THE QUARTERLY BONUS TIERS — WHERE YOU GET RICH', s['SubHead']))
    bonus = [
        ['TIER', 'MONTHLY RMR REQUIRED', 'QUARTERLY BONUS FLOOR', 'ON TOP OF COMMISSION?'],
        ['1', '$4,250', '$8,500', 'YES'],
        ['2', '$5,701', '$17,000', 'YES'],
        ['3', '$7,000', '$28,000', 'YES'],
    ]
    bt = Table(bonus, colWidths=[0.6*inch, 1.9*inch, 1.9*inch, 1.7*inch])
    bt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 8),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 11),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (0,1), (0,-1), GOLD),
        ('FONTSIZE', (0,1), (0,-1), 14),
        ('FONTNAME', (2,1), (2,-1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (2,1), (2,-1), GREEN),
        ('FONTSIZE', (2,1), (2,-1), 13),
        ('FONTNAME', (3,1), (3,-1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (3,1), (3,-1), GREEN),
        ('FONTSIZE', (3,1), (3,-1), 9),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, LIGHT),
        ('BACKGROUND', (0,3), (-1,3), HexColor('#FFF8E8')),
    ]))
    story.append(bt)

    story.append(Spacer(1, 12))
    story.append(Paragraph('INSTALL FEE COMMISSION SCHEDULE', s['SubHead']))
    install = [
        ['CHARGE', '$275', '$225', '$175', '$150', 'BELOW $150'],
        ['YOU GET', '$100 ✓', '$80', '$0', '$0', '–$75 (you pay)'],
    ]
    it = Table(install, colWidths=[0.9*inch, 1.0*inch, 1.0*inch, 1.0*inch, 1.0*inch, 1.3*inch])
    it.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('FONTNAME', (0,1), (-1,1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,1), (-1,1), 11),
        ('TEXTCOLOR', (0,1), (0,1), DIM),
        ('TEXTCOLOR', (1,1), (1,1), GREEN),
        ('TEXTCOLOR', (2,1), (3,1), NAVY),
        ('TEXTCOLOR', (4,1), (4,1), DIM),
        ('TEXTCOLOR', (5,1), (5,1), RED),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, LIGHT),
    ]))
    story.append(it)

    story.append(Spacer(1, 12))
    story.append(Paragraph('YEARLY HONORS', s['SubHead']))
    story.append(Paragraph(
        '<b>Prime Minister\'s Club:</b> 250 units in a year → <b>$7,000 cash bonus.</b><br/>'
        '<b>His Majesty\'s Circle:</b> 150+ units in a year → <b>all-expenses trip for two.</b>', s['Body']))

    story.append(Spacer(1, 8))
    story.append(lesson_box(
        '<b>The 3 rules of comp:</b> Hold price. Hold term. Charge install fees. '
        'Drop term LAST when negotiating — you lose 2x multiplier instantly.'))

    story.append(PageBreak())

    # ==========================================================
    # PAGE 8 — PRODUCTS
    # ==========================================================
    story.append(Paragraph('THE FIVE MACHINES (WHAT YOU PITCH)', s['SectionHead']))
    story.append(gold_hr())
    story.append(Paragraph(
        'These are the only five you actively pitch. Two of them — the I-14 and PW-90 — '
        'should be your default. Lead with the I-14, even if they say "no ice."', s['Body']))

    story.append(Spacer(1, 8))
    products = [
        ['MODEL', 'PRICE/MO', 'COLD', 'HOT', 'ROOM', 'ICE', 'TOUCH-FREE', 'EMPLOYEES'],
        ['PW-50', '$85', '1.8 gal', '✓', '—', '—', 'NO', '15-20'],
        ['PW-70', '$105', '2.3 gal', '✓', '—', '—', '✓', '20-30'],
        ['PW-90 ★', '$115', '3 gal', '✓', '—', '—', '✓', '30-40'],
        ['PW-90 CT', '$95', '1 gal', '✓', '—', '—', '✓', '15-20'],
        ['I-14 ★', '$199', 'YES', '✓', '✓', '13/45 lb', '✓', '40-50'],
    ]
    pt = Table(products, colWidths=[0.85*inch, 0.85*inch, 0.7*inch, 0.5*inch, 0.6*inch, 0.85*inch, 0.85*inch, 0.85*inch])
    pt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 8),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 9),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (0,1), (0,-1), NAVY),
        ('FONTNAME', (1,1), (1,-1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (1,1), (1,-1), GREEN),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('GRID', (0,0), (-1,-1), 0.25, LIGHT),
        # Highlight the two stars
        ('BACKGROUND', (0,3), (-1,3), HexColor('#FFF8E8')),
        ('BACKGROUND', (0,5), (-1,5), HexColor('#FFF8E8')),
    ]))
    story.append(pt)
    story.append(Paragraph('★ = your default pitches', s['Tiny']))

    story.append(Paragraph('SPECS YOU MUST KNOW BY HEART', s['SubHead']))
    specs = [
        ['Cold water', '3°C / ~38°F'],
        ['Hot water', '85°C / ~185°F'],
        ['RO output per membrane', '80 gallons/day (XL1 has two = 160 GPD)'],
        ['Filter rating', '1,500 gallons (RO membrane = 3,000)'],
        ['Activated oxygen kills', '100% of bacteria, mold, slime, viruses'],
        ['"+" on model number', 'Includes the boost filter (always order +)'],
    ]
    sp = Table(specs, colWidths=[2.0*inch, 4.4*inch])
    sp.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (0,-1), 9),
        ('TEXTCOLOR', (0,0), (0,-1), DIM),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica'),
        ('FONTSIZE', (1,0), (1,-1), 9),
        ('TEXTCOLOR', (1,0), (1,-1), NAVY),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LINEBELOW', (0,0), (-1,-2), 0.25, LIGHT),
    ]))
    story.append(sp)

    story.append(Paragraph('THE FILTRATION STACK (IN ORDER)', s['SubHead']))
    stack = [
        ['1', 'SEDIMENT FILTER', '10 microns - removes large particles'],
        ['2', 'GAC CARBON', '5 microns - removes chlorine, herbicides'],
        ['3', 'CARBON BLOCK', '1 micron - removes finer chemicals'],
        ['4', 'RO MEMBRANE', '0.0001 micron - removes lead, mercury, arsenic, chromium 6'],
        ['5', 'BOOST FILTER', 'Adds Ca, Mg, K, Na bicarbonate / raises pH'],
    ]
    st = Table(stack, colWidths=[0.3*inch, 1.5*inch, 4.6*inch])
    st.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (0,-1), 13),
        ('TEXTCOLOR', (0,0), (0,-1), GOLD),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (1,0), (1,-1), 9),
        ('TEXTCOLOR', (1,0), (1,-1), NAVY),
        ('FONTNAME', (2,0), (2,-1), 'Helvetica'),
        ('FONTSIZE', (2,0), (2,-1), 9),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LINEBELOW', (0,0), (-1,-2), 0.25, LIGHT),
    ]))
    story.append(st)

    story.append(PageBreak())

    # ==========================================================
    # PAGE 9 — OBJECTIONS
    # ==========================================================
    story.append(Paragraph('OBJECTION HANDLING', s['SectionHead']))
    story.append(gold_hr())
    story.append(Paragraph(
        'Every objection bounces back to value or reframes the question. Never argue. '
        'Never go yes/no. Always close on YOUR schedule.', s['Body']))

    objections = [
        ('"We\'re all set."',
         '"You may be — but Sally said you don\'t actually drink the water. Most of your neighbors said the same until they saw what we do. Have you ever had Smart Water? Our machines make Smart Water. 10 minutes — Tuesday or Thursday?"'),
        ('"We tried this before."',
         '"You haven\'t tried ours. Our systems are the most technologically advanced on the market. Have you ever had Smart Water? Our machines make Smart Water. Just 10 minutes."'),
        ('"Just send me info."',
         '"If I email you\'ll have more questions than answers. That\'s why I do everything in person. 10 minutes is all I need."'),
        ('"60 months is too long."',
         '"60 months is our standard term." [PAUSE - SHUT UP] If they push: "These machines are extremely expensive — we typically don\'t break even until 30-36 months. That\'s why."'),
        ('"What if we move?"',
         '"We\'ll relocate it for free. Lines run like cable wire — fully reversible. Same for sweep, paint, redecorate."'),
        ('"What if we cancel?"',
         '"You won\'t want to. We have a 5-day fix guarantee — if we don\'t resolve any issue in 5 days, you don\'t pay that month. That keeps us honest."'),
        ('"It\'s too expensive."',
         '"Most customers actually save money compared to their current setup. Let me run the math vs your jugs."'),
        ('"We need to think about it."',
         '"Totally understand — that\'s exactly why we offer free trials. No paperwork, no obligation. Worst case, you get amazing water for two weeks free. Which machine would you like to try?"'),
        ('"Need to ask my boss / corporate."',
         '"Of course — let me give you the materials so you can pitch them. While that\'s happening, can I drop a free trial in? Costs nothing, no contract — just lets the team taste the difference while you talk to corporate."'),
        ('"You\'re too expensive vs. the jugs."',
         '"Compare apples to apples — our $115/mo includes filters, all maintenance, 5-day fix guarantee, never-empty water, ice option. Your jugs cost $X/jug + delivery + machine rental + cleaning labor + back injury risk. Want me to do the math?"'),
    ]
    for q, a in objections:
        story.append(Paragraph(f'<font color="#A02929"><b>{q}</b></font>', s['Caption']))
        story.append(boxed_script(a, width=6.4*inch))
        story.append(Spacer(1, 5))

    story.append(PageBreak())

    # ==========================================================
    # PAGE 10 — DAILY HABITS, RESOURCES, CONTACTS
    # ==========================================================
    story.append(Paragraph('DAILY HABITS — THE WEEK OF A WINNER', s['SectionHead']))
    story.append(gold_hr())

    daily = [
        ['MORNING', '10 doors before lunch · Plan the route the night before · Dress sharp'],
        ['MIDDAY', 'Phone follow-ups · Lunch · 1-2 appointments scheduled'],
        ['AFTERNOON', '10 more doors · Run any 2-day follow-ups in person'],
        ['EVENING', 'Update Water Desk · Log CADS · Plan tomorrow\'s route · Drill the playbook 15 min'],
        ['WEEKLY', 'Review pipeline · Update LTA list (always 20+) · Send weekly projection report'],
    ]
    dt = Table(daily, colWidths=[1.0*inch, 5.4*inch])
    dt.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (0,0), (0,-1), GOLD),
        ('FONTSIZE', (0,0), (0,-1), 10),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica'),
        ('FONTSIZE', (1,0), (1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LINEBELOW', (0,0), (-1,-2), 0.25, LIGHT),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(dt)

    story.append(Paragraph('CADS — WHAT TO LOG DAILY', s['SubHead']))
    cads = Table([
        ['C', 'A', 'D', 'S'],
        ['CARDS\ncollected', 'APPTS\nset', 'DEMOS\n(free trials)', 'SALES\nclosed'],
    ], colWidths=[1.6*inch]*4)
    cads.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 36),
        ('TEXTCOLOR', (0,0), (-1,0), GOLD),
        ('FONTNAME', (0,1), (-1,1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,1), (-1,1), 9),
        ('TEXTCOLOR', (0,1), (-1,1), NAVY),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('GRID', (0,0), (-1,-1), 0.5, LIGHT),
        ('BACKGROUND', (0,0), (-1,0), CREAM),
    ]))
    story.append(cads)
    story.append(Paragraph(
        '<i>CADS counts deals, not units. 3 free trials at one company = 1 D, not 3.</i>',
        s['Tiny']))

    story.append(Paragraph('CRITICAL EMAILS', s['SubHead']))
    emails = [
        ['scheduling@drinkoptimum.com', 'Install date requests (subject: "Install Date Request")'],
        ['admin@drinkoptimum.com', 'Signed agreements (subject: [Company Name] Agreement)'],
        ['customerservice@drinkoptimum.com', 'Service tickets for current customers'],
    ]
    et = Table(emails, colWidths=[2.5*inch, 3.9*inch])
    et.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Courier-Bold'),
        ('FONTSIZE', (0,0), (0,-1), 9),
        ('TEXTCOLOR', (0,0), (0,-1), NAVY),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica'),
        ('FONTSIZE', (1,0), (1,-1), 9),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LINEBELOW', (0,0), (-1,-2), 0.25, LIGHT),
    ]))
    story.append(et)

    story.append(Paragraph('STUDY DRILL — HOW TO USE THIS DOCUMENT', s['SubHead']))
    story.append(Paragraph(
        '<b>Week 1:</b> Memorize the 4 sacred lines (RO, Smart Water, Service, 5-Day). '
        'Memorize the 10-step pitch order. Know the 5 machines + prices.', s['Body']))
    story.append(Paragraph(
        '<b>Week 2:</b> Drill the destruction scripts (jug + filter cooler) out loud. '
        'Practice "Follow the Pen" with a friend. Run mock objection drills.', s['Body']))
    story.append(Paragraph(
        '<b>Week 3+:</b> By the time you arrive at training, recite the full 10-step pitch '
        'cold. Know every install fee scenario. Track CADS daily.', s['Body']))

    story.append(Spacer(1, 14))
    story.append(gold_hr())

    # Final motto
    motto = Paragraph(
        '<para alignment="center"><font face="Helvetica-Bold" size="14" color="#0F1B2D">'
        'VOLUME OF ACCOUNTS FIXES ALL WOES.</font></para>',
        s['Body']
    )
    story.append(motto)
    story.append(Paragraph(
        '<para alignment="center"><font color="#5A5A5A" size="9"><i>'
        '20 doors a day. Every day. The rest follows.</i></font></para>',
        s['Body']
    ))

    # ===== BUILD =====
    doc.build(story, onFirstPage=cover_decorations, onLaterPages=page_decorations)
    print(f"PDF built: {OUTPUT_PATH}")


if __name__ == '__main__':
    build()
