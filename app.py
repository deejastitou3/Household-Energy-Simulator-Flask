from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import os
from calculs import calculer_energie

app = Flask(__name__)

def construire_profil_24h(appareils):
    """Builds the 24-hour power profile based on user input."""
    profil = [0] * 24
    for app in appareils:
        puissance = app['puissance']
        heures = int(app['heures'])
        # Distribute the usage evenly or in blocks (simplified for demo)
        for i in range(heures):
            profil[i % 24] += puissance
    return profil

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/simulation', methods=['POST'])
def simulation():
    prix = float(request.form.get('prix', 1.2))
    appareils = []
    
    # Parse form data (expects fields like puissance_1, heures_1, etc.)
    for key in request.form:
        if "puissance" in key:
            id_app = key.split("_")[1]
            puissance = float(request.form[key])
            heures = float(request.form.get(f"heures_{id_app}", 0))
            if puissance > 0 and heures > 0:
                appareils.append({"puissance": puissance, "heures": heures})

    if not appareils:
        return "Please add at least one appliance.", 400

    profil = construire_profil_24h(appareils)
    energie = calculer_energie(profil)
    cout = round(energie * prix, 2)

    # Generate Matplotlib Graph
    heures = list(range(24))
    plt.figure(figsize=(10, 4))
    plt.plot(heures, profil, marker='o', color='#4CAF50', linewidth=2)
    plt.title("Daily Power Consumption Profile P(t)", fontsize=14)
    plt.xlabel("Hours of the Day", fontsize=12)
    plt.ylabel("Power (Watts)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(heures)
    
    # Ensure static folder exists
    os.makedirs('static', exist_ok=True)
    plt.savefig('static/courbe.png', dpi=100, bbox_inches='tight')
    plt.close()

    return render_template('resultats.html', energie=energie, cout=cout)

if __name__ == '__main__':
    app.run(debug=True)