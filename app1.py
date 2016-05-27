import opengraph
from flask import Flask
from flask import Flask,render_template,request,redirect,url_for,session
from urllib import urlopen
from lxml import etree 
import validators
app = Flask('__name__')

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/results', methods= ['POST','GET']) 
def results():   
	
	want1=request.form['keyword']
		
	header = "http://"
	url = header+want1
	print url
	f = urlopen(url).read()
 	tree = etree.HTML( f )
	general = tree.xpath( "//meta[@name='description']" )[0].get("content")	
	meta = opengraph.OpenGraph(url)
	print meta
	return render_template("results.html",data=meta,gog=general)
if __name__=='__main__':
	app.run(debug=True)
