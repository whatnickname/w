from flask import Flask, render_template, request, redirect, url_for
import sys
import database
app = Flask(__name__)

@app.route('/')
def home():
   return render_template("report.html")

@app.route('/소리')
def 소리():
   return render_template("소리.html")

@app.route('/소피')
def 소피():
   return render_template("소피.html")

@app.route('/applyphoto')
def photo_apply():
   location = request.args.get("location")
   cleaness = request.args.get("clean")
   built_in = request.args.get("built")
   if cleaness == None:
      cleaness = False
   else:
      cleaness = True

   database.save(location,cleaness,built_in)
   return render_template("apply_photo.html")

@app.route('/upload_done',methods=["POST"])
def upload_done():
   uploaded_files=request.files["file"]
   uploaded_files.save("static/{}.jpeg".format(database.now_index()))
   return redirect(url_for("home"))

@app.route('/list')
def list():
   house_list=database.load_list()
   length=len(house_list)
   return render_template("list.html",house_list=house_list, length=length)

@app.route('/house_info/<int:index>/')
def house_info(index):
   house_info=database.load_house(index)
   location = house_info["location"]
   cleaness = house_info["cleaness"]
   built_in = house_info["built_in"]

   photo = f"{index}.jpeg"

   return render_template("house_info.html", location=location, cleaness=cleaness, built_in=built_in, photo=photo)

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)