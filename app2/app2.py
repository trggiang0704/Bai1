from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search_student():
    student = None
    if request.method == 'POST':
        ma_sv = request.form['ma_sv']
        url = f"http://172.16.16.100:5001/api/sinhvien/{ma_sv}"
        res = requests.get(url)
        if res.status_code == 200:
            student = res.json()
        else:
            student = {"error": "Không tìm thấy sinh viên"}
    return render_template('search.html', student=student)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
