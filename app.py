from flask import Flask, jsonify, request
import time
import uuid

app = Flask(__name__)

# Simulasi Database Penyimpanan Data (In-Memory Database)
transaction_db = [
    {
        "id": 1,
        "customer_name": "Budi Santoso",
        "product_category": "Electronics",
        "amount": 1500000.0,
        "payment_status": "Success"
    },
    {
        "id": 2,
        "customer_name": "Siti Aminah",
        "product_category": "Apparel",
        "amount": 350000.0,
        "payment_status": "Pending"
    }
]

# Helper function untuk mencetak logs (Observability)
def generate_server_log(request_id, method, path, status_code, message):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] [ReqID: {request_id}] {method} {path} - Status: {status_code} | Msg: {message}")

# --- ENDPOINT 1: GET - Cek Status Koneksi API (Health Check) ---
@app.route('/api/v1/health', methods=['GET'])
def health_check():
    req_id = str(uuid.uuid4())[:8]
    generate_server_log(req_id, "GET", "/api/v1/health", 200, "API is healthy and running.")
    return jsonify({
        "status": "active",
        "message": "Ingestion API is ready to receive data",
        "request_id": req_id
    }), 200

# --- ENDPOINT 2: GET - Ambil Semua Data yang Berhasil di-Ingest ---
@app.route('/api/v1/ingest', methods=['GET'])
def get_all_data():
    req_id = str(uuid.uuid4())[:8]
    generate_server_log(req_id, "GET", "/api/v1/ingest", 200, f"Retrieved {len(transaction_db)} records.")
    return jsonify({
        "request_id": req_id,
        "total_records": len(transaction_db),
        "data": transaction_db
    }), 200

# --- ENDPOINT 3: GET - Ambil Data Spesifik Berdasarkan ID ---
# Mengakomodasi Skenario Gagal 1 (Data Tidak Ditemukan)
@app.route('/api/v1/ingest/<int:data_id>', methods=['GET'])
def get_data_by_id(data_id):
    req_id = str(uuid.uuid4())[:8]
    # Cari data di list
    record = next((item for item in transaction_db if item["id"] == data_id), None)
    
    if record:
        generate_server_log(req_id, "GET", f"/api/v1/ingest/{data_id}", 200, "Data successfully found.")
        return jsonify({
            "request_id": req_id,
            "status": "success",
            "data": record
        }), 200
    else:
        # SKENARIO GAGAL 1 (404 Not Found)
        generate_server_log(req_id, "GET", f"/api/v1/ingest/{data_id}", 404, "Data ID not found.")
        return jsonify({
            "request_id": req_id,
            "status": "error",
            "message": f"Data transaksi dengan ID {data_id} tidak ditemukan di sistem."
        }), 404

# --- ENDPOINT 4: POST - Proses Ingest Data Baru ---
# Mengakomodasi Skenario Gagal 2 (Validasi Input Gagal / Bad Request)
@app.route('/api/v1/ingest', methods=['POST'])
def ingest_new_data():
    req_id = str(uuid.uuid4())[:8]
    
    # Ambil payload JSON dari client
    payload = request.get_json()
    
    # Validasi input (Skenario Gagal jika field kosong)
    if not payload:
        generate_server_log(req_id, "POST", "/api/v1/ingest", 400, "Payload is empty.")
        return jsonify({"request_id": req_id, "status": "error", "message": "Body request tidak boleh kosong"}), 400
        
    required_fields = ["customer_name", "product_category", "amount", "payment_status"]
    missing_fields = [field for field in required_fields if field not in payload]
    
    if missing_fields:
        # SKENARIO GAGAL 2 (400 Bad Request)
        error_msg = f"Validasi gagal. Field berikut wajib diisi: {', '.join(missing_fields)}"
        generate_server_log(req_id, "POST", "/api/v1/ingest", 400, error_msg)
        return jsonify({
            "request_id": req_id,
            "status": "error",
            "message": error_msg
        }), 400

    # Skenario Sukses (201 Created)
    new_id = transaction_db[-1]["id"] + 1 if transaction_db else 1
    new_record = {
        "id": new_id,
        "customer_name": payload["customer_name"],
        "product_category": payload["product_category"],
        "amount": float(payload["amount"]),
        "payment_status": payload["payment_status"]
    }
    transaction_db.append(new_record)
    
    generate_server_log(req_id, "POST", "/api/v1/ingest", 201, f"Data ID {new_id} successfully ingested.")
    return jsonify({
        "request_id": req_id,
        "status": "success",
        "message": "Data transaksi baru berhasil masuk ke sistem!",
        "data": new_record
    }), 201

# --- ENDPOINT 5: DELETE - Hapus Data dari Memori ---
@app.route('/api/v1/ingest/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    req_id = str(uuid.uuid4())[:8]
    global transaction_db
    record = next((item for item in transaction_db if item["id"] == data_id), None)
    
    if not record:
        generate_server_log(req_id, "DELETE", f"/api/v1/ingest/{data_id}", 404, "Data ID not found for deletion.")
        return jsonify({
            "request_id": req_id,
            "status": "error",
            "message": "Gagal menghapus. ID data tidak ditemukan."
        }), 404
        
    transaction_db = [item for item in transaction_db if item["id"] != data_id]
    generate_server_log(req_id, "DELETE", f"/api/v1/ingest/{data_id}", 200, f"Data ID {data_id} has been deleted.")
    return jsonify({
        "request_id": req_id,
        "status": "success",
        "message": f"Data transaksi dengan ID {data_id} berhasil dihapus dari sistem."
    }), 200

if __name__ == '__main__':
    # Berjalan lokal di port 5000
    app.run(debug=True, port=5000)