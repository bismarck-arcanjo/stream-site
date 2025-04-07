from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Lista de vídeos do YouTube para exibir no site
    videos = [
        {"title": "Bus Stop", "video_id": "fz0j2lAo4K0"},  # Substitua com IDs reais
        {"title": "CATCH YOUR BREATH", "video_id": "hBj4rcs0AiQ"},
        {"title": "Play me", "video_id": "KZi7rVwD680"},
        {"title" : "The Other Side of the Box", "video_id" : "OrOYvVf6tIM"},
        {"title" : "Born Again", "video_id" : "7Ms8GEe6bRQ"},
        {"title" : "STUCK", "video_id" : "mlShD2AvbV8&rco"},
        {"title" : "The Dollmaker", "video_id" : "OqSmb3n0j8o"},
        {"title" : "Stucco", "video_id" : "6eaZZc7O2PE"},
        {"title" : "Trial 22", "video_id" : "6i0S_0S7Sak"},
        {"title" : "Knock Knock", "video_id" : "dwDIz2YNQSo"},
        {"title" : "Knock Knock 2", "video_id" : "t8g2uh4_E-4"},
        {"title" : "Magic ball 8", "video_id" : "3OWCVKQ6aGQ"}
    ]
    
    # Renderiza a página HTML e passa a lista de vídeos
    return render_template('index.html', videos=videos)

if __name__ == '__main__':
    app.run(debug=True)
