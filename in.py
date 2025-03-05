from flask import Flask, request, jsonify
import pywhatkit
import datetime
import wikipedia
import pyjokes

app = Flask(__name__)

@app.route('/process_command', methods=['POST'])
def process_command():
    command = request.json.get('command', '').lower()

    if 'play' in command:
        song = command.replace('play', '').strip()
        pywhatkit.playonyt(song)
        return jsonify({"response": f"Playing {song} on YouTube"})

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        return jsonify({"response": f"Current time is {time}"})

    elif 'who is' in command or 'what is' in command or 'which is' in command:
        topic = command.replace('who is', '').replace('what is', '').replace('which is', '').strip()
        try:
            info = wikipedia.summary(topic, sentences=1)
            return jsonify({"response": info})
        except wikipedia.exceptions.DisambiguationError:
            return jsonify({"response": "There are multiple results. Please be more specific."})
        except wikipedia.exceptions.PageError:
            return jsonify({"response": "Sorry, I couldn't find any information on that topic."})

    elif 'date' in command:
        return jsonify({"response": "Go with Siri or Alexa"})

    elif 'are you single' in command:
        return jsonify({"response": "I am in a relationship with WiFi"})

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        return jsonify({"response": joke})

    elif 'stop' in command or 'exit' in command:
        return jsonify({"response": "Goodbye!"})

    else:
        try:
            info = wikipedia.summary(command, sentences=1)
            return jsonify({"response": info})
        except:
            return jsonify({"response": "Sorry, I didn't understand that."})

if __name__ == '__main__':
    app.run(debug=True)