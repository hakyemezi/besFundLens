# besFundLens

**Türkiye emeklilik fonları için İngilizce öncelikli, iki dilli raporlamaya hazır analiz motoru.**

besFundLens, emeklilik fonlarının AUM hareketlerini **piyasa etkisi** ve **tahmini yatırımcı akışı** olarak ayrıştırır; portföy DNA'sını haritalar, fon tiplerini sınıflandırır, piyasa-akış rejimlerini belirler ve iki dilli Markdown raporlar üretir.

> Proje şu anda Türkiye BES / emeklilik fonu verilerine odaklanmaktadır. Fiyat tahmin modeli olmaktan ziyade yeniden kullanılabilir bir analiz motoru olarak tasarlanmıştır.

## Bu proje neden var?

Fon analizlerinin çoğu getiri ve AUM değişimi seviyesinde kalır. besFundLens daha derin bir soru sorar:

> AUM piyasalar hareket ettiği için mi değişti, yoksa yatırımcılar para eklediği/çektiği için mi?

Şu analizleri bir araya getirir:

- Fon DNA'sı / portföy dağılımı analizi
- Piyasa kapsamı ve para birimi risk haritalaması
- AUM değişimi ayrıştırması
- Tahmini net yatırımcı akışı
- Katılımcı değişimi analizi
- Fon tipi sınıflandırması
- Piyasa-akış quadrant analizi
- İngilizce ve Türkçe anlatı raporlaması

## Kurulum

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .
```

## SQLite cache ile hızlı başlangıç

SQLite zorunlu değildir; ancak çok yıllı analizler ve tekrar eden iş akışları için önerilir.

```bash
python scripts/fetch_history.py \
  --start 2021-06-15 \
  --end 2026-06-15 \
  --db-path data/besfundlens.sqlite
```

İngilizce rapor üretmek için:

```bash
python scripts/generate_report.py \
  --db-path data/besfundlens.sqlite \
  --lookback 1m \
  --language en \
  --output sample_reports/market_report_en.md
```

Türkçe rapor üretmek için:

```bash
python scripts/generate_report.py \
  --db-path data/besfundlens.sqlite \
  --lookback 1m \
  --language tr \
  --output sample_reports/market_report_tr.md
```

## Python API

```python
from besfundlens.workflows import run_universe_analysis_from_sqlite

result = run_universe_analysis_from_sqlite(
    db_path="data/besfundlens.sqlite",
    lookback="1m",
    language="en",
    top_n=10,
)

print(result["markdown"])
```

Seçili fon karşılaştırması:

```python
from besfundlens.workflows import compare_funds_from_sqlite
from besfundlens.core.engine import selected_funds_report_to_markdown

comparison = compare_funds_from_sqlite(
    db_path="data/besfundlens.sqlite",
    fund_codes=["AAJ", "MHD", "MEA"],
    lookback="1m",
    sort_by="market_effect_pct",
    ascending=False,
)

print(selected_funds_report_to_markdown(comparison, language="en"))
print(selected_funds_report_to_markdown(comparison, language="tr"))
```

## Lookback presetleri

| Preset | Anlamı |
|---|---:|
| `1m` | 20 mevcut fon aralığı |
| `3m` | 60 mevcut fon aralığı |
| `6m` | 120 mevcut fon aralığı |
| `1y` | 240 mevcut fon aralığı |

Proje takvim günü yerine **mevcut gözlemler / aralıklar** kullanır. Bu önemlidir; çünkü fon verileri hafta sonları, resmi tatiller veya eksik yayın tarihleri nedeniyle kesintiye uğrayabilir.

## Veri alma stratejisi

besFundLens iki iş akışını destekler:

1. Hızlı denemeler ve notebook çalışmaları için **doğrudan API modu**.
2. Çok yıllı analizler ve tekrar eden raporlamalar için **SQLite cache modu**.

Cache güncelleyici, dönem değiştirme yaklaşımı kullanır: güncelleme başlangıç tarihinden itibaren kayıtları siler ve yeni çekilen veriyi ekler. Bu bilinçli bir tercihtir; çünkü finansal fon verilerinde geriye dönük düzeltmeler gelebilir.

## Repo yapısı

```text
besfundlens/
  core/       # analiz motoru
  data/       # API istemcisi ve veri yükleyiciler
  storage/    # SQLite cache yardımcıları
  reports/    # markdown rapor yardımcıları
scripts/      # CLI tarzı scriptler
examples/     # küçük demolar
sample_reports/
tests/
```

## Sorumlu veri kullanımı

Bu proje, orijinal araştırma scriptlerinde kullanılan herkese açık fon veri endpoint'lerine dayanır. Lütfen veri çekme yardımcılarını sorumlu şekilde kullanın, aşırı API isteğinden kaçının ve tekrar eden analizlerde SQLite cache kullanımını tercih edin.

## Teşekkür / Not

Bu proje **İlyas Hakyemez** tarafından geliştirilmiş; kodlama, refactoring ve dokümantasyon aşamalarında ChatGPT'den yapay zekâ destekli geliştirme yardımı alınmıştır.

Proje fikri, finansal analiz mantığı, veri doğrulama süreci, testler, yorumlama çerçevesi ve ürün yönü proje sahibi tarafından belirlenmiş ve gözden geçirilmiştir. Yapay zekâ desteği; kod yapısının düzenlenmesi, modülerleştirme, iki dilli raporlama ve GitHub repo hazırlığı süreçlerinde yardımcı geliştirme aracı olarak kullanılmıştır.

## Uyarı

Bu proje araştırma, eğitim ve analitik prototipleme amaçlıdır. Yatırım tavsiyesi değildir.
