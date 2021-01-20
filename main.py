import speech_recognition as sr       #speech to text 
import learn_speech_recognition as s 	#import the file containing functions
import pyttsx3

engine_main = pyttsx3.init()
'''
voices = engine_main.getProperty('voices')
voice_pre =[] 
main_r = sr.Recognizer()  			#initiate the speech recognition
for voice in voices:
	voice_pre.append(voice.id)
'''
voice = True
while(voice):
	with sr.Microphone() as source:
		#engine_main.setProperty('voices',voice_pre[0])
		engine_main.say("What you want to do\n search \n watch \n or take selfie")
		engine_main.runAndWait() 				
		main_audio = main_r.listen(source)
	google_audio = main_r.recognize_google(main_audio)  #recognize the word from the google speech api
	#google_audio = input()
	print(google_audio) 	
	if (google_audio == 'search'):
		s.Search_web() 										#call the wikipedia function
		voice = False
	elif (google_audio == 'watch'):
		s.youtube_search() 									#call the Youtube function
		voice = False
	elif(google_audio == 'selfie'):
		s.take_photo() 										#take photos
		voice = False
	else:
		#engine_main.setProperty('voices',voice_pre[0])
		engine_main.say("Cannot listen correctly please try again...")
		engine_main.runAndWait()