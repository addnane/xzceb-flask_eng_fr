from flask import Flask, render_template, request
import json
from  machinetranslation.translator  import englishtofrench,frenchtoenglish


#Istantiate flask class
app = Flask("Web Translator")


#root end point which renders index.html
@app.route("/")
def renderIndexPage():
    return render_template('index.html')




#end point to translate from French to English
@app.route("/frenchToEnglish")
def TranslateToEnglish():
 textToTranslate = request.args.get("textToTranslate")
 return frenchtoenglish(textToTranslate)["translations"][0]["translation"]




#end point to translate from English to French
@app.route("/englishToFrench")
def TranslateToFrench():

 textToTranslate = request.args.get("textToTranslate")
 return englishtofrench(textToTranslate)["translations"][0]["translation"]

#root end point which renders index.html


app.run(host="0.0.0.0",port="8080")

