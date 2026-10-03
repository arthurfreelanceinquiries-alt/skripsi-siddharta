#!/usr/bin/env python3
# build_v2.py - Rebuild DOCX v2 serapih Arthur, Pedoman 2023
# Only writes 2 files in 01_Naskah_Utama (disjoint). Builder lives in Temp.
import re, os
from pathlib import Path
from docx import Document
from docx.shared import Cm, Pt, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER, WD_LINE_SPACING
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BASE = Path(r"Z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\01_Naskah_Utama")
OUT_DOCX = BASE / "Proposal_Skripsi_MLBB_GenZ.docx"
OUT_LOG = BASE / "BUILD_LOG_DOCX.md"
BAB1 = BASE / "BAB_I_DRAF.md"
BAB2 = BASE / "BAB_II_DRAF.md"
BAB3 = BASE / "BAB_III_DRAF.md"
PUST = BASE / "DAFTAR_PUSTAKA_SEMENTARA.md"
FIG_TMP = Path(r"C:\Users\Arthur Reezan\AppData\Local\Temp\opencode\fig_rerangka_21.png")
if not FIG_TMP.exists():
    FIG_TMP = Path(r"Z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\scratch\fig_rerangka_21.png")

BLACK = RGBColor(0,0,0)

def set_run(run, size_pt=12, bold=None, italic=None, name="Times New Roman"):
    run.font.name = name
    r = run._element
    rPr = r.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.append(rFonts)
    for attr in ['w:ascii','w:hAnsi','w:cs','w:eastAsia']:
        rFonts.set(qn(attr), name)
    run.font.size = Pt(size_pt)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic
    run.font.color.rgb = BLACK

def parse_inline(par, text, base_size=12, base_bold=False):
    # nested *** ** * -> runs. Also handles `code` strip.
    # First strip backticks
    text = text.replace("`","")
    # pattern for ***text***, **text**, *text*
    pat = re.compile(r'(\*\*\*.+?\*\*\*|\*\*.+?\*\*|\*.+?\*)')
    pos = 0
    for m in pat.finditer(text):
        if m.start()>pos:
            r = par.add_run(text[pos:m.start()])
            set_run(r, base_size, base_bold, False)
        tok = m.group(0)
        if tok.startswith("***"):
            inner = tok[3:-3]
            r = par.add_run(inner)
            set_run(r, base_size, True, True)
        elif tok.startswith("**"):
            inner = tok[2:-2]
            r = par.add_run(inner)
            set_run(r, base_size, True, False)
        else:
            inner = tok[1:-1]
            r = par.add_run(inner)
            set_run(r, base_size, base_bold if base_bold else False, True)
        pos = m.end()
    if pos < len(text):
        r = par.add_run(text[pos:])
        set_run(r, base_size, base_bold, False)

def parenthetical_amp(text):
    # Replace " dan " with " & " only inside (...) that contains 4-digit year
    def repl(m):
        inner = m.group(0)
        if re.search(r'(19|20)\d{2}', inner):
            return inner.replace(" dan ", " & ")
        return inner
    return re.sub(r'\([^()]*\)', repl, text)

def add_dot_tab(par, pos_dxa=7938):
    pPr = par._p.get_or_add_pPr()
    for t in pPr.findall(qn('w:tabs')):
        pPr.remove(t)
    tabs = OxmlElement('w:tabs')
    tab = OxmlElement('w:tab')
    tab.set(qn('w:pos'), str(pos_dxa))
    tab.set(qn('w:val'), 'right')
    tab.set(qn('w:leader'), 'dot')
    tabs.append(tab)
    pPr.append(tabs)

def set_margins(sec):
    sec.left_margin = Cm(4.0)
    sec.right_margin = Cm(3.0)
    sec.top_margin = Cm(3.0)
    sec.bottom_margin = Cm(3.0)
    sec.header_distance = Cm(1.27)
    sec.footer_distance = Cm(1.27)
    sec.page_height = Cm(29.7)
    sec.page_width = Cm(21.0)

def set_pgnum(sec, fmt=None, start=None):
    sectPr = sec._sectPr
    # remove existing
    for el in sectPr.findall(qn('w:pgNumType')):
        sectPr.remove(el)
    el = OxmlElement('w:pgNumType')
    if fmt:
        el.set(qn('w:fmt'), fmt)
    if start is not None:
        el.set(qn('w:start'), str(start))
    # insert after pgMar if exists else append
    sectPr.append(el)

def add_page_field(par, display="1"):
    # adds PAGE field runs with TNR 10 bold black
    r1 = par.add_run()
    set_run(r1, 10, True, False)
    fld1 = OxmlElement('w:fldChar'); fld1.set(qn('w:fldCharType'),'begin')
    r1._element.append(fld1)
    r2 = par.add_run()
    set_run(r2, 10, True, False)
    instr = OxmlElement('w:instrText')
    instr.set(qn('xml:space'),'preserve')
    instr.text = "PAGE"
    r2._element.append(instr)
    r3 = par.add_run()
    set_run(r3, 10, True, False)
    fld2 = OxmlElement('w:fldChar'); fld2.set(qn('w:fldCharType'),'separate')
    r3._element.append(fld2)
    r4 = par.add_run(display)
    set_run(r4, 10, True, False)
    r5 = par.add_run()
    set_run(r5, 10, True, False)
    fld3 = OxmlElement('w:fldChar'); fld3.set(qn('w:fldCharType'),'end')
    r5._element.append(fld3)

def add_toc_field(par):
    r1 = par.add_run()
    set_run(r1, 12, False, False)
    fld1 = OxmlElement('w:fldChar'); fld1.set(qn('w:fldCharType'),'begin')
    r1._element.append(fld1)
    r2 = par.add_run()
    set_run(r2, 12, False, False)
    instr = OxmlElement('w:instrText')
    instr.set(qn('xml:space'),'preserve')
    instr.text = 'TOC \\o "1-3" \\h \\z \\u'
    r2._element.append(instr)
    r3 = par.add_run()
    set_run(r3, 12, False, False)
    fld2 = OxmlElement('w:fldChar'); fld2.set(qn('w:fldCharType'),'separate')
    r3._element.append(fld2)
    # fallback text will be static entries below; close field after entries? simpler close here
    r4 = par.add_run()
    set_run(r4, 12, False, False)
    fld3 = OxmlElement('w:fldChar'); fld3.set(qn('w:fldCharType'),'end')
    r4._element.append(fld3)

def set_cell_text(cell, text, size=10, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.LEFT):
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = align
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.0
    # handle *italic* inside?
    # simple: parse inline
    parse_inline(p, parenthetical_amp(text), size, bold)
    # ensure black (parse_inline already)
    # override italic for header? keep bold
    for r in p.runs:
        # if header bold already, keep
        pass

def apply_apa_borders(table):
    tbl = table._tbl
    tblPr = tbl.tblPr
    # tblLayout fixed, jc center
    # borders
    borders = OxmlElement('w:tblBorders')
    for edge in ['top','bottom']:
        el = OxmlElement(f'w:{edge}')
        el.set(qn('w:val'),'single'); el.set(qn('w:sz'),'8')
        el.set(qn('w:space'),'0'); el.set(qn('w:color'),'000000')
        borders.append(el)
    for edge in ['left','right','insideV','insideH']:
        el = OxmlElement(f'w:{edge}')
        el.set(qn('w:val'),'nil'); el.set(qn('w:sz'),'0')
        el.set(qn('w:space'),'0'); el.set(qn('w:color'),'auto')
        borders.append(el)
    tblPr.append(borders)
    # header shading + header bottom sz6
    # shade header row
    hdr = table.rows[0]
    for cell in hdr.cells:
        tcPr = cell._tc.get_or_add_tcPr()
        shd = OxmlElement('w:shd')
        shd.set(qn('w:fill'),'F2F2F2'); shd.set(qn('w:val'),'clear')
        tcPr.append(shd)
        # bottom border sz6 for header cells
        tcBorders = OxmlElement('w:tcBorders')
        btm = OxmlElement('w:bottom')
        btm.set(qn('w:val'),'single'); btm.set(qn('w:sz'),'6')
        btm.set(qn('w:space'),'0'); btm.set(qn('w:color'),'000000')
        tcBorders.append(btm)
        tcPr.append(tcBorders)
    # tblHeader + cantSplit for header row
    tr = hdr._tr
    trPr = tr.get_or_add_trPr()
    h = OxmlElement('w:tblHeader'); h.set(qn('w:val'),'true')
    trPr.append(h)
    cant = OxmlElement('w:cantSplit'); cant.set(qn('w:val'),'true')
    trPr.append(cant)

def add_hyperlink(par, url, text):
    part = par.part
    r_id = part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    hl = OxmlElement('w:hyperlink')
    hl.set(qn('r:id'), r_id)
    run = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    # TNR 12? for pustaka 12, black, no underline
    rf = OxmlElement('w:rFonts')
    for a in ['w:ascii','w:hAnsi','w:cs','w:eastAsia']:
        rf.set(qn(a),'Times New Roman')
    rPr.append(rf)
    sz = OxmlElement('w:sz'); sz.set(qn('w:val'),'24'); rPr.append(sz)
    szCs = OxmlElement('w:szCs'); szCs.set(qn('w:val'),'24'); rPr.append(szCs)
    col = OxmlElement('w:color'); col.set(qn('w:val'),'000000'); rPr.append(col)
    # no underline: omit u element (ensure none)
    run.append(rPr)
    t = OxmlElement('w:t'); t.text = text
    run.append(t)
    hl.append(run)
    par._p.append(hl)

def body_para(doc, text):
    if not text.strip():
        return None
    text = parenthetical_amp(text.strip())
    p = doc.add_paragraph()
    p.style = doc.styles['Normal']
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf = p.paragraph_format
    pf.line_spacing = 1.5
    pf.space_before = Pt(0); pf.space_after = Pt(0)
    pf.first_line_indent = Cm(1.25)
    pf.widow_control = True
    parse_inline(p, text, 12, False)
    return p

def bullet_para(doc, text):
    p = body_para(doc, text)
    if p is not None:
        # Arthur bullets: left 1.25cm hanging (first -0.4)
        p.paragraph_format.left_indent = Cm(1.25)
        p.paragraph_format.first_line_indent = Cm(-0.4)
    return p

def numbered_para(doc, text):
    # enumerasi Arthur: left 1.25cm hanging first -0.4/-0.62
    p = doc.add_paragraph()
    p.style = doc.styles['Normal']
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf = p.paragraph_format
    pf.line_spacing = 1.5
    pf.space_before = Pt(0); pf.space_after = Pt(0)
    pf.left_indent = Cm(1.25)
    pf.first_line_indent = Cm(-0.4)
    parse_inline(p, parenthetical_amp(text.strip()), 12, False)
    return p

# ---------- read sources ----------
bab1_raw = open(BAB1, encoding='utf-8').read()
bab2_raw = open(BAB2, encoding='utf-8').read()
bab3_raw = open(BAB3, encoding='utf-8').read()
pust_raw = open(PUST, encoding='utf-8').read()

def strip_meta_bab(raw, gate_markers):
    lines = raw.splitlines()
    out = []
    in_gate = False
    for ln in lines:
        s = ln.strip()
        if any(s.startswith(m) for m in gate_markers):
            in_gate = True
            continue
        if in_gate:
            if s == "---":
                in_gate = False
            continue
        if s.startswith(">"):
            continue
        if s == "---":
            continue
        if s.startswith("# BAB"):
            continue
        out.append(ln)
    return "\n".join(out)

bab1_clean = strip_meta_bab(bab1_raw, ["## 0."])
bab2_clean = strip_meta_bab(bab2_raw, ["## Verified-vs-Proposed"])
bab3_clean = strip_meta_bab(bab3_raw, ["## 0."])

# ---------- build doc ----------
doc = Document()
# styles
normal = doc.styles['Normal']
normal.font.name = 'Times New Roman'
normal.font.size = Pt(12)
normal.font.color.rgb = BLACK
normal.paragraph_format.line_spacing = 1.5
normal.paragraph_format.space_before = Pt(0)
normal.paragraph_format.space_after = Pt(0)
normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
# ensure rFonts
for st_name in ['Normal','Heading 1','Heading 2','Heading 3','Footer','Title']:
    try:
        st = doc.styles[st_name]
        st.font.name = 'Times New Roman'
        st.font.color.rgb = BLACK
        # need to set rFonts via runs? style font name suffices, but ensure eastAsia?
    except: pass

h1 = doc.styles['Heading 1']
h1.font.size = Pt(12); h1.font.bold = True; h1.font.color.rgb = BLACK; h1.font.name='Times New Roman'
h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
h1.paragraph_format.line_spacing = 1.5
h1.paragraph_format.space_before = Pt(0); h1.paragraph_format.space_after = Pt(12)

h2 = doc.styles['Heading 2']
h2.font.size = Pt(12); h2.font.bold = True; h2.font.color.rgb = BLACK; h2.font.name='Times New Roman'
h2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
h2.paragraph_format.line_spacing = 1.5
h2.paragraph_format.space_before = Pt(12); h2.paragraph_format.space_after = Pt(6)

h3 = doc.styles['Heading 3']
h3.font.size = Pt(12); h3.font.bold = True; h3.font.color.rgb = BLACK; h3.font.name='Times New Roman'
h3.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
h3.paragraph_format.line_spacing = 1.5
h3.paragraph_format.space_before = Pt(6); h3.paragraph_format.space_after = Pt(3)

footer_st = doc.styles['Footer']
footer_st.font.size = Pt(10); footer_st.font.bold = True; footer_st.font.color.rgb = BLACK; footer_st.font.name='Times New Roman'
footer_st.paragraph_format.line_spacing = 1.0
footer_st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT

# create toc styles if missing
for tname, sz, bld, left, before in [('toc 1',12,True,0,4),('toc 2',12,False,0.5,1),('toc 3',12,False,1.0,1)]:
    try:
        st = doc.styles[tname]
    except KeyError:
        st = doc.styles.add_style(tname, 1)  # paragraph
    st.base_style = doc.styles['Normal']
    st.font.name='Times New Roman'; st.font.size=Pt(sz); st.font.bold=bld; st.font.color.rgb=BLACK
    st.paragraph_format.line_spacing=1.0
    st.paragraph_format.space_before=Pt(before); st.paragraph_format.space_after=Pt(1)
    if left:
        st.paragraph_format.left_indent=Cm(left)

# sec0 cover
sec0 = doc.sections[0]
set_margins(sec0)
sec0.different_first_page_header_footer = True
# ensure no pgNumType for cover
for el in sec0._sectPr.findall(qn('w:pgNumType')):
    sec0._sectPr.remove(el)
# empty footer/header for cover
sec0.footer.is_linked_to_previous = False
sec0.header.is_linked_to_previous = False
# clear cover footer
for p in sec0.footer.paragraphs:
    p.text=""

def cover_para(text, size=12, bold=True, italic=False, before=0, after=0, runs_spec=None):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    if runs_spec:
        for txt,b,i in runs_spec:
            r = p.add_run(txt)
            set_run(r, size, b, i)
    else:
        r = p.add_run(text)
        set_run(r, size, bold, italic)
    return p

# COVER (Logo UKRIDA di paling atas, KAPITAL 14pt per G1, stage spacing)
logo_path = Path("01_Naskah_Utama/images/ukrida_pentagram.png")
if not logo_path.exists():
    logo_path = Path("01_Naskah_Utama/images/Logo_UKRIDA_300x300.png")

p_logo = doc.add_paragraph()
p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_logo.paragraph_format.line_spacing = 1.0
p_logo.paragraph_format.space_before = Pt(0)
p_logo.paragraph_format.space_after = Pt(18)
r_logo = p_logo.add_run()
r_logo.add_picture(str(logo_path), width=Cm(3.2), height=Cm(3.2))

cover_para("PROPOSAL TUGAS AKHIR", size=14, bold=True, before=6, after=18)
# judul kapital with foreign italic+bold
title_parts = [
    ("PENGARUH PEMASARAN ", True, False),
    ("INFLUENCER MARKETING", True, True),
    (" (", True, False),
    ("INFLUENCER MARKETING", True, True),
    ("), KOMUNIKASI ELEKTRONIK DARI MULUT KE MULUT (", True, False),
    ("ELECTRONIC WORD-OF-MOUTH", True, True),
    ("), DAN PERSEPSI KENIKMATAN (", True, False),
    ("PERCEIVED ENJOYMENT", True, True),
    (") TERHADAP NIAT BERMAIN BERKELANJUTAN (", True, False),
    ("CONTINUANCE INTENTION TO PLAY", True, True),
    (") ", True, False),
    ("MOBILE LEGENDS", True, True),
    (" PADA GENERASI Z", True, False),
]
cover_para("", size=14, bold=True, before=12, after=24, runs_spec=title_parts)
cover_para("Diajukan Kepada Program Studi Manajemen", size=12, bold=False, before=18, after=0)
cover_para("Untuk Menyusun Tugas Akhir Sarjana Manajemen", size=12, bold=False, before=0, after=24)
# Diajukan Oleh with Siddharta Pratama Budiono & 312023017
p_oleh = doc.add_paragraph()
p_oleh.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_oleh.paragraph_format.space_before=Pt(24); p_oleh.paragraph_format.space_after=Pt(36)
p_oleh.paragraph_format.line_spacing=1.0
r = p_oleh.add_run("Diajukan Oleh:"); set_run(r,12,False,False)
r = p_oleh.add_run(); r.add_break()
r = p_oleh.add_run("Siddharta Pratama Budiono"); set_run(r,12,True,False)
r = p_oleh.add_run(); r.add_break()
r = p_oleh.add_run("312023017"); set_run(r,12,True,False)
# prodi - KAPITAL bold, breaks
p_prodi = doc.add_paragraph()
p_prodi.alignment=WD_ALIGN_PARAGRAPH.CENTER
p_prodi.paragraph_format.space_before=Pt(48); p_prodi.paragraph_format.space_after=Pt(0)
p_prodi.paragraph_format.line_spacing=1.0
prodi_lines = ["PROGRAM STUDI MANAJEMEN","FAKULTAS EKONOMI DAN BISNIS","UNIVERSITAS KRISTEN KRIDA WACANA","JAKARTA 2026"]
for idx_line, line in enumerate(prodi_lines):
    r = p_prodi.add_run(line)
    set_run(r,12,True,False)
    if idx_line < len(prodi_lines)-1:
        r = p_prodi.add_run(); r.add_break()

# --- sec1 frontmatter ---
sec1 = doc.add_section(WD_SECTION.NEW_PAGE)
set_margins(sec1)
sec1.different_first_page_header_footer = False
sec1.footer.is_linked_to_previous = False
sec1.header.is_linked_to_previous = False
set_pgnum(sec1, fmt="lowerRoman", start=2)
# footer roman right
fp1 = sec1.footer.paragraphs[0]
fp1.style = doc.styles['Footer']
fp1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
fp1.text=""
r = fp1.add_run("Universitas Kristen Krida Wacana | "); set_run(r,10,True,False)
add_page_field(fp1, display="ii")
# header empty
for p in sec1.header.paragraphs:
    p.text=""

# DAFTAR ISI (Heading 1 at start of section 1, no extra page break before)
di = doc.add_paragraph("DAFTAR ISI", style='Heading 1')
di.alignment=WD_ALIGN_PARAGRAPH.CENTER
di.paragraph_format.page_break_before=False
for r in di.runs: set_run(r,12,True,False)
# TOC field para
ptoc = doc.add_paragraph()
ptoc.paragraph_format.space_after=Pt(6)
add_toc_field(ptoc)
# static TOC entries with dots 14.0cm (7938 dxa)
toc_entries = [
    ("DAFTAR ISI", "toc 1", "ii"),
    ("DAFTAR TABEL", "toc 1", "iii"),
    ("DAFTAR GAMBAR", "toc 1", "iv"),
    ("BAB I PENDAHULUAN", "toc 1", "1"),
    ("1.1 Latar Belakang Penelitian", "toc 2", "1"),
    ("1.2 Rumusan Masalah", "toc 2", "6"),
    ("1.3 Tujuan Penelitian", "toc 2", "7"),
    ("1.4 Manfaat Penelitian", "toc 2", "7"),
    ("1.4.1 Manfaat Teoritis", "toc 3", "7"),
    ("1.4.2 Manfaat Praktis", "toc 3", "7"),
    ("BAB II TINJAUAN PUSTAKA DAN PENGEMBANGAN HIPOTESIS", "toc 1", "8"),
    ("2.1 Landasan Teori", "toc 2", "8"),
    ("2.1.1 Influencer Marketing sebagai Kredibilitas Sumber", "toc 3", "8"),
    ("2.1.2 Electronic Word of Mouth (eWOM) dan Adopsi Informasi", "toc 3", "9"),
    ("2.1.3 Perceived Enjoyment pada Sistem Hedonik", "toc 3", "10"),
    ("2.1.4 Continuance Intention sebagai Niat Bermain Berkelanjutan", "toc 3", "11"),
    ("2.1.5 Generasi Z sebagai Konteks, bukan Variabel", "toc 3", "11"),
    ("2.2 Penelitian Sebelumnya", "toc 2", "12"),
    ("2.3 Pengembangan Hipotesis", "toc 2", "15"),
    ("2.4 Rerangka Penelitian", "toc 2", "16"),
    ("BAB III METODE PENELITIAN", "toc 1", "18"),
    ("3.1 Jenis dan Sumber Data", "toc 2", "18"),
    ("3.2 Populasi dan Sampel", "toc 2", "19"),
    ("3.3 Model Penelitian", "toc 2", "20"),
    ("3.4 Operasionalisasi Variabel", "toc 2", "21"),
    ("3.5 Metode Analisis Data", "toc 2", "25"),
    ("DAFTAR PUSTAKA", "toc 1", "27"),
]
for txt, sty, pg in toc_entries:
    p = doc.add_paragraph(style=sty)
    add_dot_tab(p, 7938)
    p.paragraph_format.right_indent = Cm(0)
    # text + tab + page
    # need runs black
    r = p.add_run(txt + "\t" + pg)
    # toc1 bold, others regular
    is_bold = (sty=="toc 1")
    set_run(r, 12, is_bold, False)
# buffer anti-merge
pb = doc.add_paragraph()
r = pb.add_run(""); set_run(r,12,False,False)

# DAFTAR TABEL
dt = doc.add_paragraph("DAFTAR TABEL", style='Heading 1')
dt.alignment=WD_ALIGN_PARAGRAPH.CENTER
dt.paragraph_format.page_break_before=True
for r in dt.runs: set_run(r,12,True,False)
lot = [
    ("Tabel 2.1 Ringkasan Penelitian Sebelumnya (S01–S18)", "12"),
    ("Tabel 3.1 Operasionalisasi Variabel", "21"),
]
for txt,pg in lot:
    p = doc.add_paragraph(style='toc 1')
    add_dot_tab(p, 7938)
    r = p.add_run(txt+"\t"+pg); set_run(r,12,False,False)
pb2 = doc.add_paragraph()
r=pb2.add_run(""); set_run(r,12,False,False)

# DAFTAR GAMBAR
dg = doc.add_paragraph("DAFTAR GAMBAR", style='Heading 1')
dg.alignment=WD_ALIGN_PARAGRAPH.CENTER
dg.paragraph_format.page_break_before=True
for r in dg.runs: set_run(r,12,True,False)
lof = [("Gambar 2.1 Model Rerangka Konseptual Penelitian","16")]
for txt,pg in lof:
    p = doc.add_paragraph(style='toc 1')
    add_dot_tab(p, 7938)
    r=p.add_run(txt+"\t"+pg); set_run(r,12,False,False)
pb3 = doc.add_paragraph()
r=pb3.add_run(""); set_run(r,12,False,False)

# --- sec2 isi ---
sec2 = doc.add_section(WD_SECTION.NEW_PAGE)
set_margins(sec2)
sec2.different_first_page_header_footer = True
sec2.footer.is_linked_to_previous=False
sec2.header.is_linked_to_previous=False
set_pgnum(sec2, fmt="decimal", start=1)
fp2 = sec2.footer.paragraphs[0]
fp2.style = doc.styles['Footer']
fp2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
fp2.text=""
r = fp2.add_run("Universitas Kristen Krida Wacana | "); set_run(r,10,True,False)
add_page_field(fp2, display="1")
for p in sec2.header.paragraphs:
    p.text=""

# helpers for headings
def add_h1(text):
    # text may contain \n
    h = doc.add_paragraph(style='Heading 1')
    h.alignment=WD_ALIGN_PARAGRAPH.CENTER
    # split lines
    parts = text.split("\n")
    for idx, part in enumerate(parts):
        if idx>0:
            h.add_run().add_break()
        r = h.add_run(part)
        set_run(r,12,True,False)
    # outline level already via style
    return h
def add_h2(text):
    h = doc.add_paragraph(style='Heading 2')
    h.alignment=WD_ALIGN_PARAGRAPH.LEFT
    # parse inline for italic foreign inside heading
    h.text=""
    parse_inline(h, parenthetical_amp(text), 12, True)
    # ensure all runs bold (parse with base_bold True already, but *italic* parts need bold+italic)
    for r in h.runs:
        # keep italic as is, ensure bold True
        r.bold=True
        set_run(r,12,True,r.italic)
        # re-assert black (set_run does)
    return h
def add_h3(text):
    h = doc.add_paragraph(style='Heading 3')
    h.alignment=WD_ALIGN_PARAGRAPH.LEFT
    h.text=""
    parse_inline(h, parenthetical_amp(text), 12, True)
    for r in h.runs:
        r.bold=True
        set_run(r,12,True,r.italic)
    return h

def add_caption_tabel(text):
    p = doc.add_paragraph()
    p.alignment=WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before=Pt(12); p.paragraph_format.space_after=Pt(6)
    p.paragraph_format.line_spacing=1.0
    # Tabel X.X: ... with foreign italic inside but overall bold 11pt
    # parse: split? use parse then force bold 11
    # need to handle *...* inside
    # We'll parse manually then set size 11 bold
    pat = re.compile(r'(\*\*\*.+?\*\*\*|\*\*.+?\*\*|\*.+?\*)')
    # first, apply parenthetical amp? captions don't have citations, skip
    pos=0
    for m in pat.finditer(text):
        if m.start()>pos:
            r=p.add_run(text[pos:m.start()]); set_run(r,11,True,False)
        tok=m.group(0)
        if tok.startswith("***"):
            r=p.add_run(tok[3:-3]); set_run(r,11,True,True)
        elif tok.startswith("**"):
            r=p.add_run(tok[2:-2]); set_run(r,11,True,False)
        else:
            r=p.add_run(tok[1:-1]); set_run(r,11,True,True)
        pos=m.end()
    if pos<len(text):
        r=p.add_run(text[pos:]); set_run(r,11,True,False)
    return p

def add_sumber(text, size=10):
    p = doc.add_paragraph()
    p.alignment=WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before=Pt(2); p.paragraph_format.space_after=Pt(12)
    p.paragraph_format.line_spacing=1.0
    r=p.add_run(text); set_run(r,size,False,True)
    return p

def add_equation(eq_text, num):
    # table 2-col no border for reliable right number, else para with tab
    # Use paragraph with right tab at 14.0cm
    p = doc.add_paragraph()
    p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before=Pt(6); p.paragraph_format.space_after=Pt(6)
    p.paragraph_format.line_spacing=1.5
    p.paragraph_format.first_line_indent=Cm(0)
    add_dot_tab(p,14.0)  # actually need right tab without dots for eq? use right no leader? We'll add right tab without dots by adding second tab? Simpler: use tab without dots: add_tab_stop right no leader
    # clear dots? python adds dots; for eq we want no dots, just space. Remove and add plain right tab
    # Clear: recreate tab stops (only one plain)
    # Workaround: keep dots? For eq, dots undesirable. So remove all and add plain.
    # Access xml to remove leader? Simpler: just use text with many spaces + number; but spec says nomor kanan.
    # We'll clear tab stops via xml and add plain right tab.
    pPr = p._p.get_or_add_pPr()
    tabs_el = pPr.find(qn('w:tabs'))
    if tabs_el is not None:
        pPr.remove(tabs_el)
    tabs_el = OxmlElement('w:tabs')
    tab = OxmlElement('w:tab'); tab.set(qn('w:val'),'right'); tab.set(qn('w:pos'),'7938')
    # no leader
    tabs_el.append(tab)
    pPr.append(tabs_el)
    # equation with subscript unicode + italic vars
    # convert b0->b₀ etc, X1->X₁, p1->p₁, R2? keep
    submap = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    # We'll split eq_text into left and keep as is but convert digits after b/p/X/Y? Convert all trailing digits? Safer convert patterns b0,b1 -> b₀ etc, X1->X₁, p1->p₁
    eq = eq_text
    # eq_text like "Y = b0 + b1X1 + b2X2 + b3X3 + e"
    # convert
    eq = re.sub(r'\bb(\d)', lambda m: 'b'+chr(0x2080+int(m.group(1))), eq)
    eq = re.sub(r'\bX(\d)', lambda m: 'X'+chr(0x2080+int(m.group(1))), eq)
    eq = re.sub(r'\bp(\d)', lambda m: 'p'+chr(0x2080+int(m.group(1))), eq)
    # split runs: make Y,X,b,p,e italic? We'll make whole eq italic for vars? Keep simple: entire eq italic? Better: make letters italic, numbers subscript already, symbols regular? Simplify: add runs with italic for letters
    # For docx, we'll add eq as italic runs + number regular
    # Parse eq char by char: letters YXbpeMRQf... italic, digits/subscripts keep italic? Keep italic True for letters
    # Simpler: one run italic for eq, one tab, one run for num
    r = p.add_run(eq + "\t" + num)
    # Need eq part italic, num not? We'll split:
    p.text=""  # clear? Actually we already added run, need redo
    # clear
    for _ in list(p.runs):
        pass
    # remove added run by clearing paragraph xml runs
    # Instead recreate:
    p.clear()
    # re-add tab stops (clear removed them? clear removes runs only, keep pPr)
    r1 = p.add_run(eq)
    set_run(r1,12,False,True)  # italic for math
    r2 = p.add_run("\t"+num)
    set_run(r2,12,False,False)
    return p

# ---------- BAB I ----------
add_h1("BAB I\nPENDAHULUAN")
# parse bab1_clean lines
def render_markdown_body(clean_text, skip_tables=False, skip_code=False):
    lines = clean_text.splitlines()
    i=0
    tbl_buf=[]
    in_code=False
    code_buf=[]
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if s.startswith("```"):
            if not in_code:
                in_code=True; code_buf=[]
            else:
                in_code=False
                # skip code (for 2.4 replaced by figure) - handled outside
                # if not skip_code, render as body? For v2, skip ascii bagan (replaced)
                pass
            i+=1; continue
        if in_code:
            code_buf.append(ln)
            i+=1; continue
        if s.startswith("|"):
            tbl_buf.append(ln)
            i+=1
            # collect contiguous
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl_buf.append(lines[i]); i+=1
            # process table unless skip
            if not skip_tables:
                # check if header separator (contains ---) -> real md table
                # find header + rows
                # remove separator row
                rows = []
                for tl in tbl_buf:
                    # split by |
                    cells = [c.strip() for c in tl.strip().strip("|").split("|")]
                    # if separator (all ---), skip
                    if all(re.match(r'^:?-{2,}:?$', c.strip()) for c in cells):
                        continue
                    rows.append(cells)
                # rows[0]=header
                # For generic (should not happen for Bab1? Bab1 has no md tables except? Bab1 has Verified table removed, no other. So skip)
                pass
            tbl_buf=[]
            continue
        if s.startswith("### "):
            add_h3(s[4:].strip())
        elif s.startswith("## "):
            title = s[3:].strip()
            # map Daftar OPEN etc to H2
            add_h2(title)
        elif s.startswith("# "):
            # shouldn't happen (removed), skip
            pass
        elif re.match(r'^\d+\.\s', s):
            numbered_para(doc, s)
        elif s.startswith("- "):
            bullet_para(doc, s[2:])
        elif s.startswith("Tabel 3.1") or s.startswith("Tabel 2."):
            # caption handled outside
            add_caption_tabel(s)
        elif re.match(r'^Y\s*=\s*.*\(3\.[12]\)\s*$', s):
            # equation line like "Y = b0 + ... (3.1)"
            m = re.match(r'^(.*)\s*(\(3\.[12]\))\s*$', s)
            if m:
                add_equation(m.group(1).strip(), m.group(2).strip())
            else:
                body_para(doc, s)
        elif s=="" :
            # empty -> skip (paragraph break implicit)
            pass
        else:
            # check for "Keterangan:" after eq? keep as body but no first indent? keep body
            # check for equation keterangan starting with "Keterangan:" -> body
            body_para(doc, ln.strip())
        i+=1

render_markdown_body(bab1_clean)

# ---------- BAB II ----------
add_h1("BAB II\nTINJAUAN PUSTAKA DAN PENGEMBANGAN HIPOTESIS")
# For Bab2, need custom handling for tables + figure + H statements
# Extract S01-S18 table data manually from clean? Parse md table
lines2 = bab2_clean.splitlines()
# We'll iterate with special handling
i=0
in_code=False
while i < len(lines2):
    ln = lines2[i]; s=ln.strip()
    if s.startswith("```"):
        in_code = not in_code
        if not in_code:
            # just closed code block (bagan ascii) -> insert Figure 2.1 here
            # Generate figure if not exists
            # (figure generation below, insert now)
            pass
            # Insert figure placeholder - actual insertion after loop? Insert now:
            # Caption above? For gambar, caption below. Insert image + caption + sumber
            # We'll insert figure now
            try:
                import math
                import matplotlib
                matplotlib.use('Agg')
                import matplotlib.pyplot as plt
                from matplotlib.patches import Ellipse, FancyArrowPatch
                fig, ax = plt.subplots(figsize=(10.5, 4.6), dpi=300)
                ax.set_xlim(0, 10); ax.set_ylim(0, 4.6); ax.axis('off')
                def draw_ellipse(cx, cy, w, h, code, label):
                    el = Ellipse((cx, cy), width=w, height=h, facecolor='white', edgecolor='black', linewidth=1.8)
                    ax.add_patch(el)
                    ax.text(cx, cy + 0.16, code, ha='center', va='center', fontsize=16, fontfamily='serif', weight='bold', color='black')
                    ax.text(cx, cy - 0.20, label, ha='center', va='center', fontsize=12.5, fontfamily='serif', style='italic', color='black')
                w_el = 3.1; h_el = 1.12; a = w_el / 2.0; b = h_el / 2.0
                cx_x = 1.85; cx_y = 8.05; cy_y = 2.20
                centers_x = [
                    (1.85, 3.40, 'X1', 'Influencer Marketing'),
                    (1.85, 2.20, 'X2', 'eWOM'),
                    (1.85, 1.00, 'X3', 'Perceived Enjoyment')
                ]
                for cx, cy, code, lbl in centers_x:
                    draw_ellipse(cx, cy, w_el, h_el, code, lbl)
                draw_ellipse(cx_y, cy_y, w_el, h_el, 'Y', 'Intention to Play')
                def ellipse_boundary(cx, cy, a, b, target_x, target_y):
                    dx = target_x - cx; dy = target_y - cy; phi = math.atan2(dy, dx)
                    r = (a * b) / math.sqrt((b * math.cos(phi))**2 + (a * math.sin(phi))**2)
                    return cx + r * math.cos(phi), cy + r * math.sin(phi)
                targets_y = [(cx_y, cy_y + 0.15), (cx_y, cy_y), (cx_y, cy_y - 0.15)]
                labels = ['H1 (+)', 'H2 (+)', 'H3 (+)']
                for idx_ar, ((cx, cy, code, _), (ty_x, ty_y)) in enumerate(zip(centers_x, targets_y)):
                    sx, sy = ellipse_boundary(cx, cy, a, b, ty_x, ty_y)
                    ex, ey = ellipse_boundary(cx_y, cy_y, a, b, cx, cy)
                    ar = FancyArrowPatch((sx, sy), (ex, ey), arrowstyle='-|>', mutation_scale=18, linewidth=1.6, color='black')
                    ax.add_patch(ar)
                    mid_x = 4.95; t = (mid_x - sx) / (ex - sx); line_y = sy + t * (ey - sy)
                    ax.text(mid_x, line_y + 0.26, labels[idx_ar], ha='center', va='center', fontsize=13, fontfamily='serif', weight='bold', color='black')
                ax.text(5.0, 4.35, 'Populasi: Generasi Z (Indonesia) — Objek: Mobile Legends', ha='center', va='center', fontsize=12.5, fontfamily='serif', color='black')
                plt.tight_layout(pad=0.2)
                plt.savefig(str(FIG_TMP), bbox_inches='tight', dpi=300)
                plt.close()
                import shutil
                for extra_p in [
                    Path(r"Z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\scratch\fig_rerangka_21.png"),
                    Path(r"Z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\scratch\fig_v2.png"),
                    Path(r"C:\Users\Arthur Reezan\AppData\Local\Temp\opencode\fig_v2.png"),
                    Path(r"C:\Users\Arthur Reezan\AppData\Local\Temp\opencode\fig_rerangka_21.png")
                ]:
                    try:
                        if extra_p.parent.exists() and str(extra_p.resolve()) != str(FIG_TMP.resolve()):
                            shutil.copyfile(str(FIG_TMP), str(extra_p))
                    except Exception:
                        pass
            except Exception as e:
                print("fig err", e)
            # insert image
            if FIG_TMP.exists():
                pg = doc.add_paragraph(); pg.alignment=WD_ALIGN_PARAGRAPH.CENTER
                pg.paragraph_format.space_before=Pt(12); pg.paragraph_format.space_after=Pt(2)
                pg.paragraph_format.first_line_indent=Cm(0)
                run = pg.add_run()
                run.add_picture(str(FIG_TMP), width=Cm(14.0))
                # caption
                add_caption_tabel("Gambar 2.1 Model Rerangka Konseptual Penelitian")
                # center caption (override left)
                cap = doc.paragraphs[-1]; cap.alignment=WD_ALIGN_PARAGRAPH.CENTER
                add_sumber("Sumber: Diolah penulis (2026).")
                doc.paragraphs[-1].alignment=WD_ALIGN_PARAGRAPH.CENTER
            else:
                body_para(doc, "[Gambar 2.1 Model Rerangka Konseptual — OPEN file gambar, lihat BUILD_LOG]")
        i+=1; continue
    if in_code:
        i+=1; continue
    if s.startswith("|"):
        # collect table
        tbl_lines=[ln]
        i+=1
        while i < len(lines2) and lines2[i].strip().startswith("|"):
            tbl_lines.append(lines2[i]); i+=1
        # parse rows
        rows=[]
        for tl in tbl_lines:
            cells=[c.strip() for c in tl.strip().strip("|").split("|")]
            if all(re.match(r'^:?-{2,}:?$', c) for c in cells):
                continue
            rows.append(cells)
        # rows[0] header: Kode|Studi|Jalur|Pola|Peran
        if rows and rows[0][0].lower().startswith("kode"):
            add_caption_tabel("Tabel 2.1 Ringkasan Penelitian Sebelumnya (S01–S18)")
            # create APA table 5 cols
            t = doc.add_table(rows=len(rows), cols=5)
            t.style='Table Grid'; t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.autofit=False
            # widths: total 14cm: 1.2+4.5+3.5+2.8+2.0 =14?
            widths=[Cm(1.2),Cm(4.2),Cm(3.2),Cm(3.0),Cm(2.4)]
            for idx,cell in enumerate(t.rows[0].cells):
                cell.width=widths[idx]
            for r_idx,rdata in enumerate(rows):
                for c_idx in range(5):
                    txt = rdata[c_idx] if c_idx < len(rdata) else ""
                    c = t.rows[r_idx].cells[c_idx]
                    c.text=""
                    p=c.paragraphs[0]
                    p.alignment=WD_ALIGN_PARAGRAPH.LEFT
                    p.paragraph_format.space_before=Pt(2); p.paragraph_format.space_after=Pt(2); p.paragraph_format.line_spacing=1.0
                    # header bold
                    if r_idx==0:
                        parse_inline(p, txt, 10, True)
                    else:
                        parse_inline(p, parenthetical_amp(txt), 10, False)
            apply_apa_borders(t)
            add_sumber("Sumber: Diolah penulis dari LITERATURE_MATRIX.md (S01–S18, S-FEB) (2026).")
        continue
    if s.startswith("### "):
        add_h3(s[4:].strip()); i+=1; continue
    if s.startswith("## "):
        title=s[3:].strip()
        # 2.4 Rerangka Penelitian etc
        add_h2(title); i+=1; continue
    if re.match(r'^\d+\.\s', s):
        numbered_para(doc, s); i+=1; continue
    if s.startswith("- "):
        bullet_para(doc, s[2:]); i+=1; continue
    if s=="":
        i+=1; continue
    # H1:/H2: statements like "H1: Variabel..." -> body bold? Keep as body with bold prefix? Pedoman: H as statement. Keep body but with bold H label? Simplify body
    if re.match(r'^H[1-4]\s*:', s):
        p = doc.add_paragraph()
        p.style=doc.styles['Normal']; p.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing=1.5; p.paragraph_format.space_before=Pt(0); p.paragraph_format.space_after=Pt(0)
        p.paragraph_format.first_line_indent=Cm(1.25)
        # bold H label?
        m=re.match(r'^(H[1-4]\s*:)(.*)$', s)
        r=p.add_run(m.group(1)); set_run(r,12,True,False)
        # rest with inline
        # need to parse rest with italic
        # create temp para to parse? Instead parse rest into same p
        rest = m.group(2)
        # parse rest manually
        pat=re.compile(r'(\*\*\*.+?\*\*\*|\*\*.+?\*\*|\*.+?\*)')
        pos=0
        rest = parenthetical_amp(rest)
        for mm in pat.finditer(rest):
            if mm.start()>pos:
                r=p.add_run(rest[pos:mm.start()]); set_run(r,12,False,False)
            tok=mm.group(0)
            if tok.startswith("***"):
                r=p.add_run(tok[3:-3]); set_run(r,12,True,True)
            elif tok.startswith("**"):
                r=p.add_run(tok[2:-2]); set_run(r,12,True,False)
            else:
                r=p.add_run(tok[1:-1]); set_run(r,12,False,True)
            pos=mm.end()
        if pos<len(rest):
            r=p.add_run(rest[pos:]); set_run(r,12,False,False)
        i+=1; continue
    # Status verifikasi / Catatan etc -> body
    body_para(doc, ln.strip())
    i+=1

# ---------- BAB III ----------
add_h1("BAB III\nMETODE PENELITIAN")
lines3 = bab3_clean.splitlines()
i=0
in_code3=False
while i < len(lines3):
    ln=lines3[i]; s=ln.strip()
    if s.startswith("```"):
        in_code3 = not in_code3; i+=1; continue
    if in_code3:
        i+=1; continue
    if s.startswith("|"):
        tbl_lines=[ln]; i+=1
        while i < len(lines3) and lines3[i].strip().startswith("|"):
            tbl_lines.append(lines3[i]); i+=1
        rows=[]
        for tl in tbl_lines:
            cells=[c.strip() for c in tl.strip().strip("|").split("|")]
            if all(re.match(r'^:?-{2,}:?$', c) for c in cells):
                continue
            rows.append(cells)
        # header check Variabel|Definisi...
        if rows and "Variabel" in rows[0][0]:
            add_caption_tabel("Tabel 3.1 Operasionalisasi Variabel")
            # Map 7 cols -> 4 cols: Variabel|Dimensi|Indikator|Sumber
            # rows[0]=header 7 cols
            header4 = ["Variabel","Dimensi","Indikator","Sumber"]
            data4=[]
            for rdata in rows[1:]:
                # pad to 7
                while len(rdata)<7: rdata.append("")
                var, defin, dim, indik, skala, sumber, status = rdata[:7]
                # Variabel cell: var + (defin if defin) - if var empty (merged), use previous? Keep as is (empty means continuation)
                var_cell = var
                if defin and defin.strip() and defin.strip()!="-":
                    if var_cell.strip():
                        var_cell = var_cell.strip() + " — " + defin.strip()
                    else:
                        var_cell = defin.strip()
                # Sumber: keep as is (narrative dan)
                data4.append([var_cell.strip(), dim.strip(), indik.strip(), sumber.strip()])
            t = doc.add_table(rows=1+len(data4), cols=4)
            t.style='Table Grid'; t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.autofit=False
            widths=[Cm(3.0),Cm(2.8),Cm(5.2),Cm(3.0)]
            for idx in range(4):
                t.rows[0].cells[idx].width=widths[idx]
            for c_idx,htxt in enumerate(header4):
                c=t.rows[0].cells[c_idx]; c.text=""
                p=c.paragraphs[0]; p.alignment=WD_ALIGN_PARAGRAPH.CENTER
                r=p.add_run(htxt); set_run(r,10,True,False)
            for r_idx,rdata in enumerate(data4, start=1):
                for c_idx,txt in enumerate(rdata):
                    c=t.rows[r_idx].cells[c_idx]; c.text=""
                    p=c.paragraphs[0]; p.alignment=WD_ALIGN_PARAGRAPH.LEFT
                    p.paragraph_format.space_before=Pt(2); p.paragraph_format.space_after=Pt(2); p.paragraph_format.line_spacing=1.0
                    # handle Opsi A/B etc, keep [OPEN] etc
                    parse_inline(p, parenthetical_amp(txt) if txt else "—", 10, False)
            apply_apa_borders(t)
            add_sumber("Sumber: Diolah penulis dari KONSTRUK_SKALA.md (Ohanian, 1990; Bambauer-Sachse & Mangold, 2011; Venkatesh, 2000; Ajzen, 1991; dan lain-lain) (2026).")
            # Catatan skala + status (pertahankan OPEN, tanpa mengarang)
            body_para(doc, "Catatan Tabel 3.1: X1 memakai diferensial semantik 7-titik; X2–X3–Y memakai Likert 5-titik (1 = sangat tidak setuju sampai 5 = sangat setuju) kecuali ditetapkan lain oleh pembimbing. Skor dimensi dihitung sebagai rerata butir; skor variabel sebagai rerata dimensi (atau second-order pada SEM bila Opsi B dipilih). Seluruh redaksi Indonesia adalah parafrase adaptasi (PROPOSED-UNVERIFIED/ADAPTED) dan wajib uji keterbacaan serta pilot; kolom α dikosongkan sampai uji pilot/utama. Pilihan X2 Opsi A atau Opsi B, skala 5- atau 7-titik, dan horizon waktu Y [OPEN] ditetapkan setelah kunci pembimbing.")
            # fix last para to small? keep body but will be 12pt; for note use 10pt italic? Keep body for faithful? Use sumber style? Keep body for now (will adjust to 10pt? keep 12)
        continue
    if s.startswith("### "):
        # a. / b. / c. -> H3? In Bab3, ### a. Identifikasi... -> H3
        add_h3(s[4:].strip()); i+=1; continue
    if s.startswith("## "):
        add_h2(s[3:].strip()); i+=1; continue
    if re.match(r'^Y\s*=\s*.*\(3\.[12]\)', s):
        m=re.match(r'^(.*)\s*(\(3\.[12]\))\s*$', s)
        if m:
            add_equation(m.group(1).strip(), m.group(2).strip())
        else:
            body_para(doc, s)
        i+=1; continue
    if s.startswith("Tabel 3.1"):
        add_caption_tabel(s); i+=1; continue
    if s.startswith("Opsi A") or s.startswith("Opsi B") or s.startswith("Jalur A") or s.startswith("Jalur B"):
        # make bold prefix? Use H3-like? Actually Opsi/Jalur as body bold? Keep as H3? Simpler body with bold lead
        # treat as body with bold first sentence? Use body
        # If short header-like (e.g., "Opsi A — regresi..."), make H3? Let's make H3 for Opsi/Jalur lines that end with : ?
        # Check: "Opsi A — regresi linear berganda (untuk SPSS):" -> H3? Keep H3 for structure
        if len(s)<120:
            add_h3(s)
        else:
            body_para(doc, s)
        i+=1; continue
    if re.match(r'^\d+\.\s', s):
        numbered_para(doc, s); i+=1; continue
    if s.startswith("- "):
        bullet_para(doc, s[2:]); i+=1; continue
    if s=="":
        i+=1; continue
    body_para(doc, ln.strip())
    i+=1

# ---------- DAFTAR PUSTAKA ----------
dp = doc.add_paragraph("DAFTAR PUSTAKA", style='Heading 1')
dp.alignment=WD_ALIGN_PARAGRAPH.CENTER
dp.paragraph_format.page_break_before=True
for r in dp.runs: set_run(r,12,True,False)

# extract 48 entries
sec2_text = pust_raw.split("## 2. Daftar")[1].split("## 3.")[0]
entries=[]
for ln in sec2_text.splitlines():
    s=ln.strip()
    if not s or s.startswith(">") or s.startswith("#"):
        continue
    if re.match(r'.+\(\d{4}|.+\(n\.d\.', s):
        entries.append(s)
    else:
        if entries:
            entries[-1] += " " + s
# entries should be 48
# ensure alphabetical? already alphabetical, keep order
url_pat = re.compile(r'(https?://\S+)')
for ent in entries:
    ent = ent.strip()
    # remove trailing status? entries already clean (no > lines)
    p = doc.add_paragraph()
    p.style = doc.styles['Normal']
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf = p.paragraph_format
    pf.line_spacing = 1.15
    pf.space_before=Pt(0); pf.space_after=Pt(0)
    pf.left_indent=Cm(1.25); pf.first_line_indent=Cm(-1.25)
    # split by URLs to hyperlink black + italic parsing for non-url parts
    parts = url_pat.split(ent)
    for idx, part in enumerate(parts):
        if idx%2==1:
            # url
            url = part.rstrip(").,;")
            trail = part[len(url):]
            add_hyperlink(p, url, url)
            if trail:
                r=p.add_run(trail); set_run(r,12,False,False)
        else:
            # parse *...* italic
            part = parenthetical_amp(part)
            pat=re.compile(r'(\*\*\*.+?\*\*\*|\*\*.+?\*\*|\*.+?\*)')
            pos=0
            for m in pat.finditer(part):
                if m.start()>pos:
                    r=p.add_run(part[pos:m.start()]); set_run(r,12,False,False)
                tok=m.group(0)
                if tok.startswith("***"):
                    r=p.add_run(tok[3:-3]); set_run(r,12,True,True)
                elif tok.startswith("**"):
                    r=p.add_run(tok[2:-2]); set_run(r,12,True,False)
                else:
                    r=p.add_run(tok[1:-1]); set_run(r,12,False,True)
                pos=m.end()
            if pos<len(part):
                r=p.add_run(part[pos:]); set_run(r,12,False,False)

# save
try:
    doc.save(str(OUT_DOCX))
    print(f"saved {OUT_DOCX} size={OUT_DOCX.stat().st_size}")
except PermissionError:
    print(f"[ERROR] {OUT_DOCX.name} sedang dibuka oleh Microsoft Word. Harap tutup Word dan jalankan ulang script ini.")
    raise
print(f"entries={len(entries)} paras={len(doc.paragraphs)} tables={len(doc.tables)} sections={len(doc.sections)}")
