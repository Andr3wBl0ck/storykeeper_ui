
from flask import Flask
from flask import render_template, url_for


app = Flask(__name__)

@app.route("/")
def render_dashboard():
    return render_template("dashboard.html")

@app.route("/cart")
def render_cart():
    return render_template("cart.html")

@app.route("/inventory")
def render_inventory():
    return render_template("inventory.html")



@app.route("/orderhistory")
def render_orderhistory():
   
   return render_template("orderhistory.html")


   #return render_template( Response(output.getvalue(), mimetype='image/png')
 





if __name__ == '__main__':
    app.run(debug=True)