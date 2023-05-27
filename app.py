from flask import Flask, render_template, request
import pickle

# Load model dari file pkl
with open('Model/stunting.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/info-stunting')
def info_stunting():
    return render_template('infostunting.html')

@app.route('/prediksi-stunting')
def prediksi_stunting():
    return render_template('prediksistunting.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Ambil nilai input dari form
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
    
    # Lakukan prediksi menggunakan model
    prediction = model.predict([input_data])
    
    # Tampilkan hasil prediksi
    if prediction[0] == 1:
        result = 'Stunting'
    else:
        result = 'Normal'

    return render_template('prediksistunting.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
