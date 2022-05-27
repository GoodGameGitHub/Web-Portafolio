from django.shortcuts import render
from flask import Flask, render_template, request, url_for
import smtplib
import requests
#import mysql.connector as sql
import Forms

dbHost = "";
dbUser = "";
dbPassword = "";
emailAdress = "";
emailPassword = "";
toEmailAddress = "";
twilioUser = "";
twilioAuthToken = "";
fromPhone = "";
toPhone = "";


def specialCharCleaning(s):
    specialCharSet = ['-','\'','"','.','|','=','\\','*','/','&'];
    for char in specialCharSet:
        if char in s:
            s.replace(char,'');
    return s;

app = Flask(__name__)
app.config['SECRET_KEY'] = '';

@app.route('/', methods=["GET","POST"])
def homepage():
    return render_template("home.html")

@app.route('/search', methods=["GET","POST"])
def search():
    return render_template("search.html",query=[])
"""
Crea el nuevo servidor SQL
#te falta limpiar la cadena de caracteres para evitar sql injection
@app.route('/search', methods=["GET","POST"])
def search():
    if request.method == "POST":
        db = sql.connect(host=dbHost,user=dbUser,password=dbPassword);
        dbCursor = db.cursor();
        dbCursor.execute('use portfolio;');
        searchText = request.form.get("searchField");
        searchText = specialCharCleaning(searchText);
        if searchText == '':
            dbCursor.execute("select * from link where 1 = 0");
        else:
            wordList = searchText.split();
            regExp = ".*";
            for i in wordList:
                regExp += "{0}|{0} | {0} |".format(i);
            regExp = regExp[:-1] + ".*";
            dbCursor.execute("select * from link where keywords regexp '"+regExp+"'");
        return render_template("search.html",query=dbCursor)
    if request.method == "GET":
        return render_template("search.html",query=[])
"""


@app.route('/aboutMe', methods=["GET"])
def aboutMe():
    return render_template("aboutMe.html")


@app.route('/skills', methods=["GET"])
def skills():
    return render_template("skills.html")


@app.route('/contactMe', methods=["GET","POST"])
def contactMe():
    form = Forms.ContactMeForm();
    if request.method == "GET":
        return render_template("contactMe.html", form = form);

    elif request.method == "POST":
        if form.validate_on_submit():
            name = form.name.data;
            email = form.email.data;
            subject = form.subject.data;
            message = form.message.data;
            contact = "\nNombre: "+name+"\nCorreo: "+email+"\nAsunto: "+subject+"\nMensaje: "+message;
            server = smtplib.SMTP(host="smtp.gmail.com",port = 587);
            server.starttls();
            server.login(emailAddress, emailPassword);
            server.sendmail(emailAddress, toEmailAddress, contact);
            server.quit();
            authToken = (twilioUser, twilioAuthToken);
            content = {'Body':name+' tried to contact you on your website','From':fromPhone,'To':toPhone};
            requests.post('https://api.twilio.com/2010-04-01/Accounts/'+twilioUser+'/Messages.json', data = content, auth = authToken);
            return render_template("contactMe.html", form = form);
        else:
            
            return render_template("contactMe.html", form = form);


@app.route('/projects', methods=["GET"])
def projects():
    return render_template("projects.html")


@app.route('/entries', methods=["GET"])
def entries():
    return render_template("entries.html")


#-----------SKILLS-----------
@app.route('/skills/softwareDevelopment', methods=["GET"])
def softwareDevelopment():
    return render_template("skills/softwareDevelopment.html")

@app.route('/skills/mechatronics', methods=["GET"])
def mechatronics():
    return render_template("skills/mechatronics.html")
    
@app.route('/skills/electronics', methods=["GET"])
def electronics():
    return render_template("skills/electronics.html")

@app.route('/skills/databases', methods=["GET"])
def databases():
    return render_template("skills/databases.html")

@app.route('/skills/linux', methods=["GET"])
def linux():
    return render_template("skills/linux.html")

@app.route('/skills/networking', methods=["GET"])
def networking():
    return render_template("skills/networking.html")

@app.route('/skills/machineLearning', methods=["GET"])
def machineLearning():
    return render_template("skills/machineLearning.html")

@app.route('/skills/mechanics', methods=["GET"])
def mechanics():
    return render_template("skills/mechanics.html")

@app.route('/skills/cybersecurity', methods=["GET"])
def cybersecurity():
    return render_template("skills/cybersecurity.html")

#-----------SKILLS-----------

#-----------PROJECTS-----------
@app.route('/projects/this-website', methods=["GET"])
def thisWebsite():
    return render_template("construction.html");

@app.route('/projects/modellingMyWorkspace', methods=["GET"])
def modellingMyWorkspace():
    return render_template("construction.html");
#-----------PROJECTS-----------


#-----------Testing-----------
@app.route('/testing',methods=['GET','POST'])
def testing():
    return render_template("projects/thisWebsite.html");

if __name__ == '__main__':
    app.run(host = '192.168.1.1', port = 80, debug=True, threaded = False);
