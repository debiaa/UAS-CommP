# Data Ingestion API - Mini Project UAS Communication Protocol

Aplikasi **REST API Gateway** berbasis Python Flask yang dirancang sebagai pintu gerbang pertama (*first-line defense*) dalam pipa data (*data pipeline*) transaksi penjualan. Proyek ini berfokus pada penerapan **Validasi Skema Protokol**, **Keandalan Jaringan (Reliability)**, dan **Pemantauan Aktivitas (Observability)** untuk memastikan integritas data sebelum masuk ke tahap analisis lanjut (Sains Data).

---

## 📂 Struktur Repositori

```text
uas-commprotocol-nama-nim/
├── app.py                  # Source code utama server API Flask
├── requirements.txt         # Daftar dependency package
├── docs/                   # Dokumentasi Proyek
│   ├── architecture.png     # Diagram Arsitektur Sistem
│   ├── laporan-uas.pdf      # Laporan Lengkap Akhir (10 Halaman)
│   └── slides-uas.pptx      # Slide Presentasi (7 Slide)
├── postman/                # Artefak Pengujian
│   └── collection.json      # Postman Collection Export v2.1
└── evidence/               # Bukti Validasi Pengujian (Screenshots)
    ├── success-01.png      # GET All Data (200 OK)
    ├── success-02.png      # POST Ingest Data Sukses (201 Created)
    ├── failure-01.png      # GET Data Tidak Ditemukan (404 Not Found)
    ├── failure-02.png      # POST Data Cacat/Kurang Atribut (400 Bad Request)
    ├── observability-log.png # Application Logs Console (PowerShell)
    └── wireshark-capture.png # Analisis Trafik / Localhost Diagnostic
