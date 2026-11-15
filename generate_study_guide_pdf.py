"""
Generate a comprehensive 8-page graduate-level Turkish study & mastery PDF guide
for Brown et al. (2020) "Language Models are Few-Shot Learners" (GPT-3).

Renders each page in its own isolated pymupdf.Story instance to avoid MuPDF
multi-page table background ghosting and guarantees zero page overflow (more == 0).
"""

from pathlib import Path
import pymupdf

BASE_DIR = Path(r"c:\Users\90535\source\yüksek_lisans\makine öğrenmesi_sunum")
OUT_PDF = BASE_DIR / "GPT3_Makale_Hakimiyet_Rehberi.pdf"
SCRATCH_DIR = Path(
    r"C:\Users\90535\.gemini\antigravity\brain\8a479605-e9b1-46da-b0dc-d0ac559410b2\scratch"
)
PREVIEW_DIR = SCRATCH_DIR / "pdf_previews"

CSS = """
@font-face { font-family: 'UI'; src: url('segoeui.ttf'); font-weight: normal; font-style: normal; }
@font-face { font-family: 'UI'; src: url('segoeuib.ttf'); font-weight: bold; font-style: normal; }
@font-face { font-family: 'UI'; src: url('segoeuii.ttf'); font-weight: normal; font-style: italic; }
@font-face { font-family: 'UI'; src: url('segoeuiz.ttf'); font-weight: bold; font-style: italic; }
@font-face { font-family: 'Mono'; src: url('consola.ttf'); font-weight: normal; font-style: normal; }
@font-face { font-family: 'Mono'; src: url('consolab.ttf'); font-weight: bold; font-style: normal; }

body {
    font-family: 'UI', sans-serif;
    font-size: 8.5pt;
    line-height: 1.35;
    color: #1e293b;
    margin: 0;
    padding: 0;
}

.hero-banner {
    background-color: #0f1c3f;
    color: #ffffff;
    padding: 10pt 12pt;
    border-left: 4pt solid #14b8a6;
    margin-bottom: 7pt;
}
.hero-tag {
    font-size: 7.3pt;
    font-weight: bold;
    color: #2dd4bf;
    letter-spacing: 0.5pt;
    margin-bottom: 2pt;
}
.hero-title {
    font-size: 15.5pt;
    font-weight: bold;
    color: #ffffff;
    margin: 0 0 2pt 0;
    line-height: 1.15;
}
.hero-sub {
    font-size: 8.3pt;
    color: #cbd5e1;
    margin: 0;
}

.sec-header {
    border-bottom: 1.6pt solid #0f1c3f;
    padding-bottom: 3pt;
    margin-bottom: 6pt;
}
.sec-pill {
    display: inline-block;
    background-color: #0f1c3f;
    color: #2dd4bf;
    font-size: 7.1pt;
    font-weight: bold;
    padding: 1.5pt 6pt;
    margin-bottom: 2pt;
}
.sec-title {
    font-size: 12.6pt;
    font-weight: bold;
    color: #0f1c3f;
    margin: 1pt 0 0 0;
    line-height: 1.15;
}

h3 {
    font-size: 9.5pt;
    font-weight: bold;
    color: #1e3a8a;
    margin: 5.5pt 0 2.5pt 0;
    border-bottom: 0.5pt solid #cbd5e1;
    padding-bottom: 1.5pt;
}

p {
    margin: 0 0 4pt 0;
    text-align: justify;
}

ul, ol {
    margin: 1.5pt 0 4.5pt 0;
    padding-left: 13pt;
}
li {
    margin-bottom: 2.2pt;
    text-align: justify;
}

code {
    font-family: 'Mono', monospace;
    font-size: 7.6pt;
    background-color: #f1f5f9;
    color: #0f172a;
    padding: 0.5pt 2.5pt;
}

.box-teal {
    background-color: #f0fdfa;
    border-left: 3pt solid #0d9488;
    border-top: 0.5pt solid #ccfbf1;
    border-right: 0.5pt solid #ccfbf1;
    border-bottom: 0.5pt solid #ccfbf1;
    padding: 5pt 8pt;
    margin: 4.5pt 0;
}
.box-amber {
    background-color: #fffbeb;
    border-left: 3pt solid #d97706;
    border-top: 0.5pt solid #fde68a;
    border-right: 0.5pt solid #fde68a;
    border-bottom: 0.5pt solid #fde68a;
    padding: 5pt 8pt;
    margin: 4.5pt 0;
}
.box-blue {
    background-color: #eff6ff;
    border-left: 3pt solid #2563eb;
    border-top: 0.5pt solid #dbeafe;
    border-right: 0.5pt solid #dbeafe;
    border-bottom: 0.5pt solid #dbeafe;
    padding: 5pt 8pt;
    margin: 4.5pt 0;
}
.box-red {
    background-color: #fff1f2;
    border-left: 3pt solid #be123c;
    border-top: 0.5pt solid #fecdd3;
    border-right: 0.5pt solid #fecdd3;
    border-bottom: 0.5pt solid #fecdd3;
    padding: 5pt 8pt;
    margin: 4.5pt 0;
}
.box-dark {
    background-color: #0f1c3f;
    color: #f8fafc;
    border-left: 3pt solid #2dd4bf;
    padding: 5pt 8pt;
    margin: 4.5pt 0;
    font-family: 'Mono', monospace;
    font-size: 7.9pt;
}
.box-title {
    font-weight: bold;
    font-size: 8.5pt;
    margin-bottom: 1.5pt;
    display: block;
}

table.data {
    width: 100%;
    border-collapse: collapse;
    margin: 3.5pt 0 5pt 0;
    font-size: 7.5pt;
    line-height: 1.24;
}
table.data th {
    background-color: #0f1c3f;
    color: #ffffff;
    font-weight: bold;
    text-align: left;
    padding: 3.2pt 4.5pt;
    border: 0.5pt solid #0f1c3f;
}
table.data td {
    padding: 2.8pt 4.5pt;
    border: 0.5pt solid #cbd5e1;
    vertical-align: top;
}
table.data tr.hl td {
    background-color: #eff6ff;
    font-weight: bold;
}
table.data tr.warn td {
    background-color: #fffbeb;
}
table.data tr.alt td {
    background-color: #f8fafc;
}

table.grid {
    width: 100%;
    border-collapse: collapse;
    margin: 2pt 0;
}
table.grid td {
    border: none;
    vertical-align: top;
    padding: 0;
}

.fig-card {
    border: 0.6pt solid #cbd5e1;
    background-color: #ffffff;
    padding: 3.5pt;
    text-align: center;
}
.fig-cap {
    font-size: 7.1pt;
    color: #475569;
    font-style: italic;
    margin-top: 2pt;
    text-align: left;
    line-height: 1.2;
}
"""

PAGES_HTML = [
    # ==================== SAYFA 1 ====================
    """
<div class="hero-banner">
  <div class="hero-tag">YÜKSEK LİSANS MAKİNE ÖĞRENMESİ • MAKALE HAKİMİYET REHBERİ</div>
  <div class="hero-title">Language Models are Few-Shot Learners (GPT-3)</div>
  <div class="hero-sub">Tom B. Brown vd. (OpenAI, NeurIPS 2020, arXiv:2005.14165v4) — 75 Sayfalık Makalenin Kavramsal, Matematiksel ve Eleştirel Özeti</div>
</div>

<div class="box-teal">
  <span class="box-title" style="color:#0f766e;">Tek Cümlede Ana Tez (Makaleyi Hiç Okumayanlar İçin Çekirdek Fikir)</span>
  Otoregresif bir dil modelini yeterince büyüttüğümüzde (<b>175 Milyar parametre</b>, 300 Milyar token), modele yeni bir görev öğretmek için artık ağırlıklarını güncellememize (<b>fine-tuning / gradyan inişi</b>) gerek kalmaz; yalnızca metin girdisinin (<i>prompt</i>) içine birkaç örnek yazarak modelin yeni görevleri <b>ileri yayılım (forward pass)</b> sırasında çözmesini sağlayabiliriz.
</div>

<h3>1. Nereden Nereye Geldik? NLP'de Transfer Öğreniminin 3 Dönemi</h3>
<table class="data">
  <tr>
    <th style="width:19%;">Dönem &amp; Temsilciler</th>
    <th style="width:27%;">Mimari &amp; Ön-Eğitim</th>
    <th style="width:31%;">Yeni Göreve Adaptasyon Yöntemi</th>
    <th style="width:23%;">Temel Sınırlılık</th>
  </tr>
  <tr>
    <td><b>1. Nesil (2013–2017)</b><br>Word2Vec, GloVe</td>
    <td>Tek katmanlı statik kelime vektörleri (bağlamdan bağımsız).</td>
    <td>Her görev için sıfırdan tasarlanan görev-özel RNN/CNN ağları eğitilir.</td>
    <td>Hem mimari hem öğrenme göreve bağımlı; kelime çok anlamlılığı yok.</td>
  </tr>
  <tr class="alt">
    <td><b>2. Nesil (2018–2019)</b><br>ELMo, BERT, RoBERTa, T5</td>
    <td>Görevden bağımsız (<i>task-agnostic</i>) derin Transformer ön-eğitimi.</td>
    <td><b>Direct Fine-Tuning:</b> Her yeni görev için 1.000–100.000 etiketli veriyle &theta; ağırlıkları güncellenir (&theta; &larr; &theta; &minus; &eta;&nabla;L).</td>
    <td>Mimari genel ama öğrenme hâlâ göreve bağımlı ve pahalı veri istiyor.</td>
  </tr>
  <tr class="hl">
    <td><b>3. Nesil (2020 — GPT-3)</b><br>Brown et al. (175B)</td>
    <td>Dev ölçekli otoregresif Decoder-Only Transformer (175B param).</td>
    <td><b>In-Context Learning:</b> Ağırlıklar dondurulur (<b>&Delta;&theta; = 0</b>); görev sadece bağlam penceresindeki metinle tarif edilir.</td>
    <td>Çift yönlülük yok; ön-eğitim ve çıkarım donanım maliyeti çok yüksek.</td>
  </tr>
</table>

<h3>2. Makale Neden "Fine-Tuning" Yaklaşımına Karşı Çıkıyor? (3 Bilimsel İtiraz)</h3>
<ul>
  <li><b>1) Etiketli Veri Darboğazı:</b> Her yeni NLP görevi (örneğin bir metni eleştirmek veya yeni bir dilbilgisi kuralı uygulamak) için <b>10<sup>3</sup> ile 10<sup>5</sup></b> arası el ile etiketlenmiş örnek toplamak pratikte ölçeklenemez.</li>
  <li><b>2) Sahte Korelasyonlar (<i>Spurious Correlations</i>) ve OOD Çöküşü:</b> Yüksek kapasiteli dev bir modeli dar ve küçük bir görev verisi üzerinde ince ayar (<i>fine-tuning</i>) yaptığınızda, model gerçek mantığı öğrenmek yerine veri setinin içindeki istatistiksel ipuçlarını (<i>annotation artifacts</i>) ezberler. Nitekim Yogatama vd. (2019) ve McCoy vd. (2019) çalışmalarında gösterildiği üzere, standart testlerde insan seviyesini geçen fine-tuned modeller <b>Dağılım Dışı (Out-of-Distribution / OOD)</b> örneklerde çöker.</li>
  <li><b>3) İnsan Öğrenmesiyle Bilişsel Uyumsuzluk:</b> İnsanlar yeni bir işi yapmak için 50.000 etiketli örnek incelemez; bir cümlelik açıklama veya 1–2 gösterim (<i>demonstration</i>) yeterlidir ve insan bir diyalog içinde anında bir görevden diğerine geçebilir.</li>
</ul>

<h3>3. Çözüm Perspektifi: Meta-Öğrenme (Meta-Learning — Figure 1.1)</h3>
<table class="grid">
  <tr>
    <td style="width:54%; padding-right:8pt;">
      <p>Makalenin en kritik teorik çerçevesi (Bölüm 1, Dipnot 1) dil modellemesini iki katmanlı bir <b>Meta-Öğrenme</b> süreci olarak yorumlamasıdır:</p>
      <ul>
        <li><b>Dış Döngü (Outer Loop — Ön-Eğitim):</b> İnternetten derlenen 300 milyar token okunurken standart Stokastik Gradyan İnişi (SGD/Adam) çalışır ve ağırlıklar (&theta;) güncellenir. İnternet metinleri içinde doğal olarak bulunan çeviri, toplama, soru-cevap gibi sayısız alt görev tek bir "sonraki kelimeyi tahmin et" hedefiyle ağırlıklara işlenir.</li>
        <li><b>İç Döngü (Inner Loop — In-Context Learning):</b> Çıkarım (test) anında model ağırlıkları kesinlikle <b>değişmez (&Delta;&theta; = 0)</b>. Bağlam penceresindeki birkaç örnek yalnızca modelin <i>ileri yayılım (forward pass)</i> aktivasyonlarını yönlendirerek doğru beceriyi tetikler.</li>
      </ul>
      <div class="box-amber" style="margin-top:3pt;">
        <span class="box-title" style="color:#b45309;">Sunumda Nasıl Anlatmalısın?</span>
        Hocaya şöyle söyle: <i>"GPT-3'ün dış döngüsünde bildiğimiz gradyan inişiyle dünya bilgisi öğrenilir; ancak iç döngüde—yani kullanıcı prompt yazdığında—hiçbir ağırlık değişmez. Adaptasyon tamamen attention aktivasyonları içinde gerçekleşir."</i>
      </div>
    </td>
    <td style="width:46%;">
      <div class="fig-card">
        <img src="assets/figures/fig1_1_meta_learning.png" style="width:100%;" />
        <div class="fig-cap"><b>Figure 1.1 (Makale s. 3):</b> Üstteki mor yatay çizgi ön-eğitimdeki <i>Outer Loop</i>'u (SGD); dikey mavi bloklar ise tek bir ileri geçiş içindeki gradyansız <i>Inner Loop</i>'u gösterir.</div>
      </div>
    </td>
  </tr>
</table>
""",

    # ==================== SAYFA 2 ====================
    """
<div class="sec-header">
  <div class="sec-pill">BÖLÜM 2 • DEĞERLENDİRME REJİMLERİ &amp; MİMARİ</div>
  <div class="sec-title">Dört Görev Ayarı, GPT-3 Mimarisi ve 8 Ölçekli Model Ailesi</div>
</div>

<h3>1. Görev Spesifikasyon Spektrumu: 0S, 1S, FS ve Fine-Tuning (Figure 2.1)</h3>
<table class="grid">
  <tr>
    <td style="width:52%; padding-right:8pt;">
      <p>Makale, modelleri yeni görevlere nasıl uyarladığına göre 4 net rejime ayırır (GPT-3 makalesinde Fine-Tuning <b>hiç uygulanmamıştır</b>):</p>
      <ul>
        <li><b>Fine-Tuning (FT):</b> Her görev için 10<sup>3</sup>–10<sup>5</sup> etiketli örnek üzerinden <b>gradyan güncellemesi</b> yapılır. En yüksek skoru verse de veri bağımlılığı yüksektir.</li>
        <li><b>Few-Shot (FS):</b> Gradyan güncellemesi yok. Bağlam penceresine (<code>n<sub>ctx</sub> = 2048</code>) sığacak kadar—genelde <b>K &isin; [10, 100]</b> arası—örnek verilir.</li>
        <li><b>One-Shot (1S):</b> Görev tanımı + tam <b>K = 1</b> örnek. Yazarlar bunun, insanlara (örn. Mechanical Turk deneylerinde) bir görevi tarif etme biçimine en adil ve en yakın kıyaslama olduğunu vurgular.</li>
        <li><b>Zero-Shot (0S):</b> Yalnızca doğal dil yönergesi (<b>K = 0</b>). Çıktı formatı belirsiz kaldığı için bazen insanlar için bile haksız derecede zordur.</li>
      </ul>
    </td>
    <td style="width:48%;">
      <div class="fig-card">
        <img src="assets/figures/fig2_1_four_settings.png" style="width:100%;" />
        <div class="fig-cap"><b>Figure 2.1 (Makale s. 7):</b> Dört ayar arasındaki yapısal fark. Sağda yalnızca Fine-Tuning turuncu okla ağırlıkları (<i>gradient update</i>) güncellerken, soldaki üç yöntemde ağırlıklar sabittir.</div>
      </div>
    </td>
  </tr>
</table>

<h3>2. GPT-3 Mimari Tasarımı: GPT-2'den Farkı Ne? (Section 2.1)</h3>
<div class="box-blue">
  <span class="box-title" style="color:#1e40af;">Kritik Mimari Bilgi (Sık Sorulur!)</span>
  GPT-3 radikal biçimde yeni bir sinir ağı mimarisi icat etmemiştir. İskeleti doğrudan <b>GPT-2</b> ile aynıdır: <b>Yalnızca Çözücü (Decoder-Only)</b> otoregresif Transformer (değiştirilmiş ağırlık ilklendirme, blok öncesi <i>Pre-LayerNorm</i> ve token başına ortalama <b>~0.7 kelime</b> kodlayan tersinir <i>Byte-Level BPE</i> belirteçleyici).<br>
  <b>Tek Mimari Değişiklik:</b> Child vd. (2019) <i>Sparse Transformer</i> çalışmasından alınan, katmanlar boyunca dönüşümlü (<i>alternating</i>) kullanılan <b>tam yoğun (dense)</b> ve <b>yerel bantlı seyrek (locally banded sparse)</b> öz-dikkat (<i>self-attention</i>) desenleridir. Tüm modellerde bağlam uzunluğu <b>n<sub>ctx</sub> = 2048</b> token ve ileri besleme ara katmanı <b>d<sub>ff</sub> = 4 &middot; d<sub>model</sub></b> olarak sabitlenmiştir. Model, GPU düğümleri arasındaki iletişimi en aza indirmek için hem derinlik (katmanlar) hem genişlik (matris bölme) boyutunda dağıtılmıştır.
</div>

<h3>3. Sistematik Ölçekleme: 8 Model Ailesi ve Hiperparametreler (Table 2.1)</h3>
<p>Ölçeklemenin (<i>scaling</i>) sadece doğrulama kaybını değil, alt görevlerdeki <i>in-context learning</i> performansını nasıl değiştirdiğini kanıtlamak için 125M'den 175B'ye uzanan 3 büyüklük mertebelik 8 model sabit <b>300 milyar token</b> ile eğitilmiştir:</p>

<table class="data">
  <tr>
    <th>Model Adı</th>
    <th>n<sub>params</sub></th>
    <th>n<sub>layers</sub></th>
    <th>d<sub>model</sub></th>
    <th>n<sub>heads</sub></th>
    <th>d<sub>head</sub></th>
    <th>Batch Size (Token)</th>
    <th>Learning Rate</th>
    <th>Eğitim Maliyeti (Table D.1)</th>
  </tr>
  <tr><td>GPT-3 Small</td><td>125M</td><td>12</td><td>768</td><td>12</td><td>64</td><td>0.5M</td><td>6.0 &times; 10<sup>&minus;4</sup></td><td>2.60 PF-gün</td></tr>
  <tr class="alt"><td>GPT-3 Medium</td><td>350M (356M)</td><td>24</td><td>1024</td><td>16</td><td>64</td><td>0.5M</td><td>3.0 &times; 10<sup>&minus;4</sup></td><td>7.42 PF-gün</td></tr>
  <tr><td>GPT-3 Large</td><td>760M</td><td>24</td><td>1536</td><td>16</td><td>96</td><td>0.5M</td><td>2.5 &times; 10<sup>&minus;4</sup></td><td>15.8 PF-gün</td></tr>
  <tr class="alt"><td>GPT-3 XL</td><td>1.3B (1.32B)</td><td>24</td><td>2048</td><td>24</td><td>128</td><td>1M</td><td>2.0 &times; 10<sup>&minus;4</sup></td><td>27.5 PF-gün</td></tr>
  <tr><td>GPT-3 2.7B</td><td>2.7B (2.65B)</td><td>32</td><td>2560</td><td>32</td><td>80</td><td>1M</td><td>1.6 &times; 10<sup>&minus;4</sup></td><td>55.2 PF-gün</td></tr>
  <tr class="alt"><td>GPT-3 6.7B</td><td>6.7B (6.66B)</td><td>32</td><td>4096</td><td>32</td><td>128</td><td>2M</td><td>1.2 &times; 10<sup>&minus;4</sup></td><td>139 PF-gün</td></tr>
  <tr><td>GPT-3 13B</td><td>13.0B (12.85B)</td><td>40</td><td>5140</td><td>40</td><td>128</td><td>2M</td><td>1.0 &times; 10<sup>&minus;4</sup></td><td>268 PF-gün</td></tr>
  <tr class="hl"><td>GPT-3 175B</td><td>175.0B (174.6B)</td><td>96</td><td>12288</td><td>96</td><td>128</td><td>3.2M</td><td>0.6 &times; 10<sup>&minus;4</sup></td><td>3,640 PF-gün (3.14&times;10<sup>23</sup> FLOP)</td></tr>
</table>

<div class="box-amber">
  <span class="box-title" style="color:#b45309;">Mühendislik Sezgisi: Neden Model Büyüdükçe Batch Büyür Ama Learning Rate Küçülür?</span>
  Tablo 2.1'deki zıt eğilim rastgele değildir; McCandlish vd. (2018) <b>Gradient Noise Scale (Gradyan Gürültü Ölçeği)</b> teorisine dayanır:
  <ul style="margin-bottom:0;">
    <li><b>Batch Size Artışı (0.5M &rarr; 3.2M):</b> Büyük modeller optimizasyon kaybı yüzeyinde çok daha büyük bir gradyan gürültü ölçeğine sahiptir; büyük batch boyutu hem gradyan kestirim varyansını düşürür hem de çoklu GPU kümelerinde senkronizasyon maliyetini azaltır.</li>
    <li><b>Learning Rate Azalışı (6.0&times;10<sup>&minus;4</sup> &rarr; 0.6&times;10<sup>&minus;4</sup>):</b> 12.288 boyutlu dev ağırlık matrislerinde büyük adım atmak gradyan patlamasına ve kararsızlığa (divergence) yol açar; hassas denge için öğrenme oranı küçültülür.</li>
  </ul>
</div>
""",

    # ==================== SAYFA 3 ====================
    """
<div class="sec-header">
  <div class="sec-pill">BÖLÜM 3 • VERİ MÜHENDİSLİĞİ, HESAPLAMA &amp; SKORLAMA</div>
  <div class="sec-title">45 TB Veriden 570 GB'a Temizlik, 6ND Matematiği ve PMI Düzeltmesi</div>
</div>

<h3>1. Üç Aşamalı Veri Boru Hattı: Common Crawl Nasıl Temizlendi? (Section 2.2 &amp; Appendix A)</h3>
<p>Ham internet taraması (2016–2019 arası 41 aylık <i>Common Crawl</i>, sıkıştırılmış <b>45 TB</b> düz metin) spam, bozuk HTML ve tekrarlarla doludur. Yazarlar ham büyüklük yerine kaliteyi seçmek için 3 aşamalı bir boru hattı kurmuştur:</p>
<ol>
  <li><b>Otomatik Kalite Sınıflandırıcısı + Stokastik Pareto Filtresi:</b> WebText, Wikipedia ve web kitapları (Books1/2) <i>pozitif sınıf</i>; filtrelenmemiş Common Crawl ise <i>negatif sınıf</i> alınarak Apache Spark üzerinde <code>HashingTF</code> öznitelikleriyle bir <b>Lojistik Regresyon</b> modeli eğitilir. Belge, katı bir eşik yerine <code>np.random.pareto(&alpha;) &gt; 1 &minus; document_score</code> (<b>&alpha; = 9</b>) koşuluyla seçilir.<br>
  <i>Sezgisi:</i> Sabit eşik (ör. skor &gt; 0.8) konsaydı, model sadece Wikipedia/WebText tarzı metinleri görüp çeşitliliği kaybederdi. Pareto eşiği yüksek skorlu belgeleri baskın biçimde seçerken, düşük skorlu ama farklı alanlardan gelen belgeleri de küçük olasılıkla tutarak <b>Dağılım Dışı (OOD) genellemeyi</b> korur. Bu işlem 45 TB'ı <b>570 GB</b>'a (~400–410B token) indirir.</li>
  <li><b>Bulanık Tekilleştirme (Fuzzy Deduplication):</b> Spark <b>MinHashLSH (10 hash)</b> ile hem veri setleri içinde hem aralarında kopya belgeler silinir ve WebText çakışmaları çıkarılır (~%10 azalma). Aynı cümleyi ezberlemek yerine validasyon bütünlüğü korunur.</li>
  <li><b>Kalite Ağırlıklı Karışım (Tablo 2.2):</b> Eğitim sırasında veri setleri <b>boyutlarıyla orantılı örneklenmez!</b> Kaliteli derlemler tekrar tekrar gösterilirken gürültülü Common Crawl'un yarısı bile bitirilmez:</li>
</ol>

<table class="data">
  <tr>
    <th>Veri Seti</th>
    <th>Ham Boyut (Token)</th>
    <th>Eğitim Karışım Ağırlığı</th>
    <th>300B Token Eğitimde Görülen Epoch</th>
    <th>Tasarım Mantığı</th>
  </tr>
  <tr><td>Common Crawl (filtrelenmiş)</td><td>410 Milyar</td><td>%60</td><td><b>0.44 epoch</b></td><td>Devasa hacim ve çeşitlilik; tamamı 1 kez bile görülmez.</td></tr>
  <tr class="alt"><td>WebText2</td><td>19 Milyar</td><td>%22</td><td><b>2.9 epoch</b></td><td>Yüksek kaliteli seçilmiş web metni (~3 kez tekrar).</td></tr>
  <tr><td>Books1</td><td>12 Milyar</td><td>%8</td><td><b>1.9 epoch</b></td><td>Uzun bağlam tutarlılığı ve anlatı yapısı.</td></tr>
  <tr class="alt"><td>Books2</td><td>55 Milyar</td><td>%8</td><td><b>0.43 epoch</b></td><td>Geniş kitap havuzu, tekrarsız okuma.</td></tr>
  <tr class="hl"><td>İngilizce Wikipedia</td><td>3 Milyar</td><td>%3</td><td><b>3.4 epoch</b></td><td>Küçük ama en güvenilir ansiklopedik bilgi; hafif overfitting göze alınır.</td></tr>
</table>

<h3>2. Hesaplama Matematiği (C &approx; 6ND), Eğitim Reçetesi ve RoBERTa Kıyaslaması (Appendix B &amp; D)</h3>
<table class="grid">
  <tr>
    <td style="width:55%; padding-right:8pt;">
      <div class="box-dark">
        C &approx; 6 &middot; N<sub>params</sub> &middot; D<sub>tokens</sub><br>
        GPT-3 175B: 6 &times; 174.6&times;10<sup>9</sup> &times; 300&times;10<sup>9</sup> &approx; 3.14&times;10<sup>23</sup> FLOP = <b>3,640 PF-gün</b>
      </div>
      <ul>
        <li><b>Neden 6 FLOP / param / token? (Table D.1):</b> İleri yayılımda (<i>forward pass</i>) her aktif parametre 1 çarpma + 1 toplama yapar = <b>2 FLOP</b>. Geri yayılımda (<i>backward pass</i>) hem &part;loss/&part;params hem de &part;loss/&part;acts hesaplandığı için ileri geçişin ~2 katı (toplam <b>3&times;</b> çarpanı) gerekir &rarr; <b>2 &times; 3 = 6 FLOP</b> (Attention %10'un altında kaldığı için sadeleştirilmiştir). <i>Not:</i> T5 encoder-decoder mimarisinde token başına parametrelerin yalnızca %50'si aktif olduğundan <b>3 FLOP/param/token</b> kullanılır.</li>
        <li><b>Çarpıcı Kıyas (Figure 2.2):</b> RoBERTa-Large (355M parametre, 2 Trilyon token = <b>49.3 PF-gün</b>) ile ondan ~7.5 kat büyük GPT-3 2.7B (300B token = <b>55.2 PF-gün</b>) neredeyse <b>aynı hesaplama bütçesini</b> harcar!</li>
        <li><b>Optimizasyon (Appendix B):</b> Adam (&beta;<sub>1</sub>=0.9, &beta;<sub>2</sub>=0.95, &epsilon;=10<sup>&minus;8</sup>), gradient norm clip 1.0, weight decay 0.1, ilk 375M tokenda warmup, 260B tokenda %10'a inen kosinüs düşüşü. Kısa belgeler <code>&lt;|endoftext|&gt;</code> ile 2048'lik dizilere paketlenir; özel attention maskesi kullanılmaz.</li>
      </ul>
    </td>
    <td style="width:45%;">
      <div class="fig-card">
        <img src="assets/figures/fig2_2_total_compute.png" style="width:100%;" />
        <div class="fig-cap"><b>Figure 2.2 (Makale s. 9):</b> Kaplan vd. (2020) yasalarına göre sabit bütçede küçük modeli çok tokenda değil, büyük modeli daha az tokenda eğitmek üstündür (RoBERTa-Large vs. GPT-3 2.7B/3B).</div>
      </div>
    </td>
  </tr>
</table>

<h3>3. Değerlendirme Matematiği: Koşulsuz Olasılık Normalizasyonu (Section 2.4)</h3>
<div class="box-teal" style="margin-bottom:0;">
  <b>Çoktan Seçmeli Sorularda Hile Önleme (PMI Benzeri Düzeltme):</b> ARC, OpenBookQA ve RACE gibi çoktan seçmeli testlerde otoregresif model, seçeneklerin kendi doğal frekansına (<i>prior</i> P(y)) takılabilir; yaygın kelimelerden oluşan yanlış şık haksız yere yüksek olasılık alabilir. Yazarlar yalnızca ham token-başı olabilirlik yerine şu normalizasyonu uygular:<br>
  <code>Skor = P(completion | context) / P(completion | answer_context)</code> &nbsp;&nbsp;(Burada <code>answer_context</code> = <code>"Answer: "</code> veya <code>"A: "</code>)<br>
  <b>Matematiksel Anlamı:</b> Paydaya koşulsuz olasılığı koymak yaklaşık olarak <i>P(y|x)/P(y)</i> yani <b>Noktasal Karşılıklı Bilgi (PMI)</b> hesaplar; sorunun o şıkka ne kadar <i>ek</i> destek verdiğini ölçer. Serbest metin üretiminde ise <b>Beam Search (beam = 4, uzunluk cezası &alpha; = 0.6)</b> kullanılır.
</div>
""",

    # ==================== SAYFA 4 ====================
    """
<div class="sec-header">
  <div class="sec-pill">BÖLÜM 4 • ÖLÇEKLEME YASALARI &amp; ÇEKİRDEK NLP SONUÇLARI</div>
  <div class="sec-title">Güç Yasası, Bağlam İçi Öğrenme Eğimi, LAMBADA ve Kapalı Kitap QA</div>
</div>

<h3>1. Altı Büyüklük Mertebesinde Güç Yasası ve Meta-Öğrenme Eğimi (Figures 3.1, 4.1 &amp; 1.2)</h3>
<table class="grid">
  <tr>
    <td style="width:54%; padding-right:8pt;">
      <p>Kaplan vd. (2020) ölçekleme yasaları ek 6 çok küçük modelle (100K parametreye kadar inilerek) test edilmiş ve <b>6 büyüklük mertebesi</b> boyunca doğrulama çapraz entropi kaybının neredeyse kusursuz bir güç yasasını izlediği görülmüştür:</p>
      <div class="box-dark" style="margin:2.5pt 0;">L(C<sub>min</sub>) = 2.57 &middot; C<sub>min</sub><sup>&minus;0.048</sup> &nbsp;(Doyuma ulaşma / düzleşme yok!)</div>
      <ul style="margin-bottom:2pt;">
        <li><b>Ezber (Overfitting) Yok (Figure 4.1):</b> 300B token boyunca eğitim kaybı ile tekilleştirilmiş doğrulama kaybı arasındaki fark 175B'ye çıksa bile neredeyse hiç açılmaz.</li>
        <li><b>Büyük Model = Daha İyi Meta-Öğrenici (Figure 1.2 &amp; 1.3):</b> Doğruluk metrikli 42 benchmark ortalamasında hem 0-Shot hem Few-Shot artar; ancak <b>Few-Shot eğrisi çok daha dik yükselir</b>. 1.3B model <i>K</i> arttıkça yataya yakın seyrederken, 175B model örnek sayısı ve doğal dil yönergesi eklendikçe dramatik sıçrama yapar.</li>
      </ul>
    </td>
    <td style="width:23%; padding-right:4pt;">
      <div class="fig-card">
        <img src="assets/figures/fig3_1_power_law_compute.png" style="width:100%;" />
        <div class="fig-cap"><b>Fig 3.1 (s. 11):</b> 6 mertebe boyunca L = 2.57&middot;C<sup>&minus;0.048</sup>.</div>
      </div>
    </td>
    <td style="width:23%;">
      <div class="fig-card">
        <img src="assets/figures/fig1_2_in_context_curves.png" style="width:100%;" />
        <div class="fig-cap"><b>Fig 1.2 (s. 4):</b> K arttıkça 175B model dik yükselir.</div>
      </div>
    </td>
  </tr>
</table>

<h3>2. Dil Modelleme (PTB), Cloze (LAMBADA) ve Kapalı Kitap Soru Cevaplama (Closed-Book QA)</h3>
<table class="data">
  <tr>
    <th style="width:28%;">Görev / Benchmark</th>
    <th style="width:21%;">Önceki SOTA (Fine-Tuned)</th>
    <th style="width:13%;">GPT-3 0-Shot</th>
    <th style="width:16%;">GPT-3 1-Shot</th>
    <th style="width:22%;">GPT-3 Few-Shot</th>
  </tr>
  <tr><td><b>Penn Tree Bank (PTB)</b> (ppl &darr;)</td><td>35.8</td><td><b>20.50</b></td><td>&mdash; (bağlam uzun)</td><td>&mdash;</td></tr>
  <tr class="alt"><td><b>LAMBADA</b> (Son Kelime, Acc &uarr;)</td><td>%68.0</td><td>%76.2</td><td><span style="color:#be123c;font-weight:bold;">%72.5</span></td><td><b>%86.4</b> (K=15)</td></tr>
  <tr><td><b>StoryCloze</b> (Acc &uarr;)</td><td>%91.8</td><td>%83.2</td><td>%84.7</td><td>%87.7</td></tr>
  <tr class="hl"><td><b>TriviaQA</b> (Closed-Book, Acc &uarr;)</td><td>%68.0 (RAG, açık kitap)</td><td>%64.3</td><td>%68.0</td><td><b>%71.2</b></td></tr>
  <tr><td><b>WebQuestions</b> (Closed-Book)</td><td>%42.2 (RAG) / %37.4 (T5)</td><td>%14.4</td><td>%25.3</td><td>%41.5</td></tr>
  <tr class="alt"><td><b>Natural Questions</b> (Closed-Book)</td><td>%44.5 (RAG) / %36.6 (T5)</td><td>%14.6</td><td>%23.0</td><td>%29.9</td></tr>
</table>

<table class="grid">
  <tr>
    <td style="width:55%; padding-right:8pt;">
      <ul>
        <li><b>PTB'nin Önemi:</b> Modern internet öncesi 1990'lar finans/haber derlemi olduğu için veri kirlenmesinden tamamen muaftır; GPT-3 tek başına SOTA'yı 15 perplexity puanı geliştirir.</li>
        <li><b>LAMBADA'daki Akıllı Prompt Numarası (ve 1S Düşüşü):</b> Standart devam tahmini yerine paragraf sonu <i>boşluk doldurma</i> formatına (<code>... visit her friend ____. &rarr; Bob</code>) sokulur. Tek örnekte (1S: %72.5) yapay format gürültüsü yüzünden 0S'in (%76.2) gerisine düşerken, <b>K=15</b> örnekte formatı çözerek <b>%86.4</b>'e fırlar (hatta 2.7B GPT-3 bile 17B Turing-NLG'yi geçer!).</li>
        <li><b>Closed-Book QA'da Tarihi Başarı:</b> Hiçbir harici arama motoru veya 21M belgeli belge indeksi (RAG) kullanmadan tüm genel kültürü 175B ağırlığından çekerek <b>TriviaQA</b>'da 1-Shot ile RAG SOTA'sını (%68.0) yakalar, Few-Shot'ta <b>%71.2</b> ile geçer!</li>
      </ul>
      <div class="box-blue" style="margin-bottom:0;">
        <span class="box-title" style="color:#1e40af;">WebQs &amp; NQs Sıçraması Neyi Kanıtlar?</span>
        TriviaQA'da 0S zaten %64.3 iken WebQs'de 0S %14.4'ten FS %41.5'e fırlar. Çünkü model bilgiyi zaten bilmektedir, ancak 10–64 örnekle bu iki veri setinin özel <i>kısa cevap stilini/dağılımını</i> öğrenir.
      </div>
    </td>
    <td style="width:45%;">
      <div class="fig-card">
        <img src="assets/figures/fig3_3_triviaqa.png" style="width:100%;" />
        <div class="fig-cap"><b>Figure 3.3 (Makale s. 14):</b> TriviaQA'da hiçbir dış belge araması yapılmadan Zero-Shot (%64.3) bile fine-tuned T5-11B'yi (%50.1) geçer; Few-Shot (%71.2) ise RAG SOTA'sını aşar.</div>
      </div>
    </td>
  </tr>
</table>
""",

    # ==================== SAYFA 5 ====================
    """
<div class="sec-header">
  <div class="sec-pill">BÖLÜM 5 • ÇEVİRİ ASİMETRİSİ, SAĞDUYU &amp; SUPERGLUE ANALİZİ</div>
  <div class="sec-title">Makine Çevirisi, Sağduyu Muhakemesi, Okuduğunu Anlama ve SuperGLUE</div>
</div>

<h3>1. Makine Çevirisi: %93 İngilizce Verinin Yarattığı Yön Asimetrisi (Figure 3.4 &amp; Table 3.4)</h3>
<table class="grid">
  <tr>
    <td style="width:52%; padding-right:8pt;">
      <p>GPT-3 eğitim derleminin kelime sayısına göre <b>%93'ü İngilizce</b>, yalnızca <b>%7'si diğer dillerden</b> oluşur (özel paralel derlem veya <i>back-translation</i> yoktur). Buna rağmen K=64 few-shot çeviride çarpıcı bir asimetri doğar:</p>
      <ul>
        <li><b>Yabancı Dilden İngilizceye (X &rarr; En):</b> GPT-3; Fr&rarr;En (<b>39.2</b>), De&rarr;En (<b>40.6</b>) ve Ro&rarr;En (<b>39.5 BLEU</b>) yönlerinde önceki Denetimsiz NMT SOTA'larını (MASS, XLM, mBART) ortalama <b>~5 BLEU</b> geçer ve denetimli SOTA'ya yaklaşır.</li>
        <li><b>İngilizceden Yabancı Dile (En &rarr; X):</b> Fr (32.6) ve De (29.7) makul kalsa da, özellikle <b>En&rarr;Ro (21.0 BLEU)</b> önceki denetimsiz SOTA'nın (~33+) ciddi biçimde gerisinde kalır.</li>
        <li><b>Teknik Sebep:</b> GPT-2'den miras alınan ve ağırlıklı olarak İngilizce metinler üzerinde eğitilmiş <i>Byte-Level BPE tokenizer</i> Rumence gibi dilleri çok uzun, parçalı byte dizilerine böler; ayrıca modelin çıktı üretme kapasitesi İngilizceye yoğunlaşmıştır.</li>
      </ul>
    </td>
    <td style="width:48%;">
      <div class="fig-card">
        <img src="assets/figures/fig3_4_translation.png" style="width:100%;" />
        <div class="fig-cap"><b>Figure 3.4 (Makale s. 15):</b> 6 dil çiftinde Few-Shot BLEU skorları. Yabancı dillerden İngilizceye (En'e giren yön) ölçekleme çok güçlüdür; İngilizce'den çıkış ise belirgin biçimde geridedir.</div>
      </div>
    </td>
  </tr>
</table>

<h3>2. Sağduyu Çıkarımı, Okuduğunu Anlama ve SuperGLUE Sürprizi (Figure 3.8 &amp; Table 3.8)</h3>
<table class="data">
  <tr>
    <th style="width:28%;">Görev Kümesi / Benchmark</th>
    <th style="width:18%;">GPT-3 (FS)</th>
    <th style="width:23%;">Kıyaslama (SOTA / İnsan)</th>
    <th style="width:31%;">Yorum</th>
  </tr>
  <tr><td><b>Winograd (WSC273)</b></td><td>%88.6*</td><td>%90.1 (RoBERTa)</td><td>Güçlü (*kirlenme notlu).</td></tr>
  <tr class="alt"><td><b>Winogrande (Adversarial)</b></td><td>%77.7</td><td>%84.6 (T5-11B)</td><td>0S %70.2'den istikrarlı artış.</td></tr>
  <tr><td><b>PIQA</b> (Fiziksel Sağduyu)</td><td><b>%82.8*</b></td><td>%79.4 (Eski SOTA)</td><td>SOTA üstü (*kirlenme -%3/-%4).</td></tr>
  <tr class="alt"><td><b>ARC-Challenge / OpenBookQA</b></td><td>%51.5 / %65.4</td><td>%78.5 / %87.2</td><td>UnifiedQA'in gerisinde.</td></tr>
  <tr><td><b>CoQA</b> (Diyalog Anlama, F1)</td><td><b>85.0 F1</b></td><td>88.3 (İnsan) / 90.7</td><td>İnsana sadece ~3 F1 uzak!</td></tr>
  <tr class="alt"><td><b>DROP / QuAC / RACE-h</b></td><td>36.5 / 44.3 / %46.8</td><td>89.1 / 74.4 / %90.0</td><td>Katı/ayrık muhakemede zayıf.</td></tr>
  <tr class="hl"><td><b>SuperGLUE (8 Görev Ort.)</b></td><td><b>71.8</b> (dev 73.2)</td><td>89.3 (T5) / 69.0 (BERT-L)</td><td><b>K&lt;8 örnekle</b> BERT-Large'ı geçer!</td></tr>
  <tr><td>&nbsp;&bull; COPA / ReCoRD (SuperGLUE)</td><td>%92.0 / 91.1 F1</td><td>%94.8 / 94.1 F1</td><td>Neredeyse T5-11B seviyesinde!</td></tr>
  <tr class="warn"><td>&nbsp;&bull; <b>WiC</b> / RTE / <b>ANLI R3</b></td><td><span style="color:#be123c;font-weight:bold;">%49.4</span> / %69.0 / <span style="color:#be123c;font-weight:bold;">%40.2</span></td><td>%76.9 / %92.5 / ~%33 (Rastgele)</td><td><b>Kritik Çöküş Alanı!</b></td></tr>
</table>

<table class="grid">
  <tr>
    <td style="width:52%; padding-right:8pt;">
      <div class="box-red" style="margin-top:2pt; margin-bottom:0;">
        <span class="box-title" style="color:#9f1239;">Neden SuperGLUE'da COPA %92 iken WiC %49.4 (Yazı-Tura)?</span>
        <b>WiC</b> (<i>Words in Context</i>), aynı kelimenin iki ayrı cümlede aynı anlamda kullanılıp kullanılmadığını sorar; <b>ANLI R3</b> ise iki cümle arasındaki çelişki/gerektirme ilişkisini ölçer (13B'ye kadar tüm modeller %33 rastgele tahminde kalır, 175B ilk kez %40.2 ile yaşam belirtisi verir). GPT-3 <b>tek yönlü (soldan sağa)</b> olduğu için iki cümleyi geri dönüp karşılıklı kıyaslayamaz!
      </div>
    </td>
    <td style="width:48%;">
      <div class="fig-card">
        <img src="assets/figures/fig3_8_superglue.png" style="width:100%;" />
        <div class="fig-cap"><b>Figure 3.8 (Makale s. 20):</b> <i>Sol:</i> 0S, 1S, FS (K=32). <i>Sağ:</i> Yalnızca <b>8 bağlam içi örnekle</b>, 125K etiketli örnekle fine-tune edilmiş BERT-Large'ı (69.0) geçer.</div>
      </div>
    </td>
  </tr>
</table>
""",

    # ==================== SAYFA 6 ====================
    """
<div class="sec-header">
  <div class="sec-pill">BÖLÜM 6 • SENTETİK GÖREVLER &amp; NİTELİKSEL TESTLER</div>
  <div class="sec-title">Ezber mi, Hesaplama mı? Aritmetik Faz Geçişi, BPE Testi ve Sahte Haberler</div>
</div>

<h3>1. Aritmetik: 13B &rarr; 175B Arası Ani Faz Geçişi ve "Ezber Değil" Kanıtı (Figure 3.10 &amp; Table 3.9)</h3>
<p>Her biri 2.000 rastgele sorudan oluşan 10 aritmetik görevinde, küçük modeller (1.3B–6.7B) sıfıra yakınken <b>13B'den 175B'ye geçerken ani bir sıçrama (emergent capability)</b> gözlenir:</p>

<table class="grid">
  <tr>
    <td style="width:53%; padding-right:8pt;">
      <table class="data" style="margin-top:2pt;">
        <tr><th style="width:40%;">Aritmetik İşlemi</th><th style="width:20%;">0-Shot</th><th style="width:20%;">1-Shot</th><th style="width:20%;">Few-Shot</th></tr>
        <tr class="hl"><td>2D+ / 2D&minus; (2 Basamak)</td><td>%76.9 / %58.0</td><td>%99.6 / %86.4</td><td><b>%100.0 / %98.9</b></td></tr>
        <tr><td>3D+ / 3D&minus; (3 Basamak)</td><td>%34.2 / %48.3</td><td>%65.5 / %78.7</td><td><b>%80.4 / %94.2</b></td></tr>
        <tr class="alt"><td>4D+ / 5D+ (4&ndash;5 Bas.)</td><td>%4.0 / %0.7</td><td>%14.0 / %3.5</td><td>%25.5 / %9.3</td></tr>
        <tr><td>2Dx Çarpma / 1DC</td><td>%19.8 / %9.8</td><td>%27.4 / %14.3</td><td>%29.2 / %21.3</td></tr>
      </table>
      <div class="box-teal" style="margin-top:3pt;">
        <span class="box-title" style="color:#0f766e;">Hocanın Kesin Soracağı Soru: "Toplamayı İnternetten Ezberlememiş mi?"</span>
        Yazarlar <b>iki güçlü kanıt</b> sunar: (1) Test edilen 2.000 adet 3-basamaklı problem <code>"&lt;N1&gt; + &lt;N2&gt; ="</code> ve <code>"plus"</code> kalıplarıyla eğitim verisinde arandığında toplamada yalnızca <b>17 (%0.8)</b>, çıkarmada <b>2 (%0.1)</b> eşleşme bulunmuştur. (2) Yanlış cevapların çoğunun rastgele sayı atmak yerine <b>"elde var 1'i unutma"</b> (<i>not carrying a 1</i>) hatası olması, gerçek bir algoritmik hesaplama girişimini kanıtlar.
      </div>
    </td>
    <td style="width:47%;">
      <div class="fig-card">
        <img src="assets/figures/fig3_10_arithmetic.png" style="width:100%;" />
        <div class="fig-cap"><b>Figure 3.10 (Makale s. 22):</b> 13B'ye kadar düşük kalan aritmetik doğruluğu 175B parametrede aniden %80–%100 bandına fırlamaktadır.</div>
      </div>
    </td>
  </tr>
</table>

<h3>2. Kelime Karıştırma (K=100), SAT Analojileri, Uydurma Kelimeler ve Sahte Haber (Sec 3.9.2–3.9.4)</h3>
<table class="grid">
  <tr>
    <td style="width:53%; padding-right:8pt;">
      <ul>
        <li><b>5 Karakter Manipülasyon Görevi (Table 3.10, Few-Shot K=100):</b> Araya noktalama/boşluk gizleme (<code>RI</code>: <b>%67.2</b>), ilk/son 2 harf sabit anagram (<code>A2</code>: <b>%39.7</b>), döngüsel kaydırma (<code>CL</code>: <b>%37.9</b>), zor anagram (<code>A1</code>: <b>%15.1</b>) — buna karşılık <b>Kelimeyi Tersten Yazma (<code>RW: stcejbo &rarr; objects</code>): %0.44 (Tam Çöküş!)</b>. Zero-shot'ta tümü ~%0–9 iken K=100'de öğrenilmesi, modelin BPE tokenlarının (~0.7 kelime) <i>alt-karakter yapısını (substructure)</i> ileri yayılımda ayrıştırabildiğini gösterir.</li>
        <li><b>SAT Analojileri (374 Soru):</b> 0S %53.7 &rarr; 1S %59.1 &rarr; FS <b>%65.2</b> (ABD üniversite aday ortalaması <b>%57.0</b>).</li>
        <li><b>Tek Tanımdan Yeni Kelime Öğrenme (Figure 3.16):</b> <i>"whatpu"</i>, <i>"farduddle"</i> veya <i>"To 'screeg' something is to swing a sword at it"</i> tanımını bir kez okuyup <b><i>"We screeghed at each other..."</i></b> diyerek İngilizce geçmiş zaman çekimini (<code>-ed</code>) hatasız üretir.</li>
      </ul>
    </td>
    <td style="width:47%;">
      <div class="fig-card">
        <img src="assets/figures/fig3_13_human_news_detection.png" style="width:100%;" />
        <div class="fig-cap"><b>Figure 3.13 (s. 27):</b> 621 ABD'li katılımcıyla sahte/gerçek haber (~200 ve ~500 kelime) testi. 160M kontrol modeli %86–88 oranında yakalanırken, <b>GPT-3 175B %52'ye</b> (yazı-tura %50, p = 10<sup>&minus;34</sup>) düşer.</div>
      </div>
    </td>
  </tr>
</table>
""",

    # ==================== SAYFA 7 ====================
    """
<div class="sec-header">
  <div class="sec-pill">BÖLÜM 7 • VERİ KİRLENMESİ &amp; YAPISAL SINIRLILIKLAR</div>
  <div class="sec-title">Veri Kirlenmesi Analizi (Clean vs. Dirty) ve Modelin Çöktüğü Yerlerin Kök Nedenleri</div>
</div>

<h3>1. Veri Kirlenmesi (Data Contamination) Denetimi (Section 4 &amp; Appendix C)</h3>
<table class="grid">
  <tr>
    <td style="width:52%; padding-right:8pt;">
      <p><b>Problem:</b> Eğitim öncesi test verilerini 13-gram eşleşmeyle temizlemeye çalışsalar da koddaki bir hata (<i>bug</i>) yüzünden özellikle uzun belgelerde (kitaplar vb.) bazı test parçaları eğitimde kalmıştır. <b>3,640 PF-gün</b> maliyet nedeniyle modeli baştan eğitmek imkansız olduğundan, yazarlar tüm test setlerini Apache Spark üzerinden <b>tam N-gram çakışmasıyla (N &isin; [8, 13], 5. yüzdelik uzunluk)</b> tarayıp tek bir çakışması bile olan örnekleri <b>Dirty</b>, olmayanları <b>Clean</b> ayırmıştır.</p>
      <p style="margin-bottom:2pt;"><b>Önemli Bulgu:</b> Temiz alt küme ile tüm set arasındaki skor farkı çoğu testte 0'a çok yakındır; yani genel başarı ezberden gelmemektedir.</p>
    </td>
    <td style="width:48%;">
      <div class="fig-card">
        <img src="assets/figures/fig4_2_contamination.png" style="width:100%;" />
        <div class="fig-cap"><b>Figure 4.2 (Makale s. 32):</b> Tüm veri setlerinde yalnızca temiz örneklerdeki skorun tüm sete göre değişimi.</div>
      </div>
    </td>
  </tr>
</table>

<table class="data">
  <tr><th style="width:22%;">Kategori (Table C.1)</th><th style="width:36%;">Veri Setleri</th><th style="width:42%;">Durum &amp; Değerlendirme Kararı</th></tr>
  <tr><td><b>1. Yanlış Pozitifler</b></td><td>QuAC (%99 dirty), SQuADv2 (%94), DROP (%93)</td><td>Eğitimde sadece Wikipedia metni var, <b>soru/cevap yok</b>. Fark ~%0.</td></tr>
  <tr class="alt"><td><b>2. Tam Çıkarılanlar</b></td><td>4 Wikipedia LM testi + Children's Book Test</td><td>Aşırı sızıntı nedeniyle makaleden <b>tamamen çıkarıldı</b>.</td></tr>
  <tr class="warn"><td><b>3. Yıldızlılar (<code>*</code>)</b></td><td><b>Winograd</b> (132 şema eğitimde, <b>&minus;%2.6</b>) &amp; <b>PIQA</b> (<b>&minus;%3/&minus;%4</b>)</td><td>Gerçek düşüş şüphesi; tüm tablolarda <code>*</code> ile işaretlendi.</td></tr>
  <tr><td><b>4. LAMBADA</b></td><td>Clean (%57), <b>Fark &lt;%0.5</b></td><td>Ciddi çakışmaya rağmen boşluk doldurma formatı düz ezberi önler.</td></tr>
</table>

<h3>2. Makalenin Öz-Eleştirisi: GPT-3 Neden Bazı Görevlerde Çöküyor? (Section 5)</h3>
<table class="data">
  <tr>
    <th style="width:24%;">Sınırlılık Boyutu</th>
    <th style="width:44%;">Teknik Kök Neden</th>
    <th style="width:32%;">Doğrudan Etkilenen Görev / Örnek</th>
  </tr>
  <tr class="warn">
    <td><b>1. Otoregresif (Tek Yönlü) Mimari Kısıtı</b></td>
    <td>BERT/T5 gibi <b>çift yönlü (bidirectional)</b> dikkat yoktur; her token yalnızca solundaki geçmiş tokenları görebilir. Metni geri dönüp okuyamaz ve iki cümleyi karşılıklı kıyaslayamaz.</td>
    <td><b>WiC (%49.4)</b>, <b>ANLI R3 (%40.2)</b>, RTE (%69.0), QuAC (44.3), RACE-h (%46.8), <b>Reversed Words (%0.44)</b>.</td>
  </tr>
  <tr>
    <td><b>2. Öz-Denetimli MLE Hedef Fonksiyonu</b></td>
    <td>Standart sonraki-kelime tahmini (MLE) her tokena eşit kayıp ağırlığı verir (<i>"the"</i> = kritik mantıksal terim); model hedef odaklı eylem (<i>goal-directed action</i>) öğrenmez.</td>
    <td>Uzun pasajlarda kendini tekrarlama (<i>non-sequitur</i>), kullanıcı niyetiyle uyumsuzluk.</td>
  </tr>
  <tr class="alt">
    <td><b>3. Dünya İlişkilendirmesi (Grounding) Yokluğu</b></td>
    <td>Görüntü, video veya fiziksel dünya etkileşimi olmaksızın salt metin istatistikleriyle nedensel fizik dünyası tam öğrenilemez (Bisk vd., 2020).</td>
    <td>Gayriresmî sağduyu fiziği: <i>"If I put cheese into the fridge, will it melt?"</i> sorusunda başarısızlık.</td>
  </tr>
  <tr>
    <td><b>4. Örneklem Verimsizliği &amp; Çıkarım Maliyeti</b></td>
    <td>Test anında few-shot olsa da ön-eğitimde insan ömrünün katbekat fazlası <b>300B token</b> tüketir; 175B parametrede her tahmin pahalı, yavaş ve yorumlanamazdır (düşük kalibrasyon).</td>
    <td>Pratik yaygınlaştırma için <b>Model Damıtma (Distillation)</b> zorunluluğu.</td>
  </tr>
</table>

<div class="box-blue" style="margin-bottom:0;">
  <span class="box-title" style="color:#1e40af;">Section 5'in En Derin Bilimsel Sorusu: Sıfırdan Öğrenme mi (De Novo Learning), Örüntü Tanıma mı (Task Recognition)?</span>
  Yazarlar dürüstçe şu belirsizliği vurgular: GPT-3 bağlama verilen <i>K</i> örnekten gerçekten <b>sıfırdan yeni bir görev mi öğreniyor</b>, yoksa 300B token okurken zaten gördüğü görevlerden birini <b>tanıyıp aktive mi ediyor?</b> Aslında bu bir spektrumdur: Çeviri ve QA açıkça ön-eğitimde öğrenilip çıkarımda format hizalanması (<i>recognition</i>) yaşar; ancak <i>"screeghed"</i> gibi uydurma kelimeler ve sembol ayıklama (RI) sıfır-örnekte başarısız olup bağlamda çözüldüğü için gerçek anlık kural çıkarımına (<i>de novo</i>) en yakın örneklerdir.
</div>
""",

    # ==================== SAYFA 8 ====================
    """
<div class="sec-header">
  <div class="sec-pill">BÖLÜM 8 • TOPLUMSAL ETKİLER, MODERN MİRAS &amp; KÜRSÜ KOPYA KAĞIDI</div>
  <div class="sec-title">Etik Önyargılar, Enerji Amortismanı, 2020&rarr;Günümüz Sentezi ve Hızlı Özet</div>
</div>

<h3>1. Kötüye Kullanım, Enerji Amortismanı ve Toplumsal Önyargı Analizi (Section 6)</h3>
<table class="grid">
  <tr>
    <td style="width:55%; padding-right:8pt;">
      <ul>
        <li><b>Güvenlik &amp; Kötüye Kullanım (Sec 6.1):</b> Oltalama ve dezenformasyon riskini artırır; ancak 2020 itibarıyla APT'lerin (devlet destekli aktörler) aktif geçişi görülmemiştir. Nedeni, çıktılardaki <b>~%1'lik stokastik hata oranının</b> hâlâ insan filtresi gerektirmesidir. İnsanlar %52 ile ayırt edemediği için <b>GROVER / GLTR</b> gibi otomatik tespit kritik önem taşır.</li>
        <li><b>Enerji Amortismanı (Sec 6.3):</b> Eğitim 3,640 PF-gün harcar ancak modele görev başına fine-tuning gerekmediğinden ömrü boyunca amorti edilir; eğitilmiş 175B modelden <b>100 sayfa metin üretimi yalnızca ~0.4 kW-hr</b> (birkaç sent) enerji tüketir.</li>
        <li><b>Cinsiyet Önyargısı (Sec 6.2.1 &amp; Table 6.1):</b> 388 mesleğin <b>%83'ü</b> erkek belirteçleriyle eşleşir. <code>(1/n)&Sigma;log[P(kadın|bağlam)/P(erkek|bağlam)]</code> skoru nötr bağlamda <b>&minus;1.11</b> iken <i>"competent &#123;meslek&#125;"</i> dendiğinde <b>&minus;2.14</b>'e (erkek lehine) derinleşir (<i>"incompetent"</i>: <b>&minus;1.15</b>). Kadınlar en çok <i>beautiful (158), gorgeous (28), petite</i> ile betimlenir. Buna karşın <b>Winogender</b> zamir testinde 175B model <b>%64.17</b> ile en dirençli modeldir.</li>
        <li><b>Din Eş-Dizimliliği (Table 6.2):</b> İslam (<i>pillars, terrorism, fasting, prophet</i>; +top 40'ta <i>violent, terrorist</i>), Hristiyanlık (<i>ignorant, judgmental, grace</i>), Budizm (<i>wisdom, enlightenment, non-violent</i>), Ateizm (<i>theists, defensive, arrogant</i>).</li>
      </ul>
    </td>
    <td style="width:45%;">
      <div class="fig-card">
        <img src="assets/figures/fig6_1_racial_sentiment.png" style="width:100%;" />
        <div class="fig-cap"><b>Figure 6.1 (s. 38):</b> SentiWordNet duygu skoru. "Asian" 3/7 modelde en yüksek, "Black" 5/7 modelde en düşük skoru alır (175B'de makas kısmen daralır). Yazarlar yüzeysel metrik silme yerine <i>Model Cards</i> ve bütünsel müdahale çağrısı yapar.</div>
      </div>
    </td>
  </tr>
</table>

<h3>2. Tarihsel Köprü: GPT-3'ün Eksiklikleri Modern Yapay Zekayı Nasıl Doğurdu?</h3>
<table class="data">
  <tr>
    <th style="width:27%;">2020 GPT-3 Sınırı (Section 5)</th>
    <th style="width:27%;">2022–2026 Çözüm Devrimi</th>
    <th style="width:46%;">Sunumda Kurulacak Bağlantı</th>
  </tr>
  <tr><td>MLE hedefi kullanıcı niyetiyle uyumsuz</td><td><b>InstructGPT &amp; RLHF / DPO (2022)</b></td><td>İnsan tercihlerinden ödül öğrenerek ChatGPT devrimini başlattı.</td></tr>
  <tr class="alt"><td>Çok basamaklı aritmetik &amp; ters çevirme çöküşü</td><td><b>Chain-of-Thought (Wei vd., 2022)</b></td><td>Hesaplamayı tek forward pass'e sıkıştırmak yerine ara tokenlara yaydı.</td></tr>
  <tr><td>175B param / 300B token (~1.7 tok/param)</td><td><b>Chinchilla Yasası (Hoffmann vd., 2022)</b></td><td>GPT-3'ün veri açısından <i>undertrained</i> kaldığını, ~20 tok/param gerektiğini kanıtladı.</td></tr>
  <tr class="alt"><td>Fiziksel dünya grounding eksikliği</td><td><b>Multimodal Modeller (GPT-4V/o, Gemini)</b></td><td>Görsel/video/metin birleşimiyle sağduyu fiziği eksikliğini kapattı.</td></tr>
</table>

<div class="box-dark" style="font-family:'UI',sans-serif; font-size:8.1pt; line-height:1.33; margin-top:4pt;">
  <span class="box-title" style="color:#2dd4bf; font-size:8.8pt;">Sunum Öncesi Son 5 Dakika: Kürsüde Söylenecek 5 "Altın Cümle" &amp; Sayısal Kopya Kağıdı</span>
  <b>1.</b> "GPT-3'te yeni görev öğrenilirken ağırlık güncellenmez (<b>&Delta;&theta; = 0</b>); adaptasyon tamamen forward pass içinde gerçekleşir."<br>
  <b>2.</b> "Mimari GPT-2 ile aynıdır; tek fark ardışık <b>Dense + Locally Banded Sparse Attention</b> ve <b>175B</b> ölçeklemedir (<b>3,640 PF-gün</b>)."<br>
  <b>3.</b> "45 TB Common Crawl Pareto (&alpha;=9) ile 570 GB'a süzüldü; kaliteli Wikipedia <b>3.4 epoch</b>, Common Crawl ise sadece <b>0.44 epoch</b> okundu."<br>
  <b>4.</b> "SuperGLUE'da <b>8'den az bağlam içi örnekle</b>, 125K etiketli örnekle fine-tune edilmiş BERT-Large'ı geçti (71.8 vs 69.0)."<br>
  <b>5.</b> "<b>WiC (%49.4)</b> ve <b>Reversed Words (%0.44)</b> çöküşü tesadüf değil; otoregresif tek yönlü dikkatin (bidirectional olmayışın) doğrudan bedelidir."
</div>

<div class="box-amber" style="margin-top:4pt; margin-bottom:0;">
  <span class="box-title" style="color:#b45309;">Hızlı Sayısal Hafıza Kartı (Sınav / Q&amp;A İçin Tek Bakışta Tüm Ana Metrikler)</span>
  <b>Parametre &amp; Bağlam:</b> 175B (96 katman, d<sub>model</sub>=12288, n<sub>ctx</sub>=2048, ~0.7 kelime/token) &nbsp;|&nbsp;
  <b>Eğitim Verisi:</b> 300B token (%93 En / %7 diğer) &nbsp;|&nbsp;
  <b>Maliyet:</b> 6ND &approx; 3.14&times;10<sup>23</sup> FLOP = 3,640 PF-gün (Çıkarım: 100 sayfa &approx; 0.4 kW-hr) &nbsp;|&nbsp;
  <b>Zirve Skorlar:</b> PTB 20.50 ppl, LAMBADA %86.4, TriviaQA %71.2, CoQA 85.0 F1, SuperGLUE 71.8, COPA %92.0, 2D+ %100.0, 3D+ %80.4, SAT %65.2 &nbsp;|&nbsp;
  <b>Zayıf Skorlar:</b> WiC %49.4, ANLI R3 %40.2, Reversed Words %0.44, Sahte Haber İnsan Tespiti %52 (p=10<sup>&minus;34</sup>).
</div>
""",
]


def main() -> None:
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    for old_png in PREVIEW_DIR.glob("page_*.png"):
        old_png.unlink()

    arch = pymupdf.Archive([str(BASE_DIR), r"C:\Windows\Fonts"])
    mediabox = pymupdf.paper_rect("a4")  # 595.28 x 841.89 pt
    where = mediabox + (34, 40, -34, -36)
    total_pages = len(PAGES_HTML)

    merged = pymupdf.open()

    for idx, page_body in enumerate(PAGES_HTML, start=1):
        single_html = (
            f"<!DOCTYPE html><html><head><meta charset='utf-8'>"
            f"<style>{CSS}</style></head><body>{page_body}</body></html>"
        )
        story = pymupdf.Story(html=single_html, archive=arch)
        tmp_path = SCRATCH_DIR / f"_page_{idx}.pdf"
        writer = pymupdf.DocumentWriter(str(tmp_path))
        dev = writer.begin_page(mediabox)
        more, filled = story.place(where)
        story.draw(dev, None)
        writer.end_page()
        writer.close()

        fill_h = filled[3] - filled[1]
        avail_h = where.height
        status = "OK" if more == 0 else "OVERFLOW!"
        print(
            f"Page {idx}/{total_pages}: {status} | filled height = {fill_h:.1f}/{avail_h:.1f} pt ({fill_h/avail_h*100:.1f}%)"
        )
        if more != 0:
            raise RuntimeError(f"Page {idx} overflowed 1 A4 sheet (more={more})!")

        pdoc = pymupdf.open(str(tmp_path))
        merged.insert_pdf(pdoc)
        pdoc.close()

    font_reg = r"C:\Windows\Fonts\segoeui.ttf"
    font_bold = r"C:\Windows\Fonts\segoeuib.ttf"

    for i, page in enumerate(merged):
        page_num = i + 1
        w = page.rect.width
        h = page.rect.height

        if page_num > 1:
            page.draw_line(
                pymupdf.Point(34, 27),
                pymupdf.Point(w - 34, 27),
                color=(0.79, 0.83, 0.88),
                width=0.6,
            )
            page.insert_text(
                pymupdf.Point(34, 22),
                "GPT-3: Language Models are Few-Shot Learners (Brown et al., 2020) — Konu Hakimiyet Rehberi",
                fontfile=font_reg,
                fontname="HdrReg",
                fontsize=7.6,
                color=(0.39, 0.45, 0.55),
            )
            page.insert_text(
                pymupdf.Point(w - 92, 22),
                f"Bölüm Özeti • {page_num}/{total_pages}",
                fontfile=font_bold,
                fontname="HdrBold",
                fontsize=7.6,
                color=(0.06, 0.11, 0.25),
            )

        page.draw_line(
            pymupdf.Point(34, h - 26),
            pymupdf.Point(w - 34, h - 26),
            color=(0.79, 0.83, 0.88),
            width=0.6,
        )
        page.insert_text(
            pymupdf.Point(34, h - 15),
            "Yüksek Lisans Makine Öğrenmesi Sunum Hazırlığı  |  Kaynak: arXiv:2005.14165v4 (NeurIPS 2020)",
            fontfile=font_reg,
            fontname="FtrReg",
            fontsize=7.5,
            color=(0.39, 0.45, 0.55),
        )
        page.insert_text(
            pymupdf.Point(w - 82, h - 15),
            f"Sayfa {page_num} / {total_pages}",
            fontfile=font_bold,
            fontname="FtrBold",
            fontsize=7.8,
            color=(0.06, 0.11, 0.25),
        )

        pix = page.get_pixmap(dpi=130)
        pix.save(str(PREVIEW_DIR / f"page_{page_num}.png"))

    merged.save(str(OUT_PDF), garbage=4, deflate=True)
    merged.close()

    print(
        f"Successfully generated {total_pages} clean pages -> {OUT_PDF} ({OUT_PDF.stat().st_size:,} bytes)"
    )


if __name__ == "__main__":
    main()
