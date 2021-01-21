from flask import Flask, render_template, url_for, request
import cv2
import numpy as np
import pytesseract 
from PIL import Image
import os
from gensim.summarization.summarizer import summarize
result=""
app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('Home1.html')

@app.route('/extraction',methods=['GET','POST'])
def extraction():
	global result
	if request.method=="POST":
		if request.files:
			Image=request.files.get("imageupload",'')
			Image=str(Image)
			ind=Image.find("'")
			Image1=Image[ind+1:]
			ind1=Image1.find("'")
			Image1=Image1[:ind1]
			print(Image1)
			img=cv2.imread(r"C:\Users\\ashwi\OneDrive\Documents\\summary_images\\"+Image1)
			img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
			config = ("--oem 1")
			result = pytesseract.image_to_string(img,lang="eng",config=config)
		else:
			result="Aw snap! :("
	return render_template('Home1.html',text=result)

@app.route('/summary',methods=['GET','POST'])
def summary():
	if request.method=="POST":
		extr=summarize(str(result))	
		print(result)
	return render_template('Home1.html',text1=extr)


if __name__ == '__main__':
    app.run(debug=True)
