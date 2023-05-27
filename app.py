from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Memuat model pkl
model_path = 'stunting.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Mendapatkan input dari form
        input_data = [
            float(request.form['JenisKelamin']),
            float(request.form['UmurBaduta']),
            float(request.form['AnakKe']),
            float(request.form['JumlahAnak']),
            float(request.form['BBLahir']),
            float(request.form['PBLahir']),
            float(request.form['PBSekarang']),
            float(request.form['BBSekarang']),
            float(request.form['UmurAyah']),
            float(request.form['UmurIbu']),
            float(request.form['usiadiberimakananpadat']),
            float(request.form['LuasBangunan']),
            float(request.form['Subtotpeng_pangan']),
            float(request.form['Subtotpeng_nonpangan']),
            float(request.form['TotalPengeluaran'])
        ]

        # Memanggil model untuk melakukan prediksi
        prediction = model.predict([input_data])

        # Menampilkan hasil prediksi
        return render_template('result.html', prediction=prediction[0])

    return render_template('/home/yayan/Desktop/tugasKp/stuntingKemranjen/form.html')

if __name__ == '__main__':
    app.run()
