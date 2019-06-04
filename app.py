from flask import Flask, render_template, jsonify, request
import speech_recognition as sr 

app = Flask(__name__, static_url_path='/static')

sentence = ""

'''@app.route('/dumb', methods=['GET'])
def index():
	return render_template("index.html")'''


@app.route('/', methods=['GET'])
@app.route('/normal', methods=['GET'])
def index():
	'''r = sr.Recognizer()                                                                                  
	with sr.Microphone() as source:                                                                       
	    print("Speak:")                                                                                   
	    audio = r.listen(source)   

	try:
	    sentence = r.recognize_google(audio)
	except sr.UnknownValueError:
	    sentence = "Could not understand audio"
	except sr.RequestError as e:
	    sentence = "Could not request results; {0}".format(e)'''

	return render_template("videocall.html")

@app.route('/speech', methods=['POST'])
def speech():
	print("started speech_recognition")
	message = request.get_json(force=True)
	sentence = message['sentence']
	r = sr.Recognizer()                                                                                  
	with sr.Microphone() as source:                                                                                                                                                         
	    audio = r.listen(source)   

	try:
	    sentence = r.recognize_google(audio)
	except sr.UnknownValueError:
	    sentence = "Could not understand audio"
	except sr.RequestError as e:
	    sentence = "Could not request results; {0}".format(e)
	response = {
		'sentence': sentence
	}
	print(sentence)
	return jsonify(response)



if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000)