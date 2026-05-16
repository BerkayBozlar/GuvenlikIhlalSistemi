# Bulut Tabanlı İhlal Tespit Sistemi (AWS Rekognition)

Bu proje, güvenlik kamerası görüntülerini bulut bilişim servisleri ve yapay zeka kullanarak analiz eden, videolardaki nesneleri (insan, araç vb.) tespit ederek olası ihlalleri anlık olarak raporlayan bir web uygulamasıdır. Proje, video üzerinden nesne tanıma ve etiketleme analizi yapma hedefleri doğrultusunda geliştirilmiştir.

## Proje Amacı
Sisteme yüklenen kısa süreli güvenlik veya gözetim videoları, doğrudan AWS S3 bulut depolama servisine aktarılır. Ardından **AWS Rekognition** (Yapay Zeka ve Görüntü İşleme) API'si tetiklenerek video saniye saniye analiz edilir. Sistem, görüntüde "Person" (İnsan) etiketi yakaladığında ekranda anında kırmızı alarm (İzinsiz Giriş) üretir.

## Kullanılan Teknolojiler
Bu sistem, bulut tabanlı video işleme çözümlerini entegre eden çok katmanlı bir mimariye sahiptir:
* **Backend:** Python & Flask (Web Sunucusu ve API Yönlendirmeleri)
* **Bulut Depolama:** AWS S3 (Kamera kayıtlarının güvenli depolanması)
* **Yapay Zeka (AI):** AWS Rekognition (Derin öğrenme tabanlı video analizi)
* **Frontend:** HTML5, CSS3 (Karanlık tema güvenlik paneli tasarımı)
* **AWS SDK:** Boto3 (Python ile AWS servisleri arası asenkron iletişim)

## Kurulum ve Çalıştırma

**1. Depoyu Klonlayın:**
\`\`\`bash
git clone https://github.com/KULLANICI_ADIN/GuvenlikIhlalSistemi.git
cd GuvenlikIhlalSistemi
\`\`\`

**2. Gerekli Kütüphaneleri Yükleyin:**
\`\`\`bash
pip install flask boto3 python-dotenv
\`\`\`

**3. Çevre Değişkenlerini Ayarlayın:**
Proje dizinindeki `.env.example` dosyasının adını `.env` olarak değiştirin ve kendi AWS kimlik bilgilerinizi girin:
\`\`\`env
AWS_ACCESS_KEY_ID=kendi_access_keyini_gir
AWS_SECRET_ACCESS_KEY=kendi_secret_keyini_gir
AWS_REGION=us-east-1
\`\`\`

**4. S3 Bucket Adını Güncelleyin:**
`app.py` dosyası içerisindeki `BUCKET_ADIM` değişkenine kendi AWS S3 kova adınızı yazın.

**5. Sunucuyu Başlatın:**
\`\`\`bash
python app.py
\`\`\`
Tarayıcınızda `http://127.0.0.1:5000` adresine giderek yönetim panelini açabilirsiniz.
