from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/Register',methods=['GET','POST'])
def handle_regiser():
    if request.method == 'GET':
        return render_template('./templates/webpage.html')
    elif request.method == 'POST':
        data = {}
        data['name'] = request.form.get('name')
        data['email'] = request.form.get('email')
        data['number'] = request.form.get('number')
        
        return render_template('./templates/success.html',data=data)
        

if __name__ == '__main__':
    app.run(debug=True)