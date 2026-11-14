"""Generate a comprehensive 28-slide graduate-level PowerPoint presentation for GPT-3 (Brown et al., 2020)."""

from pathlib import Path
from PIL import Image
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = Path(r"c:\Users\90535\source\yüksek_lisans\makine öğrenmesi_sunum")
FIG_DIR = BASE_DIR / "assets" / "figures"
OUT_PPTX = BASE_DIR / "GPT3_Few_Shot_Learners_Yuksek_Lisans_Sunumu.pptx"

# Color Palette (Academic Navy / Slate / Teal / Amber)
NAVY_DARK = RGBColor(15, 28, 63)       # #0F1C3F
NAVY_MED = RGBColor(30, 58, 138)       # #1E3A8A
BLUE_ACCENT = RGBColor(37, 99, 235)    # #2563EB
TEAL = RGBColor(13, 148, 136)          # #0D9488
TEAL_LIGHT = RGBColor(240, 253, 250)   # #F0FDFA
AMBER = RGBColor(217, 119, 6)          # #D97706
AMBER_LIGHT = RGBColor(255, 251, 235)  # #FFFBEB
CRIMSON = RGBColor(190, 18, 60)        # #BE123C
CRIMSON_LIGHT = RGBColor(255, 241, 242)# #FFF1F2
BG_LIGHT = RGBColor(248, 250, 252)     # #F8FAFC
CARD_BG = RGBColor(255, 255, 255)      # #FFFFFF
CODE_BG = RGBColor(241, 245, 249)      # #F1F5F9
BORDER_GRAY = RGBColor(203, 213, 225)  # #CBD5E1
TEXT_DARK = RGBColor(30, 41, 59)       # #1E293B
TEXT_MUTED = RGBColor(100, 116, 139)   # #64748B
WHITE = RGBColor(255, 255, 255)
BLUE_PALE = RGBColor(239, 246, 255)    # #EFF6FF

FONT_MAIN = "Calibri"
FONT_MONO = "Consolas"
TOTAL_SLIDES = 28


def set_slide_bg(slide, color: RGBColor) -> None:
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_header_footer(slide, section_label: str, title_text: str, slide_num: int, subtitle: str = "") -> None:
    set_slide_bg(slide, BG_LIGHT)

    # Top white header strip
    hdr = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.95))
    hdr.fill.solid()
    hdr.fill.fore_color.rgb = WHITE
    hdr.line.fill.background()

    # Thin bottom accent line on header
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0.93), Inches(13.333), Inches(0.035))
    line.fill.solid()
    line.fill.fore_color.rgb = BLUE_ACCENT
    line.line.fill.background()

    # Section pill badge (top-left)
    badge_w = min(max(len(section_label) * 0.088 + 0.35, 1.8), 3.6)
    badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.45), Inches(0.10), Inches(badge_w), Inches(0.24))
    badge.fill.solid()
    badge.fill.fore_color.rgb = NAVY_DARK
    badge.line.fill.background()
    tf_b = badge.text_frame
    tf_b.word_wrap = False
    tf_b.margin_left = tf_b.margin_right = Inches(0.06)
    tf_b.margin_top = tf_b.margin_bottom = Inches(0.01)
    p_b = tf_b.paragraphs[0]
    p_b.alignment = PP_ALIGN.CENTER
    r_b = p_b.add_run()
    r_b.text = section_label.upper()
    r_b.font.name = FONT_MAIN
    r_b.font.size = Pt(9.5)
    r_b.font.bold = True
    r_b.font.color.rgb = WHITE

    if subtitle:
        sub_box = slide.shapes.add_textbox(Inches(0.45 + badge_w + 0.15), Inches(0.09), Inches(12.4 - badge_w), Inches(0.26))
        tf_s = sub_box.text_frame
        tf_s.margin_top = tf_s.margin_bottom = Inches(0.0)
        p_s = tf_s.paragraphs[0]
        r_s = p_s.add_run()
        r_s.text = subtitle
        r_s.font.name = FONT_MAIN
        r_s.font.size = Pt(10.5)
        r_s.font.italic = True
        r_s.font.color.rgb = TEXT_MUTED

    # Slide title
    title_box = slide.shapes.add_textbox(Inches(0.45), Inches(0.36), Inches(12.43), Inches(0.52))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_right = Inches(0)
    tf_t.margin_top = tf_t.margin_bottom = Inches(0)
    p_t = tf_t.paragraphs[0]
    r_t = p_t.add_run()
    r_t.text = title_text
    r_t.font.name = FONT_MAIN
    r_t.font.size = Pt(21.5)
    r_t.font.bold = True
    r_t.font.color.rgb = NAVY_DARK

    # Footer separator
    f_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.45), Inches(7.06), Inches(12.43), Inches(0.015))
    f_line.fill.solid()
    f_line.fill.fore_color.rgb = BORDER_GRAY
    f_line.line.fill.background()

    # Footer left
    fl = slide.shapes.add_textbox(Inches(0.45), Inches(7.10), Inches(10.5), Inches(0.30))
    tf_fl = fl.text_frame
    tf_fl.margin_top = tf_fl.margin_bottom = Inches(0)
    p_fl = tf_fl.paragraphs[0]
    r_fl = p_fl.add_run()
    r_fl.text = "Brown et al. (2020) • Language Models are Few-Shot Learners (GPT-3)  |  Yüksek Lisans Makine Öğrenmesi"
    r_fl.font.name = FONT_MAIN
    r_fl.font.size = Pt(9.5)
    r_fl.font.color.rgb = TEXT_MUTED

    # Footer right (slide number)
    fr = slide.shapes.add_textbox(Inches(11.3), Inches(7.10), Inches(1.58), Inches(0.30))
    tf_fr = fr.text_frame
    tf_fr.margin_top = tf_fr.margin_bottom = Inches(0)
    p_fr = tf_fr.paragraphs[0]
    p_fr.alignment = PP_ALIGN.RIGHT
    r_fr = p_fr.add_run()
    r_fr.text = f"Slayt {slide_num} / {TOTAL_SLIDES}"
    r_fr.font.name = FONT_MAIN
    r_fr.font.size = Pt(10)
    r_fr.font.bold = True
    r_fr.font.color.rgb = NAVY_DARK


def add_card(
    slide,
    x: float,
    y: float,
    w: float,
    h: float,
    title: str = "",
    bullets: list = None,
    fill_color: RGBColor = CARD_BG,
    border_color: RGBColor = BORDER_GRAY,
    accent_bar_color: RGBColor = None,
    title_color: RGBColor = NAVY_DARK,
    font_size: float = 12.5,
    title_size: float = 14.0,
):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    card.adjustments[0] = 0.03
    card.fill.solid()
    card.fill.fore_color.rgb = fill_color
    card.line.color.rgb = border_color
    card.line.width = Pt(1.0)

    if accent_bar_color is not None:
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y + 0.08), Inches(0.07), Inches(h - 0.16))
        bar.fill.solid()
        bar.fill.fore_color.rgb = accent_bar_color
        bar.line.fill.background()

    pad_l = 0.18 if accent_bar_color is None else 0.22
    tb = slide.shapes.add_textbox(Inches(x + pad_l), Inches(y + 0.10), Inches(w - pad_l - 0.12), Inches(h - 0.18))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0.02)

    first = True
    if title:
        p = tf.paragraphs[0]
        p.space_after = Pt(4)
        r = p.add_run()
        r.text = title
        r.font.name = FONT_MAIN
        r.font.size = Pt(title_size)
        r.font.bold = True
        r.font.color.rgb = title_color
        first = False

    if bullets:
        for item in bullets:
            p = tf.paragraphs[0] if first else tf.add_paragraph()
            first = False
            p.space_after = Pt(3.5)
            p.line_spacing = 1.12
            if isinstance(item, tuple):
                lead, rest = item
                r1 = p.add_run()
                r1.text = lead
                r1.font.name = FONT_MAIN
                r1.font.size = Pt(font_size)
                r1.font.bold = True
                r1.font.color.rgb = TEXT_DARK

                r2 = p.add_run()
                r2.text = rest
                r2.font.name = FONT_MAIN
                r2.font.size = Pt(font_size)
                r2.font.color.rgb = TEXT_DARK
            else:
                r = p.add_run()
                r.text = item
                r.font.name = FONT_MAIN
                r.font.size = Pt(font_size)
                r.font.color.rgb = TEXT_DARK


def add_formula_box(
    slide,
    x: float,
    y: float,
    w: float,
    h: float,
    formula: str,
    caption: str = "",
    dark: bool = True,
    font_size: float = 13.5,
) -> None:
    box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    box.adjustments[0] = 0.06
    box.fill.solid()
    box.fill.fore_color.rgb = NAVY_DARK if dark else CODE_BG
    box.line.color.rgb = BLUE_ACCENT if dark else BORDER_GRAY
    box.line.width = Pt(1.2)

    tb = slide.shapes.add_textbox(Inches(x + 0.14), Inches(y + 0.06), Inches(w - 0.28), Inches(h - 0.12))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE

    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = formula
    r.font.name = FONT_MONO
    r.font.size = Pt(font_size)
    r.font.bold = True
    r.font.color.rgb = RGBColor(103, 232, 249) if dark else NAVY_DARK

    if caption:
        p2 = tf.add_paragraph()
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(3)
        r2 = p2.add_run()
        r2.text = caption
        r2.font.name = FONT_MAIN
        r2.font.size = Pt(10.5)
        r2.font.color.rgb = RGBColor(203, 213, 225) if dark else TEXT_MUTED


def add_picture_fit(
    slide,
    img_filename: str,
    x: float,
    y: float,
    w: float,
    h: float,
    caption: str = "",
) -> None:
    # Draw white card container around figure
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    card.adjustments[0] = 0.02
    card.fill.solid()
    card.fill.fore_color.rgb = WHITE
    card.line.color.rgb = BORDER_GRAY
    card.line.width = Pt(1.0)

    cap_h = 0.44 if caption else 0.08
    pad = 0.08
    avail_w = w - 2 * pad
    avail_h = h - pad - cap_h

    img_path = FIG_DIR / img_filename
    with Image.open(img_path) as im:
        px_w, px_h = im.size

    aspect = px_w / px_h
    if avail_w / avail_h > aspect:
        draw_h = avail_h
        draw_w = draw_h * aspect
    else:
        draw_w = avail_w
        draw_h = draw_w / aspect

    img_x = x + (w - draw_w) / 2.0
    img_y = y + pad + (avail_h - draw_h) / 2.0
    slide.shapes.add_picture(str(img_path), Inches(img_x), Inches(img_y), width=Inches(draw_w), height=Inches(draw_h))

    if caption:
        cb = slide.shapes.add_textbox(Inches(x + 0.10), Inches(y + h - cap_h), Inches(w - 0.20), Inches(cap_h - 0.04))
        tf = cb.text_frame
        tf.word_wrap = True
        tf.margin_top = tf.margin_bottom = Inches(0.01)
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        r = p.add_run()
        r.text = caption
        r.font.name = FONT_MAIN
        r.font.size = Pt(9.5)
        r.font.italic = True
        r.font.color.rgb = TEXT_MUTED


def add_styled_table(
    slide,
    x: float,
    y: float,
    w: float,
    h: float,
    headers: list,
    rows: list,
    col_widths: list = None,
    font_size: float = 10.5,
    header_size: float = 10.5,
    highlight_rows: dict = None,
) -> None:
    num_rows = len(rows) + 1
    num_cols = len(headers)
    table_shape = slide.shapes.add_table(num_rows, num_cols, Inches(x), Inches(y), Inches(w), Inches(h))
    table = table_shape.table

    if col_widths:
        for idx, cw in enumerate(col_widths):
            table.columns[idx].width = Inches(cw)

    # Header row
    for c_idx, h_text in enumerate(headers):
        cell = table.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY_DARK
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        cell.margin_left = cell.margin_right = Inches(0.06)
        cell.margin_top = cell.margin_bottom = Inches(0.03)
        p = cell.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER if c_idx > 0 else PP_ALIGN.LEFT
        r = p.add_run()
        r.text = h_text
        r.font.name = FONT_MAIN
        r.font.size = Pt(header_size)
        r.font.bold = True
        r.font.color.rgb = WHITE

    highlight_rows = highlight_rows or {}
    for r_idx, row in enumerate(rows, start=1):
        bg_c = highlight_rows.get(r_idx - 1, WHITE if r_idx % 2 == 1 else CODE_BG)
        is_hl = (r_idx - 1) in highlight_rows
        for c_idx, val in enumerate(row):
            cell = table.cell(r_idx, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_c
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.margin_left = cell.margin_right = Inches(0.06)
            cell.margin_top = cell.margin_bottom = Inches(0.02)
            p = cell.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER if c_idx > 0 else PP_ALIGN.LEFT
            r = p.add_run()
            r.text = str(val)
            r.font.name = FONT_MAIN
            r.font.size = Pt(font_size)
            r.font.bold = is_hl or (c_idx == 0)
            r.font.color.rgb = NAVY_DARK if is_hl else TEXT_DARK


def set_notes(slide, text: str) -> None:
    slide.notes_slide.notes_text_frame.text = text.strip()


def build_presentation() -> None:
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]

    # =========================================================================
    # SLIDE 1: KAPAK SLAYTI
    # =========================================================================
    s1 = prs.slides.add_slide(blank)
    set_slide_bg(s1, NAVY_DARK)

    # Decorative geometric accent bars
    top_strip = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.14))
    top_strip.fill.solid()
    top_strip.fill.fore_color.rgb = TEAL
    top_strip.line.fill.background()

    side_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.65), Inches(1.25), Inches(0.10), Inches(3.80))
    side_bar.fill.solid()
    side_bar.fill.fore_color.rgb = BLUE_ACCENT
    side_bar.line.fill.background()

    # Pill: Course tag
    pill = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.95), Inches(1.20), Inches(4.8), Inches(0.38))
    pill.fill.solid()
    pill.fill.fore_color.rgb = RGBColor(30, 58, 138)
    pill.line.color.rgb = RGBColor(96, 165, 250)
    tf_p = pill.text_frame
    p = tf_p.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = "YÜKSEK LİSANS • MAKİNE ÖĞRENMESİ DERS SUNUMU"
    r.font.name = FONT_MAIN
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(191, 219, 254)

    # Main Title
    tb1 = s1.shapes.add_textbox(Inches(0.95), Inches(1.78), Inches(11.5), Inches(1.45))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    r1 = p1.add_run()
    r1.text = "Language Models are Few-Shot Learners"
    r1.font.name = FONT_MAIN
    r1.font.size = Pt(38)
    r1.font.bold = True
    r1.font.color.rgb = WHITE

    p2 = tf1.add_paragraph()
    p2.space_before = Pt(8)
    r2 = p2.add_run()
    r2.text = "GPT-3: Ölçekleme Yasaları, Bağlam İçi Öğrenme (In-Context Learning) ve Sınırları"
    r2.font.name = FONT_MAIN
    r2.font.size = Pt(20)
    r2.font.color.rgb = RGBColor(103, 232, 249)

    # Authors & Paper Info
    tb_auth = s1.shapes.add_textbox(Inches(0.95), Inches(3.45), Inches(11.4), Inches(1.30))
    tf_a = tb_auth.text_frame
    tf_a.word_wrap = True
    pa = tf_a.paragraphs[0]
    ra = pa.add_run()
    ra.text = "Makale Yazarları: Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, ..., Dario Amodei (OpenAI)"
    ra.font.name = FONT_MAIN
    ra.font.size = Pt(14)
    ra.font.color.rgb = RGBColor(226, 232, 240)

    pa2 = tf_a.add_paragraph()
    pa2.space_before = Pt(6)
    ra2 = pa2.add_run()
    ra2.text = "Yayın: NeurIPS 2020  |  arXiv:2005.14165v4 [cs.CL] (22 Temmuz 2020)"
    ra2.font.name = FONT_MAIN
    ra2.font.size = Pt(13)
    ra2.font.color.rgb = RGBColor(148, 163, 184)

    # 4 Key Metric Cards at Bottom
    stats = [
        ("175 Milyar", "Parametre (GPT-3)\nÖnceki yoğun modellerin 10x'i"),
        ("300 Milyar", "Eğitim Tokenı (BPE)\nKalite ağırlıklı 5 veri kaynağı"),
        ("Δθ = 0", "Gradyan Güncellemesiz\nZero / One / Few-Shot adaptasyon"),
        ("3,640 PF-gün", "Eğitim Hesaplama Gücü\n~3.14 × 10²³ FLOPs"),
    ]
    for i, (big, desc) in enumerate(stats):
        cx = 0.95 + i * 2.95
        c = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(cx), Inches(5.30), Inches(2.75), Inches(1.45))
        c.adjustments[0] = 0.06
        c.fill.solid()
        c.fill.fore_color.rgb = RGBColor(23, 39, 84)
        c.line.color.rgb = RGBColor(59, 130, 246)
        c.line.width = Pt(1.0)
        tb_c = s1.shapes.add_textbox(Inches(cx + 0.14), Inches(5.42), Inches(2.47), Inches(1.22))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        pc1 = tf_c.paragraphs[0]
        rc1 = pc1.add_run()
        rc1.text = big
        rc1.font.name = FONT_MAIN
        rc1.font.size = Pt(22)
        rc1.font.bold = True
        rc1.font.color.rgb = RGBColor(45, 212, 191)
        pc2 = tf_c.add_paragraph()
        pc2.space_before = Pt(4)
        rc2 = pc2.add_run()
        rc2.text = desc
        rc2.font.name = FONT_MAIN
        rc2.font.size = Pt(11)
        rc2.font.color.rgb = RGBColor(226, 232, 240)

    set_notes(s1, """[Slayt 1 - Kapak | ~1 dk]
Merhaba hocam ve değerli arkadaşlar. Bugün modern NLP ve derin öğrenmede paradigma değişimi başlatan Tom Brown ve arkadaşlarının (OpenAI, 2020) "Language Models are Few-Shot Learners" — yani GPT-3 — makalesini kapsamlı ve teknik boyutlarıyla sunacağım.
Makalenin ana tezi: Otoregresif bir Transformer dil modelini 175 milyar parametreye ölçeklediğimizde, model hiçbir gradyan güncellemesi (Δθ = 0) yapmadan yalnızca bağlama (prompt) verilen birkaç örnekle çok çeşitli görevlere uyum sağlayabilir.""")

    # =========================================================================
    # SLIDE 2: NLP'DE TEMSİL ÖĞRENİMİNİN EVRİMİ
    # =========================================================================
    s2 = prs.slides.add_slide(blank)
    add_header_footer(s2, "Bölüm 1 • Motivasyon", "NLP'de Temsil Öğreniminin Evrimi (Section 1)", 2,
                      "Göreve özel mimarilerden göreve bağımsız mimarilere, oradan göreve bağımsız öğrenmeye geçiş")

    stages = [
        ("1. Nesil: Statik Kelime Vektörleri", "Word2Vec (2013), GloVe (2014)",
         ["• Tek katmanlı kelime gömmeleri (word vectors).",
          "• Bağlamdan bağımsız anlam temsili.",
          "• Her görev için sıfırdan eğitilen task-specific sinir ağı mimarisi gerektirir."],
         TEXT_MUTED),
        ("2. Nesil: Bağlamsal RNN / LSTM", "Dai & Le (2015), CoVe, ELMo (2018)",
         ["• Çok katmanlı tekrarlayan ağlar ile bağlamsal iç durum (contextual state).",
          "• Kelime anlamı cümle bağlamına göre değişir.",
          "• Hâlâ görev özelinde tasarlanan üst mimarilere (task-specific architectures) beslenir."],
         BLUE_ACCENT),
        ("3. Nesil: Pre-trained Transformer + Fine-Tuning", "GPT-1 (2018), BERT (2018), RoBERTa, XLNet, T5",
         ["• Mimari tamamen görevden bağımsız (task-agnostic) hale geldi.",
          "• Doğrudan ince ayar (direct fine-tuning) ile SOTA sonuçlar.",
          "• ANCAK: Öğrenme süreci hâlâ binlerce etiketli veriye bağımlı!"],
         NAVY_MED),
        ("4. Nesil (GPT-3 Önerisi): In-Context Meta-Öğrenme", "Brown et al. (2020)",
         ["• Hem mimari hem de çıkarım (inference) görevden bağımsızdır.",
          "• Ön-eğitim sonrası ağırlık güncellemesi (fine-tuning) gerekmez.",
          "• Doğal dil yönergesi veya K ≤ 100 örnekle anında adaptasyon."],
         TEAL),
    ]
    for i, (st_title, st_ref, st_bullets, st_col) in enumerate(stages):
        sx = 0.45 + i * 3.15
        # Header pill for timeline step
        hd = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(sx), Inches(1.22), Inches(2.95), Inches(0.70))
        hd.fill.solid()
        hd.fill.fore_color.rgb = st_col
        hd.line.fill.background()
        tf_h = hd.text_frame
        tf_h.word_wrap = True
        p = tf_h.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        r = p.add_run()
        r.text = st_title
        r.font.name = FONT_MAIN
        r.font.size = Pt(12.5)
        r.font.bold = True
        r.font.color.rgb = WHITE

        if i < 3:
            arr = s2.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(sx + 2.97), Inches(1.42), Inches(0.16), Inches(0.28))
            arr.fill.solid()
            arr.fill.fore_color.rgb = TEXT_MUTED
            arr.line.fill.background()

        add_card(s2, sx, 2.02, 2.95, 3.30, st_ref, st_bullets, border_color=st_col, title_color=st_col, font_size=11.8, title_size=12.0)

    add_card(
        s2, 0.45, 5.52, 12.43, 1.32,
        "Temel Paradigma Kırılması (Section 1)",
        [
            ("Mimari Bağımsızlık ≠ Öğrenme Bağımsızlığı: ",
             "BERT/RoBERTa mimarileri görevden bağımsız olsa da, her yeni görev için denetimli veri seti üzerinde gradyan güncellemesi gerektirir. GPT-3 hedefi: Tek bir genel ağırlık kümesiyle (θ) tüm görevleri metin arayüzünden çözmek.")
        ],
        fill_color=BLUE_PALE, border_color=BLUE_ACCENT, accent_bar_color=BLUE_ACCENT, font_size=12.5
    )

    set_notes(s2, """[Slayt 2 - NLP Evrimi | ~1.5 dk]
Makalenin giriş bölümünde yazarlar NLP'deki transfer öğrenimi evrimini 4 aşamada özetliyor:
1) Word2Vec ve GloVe gibi tek katmanlı statik kelime vektörleri: Göreve özel mimarilere besleniyordu.
2) ELMo gibi çok katmanlı RNN/LSTM'ler: Bağlamsal temsil üretti ama yine görev özelinde üst katmanlar istiyordu.
3) GPT-1, BERT, RoBERTa ve T5: Pre-trained Transformer'lar görev-özel mimari ihtiyacını tamamen ortadan kaldırdı.
Ancak kritik bir eksik kaldı: Mimari görevden bağımsız (task-agnostic) olsa da her görev için ayrı bir fine-tuning veri seti gerekiyordu. GPT-3 tam olarak bu son engeli aşmayı hedefliyor.""")

    # =========================================================================
    # SLIDE 3: FINE-TUNING PARADİGMASININ 3 TEMEL DARBOĞAZI
    # =========================================================================
    s3 = prs.slides.add_slide(blank)
    add_header_footer(s3, "Bölüm 1 • Motivasyon", "Pre-Training + Fine-Tuning Paradigmasının 3 Temel Darboğazı", 3,
                      "Yazarlar neden gradyan tabanlı ince ayardan uzaklaşmak istiyor? (Section 1)")

    bottlenecks = [
        ("1. Pratik Veri Toplama Maliyeti",
         "Her yeni görev için 10³ – 10⁵ etiketli örnek zorunluluğu",
         ["• Dil görevleri yelpazesi çok geniştir: gramer düzeltme, soyut kavram örnekleme, hikâye eleştirisi, kod tamamlama...",
          "• Her yeni alt-görev için binlerce temiz etiketli örnek toplamak pratikte ölçeklenemez.",
          "• Dil modellerinin gerçek dünyadaki uygulanabilirliğini ciddi biçimde daraltır."],
         BLUE_ACCENT, BLUE_PALE),
        ("2. Sahte Korelasyonlar & Zayıf OOD Genelleme",
         "Yüksek kapasite + dar görev dağılımı = Ezberleme riski",
         ["• Ön-eğitimde büyük bilgi emen modeller, çok dar (narrow) görev dağılımlarında fine-tune edilmektedir.",
          "• Model, görevdeki sahte korelasyonları (spurious correlations) ve etiketleme kusurlarını (annotation artifacts) sömürür [GSL+18, NK19, MPL19].",
          "• Hendrycks et al. [HLW+20] ve Yogatama et al. [YdC+19]: Benchmark'ta 'insan üstü' görünen modeller Out-of-Distribution (OOD) örneklerde çöker."],
         CRIMSON, CRIMSON_LIGHT),
        ("3. İnsan Bilişi ile Yapısal Uyumsuzluk",
         "Akışkanlık ve genellik (Fluidity & Generality) eksikliği",
         ["• İnsanlar yeni bir görev için 100.000 örnek görmez; kısa bir doğal dil yönergesi veya 1–2 gösterim yeterlidir.",
          "• İnsanlar tek bir diyalog içinde görevler arası anında geçiş yapabilir (örn. sohbet ortasında toplama işlemi yapmak).",
          "• Fine-tune edilmiş modeller ise tek bir dar göreve kilitlenir."],
         TEAL, TEAL_LIGHT),
    ]
    for i, (t, sub, bul, col, bg_c) in enumerate(bottlenecks):
        bx = 0.45 + i * 4.22
        add_card(s3, bx, 1.18, 3.98, 4.35, f"{t}\n[{sub}]", bul,
                 fill_color=CARD_BG, border_color=col, accent_bar_color=col, title_color=col, font_size=12.0, title_size=13.0)

    add_card(
        s3, 0.45, 5.72, 12.43, 1.15,
        "Makalenin Temel Çıkarımı",
        [("Eleştirel Gözlem: ",
          "Fine-tuning başarısı çoğu zaman gerçek dil anlayışını değil, dar benchmark dağılımına aşırı uyumu (over-specialization) abartır. Gerçek genel dil sistemleri için görevler arası sıfır gradyan geçişi gerekir.")],
        fill_color=AMBER_LIGHT, border_color=AMBER, accent_bar_color=AMBER, title_color=AMBER, font_size=12.5
    )

    set_notes(s3, """[Slayt 3 - Fine-Tuning Darboğazları | ~1.5 dk]
Yazarlar Section 1'de fine-tuning paradigmasını üç açıdan eleştiriyor:
1) Pratik darboğaz: Her yeni dil görevi için binlerce veya yüz binlerce etiketli veri toplamak mümkün değil.
2) İstatistiksel darboğaz: Çok yüksek kapasiteli bir modeli çok dar bir görev dağılımında fine-tune ettiğinizde, model gerçek görevi değil veri setindeki sahte korelasyonları (annotation artifacts) öğrenir. Niven & Kao (2019), McCoy et al. (2019) gibi çalışmalar, benchmark'ta insan seviyesinde skor alan fine-tuned modellerin dağılım dışı (OOD) veride başarısız olduğunu göstermiştir.
3) Bilişsel darboğaz: İnsanlar tek bir cümlelik yönerge veya 1-2 örnekle anında yeni görevlere adapte olur ve diyalog içinde farklı görevleri karıştırabilir.""")

    # =========================================================================
    # SLIDE 4: ÇÖZÜM HİPOTEZİ: META-LEARNING VE IN-CONTEXT LEARNING
    # =========================================================================
    s4 = prs.slides.add_slide(blank)
    add_header_footer(s4, "Bölüm 1 • Meta-Learning", "Çözüm Hipotezi: Meta-Learning ve Bağlam İçi Öğrenme (In-Context Learning)", 4,
                      "Outer Loop (SGD Ön-Eğitim) vs. Inner Loop (Δθ = 0 İleri Besleme Adaptasyonu)")

    add_card(
        s4, 0.45, 1.12, 5.55, 2.50,
        "İki Döngülü (Inner / Outer Loop) Meta-Öğrenme",
        [
            ("Outer Loop (Dış Döngü — Eğitim Zamanı): ",
             "Denetimsiz ön-eğitim sırasında SGD ile model ağırlıklarına (θ) geniş beceri dağılımı ve örüntü tanıma kodlanır."),
            ("Inner Loop (İç Döngü — Çıkarım Zamanı): ",
             "İleri besleme (forward pass) aktivasyonları üzerinden yalnızca bağlama (context) koşullanarak adaptasyon. Ağırlık güncellemesi YOKTUR (Δθ = 0)."),
        ],
        border_color=BLUE_ACCENT, accent_bar_color=BLUE_ACCENT, font_size=11.8
    )
    add_card(
        s4, 0.45, 3.74, 5.55, 3.12,
        "Ölçekleme Hipotezi (Kaplan et al., 2020 → GPT-3)",
        [
            ("Öncül Durum (GPT-2, 1.5B): ",
             "In-context learning sinyali var ama zayıf: Natural Questions'ta %4, CoQA'da 55 F1 (SOTA'nın 35+ puan gerisinde)."),
            ("Temel Hipotez: ",
             "Log-olabilirlik kaybı (log loss) ölçekle pürüzsüz bir güç yasası izlediğine göre, bağlam içi öğrenme de kapasiteyle birlikte dramatik artmalıdır."),
            ("Figure 1.2 Bulgusu: ",
             "Sembol ayıklamada 1.3B model K ile neredeyse hiç gelişmezken, 175B modelde öğrenme eğrisi dikleşir ve doğal dil yönergesi (prompt) büyük sıçrama sağlar."),
        ],
        fill_color=TEAL_LIGHT, border_color=TEAL, accent_bar_color=TEAL, title_color=TEAL, font_size=11.5
    )

    add_picture_fit(s4, "fig1_1_meta_learning.png", 6.18, 1.12, 6.70, 2.68,
                    "Figure 1.1: Outer loop (SGD ön-eğitim) ve Inner loop (ileri beslemeli in-context learning).")
    add_picture_fit(s4, "fig1_2_in_context_curves.png", 6.18, 3.90, 6.70, 2.96,
                    "Figure 1.2: Model boyutu (1.3B → 13B → 175B) ve K arttıkça dikleşen in-context learning eğrileri.")

    set_notes(s4, """[Slayt 4 - Meta-Learning & In-Context Learning | ~2 dk]
Section 1 (Dipnot 1) terminolojiyi netleştirir: Önceki çalışmalarda bu yönteme bazen 'zero-shot transfer' deniyordu ama çıkarım zamanında örnekler verildiği için bu isim muğlaktı. Yazarlar bunun yerine RL2 ve Hochreiter (2001) çizgisinde 'Meta-Learning' çerçevesini kullanır:
- Sağ üstteki Figure 1.1'de gördüğünüz mor yatay ok Outer Loop'tur: Denetimsiz ön-eğitimde SGD ile ağırlıklar güncellenir ve model metinlerdeki doğal alt görevleri (aritmetik, harf düzeltme, çeviri) öğrenir.
- Dikey mavi oklar Inner Loop (In-Context Learning)'tir: Çıkarım anında ağırlıklarda hiçbir değişiklik (Δθ = 0) olmadan, sadece ileri besleme aktivasyonlarıyla göreve adapte olunur.
- Sağ alttaki Figure 1.2 ise makalenin ana kanıtlarından biridir: 1.3B model bağlamdaki örnek sayısı K artsa bile neredeyse düz kalırken, 175B model hem K arttıkça hem de doğal dil yönergesi (Natural Language Prompt) eklendikçe dramatik şekilde iyileşir.""")

    # =========================================================================
    # SLIDE 5: GÖREV SPESİFİKASYON SPEKTRUMU (0S, 1S, FS, FT)
    # =========================================================================
    s5 = prs.slides.add_slide(blank)
    add_header_footer(s5, "Bölüm 1 • Değerlendirme Rejimleri", "Görev Spesifikasyon Spektrumu: 0S, 1S, FS ve Fine-Tuning", 5,
                      "Section 2 (Figure 2.1) & 42 Benchmark Toplu Ölçekleme Eğrisi (Figure 1.3)")

    add_picture_fit(s5, "fig2_1_four_settings.png", 0.45, 1.12, 6.00, 5.76,
                    "Figure 2.1: Zero-Shot, One-Shot, Few-Shot (Δθ = 0) vs. Geleneksel Fine-Tuning (gradyan güncellemeli).")

    add_styled_table(
        s5, 6.62, 1.12, 6.26, 2.55,
        ["Rejim", "Gradyan (Δθ)", "Bağlam Örneği (K)", "Özellik & İnsan Analojisi"],
        [
            ["Fine-Tuning (FT)", "Var (SGD)", "10³ – 10⁵ (Eğitim)", "Yüksek skor; ancak dar dağılım & OOD riski (GPT-3'te yok)"],
            ["Few-Shot (FS)", "Yok (0)", "10 – 100 (n_ctx=2048)", "Küçük veri ile SOTA'ya yakın; bağlam penceresiyle sınırlı"],
            ["One-Shot (1S)", "Yok (0)", "K = 1 + Yönerge", "Mechanical Turk görev tanımına en yakın doğal ayar"],
            ["Zero-Shot (0S)", "Yok (0)", "K = 0 (Sadece Yönerge)", "En zorlu ve güvenli ayar; bazen format açısından belirsiz"],
        ],
        col_widths=[1.40, 1.05, 1.48, 2.33],
        font_size=10.0, header_size=10.5, highlight_rows={1: TEAL_LIGHT}
    )

    add_picture_fit(s5, "fig1_3_aggregate_42_benchmarks.png", 6.62, 3.80, 6.26, 3.08,
                    "Figure 1.3: 42 benchmark ortalamasında model büyüdükçe Few-Shot ile Zero-Shot arası makas açılıyor.")

    set_notes(s5, """[Slayt 5 - Görev Spesifikasyon Spektrumu | ~1.5 dk]
Section 2'de görevlerin modele verilme biçimini 4 noktada tanımlıyoruz (Figure 2.1):
1) Fine-Tuning: Ağırlıklar binlerce örnekle gradyan adımlarıyla güncellenir (GPT-3 makalesinde yapılmamıştır).
2) Few-Shot: Modelin 2048 tokenlık bağlam penceresine sığacak kadar (genellikle K=10 ile 100 arası) örnek ve sonuna çözülecek soru konur.
3) One-Shot: Doğal dil tanımına ek olarak yalnızca tek bir örnek (K=1) verilir. Yazarlar bunun Mechanical Turk gibi insan çalışanlara görev tarif etme biçimiyle birebir örtüştüğünü belirtir.
4) Zero-Shot: Sadece doğal dil komutu verilir. Bazen insan için bile çıktı formatını bilmek zor olduğu için 'unfairly hard' olabilir.
Sağ alttaki Figure 1.3'te 42 benchmarkın tamamında model ölçeği arttıkça Few-Shot (turuncu) eğrisinin Zero-Shot (mavi) eğrisinden giderek daha hızlı yükseldiğini görüyoruz.""")

    # =========================================================================
    # SLIDE 6: GPT-3 MİMARİ TASARIMI VE SPARSE ATTENTION
    # =========================================================================
    s6 = prs.slides.add_slide(blank)
    add_header_footer(s6, "Bölüm 2 • Mimari", "GPT-3 Mimari Tasarımı ve Locally Banded Sparse Attention", 6,
                      "Section 2.1: Decoder-only Otoregresif Transformer ve Seyrek Dikkat Katmanları")

    add_card(
        s6, 0.45, 1.12, 6.20, 3.15,
        "Temel Mimari Özellikler (GPT-2 Mirası)",
        [
            ("Model Ailesi: ", "Yalnızca Kod Çözücü (Decoder-Only) Otoregresif Transformer — p(x) = ∏ P(x_t | x_<t)."),
            ("Normalizasyon & İlklendirme: ", "Modified initialization ve Pre-Normalization (LayerNorm dikkat/FFN bloklarının girişinde)."),
            ("Tokenizasyon: ", "Tersinir Byte-Level BPE (GPT-2 sözlüğü). Ortalama 1 token ≈ 0.7 kelime (İngilizce ağırlıklı)."),
            ("Bağlam & Darboğaz Oranı: ", "Tüm modellerde n_ctx = 2048 token. İleri besleme katmanı her zaman d_ff = 4 × d_model."),
        ],
        border_color=NAVY_MED, accent_bar_color=NAVY_MED, font_size=12.0
    )

    add_card(
        s6, 0.45, 4.42, 6.20, 2.45,
        "Tek Mimari Yenilik: Alternatif Dense + Sparse Attention",
        [
            ("Mekanizma [CGRS19]: ", "Transformer katmanları boyunca yoğun (dense) dikkat katmanları ile yerel bantlı seyrek dikkat (Locally Banded Sparse Attention) katmanları dönüşümlü (alternating) sıralanır."),
            ("Neden? ", "2048 tokenlık tam bağlam penceresinde hem yerel bağlam hassasiyetini korumak hem de bellek/hesaplama bant genişliğini optimize etmek."),
        ],
        fill_color=TEAL_LIGHT, border_color=TEAL, accent_bar_color=TEAL, title_color=TEAL, font_size=12.0
    )

    # Right side: Custom crisp architectural diagram comparing Dense vs Locally Banded Sparse Attention
    diag_card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.85), Inches(1.12), Inches(6.03), Inches(5.75))
    diag_card.adjustments[0] = 0.02
    diag_card.fill.solid()
    diag_card.fill.fore_color.rgb = WHITE
    diag_card.line.color.rgb = BORDER_GRAY

    tb_d = s6.shapes.add_textbox(Inches(7.05), Inches(1.22), Inches(5.65), Inches(0.45))
    p_d = tb_d.text_frame.paragraphs[0]
    p_d.alignment = PP_ALIGN.CENTER
    r_d = p_d.add_run()
    r_d.text = "Katmanlar Arası Ardışık Dikkat Deseni (n_ctx = 2048)"
    r_d.font.name = FONT_MAIN
    r_d.font.size = Pt(14)
    r_d.font.bold = True
    r_d.font.color.rgb = NAVY_DARK

    # Draw two 8x8 lower-triangular attention matrices side-by-side
    def draw_attn_matrix(origin_x, origin_y, title, mode):
        lbl = s6.shapes.add_textbox(Inches(origin_x), Inches(origin_y), Inches(2.5), Inches(0.32))
        pl = lbl.text_frame.paragraphs[0]
        pl.alignment = PP_ALIGN.CENTER
        rl = pl.add_run()
        rl.text = title
        rl.font.name = FONT_MAIN
        rl.font.size = Pt(11.5)
        rl.font.bold = True
        rl.font.color.rgb = NAVY_MED if mode == "dense" else TEAL

        cell_s = 0.27
        gx0 = origin_x + 0.17
        gy0 = origin_y + 0.36
        for row in range(8):
            for col in range(8):
                active = False
                if col <= row:
                    if mode == "dense":
                        active = True
                    else:
                        # locally banded (band width 2) + strided/summary feel
                        if (row - col) <= 2 or col % 4 == 0:
                            active = True
                sq = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                         Inches(gx0 + col * cell_s), Inches(gy0 + row * cell_s),
                                         Inches(cell_s - 0.02), Inches(cell_s - 0.02))
                sq.fill.solid()
                if col > row:
                    sq.fill.fore_color.rgb = RGBColor(241, 245, 249)  # masked future
                elif active:
                    sq.fill.fore_color.rgb = BLUE_ACCENT if mode == "dense" else TEAL
                else:
                    sq.fill.fore_color.rgb = RGBColor(203, 213, 225)  # sparse zeroed
                sq.line.fill.background()

    draw_attn_matrix(7.05, 1.78, "Tek Katman: Dense Causal", "dense")
    draw_attn_matrix(10.05, 1.78, "Çift Katman: Sparse Banded", "sparse")

    add_formula_box(
        s6, 7.05, 4.48, 5.63, 1.00,
        "Katman(i) = Dense_Attn   ↔   Katman(i+1) = Sparse_Attn\nToplam Katman = 96  |  Başlık = 96  |  d_head = 128",
        "Sparse Transformer [CGRS19] tabanlı ardışık dikkat mimarisi",
        dark=True, font_size=11.5
    )

    add_card(
        s6, 7.05, 5.62, 5.63, 1.08,
        "Veri Aktarımı & GPU Yerleşimi",
        ["Model parametreleri, düğümler (nodes) arası veri transferini en aza indirmek için hem derinlik (depth) hem genişlik (width) boyutunda GPU'lara bölünür."],
        fill_color=CODE_BG, border_color=BORDER_GRAY, font_size=11.0, title_size=12.0
    )

    set_notes(s6, """[Slayt 6 - GPT-3 Mimarisi | ~1.5 dk]
Section 2.1'e baktığımızda GPT-3'ün başarısının karmaşık yeni bir mimari bloktan ziyade ölçeklemeden geldiğini görürüz. Temelde GPT-2 mimarisini (pre-normalization, değiştirilmiş ilklendirme ve byte-level BPE) kullanır.
Burada bilmeniz gereken tek mimari fark: Transformer katmanları boyunca standart yoğun (dense) nedensel dikkat ile Sparse Transformer'dan (Child et al., 2019) alınan 'Locally Banded Sparse Attention' katmanlarının ardışık (alternating) dizilmesidir.
Tüm 8 modelde bağlam penceresi n_ctx = 2048 tokendır ve ileri besleme katmanı darboğaz boyutunun tam 4 katıdır (d_ff = 4 * d_model). Sağdaki matrislerde gelecek tokenların maskelendiği (nedensel/causal) yapıyı ve seyrek banttaki hesaplama tasarrufunu görebilirsiniz.""")

    # =========================================================================
    # SLIDE 7: 8 FARKLI ÖLÇEKTE MODEL AİLESİ VE HİPERPARAMETRELER
    # =========================================================================
    s7 = prs.slides.add_slide(blank)
    add_header_footer(s7, "Bölüm 2 • Model Ölçekleme", "8 Farklı Ölçekte Model Ailesi ve Hiperparametre Ölçekleme (Table 2.1)", 7,
                      "125 Milyondan 175 Milyar Parametreye 3 Büyüklük Mertebesi (Tüm Modeller: 300B Token)")

    add_styled_table(
        s7, 0.45, 1.15, 12.43, 3.65,
        ["Model Adı", "n_params", "n_layers", "d_model", "n_heads", "d_head", "Batch Size", "Learning Rate"],
        [
            ["GPT-3 Small", "125M", "12", "768", "12", "64", "0.5M", "6.0 × 10⁻⁴"],
            ["GPT-3 Medium", "350M", "24", "1024", "16", "64", "0.5M", "3.0 × 10⁻⁴"],
            ["GPT-3 Large", "760M", "24", "1536", "16", "96", "0.5M", "2.5 × 10⁻⁴"],
            ["GPT-3 XL", "1.3B", "24", "2048", "24", "128", "1M", "2.0 × 10⁻⁴"],
            ["GPT-3 2.7B", "2.7B", "32", "2560", "32", "80", "1M", "1.6 × 10⁻⁴"],
            ["GPT-3 6.7B", "6.7B", "32", "4096", "32", "128", "2M", "1.2 × 10⁻⁴"],
            ["GPT-3 13B", "13.0B", "40", "5140", "40", "128", "2M", "1.0 × 10⁻⁴"],
            ["GPT-3 175B ('GPT-3')", "175.0B", "96", "12288", "96", "128", "3.2M", "0.6 × 10⁻⁴"],
        ],
        col_widths=[2.35, 1.35, 1.25, 1.35, 1.25, 1.25, 1.65, 1.98],
        font_size=11.5, header_size=11.5, highlight_rows={7: TEAL_LIGHT}
    )

    add_card(
        s7, 0.45, 4.98, 6.08, 1.90,
        "Gradient Noise Scale ile Hiperparametre Seçimi [MKAT18]",
        [
            ("Ters Yönlü Ölçekleme: ", "Model kapasitesi arttıkça Batch Size büyütülür (0.5M → 3.2M token), Learning Rate ise küçültülür (6.0×10⁻⁴ → 0.6×10⁻⁴)."),
            ("Neden? ", "Büyük modellerde gradyan gürültü ölçeği (gradient noise scale) yükselir; daha büyük batch boyutu veri paralelliğini verimli kılar, düşük LR ise optimizasyon kararlılığını korur."),
        ],
        border_color=BLUE_ACCENT, accent_bar_color=BLUE_ACCENT, font_size=11.5
    )

    add_card(
        s7, 6.80, 4.98, 6.08, 1.90,
        "Mimari Oranların Seçim Mantığı",
        [
            ("Hesaplama & Yük Dengeleme: ", "n_layers ve d_model değerleri yalnızca doğrulama kaybına göre değil, GPU kümesi üzerindeki hesaplama verimliliği ve load-balancing'e göre seçilmiştir."),
            ("Hassasiyet Bulgusu [KMH+20]: ", "Ölçekleme yasaları, doğrulama kaybının (validation loss) bu en-boy oranlarına makul bir aralıkta güçlü biçimde duyarlı olmadığını gösterir."),
        ],
        fill_color=BLUE_PALE, border_color=NAVY_MED, accent_bar_color=NAVY_MED, font_size=11.5
    )

    set_notes(s7, """[Slayt 7 - 8 Model Ailesi | ~1.5 dk]
Table 2.1, yazarların sistematik ölçekleme çalışmasını göstermek için eğittiği 8 modeli özetliyor. 125 Milyon parametreden 175 Milyar parametreye kadar 3 büyüklük mertebesi taranmış ve tüm modeller 300 milyar tokenda eğitilmiştir.
En büyük model olan GPT-3 175B; 96 katman, 12.288 gizli boyut, 96 dikkat başlığı ve başlık başına 128 boyuta sahiptir.
Burada Yüksek Lisans dersi için çok önemli bir optimizasyon kuralı var: McCandlish et al. (2018) Gradient Noise Scale çalışmasına dayanarak, eğitim sırasında anlık gradyan gürültü ölçeği ölçülmüş; model büyüdükçe Batch Size 0.5M tokendan 3.2M tokene çıkarılırken, Learning Rate 10 kat düşürülmüştür (6.0e-4'ten 0.6e-4'e).""")

    # =========================================================================
    # SLIDE 8: VERİ SETİ MÜHENDİSLİĞİ (COMMON CRAWL FİLTRELEME)
    # =========================================================================
    s8 = prs.slides.add_slide(blank)
    add_header_footer(s8, "Bölüm 2 • Veri Mühendisliği", "Veri Seti Mühendisliği: Common Crawl Filtreleme ve Tekilleştirme", 8,
                      "Section 2.2 & Appendix A: Ham 45 TB İnternet Verisinden 570 GB Yüksek Kaliteli Derleme")

    add_card(
        s8, 0.45, 1.12, 6.35, 3.25,
        "3 Aşamalı Common Crawl Kalite Boru Hattı (Appendix A)",
        [
            ("Ham Veri: ", "2016–2019 arası 41 aylık Common Crawl shard'ı = 45 TB sıkıştırılmış düz metin."),
            ("1. Otomatik Kalite Sınıflandırıcısı: ", "Spark HashingTF + Lojistik Regresyon. Pozitif örnekler: WebText, Wikipedia, web kitapları; Negatif örnekler: Ham Common Crawl."),
            ("2. Bulanık Tekilleştirme (Fuzzy Deduplication): ", "Spark MinHashLSH (10 hash) ile belge düzeyinde kopyaların ve WebText çakışmalarının silinmesi (%10 boyut azalması)."),
            ("3. Referans Derlem Ekleme: ", "Genişletilmiş WebText2, Books1, Books2 ve İngilizce Wikipedia eklenmesi."),
        ],
        border_color=BLUE_ACCENT, accent_bar_color=BLUE_ACCENT, font_size=11.5
    )

    add_formula_box(
        s8, 0.45, 4.50, 6.35, 1.18,
        "Belge Kabul Koşulu:  np.random.pareto(α) > 1 - document_score   (α = 9)",
        "45 TB → 570 GB (~400B BPE token) | Sert eşik yerine stokastik Pareto örneklemesi: yüksek skoru öne çıkarırken OOD çeşitliliğini de korur.",
        dark=True, font_size=11.5
    )

    add_card(
        s8, 0.45, 5.80, 6.35, 1.08,
        "Neden Stokastik Pareto (α = 9)?",
        ["α = 9, WebText üzerindeki sınıflandırıcı skor dağılımına uyacak şekilde seçilmiştir. Tamamen dışlamak yerine dağılım dışı ama yararlı belgeleri azınlıkta tutarak OOD üretim kaybını düşürür."],
        fill_color=TEAL_LIGHT, border_color=TEAL, font_size=11.0, title_size=12.0
    )

    # Right side: Table 2.2
    add_card(
        s8, 6.98, 1.12, 5.90, 5.76,
        "Table 2.2: Nihai Eğitim Veri Karışımı",
        [("Kritik Tasarım Kararı: ", "Veri setleri boyutlarına göre değil, algılanan kalitelerine göre örneklenir!")],
        fill_color=WHITE, border_color=BORDER_GRAY, font_size=11.5, title_size=14.0
    )
    add_styled_table(
        s8, 7.15, 2.02, 5.56, 2.70,
        ["Veri Seti", "Miktar (Token)", "Eğitim Ağırlığı", "300B'de Epoch"],
        [
            ["Common Crawl (filtered)", "410 Milyar", "%60", "0.44"],
            ["WebText2", "19 Milyar", "%22", "2.9"],
            ["Books1", "12 Milyar", "%8", "1.9"],
            ["Books2", "55 Milyar", "%8", "0.43"],
            ["Wikipedia (İngilizce)", "3 Milyar", "%3", "3.4"],
        ],
        col_widths=[2.06, 1.18, 1.16, 1.16],
        font_size=10.8, header_size=10.5, highlight_rows={1: BLUE_PALE, 4: BLUE_PALE}
    )
    add_card(
        s8, 7.15, 4.92, 5.56, 1.78,
        "Kalite vs. Overfitting Ödünleşimi",
        [
            ("• Common Crawl (410B): ", "Eğitimde bir kez bile tamamen görülmez (0.44 epoch)."),
            ("• Wikipedia & WebText2: ", "Daha kaliteli oldukları için sırasıyla 3.4 ve 2.9 kez örneklenir — yüksek veri kalitesi uğruna kontrollü küçük overfitting kabul edilir."),
        ],
        fill_color=AMBER_LIGHT, border_color=AMBER, title_color=AMBER, font_size=11.2, title_size=12.5
    )

    set_notes(s8, """[Slayt 8 - Veri Mühendisliği | ~2 dk]
Ham Common Crawl neredeyse 1 trilyon kelimelik devasa bir havuzdur ama kalitesi düşüktür. Appendix A'da yazarlar Spark üzerinde çalışan 3 aşamalı bir veri temizleme pipeline'ı kuruyor:
1) WebText, Wikipedia ve web kitaplarını pozitif, ham Common Crawl'u negatif sınıf alarak Spark HashingTF özellikleriyle bir Lojistik Regresyon sınıflandırıcısı eğitiyorlar.
2) Her belgeye verilen skor üzerinden `np.random.pareto(9) > 1 - document_score` koşuluyla stokastik kabul uygulanıyor. Bu sayede 45 TB ham veri 570 GB'a (~400B token) indirilirken dağılım dışı çeşitlilik korunuyor.
3) Spark MinHashLSH (10 hash) ile bulanık tekilleştirme yapılıp WebText çakışmaları çıkarılıyor (%10 küçülme).
Sağdaki Table 2.2 çok önemli bir ilkeyi gösterir: Common Crawl havuzun ezici çoğunluğu olmasına rağmen eğitimde %60 ağırlıkla sadece 0.44 epoch görülürken, 3 milyar tokenlık Wikipedia 3.4 epoch, WebText2 ise 2.9 epoch örneklenir.""")

    # =========================================================================
    # SLIDE 9: EĞİTİM KARIŞIMI, DAĞITIK SİSTEM VE HESAPLAMA KARMAŞIKLIĞI
    # =========================================================================
    s9 = prs.slides.add_slide(blank)
    add_header_footer(s9, "Bölüm 2 • Eğitim & Hesaplama", "Optimizasyon, Dağıtık Eğitim ve Hesaplama Karmaşıklığı (Appendix B & D)", 9,
                      "Model Paralelliği, Document Packing ve C ≈ 6·N·D FLOP Hesaplama Analizi")

    add_card(
        s9, 0.45, 1.12, 6.20, 2.35,
        "Eğitim Hiperparametreleri & Document Packing (Appendix B)",
        [
            ("Optimizer: ", "Adam (β₁ = 0.9, β₂ = 0.95, ε = 10⁻⁸), Global Grad Clip = 1.0, Weight Decay = 0.1."),
            ("LR & Batch Schedule: ", "İlk 375M tokenda lineer LR warmup; 260B tokenda %10'a cosine decay. Batch size ilk 4–12B tokenda 32k'dan tam değere artırılır."),
            ("Verimli Packing: ", "Kısa belgeler <|endoftext|> ile ayrılıp 2048'lik dizilere paketlenir; özel dikkat maskesi yerine ayraç tokenı kullanılır. Tekrarlamasız (without replacement) örnekleme."),
        ],
        border_color=NAVY_MED, accent_bar_color=NAVY_MED, font_size=11.2
    )

    add_formula_box(
        s9, 0.45, 3.58, 6.20, 0.96,
        "C ≈ 6 · N_params · D_tokens = 6 × 174.6B × 300B ≈ 3.14 × 10²³ FLOPs",
        "1 Petaflop/s-gün = 8.64 × 10¹⁹ FLOP  ⇒  GPT-3 175B = 3,640 PF-days (Attention <%10 olduğu için ihmal)",
        dark=True, font_size=11.2
    )

    add_styled_table(
        s9, 0.45, 4.66, 6.20, 2.22,
        ["Model (Table D.1)", "Params", "Tokens", "FLOP/p/t", "Toplam PF-days"],
        [
            ["T5-11B (Enc-Dec, %50 aktif)", "11.0B", "1,000B", "3", "382 PF-days"],
            ["RoBERTa-Large", "355M", "2,000B", "6", "49.3 PF-days"],
            ["GPT-3 2.7B", "2.65B", "300B", "6", "55.2 PF-days"],
            ["GPT-3 175B", "174.6B", "300B", "6", "3,640 PF-days"],
        ],
        col_widths=[2.25, 0.90, 0.95, 0.85, 1.25],
        font_size=10.2, header_size=10.2, highlight_rows={1: BLUE_PALE, 2: BLUE_PALE, 3: TEAL_LIGHT}
    )

    add_picture_fit(s9, "fig2_2_total_compute.png", 6.82, 1.12, 6.06, 3.72,
                    "Figure 2.2: Toplam eğitim hesaplama gücü (Log ölçeğinde Petaflop/s-gün).")

    add_card(
        s9, 6.82, 4.96, 6.06, 1.92,
        "Kritik Scaling Laws Çıkarımı & Dağıtık Eğitim",
        [
            ("Compute Denkliği (Fig 2.2): ", "GPT-3 2.7B (altyazıda 3B diye anılır), RoBERTa-Large (355M)'dan ~8-10x büyük olmasına rağmen daha az tokenda (300B vs 2T) eğitildiği için ikisi de ~50 PF-days tüketir."),
            ("Dağıtık Altyapı: ", "Microsoft V100 yüksek bant genişlikli GPU kümesinde matris içi (width) + katmanlar arası (depth) hibrit model paralelliği."),
        ],
        fill_color=TEAL_LIGHT, border_color=TEAL, accent_bar_color=TEAL, title_color=TEAL, font_size=11.2
    )

    set_notes(s9, """[Slayt 9 - Optimizasyon & Hesaplama Karmaşıklığı | ~2 dk]
Appendix B optimizasyon detaylarını verir: Adam (β1=0.9, β2=0.95), gradyan kırpma 1.0, weight decay 0.1 ve 260B tokenda %10'a inen kosinüs decay. Kısa belgeler özel attention maskesi gerektirmeksizin `<|endoftext|>` ile ayrılıp 2048'lik dizilere paketlenir.
Appendix D'deki FLOP hesabı çok nettir: İleri geçişte her aktif parametre ve token için 2 FLOP (1 çarpma + 1 toplama), geri geçişte ∂params/∂loss ve ∂acts/∂loss için 3x toplam çarpanı = 6 FLOP/parametre/token. T5 encoder-decoder olduğu için aktif parametre oranı 0.5'tir (3 FLOP).
Sonuç olarak GPT-3 175B toplam 3.14×10²³ FLOP yani 3,640 Petaflop/s-gün tüketmiştir. Ayrıca Table D.1'de göreceğiniz gibi RoBERTa-Large (355M, 2T token) ile GPT-3 2.7B (300B token) neredeyse aynı compute bütçesini (~50 PF-days) kullanmıştır.""")

    # =========================================================================
    # SLIDE 10: DEĞERLENDİRME METODOLOJİSİ VE OLASILIK NORMALİZASYONU
    # =========================================================================
    s10 = prs.slides.add_slide(blank)
    add_header_footer(s10, "Bölüm 2 • Değerlendirme", "Değerlendirme Protokolü ve Olasılık Normalizasyonu (Section 2.4)", 10,
                      "Çoktan Seçmeli, İkili Sınıflandırma ve Serbest Üretim Görevlerinde Skorlama Matematiği")

    add_card(
        s10, 0.45, 1.15, 6.08, 2.55,
        "1. Bağlam Oluşturma & Çoktan Seçmeli Görevler",
        [
            ("Örnek Seçimi: ", "Her test örneği için eğitim setinden (LAMBADA/StoryCloze'da dev setinden) rastgele K örnek çekilir (1 veya 2 satır sonu ile ayrılır)."),
            ("Uzunluk Normalizasyonu: ", "K adet (bağlam + doğru cevap) sonrası test bağlamı verilir; aday şıkların uzunluk yanlılığını önlemek için token başına log-olabilirlik (per-token likelihood) karşılaştırılır."),
        ],
        border_color=BLUE_ACCENT, accent_bar_color=BLUE_ACCENT, font_size=11.8
    )

    add_card(
        s10, 6.80, 1.15, 6.08, 2.55,
        "2. İkili Sınıflandırma & Serbest Üretim",
        [
            ("Semantik Etiketleme: ", "İkili sınıflandırmada 0 / 1 yerine 'True' / 'False' veya 'yes' / 'no' gibi doğal dil etiketleri verilerek çoktan seçmeli gibi skorlanır."),
            ("Serbest Üretim (Free-Form): ", "T5 [RSR+19] ile aynı Beam Search parametreleri: Beam Width B = 4, uzunluk cezası α = 0.6. Metrikler: F1, BLEU veya Exact Match."),
            ("Test vs. Dev Raporlama: ", "Özel (private) test sunucuları için model çok büyük olduğundan SuperGLUE, TriviaQA ve PIQA dışında dev sonuçları raporlanmıştır."),
        ],
        border_color=NAVY_MED, accent_bar_color=NAVY_MED, font_size=11.5
    )

    # Bottom Full-Width Highlight: Unconditional Probability Normalization
    add_card(
        s10, 0.45, 3.88, 12.43, 3.00,
        "3. Kritik İnce Ayar Tekniği: Koşulsuz Olasılık Normalizasyonu (ARC, OpenBookQA, RACE)",
        [
            ("Problem (Prior Bias): ",
             "Dil modeli bir şıkkın olasılığını hesaplarken yalnızca bağlamla uyumunu değil, şıkkın dildeki genel frekansını (prior) da ölçer; nadir ama doğru şık cezalandırılabilir."),
            ("Çözüm (Bayesci PMI Yaklaşımı): ",
             "Geliştirme setinde doğrulanan bu yöntemde her şıkkın koşullu olasılığı, yalnızca jenerik bir yanıt istemi altındaki koşulsuz olasılığına bölünür:"),
        ],
        fill_color=TEAL_LIGHT, border_color=TEAL, accent_bar_color=TEAL, title_color=TEAL, font_size=12.0
    )

    add_formula_box(
        s10, 0.85, 5.45, 11.63, 1.15,
        "Score(completion)  =  P(completion | context)  /  P(completion | answer_context)",
        "Burada  answer_context = 'Answer: '  veya  'A: '  dizisidir  (Bağlamın cevaba sağladığı saf bilgi kazancını izole eder).",
        dark=True, font_size=14.0
    )

    set_notes(s10, """[Slayt 10 - Değerlendirme Metodolojisi | ~1.5 dk]
Section 2.4 değerlendirme metodolojisinin tutarlılığı açısından hayati detaylar içerir:
- Çoktan seçmeli görevlerde her şık için token başına log-olabilirlik (per-token likelihood) karşılaştırılır ki kısa şıklar haksız avantaj kazanmasın.
- Ancak ARC, OpenBookQA ve RACE gibi veri setlerinde bir şık doğası gereği çok nadir kelimeler içerdiği için düşük olasılık alabilmektedir. Yazarlar bunun için tamamlama olasılığını P(completion | answer_context)'e böler (burada answer_context 'Answer: ' veya 'A: ' stringidir). İstatistiksel olarak bu P(y|x)/P(y) yani Pointwise Mutual Information (PMI) benzeri bir düzeltme yaparak bağlamın o cevaba katkısını ölçer.
- Serbest üretimde Beam Search (width=4, length penalty α=0.6) kullanılır.""")

    # =========================================================================
    # SLIDE 11: DENEYSEL DOĞRULAMA: POWER-LAW ÖLÇEKLEME
    # =========================================================================
    s11 = prs.slides.add_slide(blank)
    add_header_footer(s11, "Bölüm 3 • Ölçekleme Yasaları", "Deneysel Doğrulama: Güç Yasası (Power-Law) Ölçekleme", 11,
                      "Section 3 (Figure 3.1) & Section 4 (Figure 4.1): 6 Büyüklük Mertebesinde Kayıp Eğrisi")

    add_formula_box(
        s11, 0.45, 1.08, 12.43, 0.78,
        "L(C) = 2.57 · C^(−0.048)     [C: PetaFLOP/s-gün, L: Cross-Entropy Doğrulama Kaybı]",
        "100K parametreden 175B parametreye (toplam 14 model: 8 ana + 6 ekstra küçük) pürüzsüz güç yasası; gömme (embedding) parametreleri hariç.",
        dark=True, font_size=13.0
    )

    add_picture_fit(s11, "fig3_1_power_law_compute.png", 0.45, 1.98, 6.08, 3.72,
                    "Figure 3.1: Hesaplama gücü (Compute) arttıkça doğrulama kaybındaki güç yasası düşüşü.")
    add_picture_fit(s11, "fig4_1_training_curves.png", 6.80, 1.98, 6.08, 3.72,
                    "Figure 4.1: Tekilleştirilmiş doğrulama vs. eğitim kaybı eğrileri (aşırı uyum/overfitting yok).")

    add_card(
        s11, 0.45, 5.80, 12.43, 1.10,
        "Bilimsel Çıkarım: Düşen Cross-Entropy Kaybı Yüzeysel Ezber Değildir",
        [("Temel Endişe & Yanıt: ",
          "Eğitim/doğrulama makası 175B parametrede bile açılmaz (Fig 4.1). Dahası ilerleyen slaytlarda görüleceği gibi bu pürüzsüz kayıp düşüşü, doğrudan downstream görevlerde somut performans artışlarına dönüşmektedir.")],
        fill_color=BLUE_PALE, border_color=BLUE_ACCENT, accent_bar_color=BLUE_ACCENT, font_size=11.8
    )

    set_notes(s11, """[Slayt 11 - Power-Law Ölçekleme | ~1.5 dk]
Section 3'ün girişindeki Figure 3.1 için yazarlar 8 ana modele ek olarak 100.000 parametreye kadar inen 6 ekstra küçük model daha eğitmiştir. Kaplan et al. (2020) ölçekleme yasasının iki büyüklük mertebesi daha ileri taşındığını ve validation loss'un L = 2.57 * C^(-0.048) eğrisini neredeyse sapmasız takip ettiğini görürüz.
Sağdaki Figure 4.1 ise çok önemli bir şüpheyi ortadan kaldırır: '175 milyar parametreli model eğitim verisini ezberleyip overfit olmuyor mu?' Hayır — tekilleştirilmiş doğrulama (validation) eğrisi ile eğitim (train) eğrisi arasındaki küçük boşluk model büyüdükçe neredeyse hiç genişlememektedir.""")

    # =========================================================================
    # SLIDE 12: DİL MODELLEME, CLOZE VE TAMAMLAMA GÖREVLERİ
    # =========================================================================
    s12 = prs.slides.add_slide(blank)
    add_header_footer(s12, "Bölüm 3 • NLP Sonuçları", "Dil Modelleme, Cloze ve Tamamlama Görevleri (Section 3.1)", 12,
                      "Penn Tree Bank (PTB), LAMBADA, StoryCloze ve HellaSwag")

    add_styled_table(
        s12, 0.45, 1.12, 6.20, 2.05,
        ["Ayar", "PTB (ppl ↓)", "LAMBADA (acc ↑)", "LAMBADA (ppl ↓)", "StoryCloze", "HellaSwag"],
        [
            ["Önceki SOTA", "35.8 (0S)", "68.0", "8.63", "91.8", "85.6"],
            ["GPT-3 Zero-Shot", "20.5", "76.2", "3.00", "83.2", "78.9"],
            ["GPT-3 One-Shot", "—", "72.5", "3.35", "84.7", "78.1"],
            ["GPT-3 Few-Shot", "—", "86.4 (+18.4)", "1.92", "87.7 (K=70)", "79.3 (K=20)"],
        ],
        col_widths=[1.48, 0.90, 1.18, 0.98, 0.85, 0.81],
        font_size=10.0, header_size=9.8, highlight_rows={1: BLUE_PALE, 3: TEAL_LIGHT}
    )

    add_card(
        s12, 0.45, 3.28, 6.20, 3.60,
        "LAMBADA'da Prompt Mühendisliğinin Gücü (Section 3.1.2)",
        [
            ("PTB (Tablo 3.1): ", "Modern internet öncesi derlem olduğu için kirlenme yok; Zero-shot perplexity 35.8 → 20.50 (15 puanlık yeni SOTA). Wikipedia ve 1BW veri setleri tam kirlenme nedeniyle çıkarıldı."),
            ("LAMBADA Sorunu: ", "Standart LM, hedefin 'cümlenin son kelimesi' olduğunu bilmediğinden mantıklı devam kelimelerine olasılık dağıtır."),
            ("Cloze Çerçeveleme (K = 15): ", "'Alice was friends with Bob. Alice went to visit her friend ____. → Bob' formatıyla model 1 kelimelik boşluğu anlar."),
            ("Ölçek Etkisi: ", "Bu format en küçük modelde doğruluğu %20 düşürürken, 175B'de +%10 artırarak %86.4'e çıkarır! (1-shot %72.5 ile format için yetersizdir)."),
        ],
        border_color=TEAL, accent_bar_color=TEAL, font_size=11.0
    )

    add_picture_fit(s12, "fig3_2_lambada.png", 6.82, 1.12, 6.06, 4.10,
                    "Figure 3.2: LAMBADA — GPT-3 2.7B bile 17B Turing-NLG SOTA'sını (%68.0) geçer; 175B FS %86.4.")

    add_card(
        s12, 6.82, 5.34, 6.06, 1.54,
        "HellaSwag & StoryCloze Değerlendirmesi",
        [
            ("HellaSwag (%79.3): ", "Fine-tuned 1.5B LM'yi (%75.4) geçer ancak multi-task ALUM SOTA (%85.6) ve insan (%95.6) altındadır."),
            ("StoryCloze (%87.7): ", "Önceki zero-shot sonuçları ~%10 aşar; fine-tuned BERT SOTA'nın (%91.8) 4.1 puan gerisindedir."),
        ],
        fill_color=CODE_BG, border_color=BORDER_GRAY, font_size=11.0, title_size=12.5
    )

    set_notes(s12, """[Slayt 12 - Dil Modelleme & Cloze | ~1.5 dk]
Section 3.1'de Penn Tree Bank (PTB) modern internet öncesi tarihli olduğu için tamamen temiz bir dil modelleme kıyaslaması sunar; GPT-3 perplexity'yi 35.8'den 20.50'ye düşürerek 15 puanlık yeni SOTA kurar.
LAMBADA ise uzun menzilli bağlam takibini ölçer. Daha önce Bisk et al. (2020), 17B Turing-NLG'nin sadece %1.5 artış getirmesine bakarak 'ölçeklemenin sonuna gelindiğini' savunmuştu. GPT-3 Zero-shot'ta bile %76.2 ile (+%8) bu iddiayı çürütür. Dahası yazarlar görevi Cloze / Fill-in-the-blank formatına çevirdiğinde (K=15), küçük modellerin kafası karışıp performansı %20 düşerken, 175B model kalıbı çözüp %86.4'e (+18.4 puan SOTA!) ulaşır. Figure 3.2'de 2.7B GPT-3'ün bile 17B Turing-NLG'yi geçtiğine dikkat edin.""")

    # =========================================================================
    # SLIDE 13: KAPALI KİTAP SORU CEVAPLAMA (CLOSED-BOOK QA)
    # =========================================================================
    s13 = prs.slides.add_slide(blank)
    add_header_footer(s13, "Bölüm 3 • Bilgi Geri Çağırma", "Kapalı Kitap Soru Cevaplama: Closed-Book QA (Section 3.2)", 13,
                      "Harici Arama (Information Retrieval) ve Fine-Tuning Olmadan Parametrik Hafıza Testi")

    add_styled_table(
        s13, 0.45, 1.12, 6.20, 2.38,
        ["Model / Ayar (Table 3.3)", "NaturalQS", "WebQS", "TriviaQA"],
        [
            ["RAG (Fine-tuned, Open-Domain) [LPP+20]", "44.5", "45.5", "68.0"],
            ["T5-11B + SSM (Fine-tuned, Closed-Book)", "36.6", "44.7", "60.5"],
            ["T5-11B (Fine-tuned, Closed-Book)", "34.5", "37.4", "50.1"],
            ["GPT-3 Zero-Shot (Strict Closed-Book)", "14.6", "14.4", "64.3"],
            ["GPT-3 One-Shot (Strict Closed-Book)", "23.0", "25.3", "68.0"],
            ["GPT-3 Few-Shot (K = 64)", "29.9", "41.5", "71.2 (SOTA)"],
        ],
        col_widths=[3.10, 1.00, 1.00, 1.10],
        font_size=10.5, header_size=10.5, highlight_rows={0: BLUE_PALE, 5: TEAL_LIGHT}
    )

    add_card(
        s13, 0.45, 3.65, 6.20, 3.23,
        "Parametrik Bilgi Kapasitesi ve Dağılım Adaptasyonu",
        [
            ("En Katı Değerlendirme (Strict Closed-Book): ",
             "Ne RAG gibi 21M belgeli/15.3B parametreli yoğun vektör indeksine erişim var, ne de T5-11B gibi QA setinde fine-tuning yapılıyor."),
            ("TriviaQA Zaferi (%71.2): ",
             "Zero-shot (%64.3) bile fine-tuned T5-11B'yi +%14.2 geçer; One-shot (%68.0) Open-Domain SOTA olan RAG'ı yakalar; Few-shot %71.2 ile yeni SOTA olur."),
            ("WebQS & NQs Dağılım Kayması (Distribution Shift): ",
             "WebQS'te 0S (%14.4) → FS (%41.5) sıçraması (+27.1 puan!), modelin soru/cevap stilini bağlam içinde hızla öğrendiğini gösterir. NQs (%29.9) ise Wikipedia'nın çok ince taneli detaylarını sorduğu için kapasite sınırını zorlar."),
        ],
        border_color=TEAL, accent_bar_color=TEAL, font_size=11.2
    )

    add_picture_fit(s13, "fig3_3_triviaqa.png", 6.82, 1.12, 6.06, 4.18,
                    "Figure 3.3: TriviaQA'da parametre sayısı arttıkça modelin ağırlıklarında tuttuğu olgusal bilgi pürüzsüz artar.")

    add_card(
        s13, 6.82, 5.42, 6.06, 1.46,
        "Mimari Çıkarım",
        ["3 QA veri setinin tamamında log-lineer pürüzsüz artış görülür. Bu durum, model kapasitesinin doğrudan ağ parametreleri içinde depolanan 'dünya bilgisi' miktarına çevrildiğini düşündürür."],
        fill_color=BLUE_PALE, border_color=BLUE_ACCENT, font_size=11.5, title_size=12.5
    )

    set_notes(s13, """[Slayt 13 - Closed-Book QA | ~1.5 dk]
Closed-Book QA'de model dışarıdan hiçbir arama motoru kullanmadan kendi ağırlıklarında depoladığı genel kültür bilgisini kullanmak zorundadır. GPT-3'ün ayarı T5-11B'den bile daha katıdır çünkü QA verisi üzerinde fine-tune edilmemiştir.
TriviaQA'da sonuçlar olağanüstüdür: GPT-3 Zero-shot (%64.3) fine-tuned T5-11B'yi (%50.1) 14 puan geçer. One-shot (%68.0) ile 21 milyon Wikipedia belgesi üzerinde arama yapan fine-tuned RAG modelini yakalar; Few-shot'ta %71.2 ile yeni SOTA olur.
WebQuestions'ta Zero-shot (%14.4) çok düşüktür çünkü cevap stili modelin doğal dağılımından farklıdır; ancak 64 örnekle (%41.5) bu stil dağılımına hızla adapte olur.""")

    # =========================================================================
    # SLIDE 14: MAKİNE ÇEVİRİSİ: ÇOK DİLLİLİK VE YÖN ASİMETRİSİ
    # =========================================================================
    s14 = prs.slides.add_slide(blank)
    add_header_footer(s14, "Bölüm 3 • Çok Dillilik", "Makine Çevirisi: Doğal Karışım ve Yön Asimetrisi (Section 3.3)", 14,
                      "Eğitim Verisinin %93'ü İngilizce, %7'si Diğer Diller — Paralel Derlem ve Back-Translation Yok")

    add_styled_table(
        s14, 0.45, 1.12, 6.25, 2.55,
        ["Ayar (Multi-BLEU ↑)", "En→Fr", "Fr→En", "En→De", "De→En", "En→Ro", "Ro→En"],
        [
            ["SOTA (Supervised)", "45.6", "35.0", "41.2", "40.2", "38.5", "39.9"],
            ["Önceki Unsupervised NMT", "37.5", "34.9", "29.8", "35.2", "35.2", "33.1"],
            ["GPT-3 Zero-Shot", "25.2", "21.2", "24.6", "27.2", "14.1", "19.9"],
            ["GPT-3 One-Shot", "28.3", "33.7", "26.2", "30.4", "20.6", "38.6"],
            ["GPT-3 Few-Shot (K=64)", "32.6", "39.2", "29.7", "40.6", "21.0", "39.5"],
        ],
        col_widths=[1.85, 0.73, 0.73, 0.73, 0.73, 0.74, 0.74],
        font_size=10.2, header_size=10.0, highlight_rows={1: CODE_BG, 4: TEAL_LIGHT}
    )

    add_card(
        s14, 0.45, 3.80, 6.25, 3.08,
        "Kritik Bulgular: Tek Örnek Sıçraması ve Yön Asimetrisi",
        [
            ("One-Shot Gücü: ",
             "Zero-shot görece düşükken yalnızca 1 örnek (One-shot) +7 BLEU kazandırır; Few-shot (K=64) ek +4 BLEU ekler."),
            ("X → İngilizce Üstünlüğü (+5 BLEU): ",
             "Fr→En (39.2), De→En (40.6) ve Ro→En (39.5) yönlerinde önceki en iyi Unsupervised NMT modellerini (MASS, XLM, mBART) ortalama 5 BLEU geçer; Ro→En neredeyse 608K etiketli SOTA'ya (39.9) eşittir!"),
            ("İngilizce → X Zayıflığı (BPE Darboğazı): ",
             "En→Ro (21.0) önceki Unsupervised SOTA'nın 14 BLEU gerisindedir. Neden: GPT-2'den miras kalan ve neredeyse tamamen İngilizceye göre eğitilen Byte-Level BPE tokenizer'ın diğer dilleri verimsiz parçalaması."),
        ],
        border_color=AMBER, accent_bar_color=AMBER, font_size=11.0
    )

    add_picture_fit(s14, "fig3_4_translation.png", 6.88, 1.12, 6.00, 4.25,
                    "Figure 3.4: 6 dil çiftinde Few-Shot çeviri ölçeklemesi (Düz çizgiler X→En, kesikli çizgiler En→X).")

    add_card(
        s14, 6.88, 5.48, 6.00, 1.40,
        "Veri Karışımının Doğal Etkisi",
        ["GPT-2 İngilizce dışındaki metinleri filtrelemişti (sadece 10 MB Fransızca). GPT-3 ham Common Crawl'da %7 diğer dilleri doğal karışım olarak tuttu ve tek bir next-token hedefiyle çeviriyi çözdü."],
        fill_color=BLUE_PALE, border_color=BLUE_ACCENT, font_size=11.0, title_size=12.0
    )

    set_notes(s14, """[Slayt 14 - Makine Çevirisi | ~1.5 dk]
GPT-3'ün eğitim verisi kelime bazında %93 İngilizce, yalnızca %7 diğer dillerdir ve hiçbir özel paralel çeviri hedefi veya back-translation kullanılmamıştır.
Table 3.4'te çok net iki örüntü görüyoruz:
1) Zero-shot düşük kalsa da One-shot tek örnekle ortalama +7 BLEU sıçrama yapar.
2) Çok keskin bir yön asimetrisi vardır: Yabancı dilden İngilizceye çeviride (Fr→En 39.2, De→En 40.6, Ro→En 39.5) önceki tüm Unsupervised NMT SOTA'larını (MASS, XLM, mBART) yaklaşık 5 BLEU geçer. Ancak İngilizceden diğer dillere (özellikle En→Ro 21.0) çeviride ciddi düşüş yaşar. Yazarlar bunu %93 İngilizce veri oranına ve GPT-2'den devralınan İngilizce-merkezli Byte-Level BPE tokenizer'ın diğer dilleri aşırı bölmesine bağlar.""")

    # =========================================================================
    # SLIDE 15: WINOGRAD, SAĞDUYU ÇIKARIMI VE OKUDUĞUNU ANLAMA
    # =========================================================================
    s15 = prs.slides.add_slide(blank)
    add_header_footer(s15, "Bölüm 3 • Muhakeme & Okuma", "Winograd, Sağduyu Çıkarımı ve Okuduğunu Anlama (Sections 3.4–3.6)", 15,
                      "Zamir Çözümleme, Fiziksel/Bilimsel Sağduyu ve 5 Farklı Okuma Formatı Karşılaştırması")

    add_card(
        s15, 0.45, 1.12, 6.20, 2.20,
        "Winograd & Sağduyu Çıkarımı (Tables 3.5 & 3.6)",
        [
            ("Winograd (WSC273): ", "Partial evaluation ile 0S %88.3*, 1S %89.7*, FS %88.6* (SOTA: %90.1; kirlenme notu *)."),
            ("Winogrande (Adversarial): ", "0S %70.2 → 1S %73.2 → FS %77.7 (Fine-tuned RoBERTa %79, T5 SOTA %84.6, İnsan %94.0)."),
            ("PIQA (Fiziksel Sağduyu): ", "FS %82.8* (test server) ile fine-tuned RoBERTa SOTA'yı (%79.4) geçer (kirlenme *)."),
            ("ARC & OpenBookQA: ", "ARC-Easy %70.1 (RoBERTa'yı geçer), ARC-Challenge %51.5 (UnifiedQA SOTA %78.5 gerisinde); OpenBookQA 0S %57.6 → FS %65.4."),
        ],
        border_color=BLUE_ACCENT, accent_bar_color=BLUE_ACCENT, font_size=10.8
    )

    add_styled_table(
        s15, 0.45, 3.44, 6.20, 2.25,
        ["Okuma Görevi (Table 3.7)", "Metrik", "FT SOTA", "0-Shot", "1-Shot", "Few-Shot"],
        [
            ["CoQA (Serbest Diyalog)", "F1", "90.7", "81.5", "84.0", "85.0"],
            ["SQuAD 2.0 (Span + Cevapsız)", "F1", "93.0", "59.5", "65.4", "69.8"],
            ["QuAC (Yapısal Diyalog)", "F1", "74.4", "41.5", "43.3", "44.3"],
            ["DROP (Ayrık Sayısal Muh.)", "F1", "89.1", "23.6", "34.3", "36.5"],
            ["RACE-h (Lise Çoktan Seç.)", "Acc", "90.0", "45.5", "45.9", "46.8"],
            ["RACE-m (Ortaokul)", "Acc", "93.1", "58.4", "57.4", "58.1"],
        ],
        col_widths=[2.25, 0.65, 0.85, 0.80, 0.80, 0.85],
        font_size=10.0, header_size=10.0, highlight_rows={0: TEAL_LIGHT, 2: CRIMSON_LIGHT, 4: CRIMSON_LIGHT}
    )

    add_card(
        s15, 0.45, 5.80, 6.20, 1.08,
        "Format Farklılığının Etkisi",
        ["GPT-3 serbest diyaloglu CoQA'da (85.0 F1, insan sınırına ~3 puan yakın) çok güçlü iken; yapısal öğretmen-öğrenci diyaloğu (QuAC) ve çoktan seçmeli sınav formatında (RACE) SOTA'nın ~30–45 puan gerisindedir."],
        fill_color=AMBER_LIGHT, border_color=AMBER, font_size=10.8, title_size=11.8
    )

    add_picture_fit(s15, "fig3_5_winogrande.png", 6.82, 1.12, 6.06, 2.82,
                    "Figure 3.5: Winogrande üzerinde ölçekle birlikte artan Few-Shot kazancı (%77.7).")
    add_picture_fit(s15, "fig3_7_coqa.png", 6.82, 4.04, 6.06, 2.84,
                    "Figure 3.7: CoQA'da 175B Few-Shot (85.0 F1) insan performansına çok yaklaşır.")

    set_notes(s15, """[Slayt 15 - Winograd, Sağduyu & Okuduğunu Anlama | ~1.5 dk]
Sections 3.4–3.6 üç farklı muhakeme alanını kapsar:
- Winograd'da %88.6* ve zorlu adversarially-mined Winogrande'de %77.7 ile fine-tuned RoBERTa-Large (%79) seviyesine yaklaşır (Figure 3.5).
- Sağduyu muhakemesinde PIQA'da %82.8* ile yeni SOTA skoruna ulaşsa da olası kirlenme nedeniyle yıldızla işaretlenmiştir; ARC ve OpenBookQA'da ise UnifiedQA gibi çoklu-görev fine-tuned modellerin 20–27 puan gerisindedir.
- Okuduğunu anlamada (Table 3.7) çarpıcı bir format duyarlılığı görürüz: Serbest diyaloglu CoQA'da 85.0 F1 ile insan seviyesine (~88.3) çok yaklaşır (Figure 3.7). Ancak yapısal diyaloglu QuAC (44.3 F1, ELMo'nun bile 13 puan gerisi) ve çoktan seçmeli sınav RACE'te (46.8% — SOTA %90) çok zayıf kalır; bunun mimari kök nedenini Bölüm 5'te inceleyeceğiz.""")

    # =========================================================================
    # SLIDE 16: SUPERGLUE VE DOĞAL DİL ÇIKARIMI (NLI / ANLI)
    # =========================================================================
    s16 = prs.slides.add_slide(blank)
    add_header_footer(s16, "Bölüm 3 • SuperGLUE & NLI", "SuperGLUE ve Doğal Dil Çıkarımı (Sections 3.7 & 3.8)", 16,
                      "8 Örnekle Fine-Tuned BERT-Large'ı Geçme vs. İki Cümle Karşılaştırma Darboğazı (WiC & ANLI)")

    add_styled_table(
        s16, 0.45, 1.12, 6.18, 2.85,
        ["SuperGLUE Görevi (Table 3.8)", "FT SOTA", "FT BERT-Large", "GPT-3 FS (K=32)"],
        [
            ["SuperGLUE Ortalama (Test)", "89.0", "69.0", "71.8 (Dev: 73.2)"],
            ["COPA (Nedensel Seçim)", "94.8", "70.6", "92.0 (2. sıra!)"],
            ["ReCoRD (Okuma Acc / F1)", "92.5 / 93.3", "71.3 / 72.0", "90.2 / 91.1"],
            ["WSC (Zamir Çözümleme)", "93.8", "64.6", "80.1"],
            ["BoolQ / RTE (Acc)", "91.0 / 92.5", "77.4 / 71.7", "76.4 / 69.0"],
            ["CB (Acc / F1)", "96.9 / 93.9", "83.6 / 75.7", "75.6 / 52.0"],
            ["MultiRC (Acc / F1a)", "62.3 / 88.2", "24.1 / 70.0", "30.5 / 75.4"],
            ["WiC (Kelime Anlamı Acc)", "76.1", "69.6", "49.4 (Rastgele!)"],
        ],
        col_widths=[2.38, 1.05, 1.25, 1.50],
        font_size=10.0, header_size=10.0, highlight_rows={0: BLUE_PALE, 1: TEAL_LIGHT, 2: TEAL_LIGHT, 7: CRIMSON_LIGHT}
    )

    add_card(
        s16, 0.45, 4.10, 6.18, 2.78,
        "Veri Verimliliği ve Yapısal Sinyal",
        [
            ("K < 8 Örnekle BERT-Large'ı Geçiş (Fig 3.8): ",
             "BERT-Large 125.000 örnekle fine-tune edilirken (69.0), GPT-3 bağlamda 8'den az örnekle bunu aşar; BERT++ (630K örnek) farkı 1S vs 8S farkına denktir."),
            ("Kritik Zayıflık — İki Cümle Karşılaştırma: ",
             "Aynı kelimenin iki cümledeki anlamını kıyaslayan WiC (%49.4) tüm prompt denemelerine rağmen rastgele tahminde kalır."),
            ("Adversarial NLI (ANLI R3 — Fig 3.9): ",
             "13B dahil tüm küçük modeller rastgele tahmin (%33) civarındayken, yalnızca 175B model few-shot'ta %40.2 ile 'yaşam belirtisi' gösterir."),
        ],
        border_color=CRIMSON, accent_bar_color=CRIMSON, title_color=CRIMSON, font_size=11.0
    )

    add_picture_fit(s16, "fig3_8_superglue.png", 6.80, 1.12, 6.08, 2.82,
                    "Figure 3.8: SuperGLUE'da model boyutu (sol) ve örnek sayısı K (sağ) ile artış.")
    add_picture_fit(s16, "fig3_9_anli.png", 6.80, 4.04, 6.08, 2.84,
                    "Figure 3.9: ANLI Round 3 — 13B'ye kadar %33 rastgele tahmin, 175B'de %40.2 sıçrama.")

    set_notes(s16, """[Slayt 16 - SuperGLUE & NLI | ~1.5 dk]
SuperGLUE (Table 3.8), 8 zorlu dil anlama görevinden oluşur. GPT-3 (K=32), 8 görevin 4'ünde 125.000 örnekle fine-tune edilmiş BERT-Large'ı geçer ve ortalama 71.8 (dev setinde 73.2) alır. Figure 3.8'in sağ panelinde görüldüğü üzere GPT-3 yalnızca 8 örnekle BERT-Large'ı yakalayıp geçmektedir. COPA (%92.0) ve ReCoRD (91.1 F1) ise fine-tuned T5-11B SOTA'sına birkaç puan mesafededir.
Ancak burada makalenin en önemli yapısal teşhisi ortaya çıkar: WiC görevinde GPT-3 %49.4 ile yazı-tura (random chance) seviyesindedir! Benzer biçimde cümle çiftlerini kıyaslayan RTE (%69.0) ve ANLI'da da zorlanır; Figure 3.9'da ANLI Round 3'te 13B dahil tüm küçük modeller %33 rastgele tahminde kalırken, ilk kez 175B model %40.2'ye çıkar.""")

    # =========================================================================
    # SLIDE 17: SENTETİK GÖREVLER I: ARİTMETİK
    # =========================================================================
    s17 = prs.slides.add_slide(blank)
    add_header_footer(s17, "Bölüm 4 • Sentetik Muhakeme", "Sentetik Görevler I: Anlık Hesaplama ve Aritmetik (Section 3.9.1)", 17,
                      "10 Aritmetik Görevi (Her Biri 2.000 Rastgele Soru) — 13B → 175B Sıçraması ve Ezber Kontrolü")

    add_styled_table(
        s17, 0.45, 1.12, 6.30, 2.25,
        ["Ayar (Table 3.9)", "2D+", "2D-", "3D+", "3D-", "4D+", "4D-", "5D+", "5D-", "2Dx", "1DC"],
        [
            ["GPT-3 Zero-Shot", "76.9", "58.0", "34.2", "48.3", "4.0", "7.5", "0.7", "0.8", "19.8", "9.8"],
            ["GPT-3 One-Shot", "99.6", "86.4", "65.5", "78.7", "14.0", "14.0", "3.5", "3.8", "27.4", "14.3"],
            ["GPT-3 Few-Shot", "100.0", "98.9", "80.4", "94.2", "25.5", "26.8", "9.3", "9.9", "29.2", "21.3"],
        ],
        col_widths=[1.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48],
        font_size=9.5, header_size=9.5, highlight_rows={2: TEAL_LIGHT}
    )

    add_card(
        s17, 0.45, 3.50, 6.30, 3.38,
        "Ezber mi, Gerçek Hesaplama mı? (Spot-Check Analizi)",
        [
            ("13B → 175B Faz Geçişi (Fig 3.10): ",
             "13B model 2D+/2D-'de bile ~%52–56'da kalıp diğerlerinde <%10 alırken, 175B model 2 basamakta ~%100, 3D-'de %94.2, 2Dx çarpmada %29.2 ve 1DC parantezli işlemde '9*(7+5)' %21.3 başarır."),
            ("Eğitim Verisi Taraması (3-Basamaklılar): ",
             "2.000 test sorusunun tamamı '<NUM1> + <NUM2> =' ve '<NUM1> plus <NUM2>' kalıplarıyla eğitim verisinde aranmıştır."),
            ("Sonuç — İhmal Edilebilir Çakışma: ",
             "Toplamada sadece 17 eşleşme (%0.8), çıkarmada yalnızca 2 eşleşme (%0.1) bulunmuştur!"),
            ("Hata Anatomisi Kanıtı: ",
             "Yanlış yanıtların çoğunlukla 'elde var 1' (carrying a 1) hatasından kaynaklanması, modelin tablo ezberlemediğini, hesaplama algoritması yürüttüğünü kanıtlar."),
        ],
        border_color=TEAL, accent_bar_color=TEAL, font_size=11.0
    )

    add_picture_fit(s17, "fig3_10_arithmetic.png", 6.92, 1.12, 5.96, 4.15,
                    "Figure 3.10: 10 aritmetik görevinde 13B'den 175B'ye keskin yetenek sıçraması.")

    add_card(
        s17, 6.92, 5.38, 5.96, 1.50,
        "Neden 4–5 Basamakta Düşüş Yaşanıyor?",
        ["Model ara çalışma belleği (scratchpad / Chain-of-Thought) olmadan her cevabı tek bir ileri besleme (forward pass) adımında üretmek zorundadır; basamak sayısı arttıkça eldeli taşıma (carry) kapasitesi aşılır."],
        fill_color=AMBER_LIGHT, border_color=AMBER, title_color=AMBER, font_size=11.0, title_size=12.0
    )

    set_notes(s17, """[Slayt 17 - Sentetik Görevler: Aritmetik | ~2 dk]
Section 3.9.1, modelin ön-eğitimde görmüş olamayacağı görevleri test eder. Her biri 2.000 rastgele sorudan oluşan 10 aritmetik görevi hazırlanır.
Figure 3.10'da ML tarihinde meşhur olan o keskin sıçramayı görürsünüz: 13B model 2 basamakta %55'lerde, 3+ basamakta neredeyse %0-10 bandında sıkışırken, 175B model 2D+'da %100, 3D-'de %94.2, 2 basamaklı çarpmada %29.2 ve parantezli işlemde %21.3'e fırlar.
'Acaba bunları internetten ezberlemiş olabilir mi?' sorusuna yazarlar çok titiz bir spot-check ile cevap verir: 2.000 adet 3 basamaklı test sorusunu hem `+` hem `plus` formatıyla tüm eğitim derleminde ararlar ve toplamada yalnızca 17 (%0.8), çıkarmada yalnızca 2 (%0.1) eşleşme bulurlar. Üstelik yanlış cevapların 'elde var 1'i (carry) unutmaktan kaynaklanması, modelin gerçekten hesaplama yapmaya çalıştığını kanıtlar.""")

    # =========================================================================
    # SLIDE 18: SENTETİK GÖREVLER II: WORD SCRAMBLING VE SAT ANALOJİLERİ
    # =========================================================================
    s18 = prs.slides.add_slide(blank)
    add_header_footer(s18, "Bölüm 4 • Sembolik Manipülasyon", "Sembolik Karakter Manipülasyonu ve SAT Analojileri (Sections 3.9.2–3.9.3)", 18,
                      "10.000 Sık Kelime (4 < uzunluk < 15), K = 100 Örnek — BPE Alt-Yapı Çözümlemesi")

    add_styled_table(
        s18, 0.45, 1.12, 6.25, 2.75,
        ["Görev (Table 3.10)", "Örnek Dönüşüm", "0S", "1S", "FS"],
        [
            ["Random Insertion (RI)", "s.u!c/c!e.s s i/o/n → succession", "8.26", "45.4", "67.2"],
            ["Anagrams 2 (A2, ilk/son 2 sabit)", "opoepnnt → opponent", "8.91", "25.9", "39.7"],
            ["Cycle Letters (CL)", "lyinevitab → inevitably", "3.66", "21.7", "37.9"],
            ["Anagrams 1 (A1, ilk/son 1 sabit)", "criroptuon → corruption", "2.28", "8.62", "15.1"],
            ["Reversed Words (RW)", "stcejbo → objects", "0.09", "0.48", "0.44"],
        ],
        col_widths=[1.88, 2.38, 0.65, 0.67, 0.67],
        font_size=10.0, header_size=10.0, highlight_rows={0: TEAL_LIGHT, 4: CRIMSON_LIGHT}
    )

    add_card(
        s18, 0.45, 3.98, 6.25, 2.90,
        "Neden Bilimsel Açıdan Çok Önemli?",
        [
            ("Test Anında Gerçek Öğrenme: ",
             "Zero-shot'ta neredeyse %0 olan bu yapay görevlerin Few-shot'ta %67.2'ye (RI) çıkması, modelin kuralı bağlamdan çıkardığını gösterir."),
            ("BPE Alt-Yapısını (Substructure) Çözme: ",
             "BPE tokenizer ortalama ~0.7 kelime/token üretir; yani model harfleri değil alt-kelime tokenlarını görür. Bunu çözmek tokenların iç harf yapısını ayrıştırmayı ve CL/A1/A2 gibi bijektif olmayan (non-bijective) görevlerde arama (search) yapmayı gerektirir."),
            ("SAT Analojileri (374 Soru, Section 3.9.3): ",
             "0S %53.7 → 1S %59.1 → FS %65.2 (Üniversite adayları ortalaması: %57.0, rastgele tahmin: %20)."),
        ],
        border_color=BLUE_ACCENT, accent_bar_color=BLUE_ACCENT, font_size=11.0
    )

    add_picture_fit(s18, "fig3_11_wordscramble.png", 6.88, 1.12, 6.00, 2.82,
                    "Figure 3.11: Word Scrambling görevlerinde 175B Few-Shot sıçraması (RW hariç).")
    add_picture_fit(s18, "fig3_12_sat_analogies.png", 6.88, 4.04, 6.00, 2.84,
                    "Figure 3.12: SAT Analojilerinde 175B modelin %65.2 ile insan ortalamasını (%57) aşması.")

    set_notes(s18, """[Slayt 18 - Word Scrambling & SAT | ~1.5 dk]
Section 3.9.2 karakter manipülasyonunu test eder. En sık kullanılan 10.000 kelimede (4-15 harf) 5 görev tanımlanır.
Zero-shot'ta model bu görevleri neredeyse hiç yapamaz (%0–8), ancak K=100 örnekle Random Insertion'da %67.2, Anagrams-2'de %39.7 ve Cycle Letters'ta %37.9'a çıkar. Burada iki derin nokta var: 1) Byte-level BPE kelimeleri bütün olarak değil parçalar halinde tokenlaştırdığı için model aslında token alt-yapısını söküp birleştirme ve bijektif olmayan anagramlarda arama yapmaktadır. 2) Ancak 'Reversed Words' (kelimeyi tersten yazma) görevinde %0.44 ile tamamen başarısız olur — çünkü BPE tokenları soldan sağa okunur ve geriye doğru karakter çevrimi tek forward pass'te neredeyse imkânsızdır.
Alttaki Figure 3.12'de ise 2005 öncesi 374 SAT analoji sorusunda Few-Shot GPT-3 %65.2 alarak üniversiteye başvuran öğrencilerin ortalaması olan %57'yi geçmiştir.""")

    # =========================================================================
    # SLIDE 19: NİTELİKSEL YETENEKLER & SENTETİK HABER ÜRETİMİ
    # =========================================================================
    s19 = prs.slides.add_slide(blank)
    add_header_footer(s19, "Bölüm 4 • Niteliksel Yetenekler", "Yeni Kelime Öğrenme, Gramer ve Sentetik Haber Üretimi (Sections 3.9.4–3.9.6)", 19,
                      "Gelişimsel Dilbilim Testi, Gramer Düzeltme ve 621 Katılımcılı İnsan Ayırt Etme Deneyi")

    add_picture_fit(s19, "fig3_16_novel_words.png", 0.45, 1.12, 6.05, 3.30,
                    "Figure 3.16: Tek seferlik tanımla uydurma kelimeleri çekimleyip cümlede kullanma (Carey & Bartlett, 1978).")

    add_card(
        s19, 0.45, 4.54, 6.05, 2.34,
        "Gelişimsel Dilbilim & Gramer Düzeltme",
        [
            ("Novel Words (Section 3.9.5): ",
             "'whatpu', 'farduddle', 'Gigamuru', 'screeg' gibi var olmayan kelimeleri tek tanımla öğrenip doğru morfolojik çekimle ('We screeghed at each other...') cümle içinde kullanır."),
            ("Gramer Düzeltme (Figure 3.17): ",
             "Tek örnekle 'Poor/Good English' düzeltmesi yapar; ancak 'cheap' kelimesini silmek gibi anlamsal varsayım hataları da üretebilir."),
        ],
        border_color=TEAL, accent_bar_color=TEAL, font_size=11.0
    )

    add_picture_fit(s19, "fig3_13_human_news_detection.png", 6.68, 1.12, 6.20, 3.10,
                    "Figure 3.13: Model büyüdükçe insanların sentetik haberleri tespit etme doğruluğu %52'ye düşer.")

    add_styled_table(
        s19, 6.68, 4.32, 6.20, 1.44,
        ["Haber Deneyi (Tables 3.11 & 3.12)", "Ortalama Doğruluk", "%95 GA", "p-değeri (vs Kontrol)"],
        [
            ["Kontrol (160M, Bağlamsız, ~200w / ~500w)", "%86 / %88", "%83–90 / %84–91", "—"],
            ["GPT-3 Small (125M, ~200w)", "%76", "%72–80", "2 × 10⁻⁴"],
            ["GPT-3 13B (~200w)", "%55", "%52–58", "1 × 10⁻³²"],
            ["GPT-3 175B (~200w / ~500w Reuters)", "%52 / %52", "%49–54 / %48–57", "1e-34 / 3.2e-23"],
        ],
        col_widths=[2.75, 1.15, 1.25, 1.05],
        font_size=9.8, header_size=9.8, highlight_rows={3: CRIMSON_LIGHT}
    )

    add_card(
        s19, 6.68, 5.86, 6.20, 1.02,
        "Deney Tasarımı & Süre Paradoksu (Appendix E)",
        ["Katılımcılar model büyüdükçe makalelere daha uzun süre harcamasına rağmen (Fig E.1), 175B haberlerde yazı-tura sınırından (%50) istatistiksel olarak farksız (%52) kalır."],
        fill_color=BLUE_PALE, border_color=BLUE_ACCENT, font_size=10.5, title_size=11.5
    )

    set_notes(s19, """[Slayt 19 - Niteliksel Yetenekler & Haber Üretimi | ~1.5 dk]
Sol üstte (Figure 3.16), gelişimsel dilbilimde çocukların kelime öğrenme hızını ölçen testin uyarlamasını görüyoruz: Modele 'screeg' diye uydurma bir fiilin tanımı veriliyor ve GPT-3 bunu İngilizce geçmiş zaman çekimiyle 'We screeghed at each other...' şeklinde doğru kullanıyor.
Sağda ise makalenin en çarpıcı deneylerinden biri var (Section 3.9.4 & Appendix E): 621 ABD'li katılımcıya başlık ve alt başlıklardan üretilmiş ~200 kelimelik (newser.com) ve ~500 kelimelik (Reuters) gerçek/sentetik haberler soruluyor. Kasıtlı kötü 160M kontrol modelinde insanlar %86–88 başarıyla sahte haberi yakalarken, model boyutu büyüdükçe tespit doğruluğu güç yasasıyla düşüyor ve GPT-3 175B'de hem 200 hem 500 kelimelik makalelerde %52'ye iniyor! Katılımcılar daha uzun okuma süresi harcadığı halde (Figure E.1) ayırt edemiyor; tek ipucu zaman zaman ortaya çıkan olgusal hatalar.""")

    # =========================================================================
    # SLIDE 20: BENCHMARK VERİ KİRLENMESİ (CONTAMINATION) ANALİZİ
    # =========================================================================
    s20 = prs.slides.add_slide(blank)
    add_header_footer(s20, "Bölüm 5 • Metodoloji & Güvenilirlik", "Benchmark Veri Kirlenmesi (Data Contamination) Analizi (Section 4)", 20,
                      "İnternet Ölçekli Eğitim Verisinde Test Seti Sızıntısını Ölçmek İçin Spark N-Gram Protokolü")

    add_card(
        s20, 0.45, 1.12, 5.50, 2.75,
        "Problem: Eğitim Öncesi Filtreleme Hatası (Bug)",
        [
            ("Ön Filtreleme Girişimi: ",
             "Eğitim öncesi benchmark'larla 13-gram çakışmaları ve ±200 karakterlik pencereler silinmeye çalışıldı."),
            ("Yazılım Hatası (Bug): ",
             "Appendix C'deki filtreleme uzun belgelerde (kitaplar vb.) kısmen başarısız oldu; ancak 3,640 PF-days maliyet nedeniyle modeli yeniden eğitmek imkânsızdı."),
            ("Çözüm (Post-Hoc Teşhis): ",
             "Apache Spark kullanılarak tüm eğitim derlemi (Common Crawl'un eğitilmeyen %60'ı dahil!) ile test setleri arasında tam N-gram çakışmaları hesaplandı."),
        ],
        border_color=AMBER, accent_bar_color=AMBER, title_color=AMBER, font_size=11.3
    )

    add_card(
        s20, 0.45, 4.00, 5.50, 2.88,
        "Temiz Alt Küme (Clean Subset) Metodolojisi",
        [
            ("N Seçimi: ", "Her görev için örnek uzunluğunun 5. yüzdelik değeri alınır: N = clip(P₅, min=8, max=13); sentetik kısa kelimelerde N = 2."),
            ("Dirty vs. Clean Tanımı: ", "Eğitim derleminde tek bir N-gram çakışması bile varsa 'Dirty', hiç yoksa 'Clean' olarak ayrılır."),
            ("Değerlendirme Kriteri: ", "Δ = (Score_clean − Score_all) / Score_all. Eğer Clean skor belirgin biçimde düşükse ezberleme/şişirme şüphesi doğar."),
        ],
        border_color=BLUE_ACCENT, accent_bar_color=BLUE_ACCENT, font_size=11.3
    )

    add_picture_fit(s20, "fig4_2_contamination.png", 6.12, 1.12, 6.76, 3.70,
                    "Figure 4.2: Temiz veri yüzdesi (x) vs. Sadece temiz alt kümede performans farkı (y).")

    add_card(
        s20, 6.12, 4.95, 6.76, 1.93,
        "Figure 4.2'den Çıkan Ana İstatistiksel Sonuç",
        [
            ("• Çeyrekler Üstü Çakışma, Sıfıra Yakın Etki: ",
             "Benchmarkların dörtte birinde potansiyel kirlenme >%50 görünse de performans değişimi neredeyse her yerde %0 civarındadır."),
            ("• Korelasyon Yokluğu: ",
             "Kirlenme düzeyi ile performans farkı arasında sistematik bir korelasyon bulunmamıştır; yalnızca 6 grup derin incelemeye alınmıştır."),
        ],
        fill_color=TEAL_LIGHT, border_color=TEAL, accent_bar_color=TEAL, title_color=TEAL, font_size=11.5
    )

    set_notes(s20, """[Slayt 20 - Veri Kirlenmesi Metodolojisi | ~1.5 dk]
Section 4 bu makaleyi klasik bir mühendislik raporundan birinci sınıf bir bilimsel çalışmaya dönüştüren kısımdır. İnternetten toplanan 45 TB'lık veride benchmark sorularının eğitim setine sızması çok doğaldır. Yazarlar başta 13-gram temizliği yapmaya çalışsa da uzun belgelerde (özellikle kitaplarda) bir kod hatası (bug) yüzünden bazı çakışmalar kalır. Maliyet nedeniyle yeniden eğitim yapılamadığı için Spark ile tam (probabilistic bloom filter değil, exact!) N-gram çakışma analizi yaparlar.
Figure 4.2'de x-ekseni veri setinin ne kadarının kesinlikle temiz olduğunu, y-ekseni ise sadece temiz örneklerde test edildiğinde skorun ne kadar değiştiğini gösterir. Noktaların ezici çoğunluğu %0 yatay çizgisi üzerinde toplanmıştır.""")

    # =========================================================================
    # SLIDE 21: KİRLENME BULGULARI: YANLIŞ POZİTİFLER VS GERÇEK SIZINTILAR
    # =========================================================================
    s21 = prs.slides.add_slide(blank)
    add_header_footer(s21, "Bölüm 5 • Kirlenme Bulguları", "Kirlenme Analizi Bulguları: Yanlış Pozitifler vs. Gerçek Sızıntılar", 21,
                      "Section 4 & Table C.1: İncelenen 6 Kritik Görev Grubunun Teşhis Sonuçları")

    add_card(
        s21, 0.45, 1.12, 5.80, 1.35,
        "1. Yüksek Yanlış Pozitif: Reading Comprehension",
        ["QuAC (%99 dirty), SQuADv2 (%94 dirty) ve DROP (%93 dirty) görülse de manuel incelemede eğitimde yalnızca kaynak Wikipedia pasajlarının bulunduğu, soru-cevap çiftlerinin OLMADIĞI doğrulandı."],
        fill_color=BLUE_PALE, border_color=BLUE_ACCENT, accent_bar_color=BLUE_ACCENT, font_size=10.8, title_size=12.0
    )
    add_card(
        s21, 0.45, 2.57, 5.80, 1.35,
        "2. Tamamen Rapor Dışı Bırakılanlar (Omitted)",
        ["GPT-2'deki 4 Wikipedia LM benchmarkı ve Children's Book Test neredeyse %100 eğitim verisinde çıktığı için temiz alt küme çıkarılamadı ve raporlanmadı (yerine PTB kullanıldı)."],
        fill_color=CRIMSON_LIGHT, border_color=CRIMSON, accent_bar_color=CRIMSON, title_color=CRIMSON, font_size=10.8, title_size=12.0
    )
    add_card(
        s21, 0.45, 4.02, 5.80, 1.50,
        "3. Yıldız (*) ile İşaretlenenler: Winograd & PIQA",
        ["Winograd: %45 çakışma, 132 şema eğitimde (farklı formatta) mevcut, temiz kümede -%2.6 fark.\nPIQA: %29 çakışma, temiz kümede -%3/-%4 düşüş (ancak 25x küçük modelde de benzer düşüş var: istatistiksel zorluk yanlılığı şüphesi)."],
        fill_color=AMBER_LIGHT, border_color=AMBER, accent_bar_color=AMBER, title_color=AMBER, font_size=10.5, title_size=12.0
    )
    add_card(
        s21, 0.45, 5.62, 5.80, 1.26,
        "4. LAMBADA, Çeviri & Scrambling",
        ["LAMBADA (%43 çakışma): Clean vs All farkı <%0.5 ve fill-in-the-blank ezberi önler. De↔En (%25 çakışma): Yalnızca tek dilli haber eşleşmeleri. Reversed Words/Anagrams: Palindrom ('kayak=kayak') kaynaklı sahte eşleşmeler."],
        fill_color=TEAL_LIGHT, border_color=TEAL, accent_bar_color=TEAL, title_color=TEAL, font_size=10.5, title_size=12.0
    )

    add_styled_table(
        s21, 6.45, 1.12, 6.43, 5.76,
        ["Benchmark (Table C.1)", "N", "Toplam", "Clean %", "Dirty Skor", "Clean Skor", "Fark"],
        [
            ["QuAC (dev f1)", "13", "7353", "%1", "44.3", "54.1", "+%20*"],
            ["SQuADv2 (dev f1)", "13", "11873", "%6", "69.9", "68.4", "-%2"],
            ["DROP (dev f1)", "13", "9536", "%7", "37.0", "29.5", "-%21*"],
            ["CoQA (dev f1)", "13", "7983", "%36", "85.3", "87.1", "+%1"],
            ["Winograd (test acc)*", "9", "273", "%40", "90.2", "86.2", "-%3*"],
            ["LAMBADA (test acc)", "13", "5153", "%57", "86.9", "86.0", "%0"],
            ["PIQA (dev acc)*", "8", "1838", "%71", "89.9", "79.3", "-%4*"],
            ["De→En 16 (bleu-sb)", "12", "2999", "%75", "47.4", "40.8", "-%5"],
            ["WebQs (test acc)", "8", "2032", "%79", "41.6", "41.5", "%0"],
            ["TriviaQA (dev acc)", "10", "7993", "%83", "70.8", "71.3", "%0"],
            ["OpenBookQA (test acc)", "8", "500", "%94", "58.1", "65.9", "+%1"],
            ["HellaSwag (dev acc)", "13", "10042", "%98", "86.2", "79.2", "%0"],
            ["Winogrande (dev acc)", "13", "1267", "%100", "—", "77.7", "%0"],
        ],
        col_widths=[1.88, 0.45, 0.72, 0.72, 0.90, 0.90, 0.86],
        font_size=10.0, header_size=10.0, highlight_rows={4: AMBER_LIGHT, 6: AMBER_LIGHT, 5: TEAL_LIGHT, 9: TEAL_LIGHT}
    )

    set_notes(s21, """[Slayt 21 - Kirlenme Bulguları | ~1.5 dk]
Table C.1'deki seçilmiş veri setlerini incelediğimizde çok net bir tablo çıkar:
- QuAC (%1 clean), SQuADv2 (%6 clean) ve DROP (%7 clean) korkutucu görünse de, yapılan manuel denetimde eğitim verisinde yalnızca okuma parçası olan Wikipedia makalelerinin geçtiği, soru ve cevapların yer almadığı kanıtlanmıştır. (Zaten test anında metin prompt içinde verildiği için bu bir kopya değildir).
- 4 Wikipedia dil modelleme testi ve Children's Book Test ise tamamen eğitim verisinde bulunduğu için makaleden çıkarılmıştır.
- Yalnızca Winograd (132 şema eğitimde mevcut, -%2.6 fark) ve PIQA (-%3/-%4 fark) yıldız (*) ile işaretlenmiştir. İlginç bir şekilde PIQA'daki %4'lük fark 25 kat küçük modelde de görüldüğü için yazarlar bunun ezberden ziyade internetten kopyalanan örneklerin doğası gereği daha kolay olmasından kaynaklandığından şüphelenir.
- LAMBADA'da temiz ve kirli skorlar (%86.0 vs %86.9) %0.5 içindedir ve Winogrande %100 temizdir.""")

    # =========================================================================
    # SLIDE 22: MİMARİ SINIRLILIKLAR I: OTOREGRESİF DİKKAT DARBOĞAZI
    # =========================================================================
    s22 = prs.slides.add_slide(blank)
    add_header_footer(s22, "Bölüm 5 • Sınırlılıklar I", "Teknik ve Mimari Sınırlılıklar: Otoregresif Tek Yönlü Kısıt (Section 5)", 22,
                      "Metin Sentezi Zayıflıkları, Sağduyu Fiziği Hataları ve Causal Masking'in Bedeli")

    add_card(
        s22, 0.45, 1.12, 5.95, 2.58,
        "1. Metin Sentezi ve Sağduyu Fiziği Zayıflıkları",
        [
            ("Belge Düzeyinde Dejenerasyon: ",
             "Uzun pasajlarda kendini anlamsal olarak tekrarlama, tutarlılık kaybı, kendiyle çelişme ve alakasız cümleler (non-sequitur) üretme."),
            ("Sağduyu Fiziği Eksikliği (Common Sense Physics): ",
             "PIQA'da yüksek skor alsa da gayriresmî testlerde 'If I put cheese into the fridge, will it melt?' gibi fiziksel nedensellik sorularında başarısız olur."),
        ],
        border_color=AMBER, accent_bar_color=AMBER, title_color=AMBER, font_size=11.5
    )

    add_card(
        s22, 0.45, 3.84, 5.95, 3.04,
        "2. Yapısal Mimari Kısıt: Çift Yönlülük (Bidirectionality) Yokluğu",
        [
            ("Tasarım Tercihi: ",
             "Örnekleme ve log-olabilirlik hesabı kolay olduğu için yalnızca otoregresif mimari seçildi; BERT/T5'teki çift yönlü dikkat ve denoising hedefleri kullanılmadı."),
            ("Etkilenen Görev Sınıfları: ",
             "• İki cümleyi geri dönüp kıyaslama: WiC (%49.4), ANLI (%40.2), RTE (%69.0).\n• Uzun pasajı yeniden okuyup kısa cevap bulma: QuAC (44.3), RACE (%46.8).\n• Tersten/boşluktan çift yönlü çözümleme: Reversed Words (%0.44)."),
            ("Gelecek Önerisi: ", "GPT-3 ölçeğinde çift yönlü (bidirectional) modellerle few-shot öğrenmeyi birleştirmek ('best of both worlds')."),
        ],
        border_color=CRIMSON, accent_bar_color=CRIMSON, title_color=CRIMSON, font_size=11.0
    )

    # Right side: Vector visual comparing Causal Autoregressive vs Bidirectional Attention
    vc = s22.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.60), Inches(1.12), Inches(6.28), Inches(5.76))
    vc.adjustments[0] = 0.02
    vc.fill.solid()
    vc.fill.fore_color.rgb = WHITE
    vc.line.color.rgb = BORDER_GRAY

    tb_v = s22.shapes.add_textbox(Inches(6.75), Inches(1.22), Inches(5.98), Inches(0.45))
    pv = tb_v.text_frame.paragraphs[0]
    pv.alignment = PP_ALIGN.CENTER
    rv = pv.add_run()
    rv.text = "Dikkat Topolojisi Farkı: Tek Yönlü vs. Çift Yönlü"
    rv.font.name = FONT_MAIN
    rv.font.size = Pt(14.5)
    rv.font.bold = True
    rv.font.color.rgb = NAVY_DARK

    # Two boxes inside right card
    add_card(
        s22, 6.80, 1.78, 5.88, 2.15,
        "GPT-3 (Otoregresif / Causal Masking)",
        [
            ("Token(t) yalnızca t'den önceki tokenları görür:  x₁ → x₂ → ... → x_t"),
            ("Güçlü: ", "Açık uçlu metin üretimi, sıfır-ekstra-maliyetli olasılık hesabı, next-token in-context learning."),
            ("Zayıf: ", "Cümle A ile Cümle B'yi aynı anda karşılıklı karşılaştırma (Cümle A, B'yi göremez!)."),
        ],
        fill_color=CRIMSON_LIGHT, border_color=CRIMSON, title_color=CRIMSON, font_size=11.0, title_size=12.5
    )

    add_card(
        s22, 6.80, 4.10, 5.88, 2.55,
        "BERT / T5 (Çift Yönlü / Bidirectional Denoising)",
        [
            ("Her token tüm bağlamdaki geçmiş ve gelecek tokenları görür:  x₁ ↔ x₂ ↔ ... ↔ x_n"),
            ("Güçlü: ", "İki cümle karşılaştırma (WiC, NLI/ANLI), uzun pasajdan kısa span çekme (QuAC, RACE)."),
            ("Zayıf: ", "Doğal otoregresif metin üretimi ve doğrudan next-token few-shot örneklemesi zordur (T5 bunu fine-tuning ile çözer)."),
        ],
        fill_color=TEAL_LIGHT, border_color=TEAL, title_color=TEAL, font_size=11.0, title_size=12.5
    )

    set_notes(s22, """[Slayt 22 - Mimari Sınırlılıklar I | ~1.5 dk]
Section 5'te yazarlar GPT-3'ün neden bazı görevlerde başarısız olduğunu açıkça analiz ediyor:
1) Metin sentezinde uzun pasajlarda kendini tekrarlama ve sağduyu fiziği hataları ('Peyniri buzdolabına koyarsam erir mi?').
2) Asıl yapısal neden ise otoregresif mimari tercihidir: Model sadece soldan sağa sonraki tokenı tahmin ettiği için iki cümleyi karşılıklı inceleyemez. Örneğin WiC görevinde 'Cümle 1'deki kelime, Cümle 2'ye bakarak' kodlanamaz; yalnızca Cümle 2, Cümle 1'i görebilir. Aynı sebeple ANLI (%40.2), QuAC (44.3) ve RACE (%46.8) gibi karşılaştırma/yeniden okuma görevlerinde çift yönlü (bidirectional) modellere göre dezavantajlıdır.""")

    # =========================================================================
    # SLIDE 23: TEMEL SINIRLILIKLAR II: AMAÇ FONKSİYONU, GROUNDING, VERİMLİLİK
    # =========================================================================
    s23 = prs.slides.add_slide(blank)
    add_header_footer(s23, "Bölüm 5 • Sınırlılıklar II", "Temel Sınırlılıklar: Amaç Fonksiyonu, Grounding ve Verimlilik (Section 5)", 23,
                      "Salt Öz-Denetimli Ölçeklemenin Sınırları ve Yazarların Önerdiği 4 Çıkış Yolu")

    lims = [
        ("1. Öz-Denetimli Hedefin Sınırı",
         ["• Standart LM kaybı her tokenı eşit ağırlıklandırır; hangi varlığın/bilginin kritik olduğunu bilmez [RRS20].",
          "• Görevleri 'tahmin problemine' sıkıştırır; oysa sanal asistanlar hedef odaklı eylemler (goal-directed actions) gerektirir."],
         BLUE_ACCENT),
        ("2. Dünyaya Temellenmeme (Grounding)",
         ["• Video, görüntü veya fiziksel etkileşim olmadan yalnızca metin istatistikleriyle dünya modeli kurulamaz [BHT+20].",
          "• Fiziksel sağduyu hatalarının temel kaynağı modalite eksikliğidir."],
         AMBER),
        ("3. Örneklem Verimsizliği & Maliyet",
         ["• Test zamanında few-shot olsa da ön-eğitimde insan ömrünün katbekat fazlası (300B token) görür [Lin20].",
          "• 175B modelde çıkarım (inference) pahalı ve yavaştır; kalibrasyon zayıf, kararlar yorumlanamazdır."],
         CRIMSON),
    ]
    for i, (lt, lb, lc) in enumerate(lims):
        lx = 0.45 + i * 4.22
        add_card(s23, lx, 1.15, 3.98, 2.75, lt, lb, border_color=lc, accent_bar_color=lc, title_color=lc, font_size=11.2, title_size=12.8)

    # Bottom section: 4 Future Research Directions from Section 5
    add_card(
        s23, 0.45, 4.10, 12.43, 2.78,
        "Makalenin Önerdiği Gelecek Araştırma Yönelimleri (Section 5)",
        [],
        fill_color=WHITE, border_color=TEAL, title_color=TEAL, title_size=13.5
    )

    dirs = [
        ("İnsandan Amaç Öğrenme & RL", "Ziegler et al. [ZSW+19a] çizgisinde insan tercihlerinden ödül/amaç öğrenme ve pekiştirmeli ince ayar."),
        ("Multimodal Grounding", "Görüntü, video ve fiziksel dünya deneyimi ekleyerek kavramları temellendirme [CLY+19]."),
        ("Büyük Ölçekli Damıtma (Distillation)", "175B modeldeki geniş becerileri spesifik görevler için çok daha küçük/ucuz modellere damıtma [HVD15]."),
        ("Çift Yönlü Ölçekleme", "BERT/T5 benzeri bidirectional denoising modellerini GPT-3 ölçeğinde few-shot yapabilme."),
    ]
    for i, (dt, dd) in enumerate(dirs):
        dx = 0.65 + i * 3.05
        add_card(s23, dx, 4.68, 2.88, 2.02, dt, [dd],
                 fill_color=TEAL_LIGHT, border_color=TEAL, title_color=NAVY_DARK, font_size=11.0, title_size=12.0)

    set_notes(s23, """[Slayt 23 - Temel Sınırlılıklar II | ~1.5 dk]
Yazarlar sadece otoregresif mimarinin değil, 'pure self-supervised prediction' yani salt sonraki kelimeyi tahmin etme paradigmasının kendisinin de sınırlarına işaret ediyor:
1) Her token eşit ağırlıklıdır (bir bağlaçla kritik bir tıbbi terim aynı kayıp ağırlığına sahiptir) ve sistem hedef odaklı eylem almak yerine pasif tahmin yapar.
2) Fiziksel dünya ve görsel/işitsel grounding yoktur.
3) Çıkarımda insan gibi few-shot olsa da eğitimde 300B token gibi aşırı yüksek veri ister ve 175B parametrede inference maliyeti yüksektir.
Alt kısımda makalenin Section 5'te bizzat önerdiği 4 çözüm yolunu görüyorsunuz: İnsan tercihlerinden RL öğrenimi, Multimodalite, Model Damıtma (Distillation) ve Çift Yönlü Ölçekleme.""")

    # =========================================================================
    # SLIDE 24: EPİSTEMOLOJİK TARTIŞMA: DE NOVO MU, PATTERN RECOGNITION MI?
    # =========================================================================
    s24 = prs.slides.add_slide(blank)
    add_header_footer(s24, "Bölüm 5 • Epistemoloji", "Epistemolojik Tartışma: Sıfırdan Öğrenme mi, Örüntü Tanıma mı?", 24,
                      "Section 5 & Footnote 1: In-Context Learning Gerçekte Nasıl Çalışıyor?")

    add_card(
        s24, 0.45, 1.15, 12.43, 1.35,
        "Makalenin Açık Bilimsel Sorusu (Section 5)",
        [("Temel Belirsizlik: ",
          "GPT-3 çıkarım (inference) anında bağlamda verilen K örnekten gerçekten sıfırdan ('from scratch' / de novo) yeni bir görev mi öğreniyor, yoksa 300B tokenlık ön-eğitim sırasında zaten gördüğü görevlerden birini tanıyıp (task recognition) ilgili devreyi mi aktive ediyor?")],
        fill_color=BLUE_PALE, border_color=BLUE_ACCENT, accent_bar_color=BLUE_ACCENT, font_size=12.5
    )

    # 4-stage Spectrum Diagram
    spec = [
        ("1. Tam Eşleşen Dağılım\n(Task Recognition)", "Bağlamdaki örnekler, eğitim setinde zaten sıkça görülen görev ve formatlarla birebir örtüşür.\nÖrn: Standart dil modelleme, yaygın soru kalıpları.", NAVY_MED),
        ("2. Format Hizalaması\n(Format Recognition)", "Görev ön-eğitimde öğrenilmiştir ama test veri seti farklı biçimdedir; bağlam sadece stili hizalar.\nÖrn: Makine çevirisi, WebQuestions, LAMBADA fill-in-the-blank.", BLUE_ACCENT),
        ("3. Alt-Beceri Adaptasyonu\n(Skill Composition)", "Model bildiği alt becerileri yeni bir kısıt altında birleştirir.\nÖrn: 3–4 basamaklı aritmetik, SAT analojileri, yeni stil haber üretimi.", TEAL),
        ("4. Sıfırdan Kural Çıkarımı\n(De Novo Learning)", "Ön-eğitimde bulunma ihtimali çok düşük kuralların ileri besleme içinde anlık çözümü.\nÖrn: Uydurma kelimeler ('screeghed'), Sembol ayıklama (RI).", RGBColor(124, 58, 237)),
    ]
    for i, (sp_t, sp_b, sp_c) in enumerate(spec):
        sx = 0.45 + i * 3.15
        add_card(s24, sx, 2.75, 2.95, 2.60, sp_t, [sp_b],
                 fill_color=WHITE, border_color=sp_c, accent_bar_color=sp_c, title_color=sp_c, font_size=11.0, title_size=12.0)
        if i < 3:
            arr = s24.shapes.add_shape(MSO_SHAPE.LEFT_RIGHT_ARROW, Inches(sx + 2.97), Inches(3.90), Inches(0.16), Inches(0.25))
            arr.fill.solid()
            arr.fill.fore_color.rgb = TEXT_MUTED
            arr.line.fill.background()

    add_card(
        s24, 0.45, 5.55, 12.43, 1.32,
        "Bilişsel & Kuramsal Paralellik",
        [("Yazarların Yorumu: ",
          "İnsanların da sıfırdan neyi öğrendiği vs. önceki deneyimlerden neyi tanıdığı tam ayrışmamıştır. Ön-eğitimde çeşitli gösterimleri (demonstrations) organize etmek ve çıkarımda tanımak bile devrimsel olsa da, mekanizmanın tam anlaşılması açık bir araştırma alanıdır.")],
        fill_color=CODE_BG, border_color=BORDER_GRAY, font_size=11.8
    )

    set_notes(s24, """[Slayt 24 - Epistemolojik Tartışma | ~1.5 dk]
Bu slayt Yüksek Lisans seviyesinde en derin kuramsal tartışmayı açar (Section 5 ve Footnote 1):
In-Context Learning dediğimiz olgu aslında gradyansız bir öğrenme algoritması mı (de novo learning), yoksa eğitim sırasında ezberlenmiş/öğrenilmiş milyarlarca alt-dağılım içinden doğru 'beceri kümesini' seçen bir indeksleme/tanıma mekanizması mı (task recognition)?
Yazarlar bunun siyah-beyaz olmadığını, bir spektrum oluşturduğunu vurgular: Çeviri ve genel kültür QA'sı kesinlikle ön-eğitimde öğrenilmiştir, bağlam sadece formatı hizalar. Öte yandan hiç var olmayan 'screeg' kelimesini çekimleyerek kullanma veya sembol ayıklama görevleri, zero-shot'ta %0 iken few-shot'ta öğrenildiği için de novo adaptasyona en güçlü adaylardır.""")

    # =========================================================================
    # SLIDE 25: TOPLUMSAL ETKİLER I: KÖTÜYE KULLANIM & ENERJİ ANALİZİ
    # =========================================================================
    s25 = prs.slides.add_slide(blank)
    add_header_footer(s25, "Bölüm 6 • Toplumsal Etki & Enerji", "Toplumsal Etkiler I: Kötüye Kullanım ve Enerji Amortismanı (Sections 6.1 & 6.3)", 25,
                      "NIST Güvenlik Risk Çerçevesi, Tehdit Aktörleri (APT) ve Eğitim vs. Çıkarım Enerjisi")

    add_card(
        s25, 0.45, 1.12, 6.08, 3.60,
        "Kötüye Kullanım ve Tehdit Aktörü Analizi (Section 6.1)",
        [
            ("Potansiyel Zararlı Kullanımlar: ",
             "Dezenformasyon, spam, oltalama (phishing), yasal/kamusal süreç istismarı, sahte akademik ödevler ve sosyal mühendislik."),
            ("Tehdit Aktörleri (Low/Mid vs. APT): ",
             "GPT-2 sonrası forumlarda tartışmalar artsa da aktif dağıtım gözlenmemiştir. Profesyonel tehdit analistlerine göre APT'ler (devlet destekli aktörler) henüz geçiş yapmamıştır çünkü içeriği hedefleme/kontrol (steering) erken aşamadadır."),
            ("TTP & %1 Hata Darboğazı: ",
             "Stokastik çıktılarda %99 güvenilirlik sağlansa bile %1 tutarsızlık hâlâ insan filtresi (human-in-the-loop) gerektirdiğinden tam otonom bot ölçeklenmesini sınırlar — ancak modeller kontrol edilebilir oldukça risk artacaktır."),
        ],
        border_color=CRIMSON, accent_bar_color=CRIMSON, title_color=CRIMSON, font_size=11.0
    )

    add_card(
        s25, 0.45, 4.86, 6.08, 2.02,
        "Otomatik Tespit (Automated Detection) İhtiyacı",
        [
            ("İnsan Sınırı Aşıldı: ", "İnsanlar %52 ile tespit edemediği için GROVER [ZHR+19] ve GLTR [GSR19] gibi otomatik istatistiksel ayırt ediciler hayati önem taşır [IDCBE19]."),
        ],
        fill_color=AMBER_LIGHT, border_color=AMBER, title_color=AMBER, font_size=11.3
    )

    add_card(
        s25, 6.80, 1.12, 6.08, 3.40,
        "Enerji Kullanımı ve Amortisman Perspektifi (Section 6.3)",
        [
            ("Yüksek Tek Seferlik Eğitim Maliyeti: ",
             "GPT-3 175B ön-eğitimi birkaç bin (3,640) Petaflop/s-gün tüketmiştir (GPT-2 1.5B onlarca PF-gün tüketmişti). 'Green AI' [SDSE19] açısından dikkat gerektirir."),
            ("Amortisman (Lifecycle Efficiency): ",
             "Eğitim maliyeti, modelin ömrü boyunca hizmet vereceği milyonlarca görev ve damıtma (distillation) sürecine bölünmelidir."),
            ("Şaşırtıcı Çıkarım Verimliliği: ",
             "Eğitilmiş 175B modelle bile 100 sayfa içerik üretmek yalnızca ~0.4 kW-hr (birkaç sent elektrik maliyeti) gerektirir!"),
        ],
        fill_color=TEAL_LIGHT, border_color=TEAL, accent_bar_color=TEAL, title_color=TEAL, font_size=11.3
    )

    add_formula_box(
        s25, 6.80, 4.68, 6.08, 1.05,
        "Eğitim: ~3,640 PF-days  →  Çıkarım (100 Sayfa): ~0.4 kW-hr",
        "Tek Büyük Ön-Eğitim + Göreve Özel Model Damıtma (Distillation) ile sürdürülebilirlik.",
        dark=True, font_size=12.0
    )

    add_card(
        s25, 6.80, 5.86, 6.08, 1.02,
        "Algoritmik İlerleme Notu [HB20]",
        ["Görüntü işleme ve NMT'deki gibi algoritmik verimlilik artışları zamanla aynı performansın hesaplama maliyetini hızla düşürmektedir."],
        fill_color=CODE_BG, border_color=BORDER_GRAY, font_size=10.8, title_size=11.8
    )

    set_notes(s25, """[Slayt 25 - Kötüye Kullanım & Enerji | ~1.5 dk]
Section 6.1'de yazarlar NIST risk değerlendirme çerçevesiyle kötüye kullanım analizi yapıyor: Phishing gibi düşük maliyetli saldırılar dil modelleriyle daha da ucuzlayabilir. Ancak 2020 itibarıyla ne düşük becerili forum aktörlerinde ne de devlet destekli APT'lerde yaygın bir LLM kullanımı gözlenmiştir; bunun ana nedeni çıktılardaki %1'lik stokastik hata oranının bile hâlâ insan filtresi gerektirmesidir.
Section 6.3 ise enerji eleştirilerine çok önemli bir amortisman perspektifi getirir: Evet, eğitimde 3,640 PF-days gibi muazzam enerji harcanmıştır; fakat model bir kez eğitildikten sonra 175B parametreli modelden 100 sayfa metin üretmek sadece 0.4 kW-hr (birkaç sent) elektrik tüketir ve bu tek büyük model daha küçük modellere damıtılabilir.""")

    # =========================================================================
    # SLIDE 26: TOPLUMSAL ETKİLER II: ADALET, ÖNYARGI VE TEMSİL
    # =========================================================================
    s26 = prs.slides.add_slide(blank)
    add_header_footer(s26, "Bölüm 6 • Adalet & Önyargı", "Toplumsal Etkiler II: Cinsiyet, Irk ve Din Önyargıları (Section 6.2)", 26,
                      "İnternet Ölçekli Modeller İnternet Ölçekli Stereotipleri Yansıtır (Preliminary Bias Audit)")

    add_formula_box(
        s26, 0.45, 1.12, 6.30, 0.92,
        "Meslek Önyargısı = (1/n) Σ log( P(female | Context) / P(male | Context) )",
        "Nötr Bağlam: −1.11  |  'Competent {job}': −2.14 (Erkek lehine 2x derinleşme!)  |  'Incompetent {job}': −1.15",
        dark=True, font_size=10.8
    )

    add_card(
        s26, 0.45, 2.14, 6.30, 2.38,
        "Cinsiyet Önyargısı Bulguları (Section 6.2.1 & Table 6.1)",
        [
            ("388 Meslek Testi: ", "Mesleklerin %83'ü ('legislator, banker, mason...') erkek belirteçleriyle devam eder; kadınlar ağırlıklı olarak 'midwife, nurse, receptionist' ile eşleşir."),
            ("Sıfat Eş-Dizimliliği (Table 6.1): ", "Kadın zamirleriyle en çok 'beautiful (158), gorgeous (28), bubbly, petite' gibi görünüm kelimeleri; erkeklerle 'large, lazy, eccentric, protect' gibi geniş sıfatlar çıkar."),
            ("Winogender Zamir Direnci: ", "175B en yüksek doğruluğa (%64.17) sahiptir ve kadın meslek sahiplerinde (%81.7) erkeklerden (%76.7) yüksek alan tek modeldir — büyük modeller önyargı kaynaklı hatalara daha dirençli olabilir."),
        ],
        border_color=CRIMSON, accent_bar_color=CRIMSON, title_color=CRIMSON, font_size=10.5
    )

    add_styled_table(
        s26, 0.45, 4.64, 6.30, 2.24,
        ["Din (Table 6.2)", "GPT-3 175B'de En Çok Tercih Edilen Eş-Dizimli Kelimeler"],
        [
            ["Atheism", "Theists, Cool, Agnostics, Mad, Defensive, Arrogant"],
            ["Buddhism", "Myanmar, Vegetarians, Monk, Wisdom, Enlightenment, Non-Violent"],
            ["Christianity", "Attend, Ignorant, Judgmental, Grace, Execution, Egypt"],
            ["Hinduism", "Caste, Cows, BJP, Kashmir, Modi, Dharma, Pakistani"],
            ["Islam", "Pillars, Terrorism, Fasting, Sheikh, Mosque, Prophet (+violent/terrorist top 40)"],
            ["Judaism", "Gentiles, Race, Semites, Whites, Blacks, Smartest, Racists"],
        ],
        col_widths=[1.25, 5.05],
        font_size=9.5, header_size=10.0, highlight_rows={4: AMBER_LIGHT}
    )

    add_picture_fit(s26, "fig6_1_racial_sentiment.png", 6.92, 1.12, 5.96, 3.65,
                    "Figure 6.1: SentiWordNet ile 800 örneklemde ırk kategorilerine göre duygu skorları.")

    add_card(
        s26, 6.92, 4.90, 5.96, 1.98,
        "Irk Analizi (Section 6.2.2) ve Bütünsel Müdahale Çağrısı",
        [
            ("Irk Asimetrisi: ", "7 modelin 3'ünde 'Asian' en yüksek duygu skorunu alırken, 'Black' 7 modelin 5'inde en düşük skoru almıştır (175B'de fark marjinal olarak daralır; sosyo-tarihsel bağlamlar örn. kölelik tartışmaları skoru etkiler)."),
            ("Mitigation Uyarısı (Sec 6.2.4): ", "Salt metrik odaklı 'önyargı silme' yöntemleri kör noktalara sahiptir [GG19]; Model Cards [MWZ+18] ve bütünsel toplumsal müdahale gerekir."),
        ],
        fill_color=BLUE_PALE, border_color=BLUE_ACCENT, accent_bar_color=BLUE_ACCENT, font_size=10.5
    )

    set_notes(s26, """[Slayt 26 - Adalet, Önyargı ve Temsil | ~1.5 dk]
Section 6.2, internetten eğitilen büyük modellerin toplumsal stereotipleri nasıl devraldığını nicel olarak inceler:
- Cinsiyet (Section 6.2.1): Test edilen 388 mesleğin %83'ü erkek lehinedir. Çok çarpıcı bir deneyde, 'The {occupation} was a' nötr bağlamında log-olasılık skoru -1.11 iken, 'The competent {occupation} was a' dendiğinde -2.14'e yani erkek lehine iki kat derinleşmektedir! Öte yandan Winogender zamir testinde 175B model en az önyargı hatası yapan modeldir (%64.17).
- Irk (Figure 6.1): SentiWordNet analizinde 'Black' 7 modelin 5'inde en düşük duygu skorunu almıştır (büyüdükçe fark bir miktar kapanır).
- Din (Table 6.2): İslam bağlamında 'terrorism' ve 'violent' gibi kelimelerin eş-dizimliliğinin yüksek çıktığı raporlanır ve yazarlar yüzeysel metrik yamaları yerine bütünsel çözümler çağrısı yapar.""")

    # =========================================================================
    # SLIDE 27: 2020'DEN GÜNÜMÜZE ELEŞTİREL SENTEZ
    # =========================================================================
    s27 = prs.slides.add_slide(blank)
    add_header_footer(s27, "Bölüm 6 • Akademik Miras", "2020'den Günümüze Eleştirel Sentez: GPT-3'ün Öngörüleri Nasıl Gerçekleşti?", 27,
                      "Yüksek Lisans Perspektifi: Section 5 Sınırlılıklarından Modern Yapay Zekâ Paradigmalarına")

    add_styled_table(
        s27, 0.45, 1.15, 12.43, 4.35,
        ["2020 GPT-3 Sınırlılığı / Öngörüsü (Section 5)", "Kök Neden (Makale Teşhisi)", "2022–2026 Çözüm Paradigması", "Sonuç & Literatürdeki Yeri"],
        [
            ["Amaç Fonksiyonu & Kontrol Edilemezlik\n(Section 5 & 6.1)",
             "Saf MLE sonraki-token tahmini hedefi; her tokena eşit ağırlık, kullanıcı niyeti yok.",
             "InstructGPT & RLHF / DPO\n(Ouyang et al., 2022)",
             "Yönerge takibi, hizalama (alignment) ve ChatGPT devriminin doğrudan temeli."],
            ["Çok Basamaklı Aritmetik (%9) & Ters Çevirme (%0.44)\n(Section 3.9)",
             "Tek bir forward pass aktivasyonu içinde çok adımlı ara hesaplama ve geri izleme yapılamaması.",
             "Chain-of-Thought (Wei et al., 2022) & Test-Time Reasoning",
             "Hesaplamanın ara tokenlara (scratchpad) yayılmasıyla muhakeme sıçraması."],
            ["300B Token / 175B Parametre Dengesi\n(Section 2 & Appendix D)",
             "Kaplan et al. (2020) yasalarına göre parametreyi veri sayısından çok daha hızlı büyütme.",
             "Chinchilla Scaling Laws\n(Hoffmann et al., 2022)",
             "GPT-3'ün veri açısından undertrained (~1.7 token/param) olduğunun kanıtı (~20 token/param optimal)."],
            ["Fiziksel Dünya & Grounding Eksikliği\n(Section 5)",
             "Yalnızca metin istatistikleriyle görsel ve fiziksel nedenselliğin öğrenilememesi.",
             "Multimodal Foundation Models\n(GPT-4V/o, Gemini)",
             "Görsel, işitsel, video ve metnin ortak gömme uzayında birleşmesi."],
        ],
        col_widths=[3.10, 3.25, 2.85, 3.23],
        font_size=11.0, header_size=11.0, highlight_rows={0: BLUE_PALE, 1: TEAL_LIGHT, 2: AMBER_LIGHT, 3: BLUE_PALE}
    )

    add_card(
        s27, 0.45, 5.68, 12.43, 1.20,
        "Tarihsel Değerlendirme",
        [("Öncü Yol Haritası: ",
          "GPT-3 makalesi yalnızca ölçeklemenin gücünü kanıtlamakla kalmamış; Section 5'te bizzat teşhis ettiği 4 eksiklik üzerinden son 5 yılın neredeyse tüm büyük ML araştırma gündemini (RLHF, CoT, Chinchilla, Multimodalite) öngörmüştür.")],
        fill_color=TEAL_LIGHT, border_color=TEAL, accent_bar_color=TEAL, title_color=TEAL, font_size=12.0
    )

    set_notes(s27, """[Slayt 27 - 2020'den Günümüze Sentez | ~2 dk]
Bir Yüksek Lisans sunumunda makaleyi sadece özetlemek değil, literatürdeki tarihsel konumunu ve sonrasını da sentezlemek çok değerlidir.
Brown et al. (2020)'ın Section 5'te 'gelecek yönelimler' olarak yazdığı neredeyse her madde sonraki yılların en büyük buluşlarına dönüştü:
1) 'İnsandan amaç fonksiyonu öğrenme ve RL' önerisi 2022'de InstructGPT / RLHF'e ve ChatGPT'ye yol açtı.
2) 4-5 basamaklı aritmetikte ve kelime ters çevirmedeki başarısızlık, tek forward pass kısıtından kaynaklanıyordu; 2022'de Chain-of-Thought prompting ara adımları token olarak üreterek bu sınırı aştı.
3) 175B parametreye karşılık 300B token (~1.7 token/parametre) kullanımı, 2022'deki Chinchilla Scaling Laws çalışmasıyla revize edildi ve parametre başına ~20 tokenın compute-optimal olduğu gösterildi.
4) Grounding eksikliği ise bugün GPT-4o ve Gemini gibi doğal multimodal modellerle aşılmaktadır.""")

    # =========================================================================
    # SLIDE 28: SONUÇ, TEMEL ÇIKARIMLAR VE TARTIŞMA SORULARI (Q&A)
    # =========================================================================
    s28 = prs.slides.add_slide(blank)
    add_header_footer(s28, "Bölüm 6 • Sonuç & Q&A", "Sonuç, Temel Katkılar ve Sınıf Tartışma Soruları (Q&A)", 28,
                      "Brown et al. (2020) — Language Models are Few-Shot Learners")

    contribs = [
        ("1. Gradyan Güncellemesiz Adaptasyon",
         "175B ölçeğinde tek bir modelin ağırlık güncellemesi (Δθ = 0) olmadan PTB (20.5 ppl), LAMBADA (%86.4) ve TriviaQA (%71.2) görevlerinde SOTA kurabileceğini kanıtladı.",
         BLUE_ACCENT),
        ("2. Öngörülebilir Güç Yasası Ölçeklemesi",
         "Kayıp fonksiyonunun L(C) = 2.57·C⁻⁰·⁰⁴⁸ yasasıyla iyileşmeye devam ettiğini ve model kapasitesi arttıkça in-context learning makasının açıldığını gösterdi.",
         TEAL),
        ("3. Veri Kirlenmesi Denetim Standardı",
         "Spark tabanlı tam N-gram çakışma analizi (Clean vs. Dirty) ile internet ölçekli modellerde benchmark şeffaflığı için standart oluşturdu.",
         NAVY_MED),
        ("4. Dürüst Sınırlılık & Etik Çerçevesi",
         "Çift yönlülük eksikliği (WiC/ANLI), sağduyu fiziği hataları, cinsiyet/ırk/din önyargıları ve kötüye kullanım risklerini ilk günden bilimsel açıklıkla raporladı.",
         AMBER),
    ]
    for i, (ct, cb, cc) in enumerate(contribs):
        cy = 1.15 + i * 1.42
        add_card(s28, 0.45, cy, 6.25, 1.28, ct, [cb],
                 fill_color=WHITE, border_color=cc, accent_bar_color=cc, title_color=cc, font_size=11.0, title_size=12.5)

    add_card(
        s28, 6.95, 1.15, 5.93, 4.30,
        "Sınıf & Jüri İçin Açık Tartışma Soruları",
        [
            ("Soru 1 (Mekanizma): ",
             "In-context learning gerçekte bir 'örtük gradyan inişi' (implicit SGD / mesa-optimization) midir, yoksa yalnızca eğitim verisindeki görev dağılımlarına Bayesci koşullandırma mıdır?"),
            ("Soru 2 (Mimari vs. Ölçek): ",
             "WiC (%49.4) ve ANLI (%40.2) gibi görevlerde başarısızlık tamamen otoregresif tek yönlülükten mi kaynaklanır, yoksa ölçek ve test-time reasoning ile aşılabilir mi?"),
            ("Soru 3 (Benchmark Krizi): ",
             "Web verisiyle eğitilen trilyon-tokenlı modern modellerde, veri kirlenmesini (contamination) sıfıra indiren güvenilir değerlendirme nasıl tasarlanmalıdır?"),
        ],
        fill_color=BLUE_PALE, border_color=NAVY_DARK, accent_bar_color=NAVY_DARK, title_color=NAVY_DARK, font_size=11.5, title_size=13.5
    )

    thanks = s28.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.95), Inches(5.62), Inches(5.93), Inches(1.18))
    thanks.adjustments[0] = 0.06
    thanks.fill.solid()
    thanks.fill.fore_color.rgb = NAVY_DARK
    thanks.line.color.rgb = TEAL
    thanks.line.width = Pt(1.5)
    tf_th = thanks.text_frame
    tf_th.word_wrap = True
    tf_th.vertical_anchor = MSO_ANCHOR.MIDDLE
    pt1 = tf_th.paragraphs[0]
    pt1.alignment = PP_ALIGN.CENTER
    rt1 = pt1.add_run()
    rt1.text = "Dinlediğiniz İçin Teşekkür Ederim"
    rt1.font.name = FONT_MAIN
    rt1.font.size = Pt(19)
    rt1.font.bold = True
    rt1.font.color.rgb = WHITE
    pt2 = tf_th.add_paragraph()
    pt2.alignment = PP_ALIGN.CENTER
    pt2.space_before = Pt(4)
    rt2 = pt2.add_run()
    rt2.text = "Sorularınız & Tartışma (Q&A)"
    rt2.font.name = FONT_MAIN
    rt2.font.size = Pt(13.5)
    rt2.font.color.rgb = RGBColor(45, 212, 191)

    set_notes(s28, """[Slayt 28 - Sonuç & Q&A | ~1.5 dk]
Toparlamak gerekirse Brown et al. (2020) dört kalıcı miras bırakmıştır:
1) Gradyan güncellemesi olmadan few-shot öğrenme ile birçok SOTA'yı yakalaması veya aşması,
2) Güç yasası ölçeklemesinin devamlılığını kanıtlaması,
3) İnternet verisi için Spark N-gram kirlenme denetimi standardını getirmesi,
4) Mimari eksiklikleri ve toplumsal riskleri şeffaflıkla ortaya koyması.
Dinlediğiniz için teşekkür ederim; sağdaki üç tartışma sorusu çerçevesinde sorularınızı alabilirim.""")

    prs.save(str(OUT_PPTX))
    print(f"Successfully generated {len(prs.slides)} slides -> {OUT_PPTX}")


if __name__ == "__main__":
    build_presentation()
