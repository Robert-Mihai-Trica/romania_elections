from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rezultat', methods=['POST'])
def rezultat():
    # Date pentru candidatul 1
    nume1 = request.form['nume1']
    a1 = int(request.form['experienta1'])
    b1 = int(request.form['transparenta1'])
    c1 = int(request.form['sprijin1'])

    # Date pentru candidatul 2
    nume2 = request.form['nume2']
    a2 = int(request.form['experienta2'])
    b2 = int(request.form['transparenta2'])
    c2 = int(request.form['sprijin2'])

    # Calcul scoruri pentru fiecare candidat
    scor1 = (a1 + b1) ** 2 + c1
    scor2 = (a2 + b2) ** 2 + c2

    # Creăm graficul
    labels = ['Experiență', 'Transparență', 'Sprijin public']
    valori1 = [a1, b1, c1]
    valori2 = [a2, b2, c2]

    fig, ax = plt.subplots()
    ax.bar(labels, valori1, width=0.4, label=nume1, color='green', align='center')  # Culoare verde pentru candidatul 1
    ax.bar(labels, valori2, width=0.4, label=nume2, color='gold', align='edge')    # Culoare aurie pentru candidatul 2

    ax.set_ylabel('Punctaj')
    ax.set_title(f'Comparare {nume1} vs {nume2}')
    ax.legend()

    # Salvăm imaginea graficului
    img_path = os.path.join('static', 'grafic_comparatie.png')
    plt.tight_layout()
    plt.savefig(img_path)
    plt.close()

    return render_template('rezultat.html', nume1=nume1, scor1=scor1, nume2=nume2, scor2=scor2)

if __name__ == '__main__':
    app.run(debug=True)
