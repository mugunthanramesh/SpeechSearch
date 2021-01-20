import speech_recognition as sr  	#speech to text
import pyttsx3						#offline text to speech
import bs4 as bs  					#web scrapping
import urllib.request    			#web scrapping
import webbrowser as web 			#web browser usage
import cv2,re 						#cv2 - image operation				
import datetime,os 					#functioning with os  	


# get audio from the microphone                                                                       
r = sr.Recognizer()					#initiate the speech_recognition library(speech to text library)
engine = pyttsx3.init()  
#voices = engine.getProperty('voices')
'''voice_pres =[] 
voice_id_present=[]
for voice in voices:
	voice_pres.append(str(voice))
	voice_id_present.append(voice.id)
	
	print(voice,voice.id)	#initiate the pyttsx3 library(text to sppech library)
	engine.setProperty('voice',voice.id)
	engine.say('hello world')
	engine.runAndWait()
'''
#Function for getting voice input 
def input_voice():
	with sr.Microphone() as source:
		engine.say("What do you like:")
		engine.runAndWait()
		audio = r.listen(source)                            #Listen to the voice input
	a=r.recognize_google(audio)				#recognize the word from the google speech api
	engine.say("Do you Want to know or watch about: "+a+"\nyes(or)no?")
	engine.runAndWait()			#check whether the word is right
	access = input()
	new_a = ''
	for i in a:
		if(i.isspace()):					#To get a comboined string if the word is greater than one word
			pass
		else:
			new_a += i
	return access,new_a						#return the word and the choice 
	
#Function for searching	
def Search_web():
	meaning = ""
	access, a = input_voice()
	#history('search', a)
	if(access == 'y' or acccess == 'Y' or access == 'yes' or acccess == 'YES'):
		engine.say("Thats cool")
		engine.runAndWait()
		source = urllib.request.urlopen('https://en.wikipedia.org/wiki/'+a).read()			#scrapping from the web (wikipedia)
	else:
		engine.setProperty(voice_pre[1],voice_id_present[1])
		engine.say('sorry for your inconvinence \n Please Try again')
		engine.runAndWait()
		input_voice()
	soup = bs.BeautifulSoup(source,'lxml')
	for i in soup.find_all('p'):
		if((i.text).isspace()):
			pass
		else:
			meaning+=i.text
			break
	#engine.setProperty(voice_pre[1],voice_id_present[1])
	engine.say(meaning)					#Say the meaning or info about the word listened
	engine.runAndWait()
	
#Function for watch Youtube
def youtube_search():
	access, query_string = input_voice()
	#history('watch',query_string)
	if(access == 'y' or acccess == 'Y' or access == 'yes' or acccess == 'YES'):
		#engine.setProperty('voices',voice_pre[1])
		engine.say("Thats cool")
		html_content = urllib.request.urlopen("http://www.youtube.com/results?search_query=" + query_string)		#scrapping the youtube for the contents present in the acquired string page
		search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())				
		web.open("http://www.youtube.com/watch?v=" + search_results[0])								#To Play the first in the youtube list 

#selfie
def take_photo():
	capture=1			#variable to save the file
	newpath = "E:\\"+str(datetime.date.today())		#location to save the file
	#history('photo',datetime.date.today())
	if not (os.path.exists(newpath)):				#Creates new directory to save the file location
		os.mkdir(newpath)
	os.chdir(newpath)
	cam = cv2.VideoCapture(0)							#Initiate the camera
	while True:	
		ret_val, img = cam.read()							#Read from the camera
		cv2.imshow('my webcam', img)						#Show the camera output in a frame or a dialoug box
		k=cv2.waitKey(10)								
		if(k==32):
			cv2.imwrite(str(capture)+'.jpg', img)			#To store the output in the location by name capture
			capture+=1
		if(k==27):
			#engine.setProperty(voice_pre[1],voice_id_present[1])
			engine.say("Pictures saved")
			engine.runAndWait()
			break											#End of camera