from flask import Flask, request, jsonify, render_template, redirect, url_for
import pyodbc

app = Flask(__name__)

# Kết nối SQL Server
def get_db():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'SERVER=DESKTOP-U7QQ8GS\VIETHUNG;'
        'DATABASE=QlySV;'    
        'Trusted_Connection=yes;'
        'Encrypt=yes;'
        'TrustServerCertificate=yes;'
    )
    return conn

# Trang nhập và hiển thị danh sách sinh viên
@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db()
    cursor = conn.cursor()

    if request.method == 'POST':
        ma_sv = request.form['ma_sv']
        ten_sv = request.form['ten_sv']
        lop = request.form['lop']
        email = request.form['email']
        try:
            cursor.execute(
                "INSERT INTO sinh_vien (ma_sv, ten_sv, lop, email) VALUES (?, ?, ?, ?)",
                (ma_sv, ten_sv, lop, email)
            )
            conn.commit()
        except Exception as e:
            return f"Lỗi khi thêm sinh viên: {e}"
        return redirect(url_for('index'))

    cursor.execute("SELECT * FROM sinh_vien")
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    students = [dict(zip(columns, row)) for row in rows]

    conn.close()
    return render_template("index.html", students=students)

# API thêm sinh viên từ App2
@app.route('/api/sinhvien', methods=['POST'])
def add_student():
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO sinh_vien (ma_sv, ten_sv, lop, email) VALUES (?, ?, ?, ?)",
                       (data['ma_sv'], data['ten_sv'], data['lop'], data['email']))
        conn.commit()
        return jsonify({"message": "Đã thêm sinh viên"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        conn.close()

# API lấy sinh viên theo mã (App2 dùng)
@app.route('/api/sinhvien/<ma_sv>', methods=['GET'])
def get_student(ma_sv):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM sinh_vien WHERE ma_sv = ?", (ma_sv,))
        row = cursor.fetchone()
        if row:
            columns = [column[0] for column in cursor.description]
            student = dict(zip(columns, row))
            return jsonify(student)
        else:
            return jsonify({"error": "Không tìm thấy sinh viên"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
