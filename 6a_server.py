from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    # Obtener el texto del argumento de la URL
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Llamar a la función que creaste antes
    response = emotion_detector(text_to_analyze)
    
    # Verificar si la entrada es válida (si la emoción dominante es None, significa error)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
        
    # Retornar la respuesta formateada como cadena de texto
    return f"The given text has been identified as {response}"

@app.route("/")
def render_index_page():
    # Esto renderiza el archivo index.html que deberías tener en tu carpeta templates
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
