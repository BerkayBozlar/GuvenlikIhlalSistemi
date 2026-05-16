import os
import time
import boto3
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# AWS İstemcileri
s3_client = boto3.client('s3', region_name=os.getenv('AWS_REGION'))
rekognition_client = boto3.client('rekognition', region_name=os.getenv('AWS_REGION'))

BUCKET_ADIM = "berkay-guvenlik-videolari-2026" # BURAYI KENDİ BUCKET ADINLA DEĞİŞTİR!
S3_KAYIT_ADI = "kamera1_kayit.mp4"

@app.route('/')
def ana_sayfa():
    # Sayfa ilk açıldığında analiz yok
    return render_template('index.html', durum=False)

@app.route('/analiz-et', methods=['POST'])
def analizi_baslat():
    print("Yapay zeka tetiklendi...")
    
    response = rekognition_client.start_label_detection(
        Video={'S3Object': {'Bucket': BUCKET_ADIM, 'Name': S3_KAYIT_ADI}},
        MinConfidence=75
    )
    job_id = response['JobId']
    
    is_person_detected = False
    islenen_etiketler = []

    while True:
        result = rekognition_client.get_label_detection(JobId=job_id)
        status = result['JobStatus']
        
        if status == 'SUCCEEDED':
            bulunanlar = set()
            for label in result['Labels']:
                isim = label['Label']['Name']
                guven = round(label['Label']['Confidence'], 1)
                
                if isim not in bulunanlar:
                    bulunanlar.add(isim)
                    islenen_etiketler.append({"isim": isim, "guven": guven})
                    
                    # Eğer "Person" görürsek alarmı tetikliyoruz
                    if isim == "Person":
                        is_person_detected = True
            break
        elif status == 'FAILED':
            break
            
        time.sleep(3)

    return render_template('index.html', durum=is_person_detected, etiketler=islenen_etiketler)

if __name__ == "__main__":
    app.run(debug=True)