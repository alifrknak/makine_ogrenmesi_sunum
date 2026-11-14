# Yüksek Lisans Sunumu: Konuşmacı Notları ve Soru-Cevap (Q&A) Rehberi

**Makale:** *Language Models are Few-Shot Learners* (Brown et al., OpenAI, NeurIPS 2020, `arXiv:2005.14165v4`)  
**Sunum Dosyası:** [GPT3_Few_Shot_Learners_Yuksek_Lisans_Sunumu.pptx](file:///c:/Users/90535/source/yüksek_lisans/makine öğrenmesi_sunum/GPT3_Few_Shot_Learners_Yuksek_Lisans_Sunumu.pptx)  
**Hedef Süre:** ~35–42 dakika sunum + 10 dakika Soru-Cevap (Toplam 28 Slayt)

---

## Zaman Planlaması (Bölüm Bazlı)

| Bölüm | Slayt Aralığı | Konu Başlığı | Önerilen Süre |
| :--- | :--- | :--- | :--- |
| **Bölüm 1** | Slayt 1–5 | Giriş, Motivasyon, Meta-Learning & Değerlendirme Spektrumu | 6 dakika |
| **Bölüm 2** | Slayt 6–10 | Mimari Tasarım, Veri Mühendisliği, Dağıtık Eğitim & Skorlama | 8 dakika |
| **Bölüm 3** | Slayt 11–16 | Ölçekleme Yasaları ve Standart NLP Benchmark Sonuçları | 8 dakika |
| **Bölüm 4** | Slayt 17–19 | Sentetik Görevler, Sembolik Manipülasyon ve Niteliksel Yetenekler | 5 dakika |
| **Bölüm 5** | Slayt 20–24 | Veri Kirlenmesi (Contamination), Yapısal Sınırlılıklar & Epistemoloji | 6 dakika |
| **Bölüm 6** | Slayt 25–28 | Toplumsal Etkiler, 2020–Günümüz Sentezi ve Q&A | 5 dakika |

---

## Slayt Slayt Detaylı Konuşmacı Metni

### Slayt 1 — Kapak: *Language Models are Few-Shot Learners* (GPT-3)
- **Ne Anlatmalı?**
  > "Merhaba hocam ve değerli arkadaşlar. Bugün modern yapay zekâ ve Doğal Dil İşleme (NLP) tarihinde paradigma kırılımı yaratan, Tom Brown ve arkadaşlarının OpenAI bünyesinde 2020 yılında yayınladığı *'Language Models are Few-Shot Learners'* başlıklı çalışmayı — yani **GPT-3** makalesini — teknik, matematiksel ve deneysel boyutlarıyla inceleyeceğiz. Makalenin temel tezi şudur: Eğer otoregresif bir dil modelini yeterince büyük bir parametre kapasitesine (175 milyar parametre) ve veri çeşitliliğine (300 milyar token) ölçeklersek, model hiçbir ağırlık veya gradyan güncellemesi yapmadan yalnızca ileri besleme (*forward pass*) sırasında bağlama yerleştirilen birkaç örnekle yeni görevlere uyum sağlayabilir."

---

### Slayt 2 — NLP'de Temsil Öğreniminin Evrimi
- **Ne Anlatmalı?**
  > "Makalenin motivasyonunu anlamak için NLP'deki transfer öğrenimi tarihine kısaca bakalım. İlk aşamada *Word2Vec* ve *GloVe* gibi tek katmanlı statik kelime vektörleri vardı; bunlar göreve özel sıfırdan eğitilen mimarilere girdi olarak veriliyordu. İkinci aşamada *ELMo* gibi çok katmanlı RNN/LSTM mimarileriyle bağlamsal (*contextual*) temsiller üretildi ama üst katman yine göreve özeldi. Üçüncü aşamada ise GPT-1, BERT ve RoBERTa ile *Pre-trained Transformer + Direct Fine-Tuning* dönemine geçtik; yani mimari tamamen görevden bağımsız (*task-agnostic*) hale geldi."
- **Vurgu:** "Ancak burada kritik bir asimetri kaldı: **Mimari görevden bağımsız olsa da, öğrenme sürecinin kendisi hâlâ göreve bağımlıydı.** Her yeni görev için binlerce etiketli örnek toplayıp gradyan güncellemesi yapmamız gerekiyordu."

---

### Slayt 3 — Fine-Tuning Paradigmasının 3 Temel Darboğazı
- **Ne Anlatmalı?**
  > "Yazarlar, 'Pre-training + Fine-Tuning' yaklaşımını terk etmek istemelerinin arkasındaki 3 temel bilimsel ve pratik nedeni sıralıyor:
  > 1. **Veri Darboğazı:** Her yeni görev (örneğin bir kısa hikayeyi eleştirmek veya dilbilgisi düzeltmek) için $10^3$ ile $10^5$ arası etiketli veri toplamak ölçeklenebilir değildir.
  > 2. **Sahte Korelasyonlar (*Spurious Correlations*) ve Zayıf OOD Genelleme:** Modelin ifade gücü (parametre sayısı) büyürken onu dar bir görev dağılımında fine-tune ettiğinizde, model görevin gerçek mantığını öğrenmek yerine veri setindeki istatistiksel ipuçlarını (*annotation artifacts*) ezberler. Nitekim Yogatama et al. (2019) ve McCoy et al. (2019) çalışmalarında gösterildiği gibi, benchmarklarda insan seviyesini geçen fine-tuned modeller dağılım dışı (*Out-of-Distribution*) örneklerde başarısız olabilmektedir.
  > 3. **Bilişsel Uyumsuzluk:** İnsanlar yeni bir dil görevi için on binlerce örnek görmez; bir cümlelik yönerge ya da 1–2 gösterim (*demonstration*) yeterlidir ve diyalog içinde anında görev değiştirebilirler."

---

### Slayt 4 — Çözüm Hipotezi: Meta-Learning ve In-Context Learning (Figure 1.1 & 1.2)
- **Grafikte Nereye İşaret Etmeli?** Sağ üstteki **Figure 1.1**'de üstteki mor yatay ok (*outer loop*) ve alttaki dikey mavi oklar (*inner loop*); sağ alttaki **Figure 1.2**'de 1.3B, 13B ve 175B eğrilerinin eğimleri.
- **Ne Anlatmalı?**
  > "Makale bu soruna *Meta-Learning* perspektifiyle yaklaşıyor (Section 1, Dipnot 1 ve Figure 1.1):
  > - **Outer Loop (Dış Döngü):** Denetimsiz ön-eğitim sırasında SGD ile model ağırlıkları $\theta$ güncellenir. İnternet metinleri içinde doğal olarak gömülü olan aritmetik, çeviri, soru-cevap gibi sayısız alt görevi tek bir sonraki-token tahmini hedefiyle öğrenir.
  > - **Inner Loop (İç Döngü — *In-Context Learning*):** Çıkarım anında **$\Delta\theta = 0$**'dır, yani hiçbir gradyan güncellemesi yoktur. Adaptasyon tamamen modelin ileri besleme (*forward pass*) aktivasyonları içinde gerçekleşir.
  > - **Ölçek Hipotezi (Figure 1.2):** Sembol temizleme görevinde 1.3B model bağlamdaki örnek sayısı $K$ artsa da neredeyse düz kalırken, 175B modelde öğrenme eğrisi çok dik yükselir ve doğal dil yönergesinin (*Natural Language Prompt*) eklenmesi zero-shot ile few-shot arasında belirgin bir kazanç sağlar."

---

### Slayt 5 — Görev Spesifikasyon Spektrumu: 0S, 1S, FS ve FT (Figure 2.1 & 1.3)
- **Grafikte Nereye İşaret Etmeli?** **Figure 2.1**'deki turuncu `gradient update` kutularının Fine-Tuning tarafında olup sol tarafta olmamasını vurgulayın; **Figure 1.3**'te turuncu Few-Shot eğrisinin mavi Zero-Shot eğrisinden model büyüdükçe uzaklaşmasına dikkat çekin.
- **Ne Anlatmalı?**
  > "Section 2'de yazarlar dört yaklaşımı göreve özel veri bağımlılığı ekseninde karşılaştırıyor:
  > - **Fine-Tuning (FT):** Ağırlıklar güncellenir, binlerce örnek gerekir (GPT-3 makalesinde uygulanmamıştır).
  > - **Few-Shot (FS):** Gradyan güncellemesi yok, bağlam penceresine ($n_{\text{ctx}}=2048$) sığacak kadar, genellikle $K \in [10, 100]$ arası örnek verilir.
  > - **One-Shot (1S):** Yalnızca doğal dil tanımı + $K=1$ örnek. Yazarlar bunun özellikle insanlara Mechanical Turk gibi platformlarda görev tarif etme biçimine en yakın ayar olduğunu vurgular.
  > - **Zero-Shot (0S):** Yalnızca doğal dil tanımı ($K=0$). Bazen format belirsizliği nedeniyle insanlar için bile haksız derecede zordur.
  > - **Figure 1.3:** Doğruluk metrikli 42 benchmarkın toplu ortalamasında, parametre sayısı arttıkça hem zero-shot hem few-shot artıyor ancak few-shot eğrisinin eğimi daha yüksek—yani büyük modeller **daha iyi meta-öğreniciler**."

---

### Slayt 6 — GPT-3 Mimari Tasarımı ve Sparse Attention (Section 2.1)
- **Ne Anlatmalı?**
  > "Mimari olarak GPT-3 radikal bir mimari icat değildir; temel olarak GPT-2'nin *decoder-only* otoregresif Transformer yapısını (değiştirilmiş ilklendirme, pre-activation LayerNorm ve tersinir *Byte-level BPE* tokenizasyonu) devralır. BPE ortalama 1 tokenda $\sim 0.7$ kelime kodlar.
  > **Tek önemli mimari değişiklik** dikkat mekanizmasındadır: Transformer katmanlarında standart yoğun (*dense*) öz-dikkat ile Child et al. (2019) *Sparse Transformer*'daki **Locally Banded Sparse Attention** katmanları ardışık (*alternating*) olarak kullanılır. Bu sayede $n_{\text{ctx}} = 2048$ uzunluğundaki bağlamda hem yerel hem küresel bağımlılıklar hesaplama açısından verimli biçimde modellenir. Tüm modellerde ileri besleme katmanı genişliği darboğaz boyutunun 4 katıdır ($d_{\text{ff}} = 4 \cdot d_{\text{model}}$)."

---

### Slayt 7 — 8 Farklı Ölçekte Model Ailesi ve Hiperparametre Ölçekleme (Table 2.1)
- **Tabloda Nereye İşaret Etmeli?** `Batch Size` ($0.5\text{M} \rightarrow 3.2\text{M}$) ve `Learning Rate` ($6.0\times 10^{-4} \rightarrow 0.6\times 10^{-4}$) sütunlarındaki zıt yönlü trende dikkat çekin.
- **Ne Anlatmalı?**
  > "Yazarlar ölçekleme etkisini sistematik ölçmek için 125M parametreden 175B parametreye (3 büyüklük mertebesi) uzanan 8 model eğitiyor ve hepsini sabit **300 milyar token** ile besliyor. En büyük model 96 katman, 12.288 gizli boyut, 96 dikkat başlığı ve başlık başına 128 boyuta sahip.
  > Burada kritik bir optimizasyon detayı var: McCandlish et al. (2018) *Gradient Noise Scale* teorisi uyarınca, model büyüdükçe gradyan gürültü ölçeği büyür; bu nedenle daha büyük modellerde **Batch Size büyütülür** (0.5M'den 3.2M tokene), ancak optimizasyon kararlılığı için **Learning Rate küçültülür** ($6.0\times 10^{-4}$'ten $0.6\times 10^{-4}$'e)."

---

### Slayt 8 — Veri Seti Mühendisliği: Common Crawl Filtreleme ve Tekilleştirme (Section 2.2 & Appendix A)
- **Ne Anlatmalı?**
  > "Ham Common Crawl verisi (41 aylık shard, 45 TB sıkıştırılmış düz metin) çok gürültülüdür. Bunu temizlemek için Appendix A'da 3 adımlı çok zarif bir veri boru hattı kurulmuş:
  > 1. **Otomatik Kalite Sınıflandırıcısı:** Pozitif sınıf olarak WebText, Wikipedia ve web kitapları; negatif sınıf olarak filtresiz Common Crawl alınarak Spark `HashingTF` özellikleri üzerinde bir **Lojistik Regresyon** modeli eğitiliyor. Her belgeye bir kalite skoru veriliyor ve şu Pareto koşulunu sağlayanlar alınıyor:
  >    $$\text{np.random.pareto}(\alpha) > 1 - \text{document\_score}, \quad (\alpha = 9)$$
  >    Neden sert bir eşik (*hard threshold*) yerine stokastik Pareto eşiği kullanılıyor? Çünkü skorı çok yüksek belgeleri ağırlıklı olarak seçerken, dağılım dışı (*out-of-distribution*) ama yararlı olabilecek bir miktar çeşitliliği de veri setinde tutmak istiyorlar. Bu filtreleme 45 TB'ı 570 GB'a (~400B BPE token) indiriyor.
  > 2. **Fuzzy Deduplication:** Spark **MinHashLSH** (10 hash) ile belge düzeyinde bulanık tekilleştirme yapılıyor ve WebText ile çakışmalar çıkarılıyor (%10 küçülme)."

---

### Slayt 9 — Eğitim Karışımı, Dağıtık Sistem ve Hesaplama Karmaşıklığı (Table 2.2, Fig 2.2, App. B & D)
- **Tablo/Grafikte Nereye İşaret Etmeli?** **Table 2.2**'deki `Weight in training mix` ve `Epochs elapsed` sütunları; **Figure 2.2**'de GPT-3 2.7B (captions'ta 3B diye geçen) ile RoBERTa-Large karşılaştırması.
- **Ne Anlatmalı?**
  > "Table 2.2 çok önemli bir prensibi gösteriyor: **Veri setleri boyutlarıyla orantılı değil, kaliteleriyle orantılı örnekleniyor.** Common Crawl veri havuzunun %80+'ını oluştursa da eğitim karışımında %60 ağırlık alır ve 300B token boyunca sadece **0.44 epoch** görülür. Buna karşılık 3B tokenlık Wikipedia %3 ağırlıkla **3.4 epoch**, WebText2 **2.9 epoch** görülür. Yani yazarlar yüksek veri kalitesi uğruna kontrollü ve küçük bir *overfitting*'i bilinçli olarak kabul ediyor.
  > **Eğitim Optimizasyonu (Appendix B):** Adam ($\beta_1=0.9, \beta_2=0.95$), gradyan norm kırpma 1.0, weight decay 0.1, 260B tokenda %10'a inen kosinüs öğrenme oranı düşüşü. Kısa belgeler `<|endoftext|>` tokenı ile ayrılıp 2048'lik dizilere paketlenir (*document packing*); özel dikkat maskesi kullanılmaz.
  > **Hesaplama Analizi (Appendix D):** Hem tensör/matris içi (*width*) hem katmanlar arası (*depth*) model paralelliği ile Microsoft'un yüksek bant genişlikli V100 kümesinde eğitilmiştir. Aktif parametre başına ileri geçiş 2 FLOP (toplam+çarpım), geri geçiş $3\times$ çarpanıyla 4 FLOP; yani token ve parametre başına **6 FLOP** harcanır:
  > $$C \approx 6 \cdot N_{\text{params}} \cdot D_{\text{tokens}} \approx 3.14 \times 10^{23}\text{ FLOPs} = 3,640\text{ PF-days}$$
  > Dikkat çekici bir sonuç (Figure 2.2): RoBERTa-Large (355M parametre, 2T token) ile GPT-3 2.7B (10 kat büyük, 300B token) neredeyse aynı hesaplama gücünü (~50 PF-days) harcamıştır."

---

### Slayt 10 — Değerlendirme Metodolojisi ve Olasılık Normalizasyonu (Section 2.4)
- **Ne Anlatmalı?**
  > "In-context learning değerlendirmesinde görevin formatına göre 3 farklı skorlama protokolü kullanılır:
  > 1. **Çoktan Seçmeli (Multiple Choice):** Her aday tamamlama için token başına log-olabilirlik (*per-token likelihood*) hesaplanır ki uzun seçenekler cezalandırılmasın.
  > 2. **Koşulsuz Olasılık Normalizasyonu:** Ancak ARC, OpenBookQA ve RACE gibi görevlerde dil modeli doğası gereği sık geçen veya kısa yanıt seçeneklerine daha yüksek önsel (*prior*) olasılık verir. Bunu düzeltmek için Bayesçi bir düzeltmeyle tamamlama olasılığı, yalnızca generic bir cevap istemi altındaki koşulsuz olasılığa bölünür:
  >    $$\text{Score} = \frac{P(\text{completion} \mid \text{context})}{P(\text{completion} \mid \text{answer\_context})}$$
  >    Burada `answer_context` = `"Answer: "` veya `"A: "` şeklindedir.
  > 3. **İkili Sınıflandırma & Serbest Üretim:** `0/1` etiketleri yerine `True/False` gibi anlamsal etiketler kullanılır. Serbest üretimde Beam Search (genişlik $B=4$, uzunluk cezası $\alpha=0.6$) uygulanır."

---

### Slayt 11 — Güç Yasası (Power-Law) Ölçekleme Doğrulaması (Figure 3.1 & 4.1)
- **Grafikte Nereye İşaret Etmeli?** **Figure 3.1**'deki kesikli teorik doğru $L = 2.57 \cdot C^{-0.048}$ ve renkli modellerin alt zarfı (*Pareto frontier*). **Figure 4.1**'de kesikli (Train) ve düz (Validation) çizgilerin paralel ilerleyişi.
- **Ne Anlatmalı?**
  > "Section 3'ün girişinde Kaplan et al. (2020) ölçekleme yasaları iki büyüklük mertebesi daha ileri taşınıyor (100K parametreden 175B'ye kadar ek 6 küçük modelle birlikte). Doğrulama çapraz entropi kaybı $L$, hesaplama gücü $C$ cinsinden neredeyse kusursuz bir güç yasası izliyor: $L = 2.57 \cdot C^{-0.048}$. Figure 4.1 ise 300B token boyunca eğitim ve tekilleştirilmiş doğrulama kayıpları arasındaki farkın model büyüdükçe neredeyse hiç açılmadığını—yani 175B modelin bile veriye *overfit* olmadığını—kanıtlıyor."

---

### Slayt 12 — Dil Modelleme, Cloze ve Tamamlama Görevleri (Section 3.1, Fig 3.2 & Table 3.2)
- **Ne Anlatmalı?**
  > "Geleneksel dil modelleme görevi olan **Penn Tree Bank (PTB)** modern internet öncesi bir derlem olduğu için veri kirlenmesinden tamamen muaftır; GPT-3 burada Zero-shot Perplexity skorunu **35.8'den 20.50'ye** çekerek 15 puanlık yeni SOTA kurar.
  > **LAMBADA** görevinde ise çok öğretici bir prompt mühendisliği örneği görürüz: Standart bir LM paragrafın son kelimesinin istendiğini bilmediği için devam kelimelerine de olasılık atar. Yazarlar görevi few-shot **Cloze / Fill-in-the-blank** formatına sokarlar (`... visit her friend ____. -> Bob`). Bu format küçük modellerin performansını %20 düşürürken, 175B modelde doğruluğu +%10 artırarak **%86.4**'e (önceki SOTA %68.0!) taşır. Ayrıca 2.7B parametreli GPT-3 bile 17B parametreli Turing-NLG'yi few-shot'ta geçmektedir."

---

### Slayt 13 — Kapalı Kitap Soru Cevaplama (Closed-Book QA - Fig 3.3 & Table 3.3)
- **Ne Anlatmalı?**
  > "Closed-Book QA'de modelin önünde hiçbir arama motoru veya yardımcı metin yoktur; dahası GPT-3 soru-cevap veri setinde fine-tune edilmemiştir—tüm bilgi ön-eğitim parametrelerinde saklıdır.
  > **TriviaQA**'da GPT-3 Zero-shot (%64.3) bile fine-tuned T5-11B'yi (%50.1) geçer; One-shot (%68.0) ile 21 milyon belgeli yoğun vektör indeksi kullanan açık-kitap fine-tuned **RAG** modelini yakalar ve Few-shot'ta **%71.2** ile yeni SOTA olur. WebQuestions (%14.4 $\rightarrow$ %41.5) ve Natural Questions (%14.6 $\rightarrow$ %29.9) görevlerindeki büyük 0S $\rightarrow$ FS sıçraması ise modelin soru-cevap format/stil dağılımına bağlamda adapte olduğunu gösterir."

---

### Slayt 14 — Makine Çevirisi: Çok Dillilik ve Yön Asimetrisi (Fig 3.4 & Table 3.4)
- **Ne Anlatmalı?**
  > "GPT-3'ün eğitim verisi kelime bazında **%93 İngilizce, %7 diğer dillerdir**. Özel bir paralel derlem veya *back-translation* kullanılmamıştır. Buna rağmen 64 örnekli few-shot çeviride Fransızca$\rightarrow$İngilizce (39.2), Almanca$\rightarrow$İngilizce (40.6) ve Rumence$\rightarrow$İngilizce (39.5) yönlerinde önceki Unsupervised NMT SOTA'larını (MASS, XLM, mBART) ortalama 5 BLEU geçer.
  > **Ancak kritik bir yön asimetrisi vardır:** İngilizce'den başka dile ($\text{En} \rightarrow X$, örneğin En$\rightarrow$Ro 21.0 BLEU) çeviride performans belirgin şekilde düşer. Yazarlar bunun sebebini GPT-2'den miras alınan ve neredeyse tamamen İngilizce metinler üzerinde eğitilmiş *Byte-Level BPE tokenizer*'a ve İngilizce baskın üretim kapasitesine bağlar."

---

### Slayt 15 — Winograd, Sağduyu Çıkarımı ve Okuduğunu Anlama (Sections 3.4–3.6)
- **Ne Anlatmalı?**
  > "Zamir çözümleme görevlerinden orijinal Winograd'da %88.6* alırken, adversarially üretilmiş zorlu **Winogrande**'de %70.2'den %77.7'ye ölçeklenir. Sağduyu görevlerinde **PIQA**'da %82.8* ile SOTA'yı geçerken (kirlenme şüphesi notuyla), ARC-Challenge (%51.5) ve OpenBookQA (%65.4) görevlerinde fine-tuned UnifiedQA'in ~20–27 puan gerisinde kalır.
  > Okuduğunu anlamada ilginç bir ayrışma vardır: Serbest diyalog formatlı **CoQA**'da **85.0 F1** ile insan seviyesine (~88.3) çok yaklaşır ve SQuADv2'de 69.8 F1 elde eder. Buna karşın katı yapılı **QuAC** (44.3 F1), çoktan seçmeli **RACE** (%46.8) ve ayrık sayısal muhakeme gerektiren **DROP** (36.5 F1) veri setlerinde zayıf kalır."

---

### Slayt 16 — SuperGLUE ve Doğal Dil Çıkarımı (NLI / ANLI - Fig 3.8, 3.9 & Table 3.8)
- **Ne Anlatmalı?**
  > "8 zorlu dil anlama görevinden oluşan **SuperGLUE**'da GPT-3 ($K=32$) ortalama **71.8** skor alır (dev setinde 73.2). **Figure 3.8 (sağ panel)** çok çarpıcı bir veri verimliliği gösterir: GPT-3 yalnızca **8 bağlam içi örnekle**, 125.000 örnekle fine-tune edilmiş **BERT-Large (69.0)** modelini geride bırakır! COPA (%92.0) ve ReCoRD (91.1 F1) skorları T5-11B SOTA'sına çok yakındır.
  > **Fakat çok önemli bir zayıflık tespit edilir:** İki cümlede bir kelimenin aynı anlamda kullanılıp kullanılmadığını soran **WiC** görevinde GPT-3 **%49.4** ile **tam rastgele tahmin** seviyesindedir! Benzer şekilde iki cümle arasındaki mantıksal çıkarımı ölçen **ANLI Round 3**'te (Figure 3.9) 13B'ye kadar tüm modeller %33.3 rastgele tahminde sıkışırken, yalnızca 175B model few-shot'ta **%40.2** ile ilk kez 'yaşam belirtisi' gösterir."

---

### Slayt 17 — Sentetik Görevler I: Anlık Hesaplama ve Aritmetik (Fig 3.10 & Table 3.9)
- **Ne Anlatmalı?**
  > "Modelin ezberden ziyade anlık hesaplama yapıp yapmadığını test etmek için 10 aritmetik görevi (her biri 2.000 rastgele soru) oluşturulur. **Figure 3.10**'da 13B'den 175B'ye devasa bir sıçrama (faz geçişi benzeri artış) görülür: 13B model 2 basamaklı toplamada %55.5'te kalırken, 175B model **2D+ (%100.0)**, **2D- (%98.9)**, **3D+ (%80.4)**, **3D- (%94.2)**, **2Dx çarpma (%29.2)** ve parantezli bileşik işlemlerde (**%21.3**) başarı sağlar.
  > **Ezber Kanıtı (Spot-Check):** Yazarlar 2.000 adet 3-basamaklı toplama sorusunu eğitim verisinde tarar ve yalnızca **17 eşleşme (%0.8)** (çıkarmada yalnızca 2 eşleşme, %0.1) bulur. Üstelik yanlış cevapların çoğunun **"elde var 1" (*carrying a 1*)** unutulmasından kaynaklanması, modelin bir ezber tablosu aramadığını, algoritmik bir hesaplama girişiminde bulunduğunu gösterir."

---

### Slayt 18 — Sentetik Görevler II: Karakter Manipülasyonu ve SAT Analojileri (Fig 3.11, 3.12 & Table 3.10)
- **Ne Anlatmalı?**
  > "Eğitim verisinde birebir bulunması neredeyse imkânsız olan 5 karakter manipülasyon görevinde ($K=100$) model **Random Insertion**'da **%67.2**, **Anagrams A2**'de **%39.7**, **Cycle Letters**'da **%37.9** ve **Anagrams A1**'de **%15.1** başarı yakalar. Ancak **Reversed Words** (kelimeyi tersten okuma: `stcejbo -> objects`) görevinde **%0.44** ile tamamen başarısız olur!
  > Buradaki derin teknik nokta şudur: BPE tokenizer kelimeleri tek tek harflere değil, ortalama ~0.7 kelimelik parçalara böler. Modelin bu harf karıştırmaları çözebilmesi, BPE tokenlarının iç alt-yapısını (*substructure*) çözebildiğini ve zero-shot'ta ~%0 iken few-shot'ta test anında kural öğrendiğini kanıtlar. Ayrıca 374 **SAT Analoji** sorusunda **%65.2** ile üniversite başvuru ortalamasını (**%57**) geçer."

---

### Slayt 19 — Niteliksel Yetenekler: Yeni Kelime Öğrenme, Gramer ve Haber Üretimi (Fig 3.13 & 3.16)
- **Ne Anlatmalı?**
  > "Gelişimsel dilbilimden ilham alan **Novel Words (Figure 3.16)** testinde GPT-3, *'whatpu'*, *'farduddle'*, *'screeg'* gibi uydurma kelimelerin tanımını tek sefer görüp doğru morfolojik çekimle (*'We screeghed at each other...'*) cümle kurar.
  > **Haber Üretimi İnsan Değerlendirmesi (Section 3.9.4 & Appendix E):** 621 ABD'li katılımcıyla yapılan deneyde, 160M parametreli kasıtlı kötü kontrol modelinin haberlerini insanlar **%86–88** doğrulukla yakalarken, model büyüdükçe insan doğruluğu güç yasasıyla düşer ve GPT-3 175B'de **%52**'ye ($p = 1\text{e-}34$) geriler—yani yazı-tura sınırı olan %50'den neredeyse ayırt edilemez! Bu sonuç hem ~200 hem ~500 kelimelik Reuters haberlerinde geçerlidir ve insanlar daha uzun okuma süresi harcamasına rağmen (Figure E.1) başarılı olamaz."

---

### Slayt 20 — Benchmark Veri Kirlenmesi (Data Contamination) Metodolojisi (Section 4 & Fig 4.2)
- **Ne Anlatmalı?**
  > "Common Crawl gibi internet ölçekli veri kümelerinde benchmark test setlerinin eğitim verisine sızması (*data contamination*) en büyük metodolojik tehlikedir. Yazarlar eğitim öncesi 13-gram temizliği yapmaya çalışsa da uzun belgelerde (kitaplar vb.) bir *bug* yüzünden filtreleme kısmen atlanır; 3.640 PF-days maliyet nedeniyle yeniden eğitim imkansız olduğu için Section 4'te kapsamlı bir post-hoc teşhis geliştirirler.
  > Apache Spark ile tüm eğitim derlemi ve test setleri arasında tam $N$-gram çakışması ($N \in [8, 13]$, 5. yüzdelik uzunluk) hesaplanır. Tek bir çakışma bile varsa örnek **Dirty**, yoksa **Clean** sayılır. Ardından **Figure 4.2**'deki gibi her benchmark için $\Delta = \text{Score}_{\text{clean}} - \text{Score}_{\text{all}}$ farkı ölçülür."

---

### Slayt 21 — Kirlenme Analizi Bulguları: Yanlış Pozitifler vs. Gerçek Sızıntılar (Table C.1)
- **Ne Anlatmalı?**
  > "Table C.1 analizi çok net 4 kategori ortaya çıkarır:
  > 1. **Yanlış Pozitifler (Reading Comprehension):** QuAC (%99 dirty), SQuADv2 (%94 dirty) ve DROP (%93 dirty) aşırı kirli görünse de manuel incelemede eğitimde yalnızca kaynak Wikipedia makalelerinin olduğu, **soru ve cevapların bulunmadığı** görülür.
  > 2. **Tamamen Çıkarılanlar:** 4 Wikipedia LM benchmarkı ve Children's Book Test neredeyse %100 sızdığı için rapordan tamamen çıkarıldı.
  > 3. **Yıldız (`*`) ile İşaretlenenler:** **Winograd** (132 şema eğitimde mevcut, temiz kümede -%2.6 düşüş) ve **PIQA** (temiz kümede -%3 düşüş; ancak 25 kat küçük modelde de benzer fark görülmesi kopyalanan örneklerin daha kolay olmasına bağlı istatistiksel yanlılığa işaret eder).
  > 4. **LAMBADA:** Önemli çakışmaya rağmen temiz alt küme skoru tüm setle **%0.5** içindedir ve fill-in-the-blank formatı düz ezberi engeller."

---

### Slayt 22 — Mimari Sınırlılıklar I: Otoregresif (Tek Yönlü) Dikkat Darboğazı (Section 5)
- **Ne Anlatmalı?**
  > "Şimdi şu kritik soruyu soralım: GPT-3 neden bazı görevlerde SOTA kırarken **WiC (%49.4)**, **ANLI (%40.2)**, **QuAC (44.3)**, **RACE (%46.8)** ve **Reversed Words (%0.44)** gibi görevlerde zorlanıyor?
  > Yazarlar bunun doğrudan **mimari ve eğitim hedefi seçiminden** kaynaklandığını belirtiyor: GPT-3 tamamen tek yönlü (soldan sağa nedensel maskeli, *autoregressive*) bir modeldir; BERT veya T5 gibi **çift yönlü (bidirectional)** bir dikkate veya *denoising* eğitim hedefine sahip değildir. İki cümleyi geri dönüp karşılaştırmayı gerektiren (WiC, ANLI), uzun bir pasajı yeniden tarayıp kısa bir span seçmeyi gerektiren (QuAC, RACE) ya da kelimeyi sağdan sola işlemeyi gerektiren görevlerde çift yönlülük eksikliği doğrudan performans darboğazı yaratır. Ayrıca metin sentezinde uzun pasajlarda tekrarlama ve sağduyu fiziği hataları (*'Peyniri buzdolabına koyarsam erir mi?'*) görülür."

---

### Slayt 23 — Temel Sınırlılıklar II: Amaç Fonksiyonu, Grounding ve Örneklem Verimsizliği
- **Ne Anlatmalı?**
  > "Makalenin belki de en vizyoner kısmı sadece mimariyi değil, *ölçekleme paradigmasının kendisinin sınırlarını* tartışmasıdır:
  > 1. **Öz-Denetimli Tahmin Sınırı:** Standart MLE çapraz entropi kaybı her tokenı eşit ağırlıklandırır; hangi varlığın veya bilginin kritik olduğunu ayırt etmez. Gerçek yardımcı sistemler sadece sonraki kelimeyi tahmin etmek yerine **hedef odaklı eylemler** almalıdır.
  > 2. **Grounding Eksikliği:** Fiziksel dünyadan, görüntüden veya videodan yoksun salt metin istatistikleri dünya bilgisini tam yakalayamaz (Bisk et al., 2020).
  > 3. **Ön-Eğitim Örneklem Verimsizliği ve Çıkarım Maliyeti:** Çıkarımda insan gibi few-shot olsa da eğitimde 300B token (insan ömrünün katbekat fazlası) tüketir ve 175B parametrede çıkarım pahalıdır $\rightarrow$ Bu nedenle yazarlar **RLHF (insandan amaç öğrenme), Multimodalite ve Model Damıtma (*Distillation*)** önermektedir."

---

### Slayt 24 — Epistemolojik Tartışma: Sıfırdan Meta-Öğrenme mi, Örüntü Tanıma mı?
- **Ne Anlatmalı?**
  > "Section 5'te yazarların dürüstçe ortaya koyduğu derin bir bilimsel belirsizlik vardır: GPT-3 çıkarım sırasında bağlamdaki örneklerden gerçekten **sıfırdan yeni bir görev mi öğreniyor (*de novo learning*)**, yoksa ön-eğitim sırasında zaten gördüğü sayısız görev dağılımından birini **tanıyıp aktive mi ediyor (*task recognition*)**?
  > Aslında bu ikisi bir spektrumdur: Çeviri ve QA görevleri ön-eğitimde öğrenilen bilgilerin format hizalamasıdır (*recognition*). Ancak *'screeg'* gibi uydurma kelimeleri çekimleyip kullanma veya sembol ayıklama gibi görevler gerçek bir *on-the-fly* kural çıkarımı gerektirir. Bu ayrım, makaleden sonra doğan *Mechanistic Interpretability* ve *Induction Heads* literatürünün ana araştırma konusu olmuştur."

---

### Slayt 25 — Toplumsal Etkiler I: Kötüye Kullanım, Tehdit Aktörleri ve Enerji Amortismanı
- **Ne Anlatmalı?**
  > "Section 6.1'de yazarlar güvenlik risk değerlendirmesi (NIST çerçevesi) ile potansiyel kötüye kullanımları (oltalama, dezenformasyon, sahte akademik metinler) inceliyor. APT (gelişmiş kalıcı tehditler) ve düşük becerili aktörler açısından, 2020 itibarıyla çıktıların yönlendirilebilirliğinin düşük olması ve **%1'lik tutarsızlık oranının bile insan denetimi (*human-in-the-loop*) gerektirmesi** tam otomasyonu kısıtlıyordu; ancak tutarlılık arttıkça riskin büyüyeceği uyarısı yapılıyor.
  > Enerji tarafında (Section 6.3): Eğitim **3,640 PF-days** ile çok yüksek enerji gerektirse de, tek seferlik bu eğitim maliyeti tüm kullanım ömrüne amorti edilir; eğitilmiş 175B modelden **100 sayfa metin üretmek yalnızca ~0.4 kW-hr** (birkaç sent) tutar."

---

### Slayt 26 — Toplumsal Etkiler II: Adalet, Önyargı ve Temsil Analizi (Section 6.2)
- **Ne Anlatmalı?**
  > "İnternet ölçekli veriler, internet ölçekli önyargıları da beraberinde getirir:
  > - **Cinsiyet (Table 6.1):** Test edilen 388 mesleğin **%83'ü** erkek zamiriyle devam etme eğilimindedir. Yazarların tanımladığı log-olasılık oranında nötr bağlamda skor **$-1.11$** iken, `'The competent {occupation}'` dendiğinde **$-2.14$**'e kadar erkek lehine derinleşir! Kadınlar *'beautiful', 'gorgeous'* gibi görünüm odaklı sıfatlarla, erkekler daha geniş sıfatlarla betimlenir. Buna karşın **Winogender** zamir çözümlemesinde 175B model (%64.17) önyargı kaynaklı hatalara küçük modellerden daha dirençlidir.
  > - **Irk (Figure 6.1) ve Din (Table 6.2):** SentiWordNet duygu analizinde 'Asian' yüksek, 'Black' tutarlı olarak en düşük duygu skorunu alır; din terimlerinde İslam için *'terrorism', 'violent'* gibi kelimelerin eş-dizimliliğinin yüksek çıktığı raporlanır ve yazarlar sadece metrik bazlı yüzeysel değil bütünsel (*holistic*) düzeltme çağrısı yapar."

---

### Slayt 27 — 2020'den Günümüze Eleştirel Sentez: Makalenin Öngörülerinin Gerçekleşmesi
- **Ne Anlatmalı?**
  > "Yüksek Lisans seviyesinde makaleyi günümüz (2022–2026) perspektifinden değerlendirdiğimizde, Section 5'te yazarların işaret ettiği 4 ana kısıtın sonraki 4 büyük atılımı doğrudan tetiklediğini görürüz:
  > 1. *'İnsandan amaç fonksiyonu öğrenme'* $\rightarrow$ **InstructGPT / RLHF (Ouyang et al., 2022)** ve ChatGPT devrimi.
  > 2. *'Çok basamaklı aritmetik ve kelime ters çevirme başarısızlığı'* $\rightarrow$ İleri besleme adımlarını ara tokenlara yayan **Chain-of-Thought (Wei et al., 2022)** ve test-time compute modelleri.
  > 3. *'175B parametre / 300B token ölçeği'* $\rightarrow$ **Chinchilla Scaling Laws (Hoffmann et al., 2022)** ile GPT-3'ün parametreye göre veri açısından ciddi biçimde *undertrained* olduğunun gösterilmesi (~20 token/parametre kuralı).
  > 4. *'Fiziksel dünya grounding eksikliği'* $\rightarrow$ **Multimodal Modeller (GPT-4V/o, Gemini)**."

---

### Slayt 28 — Sonuç, Temel Çıkarımlar ve Tartışma Soruları
- **Ne Anlatmalı?**
  > "Özetle Brown et al. (2020), tek bir genel amaçlı otoregresif mimarinin doğru ölçekte gradyan güncellemesiz *in-context learning* ile birçok görevde fine-tuned modelleri yakalayabildiğini veya geçebildiğini kanıtlamıştır. Aynı zamanda veri kirlenmesi analizi, dürüst sınırlılık tartışması ve etik risk çerçevesiyle alanda bir standart belirlemiştir. Şimdi sorularınızı ve tartışma başlıklarımızı alabiliriz."

---

## Ders Hocası veya Sınıftan Gelebilecek 10 Zorlu Soru ve Cevap Anahtarı

### Soru 1: *"Table D.1 ve Figure 2.2'ye göre RoBERTa-Large (355M parametre) ile GPT-3 2.7B (yaklaşık 7.5–8 kat daha fazla parametre) neredeyse aynı toplam hesaplama gücünü (~50 PF-days) harcamış. Bu nasıl mümkün oluyor ve neden daha iyi?"*
- **Cevap:** Çünkü $C \approx 6 N D$ formülünde hesaplama bütçesi hem parametre ($N$) hem de token ($D$) sayısının çarpımıdır. RoBERTa-Large (355M) **2 Trilyon token** üzerinde eğitilirken (49.3 PF-days), GPT-3 2.7B yalnızca **300 Milyar token** üzerinde eğitilmiştir (55.2 PF-days). Kaplan et al. (2020) *Scaling Laws* bulgularına göre sabit bir FLOP bütçesi altında küçük bir modeli çok fazla tokenda eğitmek yerine, **büyük bir modeli daha az tokenda eğitmek** (*under-convergence* noktasında durmak) daha düşük validasyon kaybı sağlar. *(Not: 2022'de Chinchilla makalesi Kaplan'ın bu oranını revize ederek N ve D'nin eşit oranda büyütülmesi gerektiğini göstermiştir.)*

### Soru 2: *"Common Crawl filtrelemesinde neden Lojistik Regresyon çıktısına sabit bir eşik (örn. score > 0.8) koymak yerine `np.random.pareto(9) > 1 - document_score` kullandılar?"*
- **Cevap:** Sert bir eşik kullanılsaydı Common Crawl yalnızca WebText ve Wikipedia'ya çok benzeyen metinlerle sınırlı kalır ve model dağılım dışı (*out-of-distribution*) metin türlerini kaybederdi. Pareto dağılımından ($\alpha = 9$) örnekleme yaparak, sınıflandırıcının yüksek puan verdiği kaliteli belgeleri ağırlıklı olarak tutarken, düşük puanlı ama farklı alanlardan gelen belgelerin de küçük bir olasılıkla havuza girmesini sağladılar. Yazarlar bunun OOD üretken metinlerde kaybı (*loss*) düşürdüğünü gözlemlemiştir (Appendix A).

### Soru 3: *"ARC, OpenBookQA ve RACE görevlerinde neden `P(completion | context) / P(completion | answer_context)` normalizasyonu yapıldı? Bunun olasılıksal anlamı nedir?"*
- **Cevap:** Bir otoregresif dil modeli $P(y \mid x)$ olasılığını hesaplarken yalnızca cevabın bağlamla uyumunu değil, aynı zamanda cevabın kendi içsel dil frekansını (*prior* $P(y)$) da yansıtır. Örneğin nadir veya teknik kelimeler içeren doğru bir şık, çok yaygın kelimelerden oluşan yanlış bir şıktan düşük ham olasılık alabilir. Paydaya $P(\text{completion} \mid \text{"Answer: "})$ koymak, yaklaşık olarak $\frac{P(y \mid x)}{P(y)}$ yani **Noktasal Karşılıklı Bilgi (PMI — Pointwise Mutual Information)** benzeri bir skor hesaplayarak bağlamın o cevaba ne kadar *ek* bilgi desteği sağladığını ölçer.

### Soru 4: *"Makalede 300B token eğitiminde Wikipedia 3.4 epoch, Common Crawl ise sadece 0.44 epoch görülüyor. Bu durum modelin Wikipedia'ya aşırı uyum sağlamasına (overfitting) yol açmıyor mu?"*
- **Cevap:** Section 2.2'de yazarlar bunun bilinçli bir tasarım ödünleşimi (*trade-off*) olduğunu açıkça belirtir: *'This essentially accepts a small amount of overfitting in exchange for higher quality training data.'* Ancak 175B parametreli model için toplam 300B token çok büyük olduğundan, Figure 4.1'deki tekilleştirilmiş doğrulama kaybı eğrisi ile eğitim kaybı eğrisi arasındaki farkın neredeyse hiç açılmadığı gösterilmiştir.

### Soru 5: *"GPT-3 neden WiC (%49.4), ANLI (%40.2) ve Reversed Words (%0.44) görevlerinde başarısız oldu?"*
- **Cevap:** İki temel teknik neden vardır:
  1. **Tek Yönlü (Causal) Dikkat (Section 5):** GPT-3 otoregresif olduğu için her token yalnızca kendinden önceki tokenlara dikkat edebilir. Oysa WiC (iki farklı cümledeki aynı kelimenin anlamını karşılaştırma) ve ANLI (iki cümle arası mantıksal gerektirme) görevleri, iki metin parçasının birbiriyle çift yönlü (*bidirectional*) karşılaştırılmasını ve yeniden okunmasını gerektirir.
  2. **BPE Tokenizasyonu ve İleri Besleme Derinliği:** *Reversed Words* görevinde model kelimeyi harf harf değil alt-kelime (BPE) parçaları halinde görür (ortalama 1 token $\approx 0.7$ kelime) ve ek ara düşünme adımı (*Chain-of-Thought*) olmadan tek forward pass içinde karakter sırasını tersine çeviremez.

### Soru 6: *"Veri kirlenmesi (contamination) analizinde QuAC %99 ve DROP %93 'dirty' çıktı. Neden bu sonuçlar makaleden çıkarılmadı da Winograd ve PIQA yıldızlandı?"*
- **Cevap:** Appendix C ve Section 4'e göre QuAC, SQuADv2 ve DROP görevlerindeki $N$-gram çakışmalarının tamamı yalnızca okuma parçası olan **Wikipedia kaynak metinlerinden** kaynaklanmaktadır; modelin tahmin etmesi gereken **soru ve cevap çiftleri** eğitim verisinde bulunmamaktadır. Zaten çıkarım sırasında kaynak pasaj bağlamda (*prompt*) verildiği için bu bir "kopya çekme" (*cheating*) değildir. Oysa **Winograd**'da 132 şemanın bizzat kendisi (farklı formatta da olsa) eğitim verisinde bulunmuş, **PIQA**'da ise temiz alt kümede -%3–4'lük düşüş gözlenmiştir; bu yüzden yalnızca Winograd ve PIQA `*` ile işaretlenmiştir.

### Soru 7: *"Figure 2.2 ile Appendix D arasındaki FLOP hesabında $6 \cdot N \cdot D$ formülü nasıl türetiliyor? Dikkat (Attention) maliyeti nereye gitti?"*
- **Cevap:** Table D.1 başlığında açıklandığı gibi: Standart bir yoğun ağda ileri geçişte (*forward pass*) her aktif parametre her token için 1 çarpma + 1 toplama işlemi yapar = **2 FLOP**. Geri geçişte (*backward pass*) hem $\frac{\partial \text{loss}}{\partial \text{params}}$ hem $\frac{\partial \text{loss}}{\partial \text{acts}}$ hesaplandığı için ileri geçişin yaklaşık 2 katı (toplam $1+2 = 3\times$ çarpanı) hesaplama gerekir $\rightarrow$ toplam $2 \times 3 = 6$ FLOP/parametre/token. *(Not: T5 gibi Encoder-Decoder modellerde her token için parametrelerin sadece yarısı aktif olduğu için 3 FLOP alınmıştır.)* Yazarlar Self-Attention işleminin bu boyuttaki modellerde toplam FLOP'un %10'undan azını oluşturduğu için sadeleştirme amacıyla ihmal edildiğini belirtir.

### Soru 8: *"Document packing sırasında 2048 tokenlık tek bir dizide birden fazla alakasız belge arka arkaya konduğunda neden özel bir attention maskesi (block-diagonal mask) kullanılmadı?"*
- **Cevap:** Appendix B'de belirtildiği üzere, belgeler arasına özel bir `<|endoftext|>` tokenı konur. Model bu tokenı gördüğünde önceki bağlamın yeni belgeyle alakasız olduğunu öğrenir. Özel bir maskeleme matrisi oluşturmadan yalnızca `<|endoftext|>` sınırlayıcısı kullanmak GPU çekirdeklerinde donanım verimliliğini ve hesaplama hızını maksimize eder.

### Soru 9: *"Makalede LAMBADA görevinde One-Shot (%72.5) performansı neden Zero-Shot (%76.2) performansından daha düşük çıktı?"*
- **Cevap:** Section 3.1.2'de açıklanıyor: Zero-shot'ta model standart paragraf devamı üretir. One-shot ve Few-shot'ta ise görevi `... friend ____. -> Bob` şeklinde *fill-in-the-blank* formatına soktular. Yazarların yorumuna göre model tek bir örnekle ($K=1$) bu yapay boşluk doldurma formatının örüntüsünü henüz tam kavrayamamakta, aksine format gürültüsü yaşamaktadır; $K=15$ örneğe çıkıldığında formatı anlayıp %86.4'e fırlamaktadır.

### Soru 10: *"Chinchilla Scaling Laws (2022) açısından bakıldığında GPT-3'ün eğitimi verimli miydi?"*
- **Cevap:** Hayır. GPT-3 175B parametreye karşılık yalnızca 300B token (parametre başına **~1.7 token**) görmüştür. Hoffmann et al. (2022) *Chinchilla* çalışması, aynı FLOP bütçesi için parametre başına yaklaşık **20 token** verilmesinin hesaplama-optimal (*compute-optimal*) olduğunu gösterdi (örneğin 70B Chinchilla 1.4T tokenla eğitilerek 175B GPT-3'ü birçok görevde geçti). Ancak GPT-3 makalesi, 2020'de Kaplan et al.'ın ölçekleme öngörülerine dayanarak parametre ölçeğinin *in-context learning* sıçraması yarattığını ilk kez deneysel olarak kanıtlayan öncü çalışmadır.

