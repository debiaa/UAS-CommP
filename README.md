# Data Ingestion API - Mini Project UAS Communication Protocol

Aplikasi **REST API Gateway** berbasis Python Flask yang dirancang sebagai pintu gerbang pertama (*first-line defense*) dalam pipa data (*data pipeline*) transaksi penjualan. Proyek ini berfokus pada penerapan **Validasi Skema Protokol**, **Keandalan Jaringan (Reliability)**, dan **Pemantauan Aktivitas (Observability)** untuk memastikan integritas data sebelum masuk ke tahap analisis lanjut (Sains Data).

---

## 📂 Struktur Repositori

```text
uas-commprotocol-nama-nim/
├── app.py                  # Source code utama server API Flask
├── docs/                   # Dokumentasi Proyek
│   ├── architecture.png     # Diagram Arsitektur Sistem
│   ├── LAPORAN MINI PROJECT UJIAN AKHIR SEMESTER.pdf      # Laporan Lengkap Akhir (10 Halaman)
│   └── LAPORAN MINI PROJECT UJIAN AKHIR SEMESTER.pptx      # Slide Presentasi (7 Slide)
├── postman/                # Artefak Pengujian
│   └── UAS CP.postman_collection.json      # Postman Collection Export v2.1
└── evidence/               # Bukti Validasi Pengujian (Screenshots)
    ├── get 1.png      # GET All Data (200 OK)
    ├── post 1.png      # POST Ingest Data Sukses (201 Created)
    ├── failed 1.png      # GET Data Tidak Ditemukan (404 Not Found)
    ├── failed 2.png      # POST Data Cacat/Kurang Atribut (400 Bad Request)
    ├── observability.png # Application Logs Console (PowerShell)
    └── wireshark.png # Analisis Trafik / Localhost Diagnostic

## Author
Anggi debia zahra
25120500005
