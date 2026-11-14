"""Extract high-resolution (300 DPI) figures from 2005.14165v4.pdf into assets/figures/."""

from pathlib import Path
import pymupdf

PDF_PATH = Path(r"c:\Users\90535\Desktop\2005.14165v4.pdf")
OUT_DIR = Path(r"c:\Users\90535\source\yüksek_lisans\makine öğrenmesi_sunum\assets\figures")

# (filename, 1-based page number, image index on page or explicit clip tuple)
FIGURES = [
    ("fig1_1_meta_learning.png", 3, 0),
    ("fig1_2_in_context_curves.png", 4, 0),
    ("fig1_3_aggregate_42_benchmarks.png", 5, 0),
    ("fig2_1_four_settings.png", 7, 0),
    ("fig2_2_total_compute.png", 9, 0),
    ("fig3_1_power_law_compute.png", 11, 0),
    ("fig3_2_lambada.png", 12, 0),
    ("fig3_3_triviaqa.png", 14, 0),
    ("fig3_4_translation.png", 15, 0),
    ("fig3_5_winogrande.png", 16, 0),
    ("fig3_7_coqa.png", 19, 0),
    ("fig3_8_superglue.png", 20, 0),
    ("fig3_9_anli.png", 21, 0),
    ("fig3_10_arithmetic.png", 22, 0),
    ("fig3_11_wordscramble.png", 24, 0),
    ("fig3_12_sat_analogies.png", 25, 0),
    ("fig3_13_human_news_detection.png", 27, 0),
    ("fig3_16_novel_words.png", 29, (71.5, 70.5, 540.5, 354.5)),
    ("fig4_1_training_curves.png", 31, 0),
    ("fig4_2_contamination.png", 32, 0),
    ("fig6_1_racial_sentiment.png", 38, 0),
]


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(PDF_PATH)

    for filename, page_num, target in FIGURES:
        page = doc[page_num - 1]
        if isinstance(target, int):
            images = page.get_images(full=True)
            if target >= len(images):
                raise IndexError(f"Page {page_num} has only {len(images)} images; cannot get index {target}")
            xref = images[target][0]
            rects = page.get_image_rects(xref)
            if not rects:
                raise RuntimeError(f"No rect found for xref {xref} on page {page_num}")
            rect = rects[0]
            clip = pymupdf.Rect(rect.x0 - 2, rect.y0 - 2, rect.x1 + 2, rect.y1 + 2)
        else:
            clip = pymupdf.Rect(*target)

        pix = page.get_pixmap(clip=clip, dpi=300, alpha=False)
        out_path = OUT_DIR / filename
        pix.save(out_path)
        print(f"Saved {filename}: {pix.width}x{pix.height} px")


if __name__ == "__main__":
    main()

