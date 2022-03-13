import io
from flask import Flask
from flask import render_template, url_for, Response
import matplotlib as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

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

# Setup for Order History Graph
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

@app.route("/orderhistory")
def render_orderhistory():
   fig = Figure()
   axis = fig.add_subplot(1, 1, 1)
   xs = np.random.rand(100)
   ys = np.random.rand(100)
   axis.plot(xs, ys)
   output = io.BytesIO()
   FigureCanvas(fig).print_png(output)
   

   return render_template("orderhistory.html", Response = output.getvalue(),mimetype='image/png')


   #return render_template( Response(output.getvalue(), mimetype='image/png')
 





if __name__ == '__main__':
    app.run(debug=True)