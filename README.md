# Quản lý Sinh viên với Flask và SQL Server

## 📌 Giới thiệu

Đây là một ứng dụng web đơn giản dùng để **quản lý thông tin sinh viên**, bao gồm các chức năng:

- Thêm sinh viên mới
- Kiểm tra trùng mã sinh viên
- Hiển thị danh sách sinh viên
- Tích hợp API để truy vấn từ hệ thống khác

Ứng dụng phù hợp cho bài tập thực hành Flask kết nối cơ sở dữ liệu SQL Server.

---

## 🛠️ Công nghệ và công cụ sử dụng

| Thành phần | Công nghệ sử dụng |
|-----------|------------------|
| Ngôn ngữ lập trình | Python 3 |
| Web framework | Flask |
| Cơ sở dữ liệu | SQL Server |
| Thư viện kết nối DB | pyodbc |
| Frontend | HTML, CSS, Bootstrap 5 |
| Template engine | Jinja2 (tích hợp trong Flask) |

---

## 🧠 Logic & thuật toán

- Khi người dùng thêm sinh viên:
  - Hệ thống kiểm tra mã sinh viên đã tồn tại trong DB chưa.
  - Nếu trùng mã: hiển thị thông báo lỗi.
  - Nếu chưa trùng: thêm mới vào bảng `sinh_vien`.
- Giao diện danh sách sinh viên được lấy động từ database.
- Các API hỗ trợ truy cập dữ liệu từ app khác (`GET`, `POST` sinh viên).

---

## 🖼️ Một số giao diện cơ bản

### 🔹 Form thêm sinh viên
<img width="1370" height="808" alt="image" src="https://github.com/user-attachments/assets/a3b2a47b-6d5d-4b29-92b2-ead0d94fc6f0" />

---

### 🔹 Bảng danh sách sinh viên
<img width="1458" height="626" alt="image" src="https://github.com/user-attachments/assets/ddc3ea93-caf4-425b-85ac-7a7a46a37d1e" />
---

## 🚀 Khởi chạy ứng dụng

```bash
# Cài đặt thư viện
pip install flask pyodbc

# Chạy ứng dụng Flask
python app.py
