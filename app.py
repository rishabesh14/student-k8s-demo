from flask import Flask, render_template_string, request

app = Flask(__name__)

def total_bill(price, quantity):
    return price * quantity

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        price = float(request.form.get("price", 0))
        quantity = int(request.form.get("quantity", 1))
        result = total_bill(price, quantity)

    return render_template_string("""
    <!doctype html>
    <html>
    <head>
        <title>Shopping Bill Calculator</title>
    </head>
    <body>
        <h2>Shopping Bill Calculator</h2>
        <form method="POST">
            <label>Price: </label>
            <input type="number" name="price" step="0.01" required><br><br>
            <label>Quantity: </label>
            <input type="number" name="quantity" min="1" value="1" required><br><br>
            <button type="submit">Calculate</button>
        </form>

        {% if result is not none %}
            <h3>Total Bill: {{ result }}</h3>
        {% endif %}
    </body>
    </html>
    """ , result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)