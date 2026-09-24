"""Fill the official Houston coffee-shop permit forms twice: one PASS set, one FAIL set.

Blank forms live in blank_forms/ (downloaded from the issuing agencies).
Every applicant, address, phone, ID number and signature is made up. Phone numbers
use the reserved 555-01xx range, the SSN is the reserved 987-65-432x range, and email
addresses use the reserved .example TLD. Each output page carries a SAMPLE footer.

Run:  .venv/bin/python build_sets.py
"""
import pathlib
import shutil

import pymupdf
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak)

ROOT = pathlib.Path(__file__).parent
BLANK = ROOT / "blank_forms"
INK = (0.05, 0.1, 0.55)          # "typed" entries
SIG = (0.0, 0.15, 0.45)          # signatures
FOOTER = "SAMPLE / TEST DATA - fictitious applicant, not an actual filing. Generated 2026-09-23."


# ---------------------------------------------------------------- helpers
def footer(doc):
    for page in doc:
        r = page.rect
        page.insert_text((r.width / 2 - 170, r.height - 4), FOOTER,
                         fontsize=6.5, fontname="helv", color=(0.8, 0, 0))


def put(page, xy, text, size=8.5, font="helv", color=INK):
    if text:
        page.insert_text(xy, str(text), fontsize=size, fontname=font, color=color)


def sign(page, xy, name, size=13):
    if name:
        page.insert_text(xy, name, fontsize=size, fontname="tiit", color=SIG)


def hit(page, label, idx=0, max_x=None, near_x=None):
    hits = page.search_for(label)
    if max_x is not None:
        hits = [h for h in hits if h.x0 < max_x]
    if near_x is not None:
        hits = [h for h in hits if abs(h.x0 - near_x) < 4]
    hits.sort(key=lambda r: (round(r.y0), r.x0))
    return hits[idx]


def after(page, label, text, idx=0, dx=4, size=8.5):
    r = hit(page, label, idx)
    put(page, (r.x1 + dx, r.y1 - 2.5), text, size)


def xbox(page, label, idx=0, dx=-9.5, max_x=None, near_x=None):
    r = hit(page, label, idx, max_x, near_x)
    put(page, (r.x0 + dx, r.y1 - 2.2), "X", size=9, font="hebo")


def fill_fields(doc, values, size=9, sizes=None):
    """values: {field_name: str | True}. Checkbox/radio: True, or the on-state name."""
    sizes = sizes or {}
    seen = set()
    for page in doc:
        for w in page.widgets():
            name = w.field_name
            if name not in values:
                continue
            v = values[name]
            if w.field_type in (pymupdf.PDF_WIDGET_TYPE_CHECKBOX, pymupdf.PDF_WIDGET_TYPE_RADIOBUTTON):
                want = w.on_state() if v is True else v
                if w.on_state() != want:
                    continue
                w.field_value = w.on_state()
            elif w.field_type == pymupdf.PDF_WIDGET_TYPE_SIGNATURE:
                continue
            else:
                w.field_value = str(v)
                w.text_color = INK
                w.text_fontsize = sizes.get(name, size)
            w.update()
            seen.add(name)
    missing = set(values) - seen
    assert not missing, f"unknown fields: {missing}"


def widget_rect(doc, name):
    for page in doc:
        for w in page.widgets():
            if w.field_name == name:
                return page, w.rect
    raise KeyError(name)


def sign_field(doc, name, signer, size=12):
    if signer:
        page, r = widget_rect(doc, name)
        sign(page, (r.x0 + 6, r.y1 - 4), signer, size)


def save(doc, out):
    # Drop form buttons and JavaScript (AP-201 ships Print/Clear buttons); upload scanners reject active PDF content.
    for page in doc:
        for w in list(page.widgets()):
            if w.field_type == pymupdf.PDF_WIDGET_TYPE_BUTTON:
                page.delete_widget(w)
    doc.scrub(attached_files=False, clean_pages=False, embedded_files=False, hidden_text=False, javascript=True,
              metadata=False, redactions=False, redact_images=0, remove_links=False, reset_fields=False,
              reset_responses=False, thumbnails=False, xml_metadata=False)
    for x in range(1, doc.xref_length()):  # scrub empties scripts but leaves the action/name entries behind
        if not doc.xref_is_stream(x) and doc.xref_get_key(x, "JavaScript")[0] != "null":
            doc.xref_set_key(x, "JavaScript", "null")
        if doc.xref_get_key(x, "AA")[0] != "null":
            doc.xref_set_key(x, "AA", "null")
        t, v = doc.xref_get_key(x, "A")
        if t == "xref" and doc.xref_get_key(int(v.split()[0]), "S")[1] == "/JavaScript":
            doc.xref_set_key(x, "A", "null")
        elif t == "dict" and "/JavaScript" in v:
            doc.xref_set_key(x, "A", "null")
    cat = doc.pdf_catalog()
    t, v = doc.xref_get_key(cat, "Names")
    if t == "xref" and set(doc.xref_get_keys(int(v.split()[0]))) <= {"JavaScript"}:
        doc.xref_set_key(cat, "Names", "null")
    footer(doc)
    doc.save(out, garbage=3, deflate=True)
    doc.close()


# ---------------------------------------------------------------- data
PASS = dict(
    key="PASS", folder="set_PASS_bayou_bean_coffee",
    dba="Bayou Bean Coffee", entity="Elena Rose Marsh (sole proprietor)", org="Proprietorship",
    owner_first="Elena", owner_mid="Rose", owner_last="Marsh", owner="Elena R. Marsh",
    dob="04/12/1988", dl="09876543", dl_state="TX", ssn="987654321",
    home="2915 Bayland Ave", home_city="Houston", home_zip="77009",
    street="1847 Yale St", suite="Suite 110", unit="110", zip="77008", county="Harris",
    phone="713-555-0142", cell="713-555-0187", email="elena@bayoubeancoffee.example",
    sqft="1,450", seats=32,
)
FAIL = dict(
    key="FAIL", folder="set_FAIL_magnolia_grind_coffee",
    dba="Magnolia Grind Coffee", entity="Magnolia Grind Coffee LLC", org="LLC",
    owner_first="Derek", owner_mid="Thomas", owner_last="Vance", owner="Derek T. Vance",
    street="3302 White Oak Dr", suite="Suite 200", unit="200", zip="77007", county="Harris",
    home="611 Sample Grove Ln", home_city="Houston", home_zip="77018",
    phone="713-555-0164", cell="713-555-0165", email="derek@magnoliagrind.example",
    sqft="2,300", seats=64,
)


# ---------------------------------------------------------------- 1. Harris County assumed name (D-02-07)
def dba_certificate(s, out):
    doc = pymupdf.open(BLANK / "HarrisCounty_D0207_Assumed_Name_Certificate.pdf")
    if s["key"] == "PASS":
        v = {
            "1NAME OF BUSINESS": s["dba"],
            "2ADDRESS OF BUSINESS": f'{s["street"]}, {s["suite"]}',
            "3CITY": "Houston", "4 STATE": "TX", "5 ZIP CODE": s["zip"],
            "6Number of years business will be active not to exceed 10 years": "10",
            "Group1": "Choice1",  # Sole Proprietorship
            "8NAME OF OWNER 1": "Elena                        Rose                        Marsh",
            "9ADDRESS OF RESIDENCE": s["home"], "10CITY": s["home_city"], "11STATE": "TX",
            "12ZIP CODE": s["home_zip"], "14Veteran Status": "No",
            "21BEFORE ME THE UNDERSIGNED AUTHORITY on this day personally appeared 1": "Elena Rose Marsh",
            "GIVEN UNDER MY HAND AND SEAL OF OFFICE THIS": "02", "DAY OF": "June", "undefined_2": "2026",
        }
        fill_fields(doc, v)
        sign_field(doc, "13SIGNATURE OF OWNER", "Elena R. Marsh")
        sign_field(doc, "Signature of Notary or Deputy County Clerk", "Notary Public (sample)", 11)
        page, r = widget_rect(doc, "Signature of Notary or Deputy County Clerk")
        box = pymupdf.Rect(45, r.y0 - 4, 175, r.y1 + 6)
        page.draw_rect(box, color=SIG, width=0.8, dashes="[2] 2")
        put(page, (box.x0 + 6, box.y0 + 13), "NOTARY SEAL", 8, "hebo", SIG)
        put(page, (box.x0 + 6, box.y0 + 26), "(placeholder - sample only)", 6.5, "helv", SIG)
    else:
        v = {
            "1NAME OF BUSINESS": s["dba"],
            "2ADDRESS OF BUSINESS": f'{s["street"]}, {s["suite"]}',
            "3CITY": "Houston", "4 STATE": "TX", "5 ZIP CODE": s["zip"],
            "6Number of years business will be active not to exceed 10 years": "15",
            "Group1": "Choice7",  # Other (an LLC - wrong filing office)
            "8NAME OF OWNER 1": "Magnolia Grind Coffee LLC (Derek T. Vance, member)",
            "9ADDRESS OF RESIDENCE": s["home"], "10CITY": s["home_city"], "11STATE": "TX",
            "12ZIP CODE": s["home_zip"], "14Veteran Status": "Yes",
        }
        fill_fields(doc, v)
        sign_field(doc, "13SIGNATURE OF OWNER", "Derek Vance")
    save(doc, out)


# ---------------------------------------------------------------- 2. Texas Comptroller AP-201
def ap201(s, out):
    doc = pymupdf.open(BLANK / "TX_Comptroller_AP-201_Sales_Tax_Permit.pdf")
    common = {
        "15a": s["street"], "15b": s["suite"], "15c": "Houston", "15d": "TX", "15e": s["zip"], "15f": "Harris",
        "16": s["phone"], "18": s["cell"],
        "24a": s["dba"], "25a": "Houston", "26": "Harris",
        "POB27b": True, "POBjb": True,
        "IntSales37b": True, "38b": True, "Wine41b": True, "Spa42b": True, "Item43b": True, "Item44b": True,
        "AllYear47a": True, "48a": "722515", "IntEarned49b": True, "Diesel50b": True, "Prepaid52b": True,
        "48d": "Coffee shop: espresso drinks, brewed coffee, tea and packaged bakery items; dine-in and to-go.",
    }
    if s["key"] == "PASS":
        v = common | {
            "10": "Elena R. Marsh", "11a": s["ssn"], "TIN13b": True,
            "19": "www.bayoubeancoffee.example",
            "20a": "Elena R. Marsh", "20b": s["email"], "20d": s["cell"],
            "21a": "Luis Ortega (bookkeeper)", "21b": "books@bayoubeancoffee.example", "21d": "832-555-0123",
            "22": "Sample Community Bank, N.A.", "Account22b1": True,
            "23a": "Square (card processing)", "23b": "SAMPLE-MID-0001",
            "Page3Name": "Elena R. Marsh", "Page4Name": "Elena R. Marsh", "Page5Name": "Elena R. Marsh",
            "24b": s["street"], "24c": s["suite"], "24d": "Houston", "24f": s["zip"], "24g": s["phone"],
            "28": "Yale Street Retail Partners, LP - 5120 Sample Commerce Dr, Suite 900, Houston, TX 77027",
            "29b": True, "30b": True, "31a": True, "CustLoc32b": True, "TempLoc33b": True,
            "34b": True, "35b": True, "36b": True,
            "Taxable39a": True, "40b": True, "45b": True, "46": "11/02/2026", "NAICS48b03": True,
            "54dateofsig": "06/05/2026", "54a1": "Elena R. Marsh, Sole Owner",
            "54b1": s["dl"], "54c1": "TX", "54d1": True,
        }
        fill_fields(doc, v)
        put(doc[4], (345, 213), "Elena R. Marsh", 13, "tiit", SIG)
    else:
        v = common | {
            "BusOrgType07": True, "2": "Magnolia Grind Coffee LLC",
            "7a": "Texas", "7b": "03/15/2026",
            "9a1": "Derek T. Vance", "9b1": s["cell"], "9c1": s["home"], "9d1": "Houston", "9e1": "TX",
            "9f1": s["home_zip"], "9i1": "100", "Box9a3": True,
            "15a": "PO Box 7781", "15b": "", "15e": "77270",
            "20a": "Derek T. Vance", "20b": s["email"],
            "Page3Name": "Magnolia Grind Coffee LLC", "Page4Name": "Magnolia Grind Coffee LLC",
            "Page5Name": "Magnolia Grind Coffee LLC",
            "24b": "PO Box 7781", "24d": "Houston", "24f": "77270", "24g": s["phone"],
            "29b": True, "30b": True, "31b": True, "CustLoc32b": True, "TempLoc33b": True,
            "34b": True, "35b": True, "36b": True,
            "Taxable39a": True, "40b": True, "46": "10/05/2026",
            "54a1": "Derek Vance - Managing Member",
        }
        fill_fields(doc, v)
    save(doc, out)


# ---------------------------------------------------------------- 3. Building permit application CE-1263
def building_permit(s, out):
    doc = pymupdf.open(BLANK / "HPC_Building_Permit_Application.pdf")
    page = doc[0]
    if s["key"] == "PASS":
        v = {
            "Commercial": True, "Date": "06/15/2026", "Applicant Name": "Elena R. Marsh",
            "Applicant Email": s["email"], "Other": True, "relationship to project_other": "Tenant / business owner",
            "area code 1": "713", "applicant phone number": "555-0187",
            "Owner Tenant or Business NameRow1": "Bayou Bean Coffee (tenant)", "project address": s["street"],
            "UnitSte No": s["unit"], "city": "Houston", "zip code": s["zip"], "county": "Harris",
            "Key Map": "493F", "No of Stories": "1",
            "Project Manager": "Priya Natarajan, AIA\nNorthside Studio Architects",
            "prj manager address": "400 Sample Heights Blvd, Ste 5", "prj manager city": "Houston",
            "prj manager zip code": "77007", "prj manager email": "priya@northsidestudio.example",
            "prj manager area code": "713", "prj manager phone number": "555-0176",
            "General ContractorRow1": "Heights Build Group LLC\n(Lic. GC - sample)",
            "gc address": "9150 Sample Industrial Rd", "gc city": "Houston", "gc zip code": "77022",
            "gc email": "permits@heightsbuild.example", "area code 3": "713", "gc phone number": "555-0170",
            "Other_3": True, "undefined_3": "Coffee shop",
            "Remodel": True, "total cost of improvements": "86,500",
            "Square Footage added": "0 (1,450 sf finish-out)",
            "Present Occupancy": "M - vacant retail", "Proposed Occupancy": "B - coffee shop (OL 42)",
            "Construction TypeRow1": "II-B", "Fire RatingRow1": "0 hr", "Sprinklers no": True,
            "TDLR Project No": "TABS2026045817",
            "Other Remarks": "Interior finish-out for coffee shop: 3-comp sink, 2 hand sinks, mop sink, 100-gal "
                             "grease interceptor w/ sample well (Sec. 47-513). No cooking equipment.",
        }
        fill_fields(doc, v, sizes={"Other Remarks": 6.5, "Project Manager": 8, "General ContractorRow1": 8})
        sign(page, (140, 747), "Elena R. Marsh")
        put(page, (445, 747), "06/15/2026", 9)
    else:
        v = {
            "Commercial": True, "Date": "09/21/2026", "Applicant Name": "Derek Vance",
            "Applicant Email": s["email"], "Owner": True,
            "area code 1": "713", "applicant phone number": "555-0165",
            "Owner Tenant or Business NameRow1": "Magnolia Grind Cafe", "project address": s["street"],
            "UnitSte No": s["unit"], "city": "Houston", "zip code": s["zip"], "county": "Harris",
            "No of Stories": "1",
            "Retail": True, "Other_4": True, "other scope": "cosmetic",
            "Present Occupancy": "Retail",
            "Other Remarks": "Paint, new counters, add espresso bar + flat-top griddle. Owner will do plumbing.",
        }
        fill_fields(doc, v, sizes={"Other Remarks": 7.5})
    save(doc, out)


# ---------------------------------------------------------------- 4. Deed-restriction declaration (CE-1381 / CE-1380)
def declaration(s, out):
    if s["key"] == "PASS":
        # The tenant is not the land owner, so the landlord entity signs CE-1381.
        doc = pymupdf.open(BLANK / "HPC_CE-1381_Declaration_Business_Entity.pdf")
        v = {
            "IPERMITS APPLICATION": "26045817", "Name (First, middle, last)": "Marcus James Whitfield",
            "DOB": "07/02/1971", "Address": "5120 Sample Commerce Dr, Ste 900, Houston, TX 77027",
            "Country": "USA", "Subdivision": "Houston Heights", "Reserve": "-", "Block No": "112",
            "Lot No": "5", "Street Address": s["street"], "city": "Houston", "Zip Code": s["zip"],
            "Business Entity Owner Name": "Yale Street Retail Partners, LP",
            "Type of Entity": "Texas limited partnership",
            "Title of Position": "VP, Yale Street Retail GP, LLC (its GP)",
            "Executed in": "Harris", "State Of": "Texas", "Day": "12", "Month": "June", "Year": "2026",
            "Business Entity": "Yale Street Retail Partners, LP", "Name print": "Marcus J. Whitfield",
            "Title print": "Vice President of its General Partner",
        }
        fill_fields(doc, v)
        sign_field(doc, "Signature", "Marcus J. Whitfield")
    else:
        # Tenant LLC member signs the INDIVIDUAL form and declares "I am an OWNER of the Land".
        doc = pymupdf.open(BLANK / "HPC_CE-1380_Declaration_Individual.pdf")
        v = {
            "Name (first middle and last)": "Derek Thomas Vance",
            "Address": f'{s["home"]}, Houston, TX {s["home_zip"]}', "Country": "USA",
            "Street Address": s["street"], "Texas": "Houston", "Zip Cod": s["zip"],
        }
        fill_fields(doc, v)
        sign_field(doc, "Signature2", "Derek Vance")
    save(doc, out)


# ---------------------------------------------------------------- 5. Occupancy inspection CE-1045A
def occupancy(s, out):
    doc = pymupdf.open(BLANK / "HPC_CE-1045A_Occupancy_Inspection_Application.pdf")
    if s["key"] == "PASS":
        v = {
            "Date": "09/14/2026", "Business Name on Certificate": s["dba"], "Address of Business": s["street"],
            "Building or Space No If Applicable": s["suite"], "Zip Code": s["zip"], "Total No of Floors": "1",
            "Cell Number": s["cell"],
            "Description of Usage of the Building or Space": "Coffee shop (B occ.), 32 seats, OL 42, no cooking",
            "Total Square Feet": s["sqft"], "Applicants Full Name": "Elena Rose Marsh",
            "Applicants Home Address": s["home"], "Applicants Home CityStateZip": f'Houston, TX {s["home_zip"]}',
            "Applicants Email": s["email"],
        }
        fill_fields(doc, v)
        sign_field(doc, "Applicant Signature", "Elena R. Marsh")
    else:
        v = {
            "Date": "09/21/2026", "Business Name on Certificate": "Magnolia Grind Cafe",
            "Address of Business": s["street"], "Building or Space No If Applicable": "Suite 210",
            "Zip Code": s["zip"], "Total No of Floors": "1",
            "Description of Usage of the Building or Space": "Retail",
            "Applicants Full Name": "Derek Vance", "Applicants Home Address": s["home"],
            "Applicants Home CityStateZip": f'Houston, TX {s["home_zip"]}', "Applicants Email": s["email"],
        }
        fill_fields(doc, v)
    save(doc, out)


# ---------------------------------------------------------------- 6. HHD Food Dealer's Permit application (flat PDF -> overlay)
def food_dealer(s, out):
    doc = pymupdf.open(BLANK / "HHD_Food_Dealer_Permit_Application.pdf")
    p = doc[0]
    xbox(p, "New Application/Preopening", dx=-10)
    xbox(p, "Restaurant", dx=-9)
    p3 = doc[2]
    if s["key"] == "PASS":
        after(p, "Business Name/DBA:", s["dba"])
        after(p, "Business Address:", f'{s["street"]}, {s["suite"]}, Houston, TX')
        after(p, "Zip Code:", s["zip"], 0)
        after(p, "Mailing Address:", f'{s["street"]}, {s["suite"]}, Houston, TX', 0)
        after(p, "Zip Code:", s["zip"], 1)
        after(p, "Business Phone:", s["phone"])
        after(p, "Alternate Phone:", s["cell"])
        after(p, "Email:", s["email"], 0)
        after(p, "Tax ID:", "32093456781 (TX sales tax)", size=7.5)
        after(p, "Hours of Operation:", "Mon-Sat 6:30 AM - 6:00 PM; Sun 7:00 AM - 4:00 PM")
        after(p, "Business Entity/Owner:", "Elena Rose Marsh, sole proprietor, d/b/a Bayou Bean Coffee")
        xbox(p, "Proprietorship", dx=-9)
        after(p, "Contact Phone:", s["cell"], 0)
        after(p, "Contact email:", s["email"], 0)
        after(p, "Responsible Party:", "Same as owner - Elena R. Marsh (Certified Food Manager)", dx=62)
        after(p, "Date of Birth:", s["dob"])
        after(p, "Contact Phone:", s["cell"], 1)
        after(p, "Contact email:", s["email"], 1)
        after(p, "Mailing Address:", f'{s["home"]}, Houston, TX {s["home_zip"]}', 1)
        after(p, "(number /State)", f'{s["dl"]} / TX')
        xbox(p, "Low", max_x=300, dx=-10)
        put(p, (306, hit(p, "Proposed Business Start Date:").y1 - 2.5), "11/02/2026 (pre-opening inspection requested 10/26/2026)")
        put(p, (306, hit(p, "Project Number:").y1 - 2.5), "26045817 (approved plans attached)")
        xbox(p3, "Low Risk", dx=-11)
        for i in range(3):
            xbox(p3, "No", i, dx=-11, near_x=189)
        put(p3, (40, 720), "Signed: ", 8.5)
        sign(p3, (72, 720), "Elena R. Marsh", 12)
        put(p3, (170, 720), "Date: 09/21/2026", 8.5)
    else:
        xbox(p, "LLC", dx=-9)  # before any typed text containing "LLC"
        after(p, "Business Name/DBA:", s["dba"])
        after(p, "Business Address:", f'{s["street"]}, Suite 210, Houston, TX')
        after(p, "Zip Code:", s["zip"], 0)
        after(p, "Mailing Address:", "PO Box 7781, Houston, TX", 0)
        after(p, "Business Phone:", s["phone"])
        after(p, "Email:", s["email"], 0)
        after(p, "Hours of Operation:", "7 days, 6:00 AM - 10:00 PM")
        after(p, "Business Entity/Owner:", "Magnolia Grind Coffee LLC")
        after(p, "Contact Phone:", s["cell"], 0)
        after(p, "Contact email:", s["email"], 0)
        after(p, "Responsible Party:", "Derek Vance", dx=62)
        xbox(p, "Low", max_x=300, dx=-10)
        put(p, (306, hit(p, "Proposed Business Start Date:").y1 - 2.5), "10/05/2026")
        xbox(p3, "Low Risk", dx=-11)
        for i in range(3):
            xbox(p3, "No", i, dx=-11, near_x=189)
    save(doc, out)


# ---------------------------------------------------------------- 7. HFD fire alarm permit (flat PDF -> overlay)
def fire_alarm(s, out):
    doc = pymupdf.open(BLANK / "HFD_Fire_Alarm_Permit_Application.pdf")
    p = doc[0]
    X = 158

    def row(label, idx=0):
        return hit(p, label, idx).y1 - 2.5

    new = hit(p, "New", max_x=250)
    p.draw_oval(pymupdf.Rect(new.x0 - 6, new.y0 - 2, new.x1 + 6, new.y1 + 2), color=INK, width=1)
    xbox(p, "Non-Residence/Business", dx=-26)
    xbox(p, "0-10 actuating devices", dx=-26)
    y_addr = row("Address of Alarm:")
    put(p, (X, y_addr + 3), f'{s["street"]}, {s["suite"]}')
    put(p, (X, y_addr + 26), f'Houston, TX {s["zip"]}')
    tel = [h for h in p.search_for("Number") if h.x0 > 400 and 250 < h.y0 < 320][0]
    put(p, (tel.x1 + 14, tel.y1 - 2.5), s["phone"][:3])
    put(p, (tel.x1 + 52, tel.y1 - 2.5), s["phone"][4:])
    if s["key"] == "PASS":
        put(p, (X, row("Applicant’s Name:") - 2), "Marsh, Elena R.")
        yt = row("Applicant’s Telephone No.:") - 1
        put(p, (166, yt), "713"); put(p, (225, yt), "555-0187")
        put(p, (406, yt), "713"); put(p, (455, yt), "555-0142")
        yd = row("Applicant’s Driver’s Lic. No.:")
        put(p, (X, yd), s["dl"])
        put(p, (hit(p, "State", 0).x1 + 10, yd), "TX")
        put(p, (hit(p, "SSN#").x1 + 12, yd), "987-65-4321")
        put(p, (X, row("Business Name:")), s["dba"])
        yf = row("Federal Tax Number:")
        put(p, (X, yf), "N/A - sole prop.", 7.5)
        put(p, (hit(p, "State Sales Tax No.").x1 + 5, yf), "32093456781", 7.5)
        put(p, (hit(p, "Corporate Charter No.").x1 + 5, yf), "N/A", 7.5)
        put(p, (X, row("Owner Name(if other than")), "N/A - applicant is owner")
        yi = row("Installation of Alarm Date:")
        put(p, (X, yi), "09/08/2026")
        put(p, (hit(p, "Number of actuating devices:").x1 + 10, yi), "6")
        ya = row("Alarm Company:")
        put(p, (X, ya), "Gulf Coast Fire & Alarm Co. (sample)")
        tn = [h for h in p.search_for("Telephone No.") if abs(h.y1 - 2.5 - ya) < 4][0]
        put(p, (tn.x1 + 10, ya), "(713) 555-0199")
        y1 = row("Name of Contact #1:")
        put(p, (X, y1 - 1), "Elena R. Marsh (owner)")
        put(p, (hit(p, "Local Phone No.", 0).x1 + 12, y1 - 1), "(713) 555-0187")
        y2 = row("Name of Contact #2:")
        put(p, (X, y2 - 1), "Luis Ortega (shift manager)")
        put(p, (hit(p, "Local Phone No.", 1).x1 + 12, y2 - 1), "(832) 555-0123")
        ys = hit(p, "Signature of Applicant").y0 - 3
        sign(p, (60, ys), "Elena R. Marsh")
        put(p, (410, ys), "09/14/2026")
    else:
        put(p, (X, row("Applicant’s Name:") - 2), "Vance, Derek")
        yt = row("Applicant’s Telephone No.:") - 1
        put(p, (166, yt), "713"); put(p, (225, yt), "555-0165")
        put(p, (X, row("Business Name:")), "Magnolia Grind Cafe")
        yi = row("Installation of Alarm Date:")
        put(p, (hit(p, "Number of actuating devices:").x1 + 10, yi), "14")
        ya = row("Alarm Company:")
        put(p, (X, ya), "Gulf Coast Fire & Alarm Co. (sample)")
        y1 = row("Name of Contact #1:")
        put(p, (X, y1 - 1), "Derek Vance")
        put(p, (hit(p, "Local Phone No.", 0).x1 + 12, y1 - 1), "(713) 555-0165")
    save(doc, out)


# ---------------------------------------------------------------- 8. HFD unsworn declaration (scanned image -> fixed coords)
def unsworn(s, out):
    doc = pymupdf.open(BLANK / "HFD_Unsworn_Declaration.pdf")
    p = doc[0]
    p.remove_rotation()
    for x, t in [(90, "Elena"), (240, "Rose"), (390, "Marsh")]:
        put(p, (x, 126), t, 10)
    for x, t in [(190, "April"), (340, "12"), (428, "1988")]:
        put(p, (x, 196), t, 10)
    for x, t in [(172, "2915 Bayland Ave"), (324, "Houston"), (428, "TX"), (488, "77009")]:
        put(p, (x, 250), t, 9)
    put(p, (100, 302), "USA", 10)
    put(p, (150, 490), "Harris", 10)
    put(p, (340, 490), "Texas", 10)
    for x, t in [(195, "14th"), (305, "September"), (420, "2026")]:
        put(p, (x, 524), t, 10)
    sign(p, (195, 597), "Elena R. Marsh")
    put(p, (410, 597), "Elena R. Marsh", 10)
    save(doc, out)


# ---------------------------------------------------------------- generated applicant documents (reportlab)
styles = getSampleStyleSheet()
H1 = styles["Title"]
H2 = styles["Heading2"]
BODY = ParagraphStyle("b", parent=styles["BodyText"], fontSize=9.5, leading=12.5)
SMALL = ParagraphStyle("s", parent=BODY, fontSize=8, leading=10)


def rl_footer(c, _doc=None):
    c.saveState()
    c.setFont("Helvetica", 6.5)
    c.setFillColor(colors.red)
    w, _ = c._pagesize
    c.drawCentredString(w / 2, 6, FOOTER)
    c.restoreState()


def table(rows, widths, head=True):
    t = Table(rows, colWidths=widths, repeatRows=1 if head else 0)
    st = [("GRID", (0, 0), (-1, -1), 0.4, colors.grey), ("VALIGN", (0, 0), (-1, -1), "TOP"),
          ("FONTSIZE", (0, 0), (-1, -1), 8.5), ("LEADING", (0, 0), (-1, -1), 10.5)]
    if head:
        st += [("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f3b63")),
               ("TEXTCOLOR", (0, 0), (-1, 0), colors.white), ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold")]
    t.setStyle(TableStyle(st))
    return t


def P(t, st=BODY):
    return Paragraph(t, st)


MENU = {
    "PASS": [
        ("Espresso, Americano, Cortado, Cappuccino, Latte, Mocha", "Espresso + steamed dairy / oat milk (milk held at 41 F or below)"),
        ("Drip coffee, pour-over, cold brew (brewed in-house, held refrigerated)", "Beverage"),
        ("Hot & iced teas, chai latte, lemonade (commercial concentrate)", "Beverage"),
        ("Croissants, muffins, scones, kolaches", "Delivered daily, fully baked, from a permitted commercial bakery; displayed in covered case"),
        ("Pre-packaged yogurt parfaits, sandwiches, salads", "Commercially packaged & labeled; held at 41 F or below in reach-in"),
    ],
    "FAIL": [
        ("Espresso, lattes, cappuccino, drip coffee, cold brew", "Beverage"),
        ("Breakfast tacos - eggs cooked to order (over easy available), chorizo, bacon", "Cooked on flat-top griddle from raw"),
        ("Avocado toast with a soft-poached egg", "Egg cooked to order"),
        ("House-made chicken salad croissant", "Chicken cooked, cooled and held in-house"),
        ("Espresso martini, mimosas (weekends)", "Alcoholic beverage"),
    ],
}


def ops_doc(s, out):
    d = SimpleDocTemplate(str(out), pagesize=letter, topMargin=0.6 * inch, bottomMargin=0.6 * inch,
                          title=f'{s["dba"]} - Menu and Scope of Operations')
    k = s["key"]
    story = [P(f'{s["dba"]}', H1), P("Menu and Scope of Operations", H2),
             P(f'Attachment to Houston Health Department Food Dealer\'s Permit Application - '
               f'{s["street"]}, {s["suite"] if k == "PASS" else "Suite 210"}, Houston, TX {s["zip"]}'), Spacer(1, 8),
             P("Menu", H2), table([["Item", "Preparation / source"]] + [[P(a, SMALL), P(b, SMALL)] for a, b in MENU[k]],
                                  [3.3 * inch, 3.7 * inch])]
    if k == "PASS":
        ops = [
            "Food preparation limited to beverage preparation and plating of fully baked pastries. <b>No cooking, cooling or reheating of TCS food.</b> No raw animal foods.",
            "Milk and plant milks stored in under-counter refrigerators at 41 F or below; thermometers in every unit; temperature log twice daily.",
            "Pastries received daily from a permitted commercial bakery with invoices retained 90 days.",
            "Warewashing: 3-compartment sink (18 x 18 x 12 in. compartments) with drainboards; quaternary ammonium sanitizer with test strips.",
            "Hand sinks at espresso bar and prep/ware area (each within 20 ft of work areas, no door in path); soap, paper towels, signage.",
            "Certified Food Manager on staff: Elena R. Marsh (certificate copy attached). All staff hold Food Handler cards within 60 days of hire.",
            "Grease interceptor: 100-gal exterior unit with sample well; pumped every 90 days by a City-permitted transporter; manifests kept on site 5 years. FOG permit to be issued with food permit.",
            "Solid waste: shared landlord dumpster on concrete pad; recyclables picked up weekly.",
            "Seating: 32 seats (occupant load 42, Group B); no alcohol; no outdoor seating.",
            "No HACCP plan or variance required (no specialized processes, no ROP, no time as a public health control).",
        ]
    else:
        ops = [
            "Full breakfast menu cooked on a 36 in. flat-top griddle behind the espresso bar.",
            "Eggs offered cooked to order. Chicken salad prepared in-house the night before.",
            "Dishes washed in the existing 2-compartment bar sink.",
            "Seating: 64 seats inside plus 12 on the patio. Mimosas served on weekends.",
            "Staff will take a food handler class after opening.",
        ]
    story += [Spacer(1, 10), P("Scope of operations", H2)] + [P("&bull; " + o) for o in ops]
    d.build(story, onFirstPage=rl_footer, onLaterPages=rl_footer)


def plan_sheet(s, out):
    """One-sheet tenant finish-out plan: floor plan + schedules + code notes."""
    c = rl_canvas.Canvas(str(out), pagesize=landscape((11 * inch, 17 * inch)))
    W, H = landscape((11 * inch, 17 * inch))
    k = s["key"]
    c.setTitle(f'{s["dba"]} - Sheet A-1 Floor Plan')
    # title block
    c.setStrokeColor(colors.black); c.setLineWidth(1.2)
    c.rect(18, 18, W - 36, H - 36)
    c.rect(W - 250, 18, 232, 150)
    c.setFont("Helvetica-Bold", 13); c.drawString(W - 240, 146, s["dba"].upper())
    c.setFont("Helvetica", 8)
    suite = s["suite"] if k == "PASS" else "Suite 210"
    for i, t in enumerate([f'{s["street"]}, {suite}', f'Houston, TX {s["zip"]}',
                           "TENANT FINISH-OUT - FOOD SERVICE", f'Area: {s["sqft"]} sf   Seats: {s["seats"]}',
                           "Sheet A-1   Scale: 1/6\" = 1'-0\"",
                           "Northside Studio Architects (sample)" if k == "PASS" else "Drawn by: owner",
                           "Date: 06/10/2026" if k == "PASS" else "Date: 09/18/2026"]):
        c.drawString(W - 240, 128 - i * 13, t)
    if k == "PASS":
        c.setFont("Helvetica-Oblique", 7); c.drawString(W - 240, 30, "Sealed & signed: P. Natarajan, AIA (sample)")
    else:
        c.setFont("Helvetica-Oblique", 7); c.drawString(W - 240, 30, "Not to scale - not for construction")

    ft = 12.0  # points per foot on the drawing (1/6 in = 1 ft)
    ox, oy = 60, 250
    c.setFont("Helvetica-Bold", 11)
    c.drawString(ox, H - 50, "FLOOR PLAN")

    def room(x, y, w, h, label, fill=None):
        if fill:
            c.setFillColor(fill); c.rect(ox + x * ft, oy + y * ft, w * ft, h * ft, fill=1, stroke=0)
        c.setFillColor(colors.black); c.setStrokeColor(colors.black); c.setLineWidth(2)
        c.rect(ox + x * ft, oy + y * ft, w * ft, h * ft)
        c.setFont("Helvetica-Bold", 8); c.drawCentredString(ox + (x + w / 2) * ft, oy + (y + h / 2) * ft + 4, label)

    def equip(x, y, w, h, tag, color=colors.HexColor("#dbe7f5")):
        c.setFillColor(color); c.setLineWidth(0.6)
        c.rect(ox + x * ft, oy + y * ft, w * ft, h * ft, fill=1)
        c.setFillColor(colors.black); c.setFont("Helvetica", 6.5)
        c.drawCentredString(ox + (x + w / 2) * ft, oy + (y + h / 2) * ft - 2, tag)

    def door(x, y, horiz=True):
        c.setStrokeColor(colors.white); c.setLineWidth(3)
        if horiz:
            c.line(ox + x * ft, oy + y * ft, ox + (x + 3) * ft, oy + y * ft)
        else:
            c.line(ox + x * ft, oy + y * ft, ox + x * ft, oy + (y + 3) * ft)
        c.setStrokeColor(colors.black); c.setLineWidth(0.5)
        c.arc(ox + (x - 3) * ft, oy + (y - 3) * ft, ox + (x + 3) * ft, oy + (y + 3) * ft, 0, 90)

    if k == "PASS":
        L, D = 50, 29
        green = colors.HexColor("#c9f0d0")
        room(0, 0, L, D, "")
        room(0, 0, 22, D, "DINING  (600 sf net, 32 seats)", colors.HexColor("#fbfbf5"))
        room(22, 25, 28, 4, "PUBLIC CORRIDOR", colors.HexColor("#fbfbf5"))
        room(22, 13, 16, 12, "BAR / SERVICE", colors.HexColor("#f4f8fc"))
        room(22, 0, 16, 13, "PREP / WAREWASH", colors.HexColor("#f4f8fc"))
        room(38, 13, 12, 12, "RESTROOM (public, ADA)")
        room(38, 5, 12, 8, "DRY STORAGE / OFFICE")
        room(38, 0, 12, 5, "MOP / JANITOR")
        # openings: dining->corridor (cased opening), restroom off corridor, staff doors
        c.setStrokeColor(colors.white); c.setLineWidth(3)
        c.line(ox + 22 * ft, oy + 25.3 * ft, ox + 22 * ft, oy + 28.7 * ft)
        c.line(ox + 22 * ft, oy + 14 * ft, ox + 22 * ft, oy + 20 * ft)   # open service counter to dining
        c.setStrokeColor(colors.black)
        door(0, 12, False); door(41, 25); door(28, 13); door(38, 7, False); door(38, 1, False); door(24, 0)
        c.setFont("Helvetica", 6.5)
        c.drawString(ox + 22.4 * ft, oy + 17 * ft, "counter")
        equip(23, 21.5, 7, 2.5, "E1 espresso"); equip(31, 21.5, 3, 2.5, "HS-1", green)
        equip(34.5, 21.5, 3, 2.5, "E3 grinders"); equip(24, 14, 5, 2.5, "E4 u/c fridge")
        equip(30.5, 14, 7, 2.5, "E5 pastry case")
        equip(23, 1, 9, 2.5, "S-1 3-comp sink", green); equip(32.5, 1, 3, 2.5, "HS-2", green)
        equip(23, 8, 6, 2.5, "E6 reach-in 41F"); equip(30, 8, 7, 2.5, "E7 SS work table")
        equip(46, 0.8, 3, 3, "MS-1", green)
        equip(52, 2, 6, 5, "GI-1 100 gal", colors.HexColor("#f5e3c9"))
        c.setFont("Helvetica", 6.5); c.drawString(ox + 52 * ft, oy + 1 * ft, "sample well SW-1 (exterior)")
        for i in range(4):
            for j in range(4):
                c.circle(ox + (3 + i * 5) * ft, oy + (4 + j * 6) * ft, 6)
        c.setFont("Helvetica", 7)
        c.drawString(ox, oy - 14, "Customer path to restroom: dining -> public corridor -> restroom. Does not pass through bar, prep or warewash.")
    else:
        L, D = 57.5, 40
        room(0, 0, L, D, "")
        room(0, 0, 30, D, "DINING  (1,100 sf net, 64 seats)", colors.HexColor("#fbfbf5"))
        room(30, 20, 17.5, 20, "ESPRESSO BAR / GRIDDLE", colors.HexColor("#f4f8fc"))
        room(30, 0, 17.5, 20, "KITCHEN / PREP", colors.HexColor("#f4f8fc"))
        room(47.5, 20, 10, 20, "STORAGE")
        room(47.5, 0, 10, 20, "RESTROOM")
        door(0, 18, False); door(30, 30, False); door(30, 8, False); door(47.5, 10, False); door(47.5, 30, False)
        equip(31, 37, 8, 2.5, "E1 espresso"); equip(40, 37, 6, 2.5, "E2 griddle")
        equip(31, 21, 7, 2.5, "E4 u/c fridge"); equip(39, 21, 7, 2.5, "E5 pastry case")
        equip(31, 1, 6, 2.5, "S-1 2-comp sink")
        equip(38, 1, 6, 2.5, "E7 work table"); equip(44.5, 10, 2.5, 6, "E6 fridge")
        equip(44, 1, 3, 2.5, "HS-1", colors.HexColor("#c9f0d0"))
        for i in range(6):
            for j in range(5):
                c.circle(ox + (3 + i * 4.6) * ft, oy + (4 + j * 7) * ft, 6)
        c.setFont("Helvetica", 7)
        c.drawString(ox, oy - 14, "Restroom door off kitchen/prep. Rear door at kitchen.")
    # dimensions
    c.setFont("Helvetica", 7); c.setLineWidth(0.4)
    c.line(ox, oy - 26, ox + L * ft, oy - 26); c.drawCentredString(ox + L * ft / 2, oy - 36, f"{L}'-0\"")
    c.line(ox - 16, oy, ox - 16, oy + D * ft); c.drawString(ox - 45, oy + D * ft / 2, f"{D}'-0\"")

    # schedules on the right
    sx = ox + 62 * ft + 30
    if k == "PASS":
        equip_rows = [["Tag", "Item", "Spec"],
                      ["E1", "2-group espresso machine", "NSF/ANSI 4, on legs 4 in."],
                      ["E3", "Grinders (3)", "NSF, counter-sealed"],
                      ["E4", "Under-counter refrigerator", "NSF/ANSI 7, 41 F"],
                      ["E5", "Refrigerated pastry case", "NSF/ANSI 7"],
                      ["E6", "Reach-in refrigerator", "NSF/ANSI 7, 6 in. legs"],
                      ["E7", "Stainless work table", "NSF/ANSI 2, 6 in. legs"],
                      ["S-1", "3-comp sink 18x18x12 + 2 drainboards", "NSF, indirect waste to GI-1"],
                      ["HS-1/2", "Hand sinks, 100 F mixing valve", "20-sec metered faucet"],
                      ["MS-1", "Mop sink (floor, curbed)", "to GI-1"],
                      ["GI-1", "Grease interceptor 100 gal", "Exterior + sample well SW-1"]]
        finish_rows = [["Room", "Floor", "Base", "Walls", "Ceiling"],
                       ["Bar / Prep", "Quarry tile", "Coved tile", "FRP white to 8 ft", "Vinyl-faced ACT, white (LRV 85)"],
                       ["Restroom", "Ceramic tile", "Coved tile", "Tile to 4 ft / paint", "Gyp. bd, semi-gloss white"],
                       ["Mop / storage", "Sealed concrete", "Coved vinyl", "FRP white", "Vinyl-faced ACT, white"],
                       ["Dining", "LVT", "Rubber", "Paint", "Open (dining only)"]]
        notes = ["OCCUPANT LOAD: dining 600 sf / 15 = 40; bar/prep/storage 850 sf / 200 = 5 -> 42 total (< 50). Group B per IBC 303.1.1.",
                 "Hand sinks within 20 ft of espresso bar, prep and warewash, no doors in path (Sec. 20-21.19).",
                 "3-comp sink compartments >= 15x15x12 in. (Sec. 20-21.11).",
                 "Interceptor + sample well per Sec. 47-513; sized per Houston Plumbing Code.",
                 "Lighting: 50 fc prep/bar, 20 fc ware/restroom, 10 fc storage; shielded fixtures over food.",
                 "No cooking appliances; no Type I hood required. Electric equipment only.",
                 "Public restroom accessible without passing through prep (Houston Bldg. Code 2902).",
                 "Pest: self-closing rear door, air curtain at service door."]
    else:
        equip_rows = [["Tag", "Item", "Spec"],
                      ["E1", "Espresso machine", "-"],
                      ["E2", "36 in. gas flat-top griddle", "hood 'TBD'"],
                      ["E4", "Under-counter fridge", "residential"],
                      ["E5", "Pastry case", "-"],
                      ["E6", "Fridge", "-"],
                      ["E7", "Work table", "wood butcher block"],
                      ["S-1", "2-comp bar sink 10x14x10", "-"],
                      ["HS-1", "Hand sink", "-"]]
        finish_rows = [["Room", "Floor", "Base", "Walls", "Ceiling"],
                       ["Bar / Kitchen", "Stained concrete", "-", "Reclaimed wood / paint", "Open deck, painted charcoal black (LRV 8)"],
                       ["Restroom", "Existing", "-", "Paint", "Existing"],
                       ["Dining", "Stained concrete", "-", "Reclaimed wood", "Open deck, black"]]
        notes = ["Seats: 64 inside + 12 patio.",
                 "Grease trap: existing building sewer (none planned).",
                 "Plumbing by owner."]
    c.setFont("Helvetica-Bold", 10); c.drawString(sx, H - 50, "EQUIPMENT SCHEDULE")
    t = table(equip_rows, [40, 170, 140]); tw, th = t.wrapOn(c, 400, 400); t.drawOn(c, sx, H - 60 - th)
    y = H - 60 - th - 30
    c.setFont("Helvetica-Bold", 10); c.drawString(sx, y, "ROOM FINISH SCHEDULE")
    finish_rows = [finish_rows[0]] + [[P(x, SMALL) for x in r] for r in finish_rows[1:]]
    t = table(finish_rows, [62, 62, 52, 78, 116]); tw, th = t.wrapOn(c, 400, 400); t.drawOn(c, sx, y - 10 - th)
    y = y - 10 - th - 30
    c.setFont("Helvetica-Bold", 10); c.drawString(sx, y, "GENERAL / HEALTH CODE NOTES")
    y -= 4
    for n in notes:
        p = Paragraph("&bull; " + n, SMALL); pw, ph = p.wrapOn(c, 340, 200); p.drawOn(c, sx, y - ph); y -= ph + 3
    rl_footer(c)
    c.showPage(); c.save()


def cover(s, out, index, placeholders):
    d = SimpleDocTemplate(str(out), pagesize=letter, topMargin=0.6 * inch, bottomMargin=0.6 * inch,
                          title=f'{s["dba"]} - Permit Package Cover and Index')
    k = s["key"]
    suite = s["suite"] if k == "PASS" else "Suite 200"
    story = [P(f'{s["dba"]}', H1), P("Permit application package - coffee shop / cafe, City of Houston", H2),
             table([["Applicant / owner", s["entity"]],
                    ["Premises", f'{s["street"]}, {suite}, Houston, TX {s["zip"]} (Harris County, inside city limits)'],
                    ["Area / seats", f'{s["sqft"]} sf / {s["seats"]} seats'],
                    ["Contact", f'{s["owner"]} - {s["cell"]} - {s["email"]}']],
                   [1.6 * inch, 5.4 * inch], head=False),
             Spacer(1, 10), P("Documents in this package", H2),
             table([["#", "Document", "Agency", "Form"]] + [[str(i + 1).zfill(2), P(a, SMALL), P(b, SMALL), P(c_, SMALL)]
                                                           for i, (a, b, c_) in enumerate(index)],
                   [0.35 * inch, 3.4 * inch, 2.1 * inch, 1.15 * inch])]
    if placeholders:
        story += [PageBreak()]
        for title, body in placeholders:
            story += [P("ATTACHMENT PLACEHOLDER", H1), P(title, H2), P(body), Spacer(1, 10),
                      P("<i>This sample package does not reproduce government- or third-party-issued documents "
                        "(certificates, IDs, filings). In a real submission, a copy of the document described above "
                        "is attached here.</i>", SMALL), PageBreak()]
        story.pop()
    d.build(story, onFirstPage=rl_footer, onLaterPages=rl_footer)


# ---------------------------------------------------------------- build
def build(s):
    out = ROOT / s["folder"]
    out.mkdir(exist_ok=True)
    for f in out.glob("*.pdf"):
        f.unlink()
    k = s["key"]
    files = [
        ("01_Harris_County_Assumed_Name_Certificate_D-02-07.pdf", dba_certificate,
         "Assumed Name (DBA) Certificate", "Harris County Clerk", "D-02-07"),
        ("02_TX_Sales_and_Use_Tax_Permit_Application_AP-201.pdf", ap201,
         "Texas Sales and Use Tax Permit application", "Texas Comptroller", "AP-201"),
        ("03_Building_Permit_Application_CE-1263.pdf", building_permit,
         "Building permit application (tenant finish-out)", "Houston Permitting Center", "CE-1263"),
        ("04_Deed_Restriction_Declaration_CE-1381.pdf" if k == "PASS" else "04_Deed_Restriction_Declaration_CE-1380.pdf",
         declaration, "Deed-restriction declaration supporting building permit", "Houston Permitting Center",
         "CE-1381" if k == "PASS" else "CE-1380"),
        ("05_Plan_Sheet_A-1_Floor_Plan.pdf", plan_sheet, "Plan sheet A-1 (floor plan, equipment & finish schedules)",
         "HPC / Health Dept. plan review (ProjectDox)", "-"),
        ("06_Menu_and_Scope_of_Operations.pdf", ops_doc, "Menu and scope of operations", "Houston Health Dept.", "-"),
        ("07_Food_Dealers_Permit_Application.pdf", food_dealer, "Food Dealer's Permit application",
         "Houston Health Dept. (Consumer Health)", "HHD Food Dealer App."),
        ("08_Certificate_of_Occupancy_Inspection_Application_CE-1045A.pdf", occupancy,
         "Application for Occupancy Compliance Inspection (Certificate of Occupancy)", "Houston Permitting Center", "CE-1045-A"),
        ("09_Fire_Alarm_Permit_Application.pdf", fire_alarm, "Fire alarm permit application", "Houston Fire Dept.", "HFD"),
    ]
    if k == "PASS":
        files.append(("10_HFD_Unsworn_Declaration.pdf", unsworn, "Unsworn declaration (for fire alarm permit)",
                      "Houston Fire Dept.", "HFD Unsworn Decl."))
    index = []
    for name, fn, title, agency, form in files:
        fn(s, out / name)
        index.append((title, agency, form))
    placeholders = []
    if k == "PASS":
        placeholders = [
            ("Certified Food Manager certificate - Elena R. Marsh",
             "Texas-accredited Certified Food Manager certificate, current through 2029. Required by the Food Dealer's Permit application."),
            ("Government photo ID - Elena R. Marsh (Responsible Party)", "Texas driver license copy."),
            ("Approved, stamped plans - Project 26045817", "Health Dept. and building plan review approval stamps (ProjectDox)."),
            ("Certificate of Occupancy", "Issued after the CE-1045A inspection; attached to the Food Dealer's Permit application before the pre-opening inspection."),
            ("Texas Sales and Use Tax Permit", "Taxpayer No. 32093456781 (issued on the AP-201 in this package)."),
            ("Date-stamped Assumed Name Certificate", "File-stamped copy of the D-02-07 in this package (ownership documentation for a proprietorship)."),
        ]
        index.append(("Attachment placeholders: CFM certificate, ID, stamped plans, CO, sales tax permit, file-stamped DBA",
                      "-", "(see pages 2+ of this file)"))
    cover(s, out / "00_Cover_and_Index.pdf", index, placeholders)


APP_DEMO = ROOT / "app" / "demo-files"


def copy_to_app(s):
    """Mirror a built set into the web app's demo folder (loaded by the preflight page's demo buttons)."""
    if not APP_DEMO.is_dir():
        return
    dest = APP_DEMO / ("official-passing" if s["key"] == "PASS" else "official-failing")
    dest.mkdir(exist_ok=True)
    for f in dest.iterdir():
        f.unlink()
    for f in sorted((ROOT / s["folder"]).iterdir()):
        if f.suffix in (".pdf", ".md"):
            shutil.copy2(f, dest / f.name)
    print("  copied to", dest.relative_to(ROOT))


if __name__ == "__main__":
    for s in (PASS, FAIL):
        build(s)
        print("built", s["folder"])
        copy_to_app(s)
