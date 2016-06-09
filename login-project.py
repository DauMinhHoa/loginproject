from flask import Flask,render_template,request

app = Flask(__name__)
#home page
@app.route('/')
def home():
    return "Welcome home!"
#login page
@app.route('/login',methods=['GET','POST']) # vứt thuộc tính vào đây
def login():
    #viết điều kiện check thuộc tính
    if request.method == 'POST':
        print("someone is logging...")
        # print(request.form)
        # print("username is: ",request.form['username'])
        # print("password is: ",request.form['password'])
        #================================================
        # check user đã đúng thì
        # chuyển hướng người dùng về trang home
        return "Welcome home"
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
