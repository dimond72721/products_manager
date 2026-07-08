from flask import Flask, render_template, request, flash, redirect, url_for
from action_db import (
    add_product,
    get_products,
    product_exists,
    delete_product,
    edit_product
)

app = Flask(__name__)
app.secret_key = "secret_key"


@app.route("/", methods=["GET", "POST"])
@app.route("/products", methods=["GET", "POST"])
def products():
    if request.method == "POST":
        title = request.form.get("title")
        price = float(request.form.get("price"))
        category = request.form.get("category")

        if product_exists(title):
            flash(f"Product {title} already exists!")
        else:
            add_product(title, price, category)
            flash(f"Product {title} was added!")

        return redirect(url_for("products"))

    return render_template(
        "product.html",
        products=get_products()
    )


@app.route("/edit/<name_product>", methods=["GET", "POST"])
def edit(name_product):
    product = None

    for p in get_products():
        if p.name == name_product:
            product = p
            break

    if product is None:
        flash("Product not found!")
        return redirect(url_for("products"))

    if request.method == "POST":
        price = float(request.form.get("price"))
        category = request.form.get("category")

        edit_product(name_product, price, category)

        flash("Товар оновлено!")
        return redirect(url_for("products"))

    return render_template(
        "edit.html",
        name=name_product,
        product={
            "price": product.price,
            "category": product.category
        }
    )


@app.route("/delete/<name_product>")
def delete(name_product):
    delete_product(name_product)
    flash(f"Product {name_product} was deleted!")
    return redirect(url_for("products"))


if __name__ == "__main__":
    app.run(debug=True)
