from flask import Flask, request, render_template, redirect

app = Flask(__name__)
ITEMS = []


@app.route("/")
def index():
    return render_template("index.html", items=ITEMS)


@app.route("/add", methods=["POST", "GET"])
def add_item():
    if request.method == "POST":
        new_item = request.form["new_item"]
        ITEMS.append(new_item)
        return redirect("/")
    return render_template("add.html")


@app.route("/edit/<int:item_id>", methods=["POST", "GET"])
def edit_item(item_id):
    if request.method == "POST":
        updated_item = request.form["edit_item"]
        ITEMS[item_id] = updated_item
        return redirect("/")
    return render_template("edit.html",items=ITEMS, id=item_id)


@app.route("/delete/<int:item_id>")
def delete_item(item_id):
    ITEMS.pop(item_id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
