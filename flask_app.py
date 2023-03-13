#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,render_template,request
import replicate,os

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        t = request.form.get("txt")
        os.environ["REPLICATE_API_TOKEN"] = "787f515cb0624813736c11e7fefec66473394f02"
        model = replicate.models.get("tstramer/midjourney-diffusion")
        version = model.versions.get("436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b")
        inputs = {'prompt': t, 'height':256, 'width':256}
        output = version.predict(**inputs)
        return(render_template("index.html",result=output))
    else:
        return(render_template("index.html",result="waiting"))

if __name__ == "__main__":
    app.run()


# In[ ]:




