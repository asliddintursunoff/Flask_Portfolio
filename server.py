from flask import Flask,render_template,request,redirect
import csv


app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:url_path>")
def url_link(url_path):
    return render_template(url_path)

def write_to_text(data):
    with open("database.txt", mode="a") as file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file.write(f"\n {email},{subject},{message}")
    
def write_to_csv(data):
    with open("database.csv", mode="a" , newline="") as file:
        
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database2 = csv.writer(file, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        database2.writerow([email,subject,message])
        
             
@app.route('/submit_form', methods=['POST', 'GET'])
def submitform():
    data = request.form.to_dict()
    if request.method=="POST":
        write_to_csv(data)
        return redirect("contact.html")
    else:  
        return "something went wrong"


def read_csv():
    data = []
    with open('database.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        
        for row in reader:
            data.append(row)  # Append each row to data
    return data

@app.route('/mydata')
def home():
    # Read data from the CSV file
    data = read_csv()
    
    # Pass the data to the HTML template
    return render_template('reading.html', data=data)
