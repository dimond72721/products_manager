from flask import Flask, render_template, request, flash, redirect, url_for
from action_db import delete_product, edit_product

app = Flask(__name__)
app.secret_key = 'secret_key'

all_products = {}


@app.route('/', methods=['GET', 'POST'])
@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        title = request.form.get('title')
        price = float(request.form.get('price'))
        category = request.form.get('category')

        if title in all_products:
            flash(f'Product {title} already exists!')
        else:
            all_products[title] = {
                'price': price,
                'category': category
            }
            flash(f'Product {title} was added!')

        return redirect(url_for('products'))

    return render_template('product.html', products=all_products)


@app.route('/edit/<name_product>', methods=['GET', 'POST'])
def edit(name_product):
    product = all_products.get(name_product)

    if product is None:
        flash('Product not found!')
        return redirect(url_for('products'))

    if request.method == 'POST':
        price = float(request.form.get('price'))
        category = request.form.get('category')

        
        edit_product(name_product, price, category)

        
        product['price'] = price
        product['category'] = category

        flash('Товар оновлено!')
        return redirect(url_for('products'))

    return render_template(
        'edit.html',
        name=name_product,
        product=product
    )


@app.route('/delete/<name_product>')
def delete(name_product):
    
    delete_product(name_product)

    
    all_products.pop(name_product, None)

    flash(f'Product {name_product} was deleted!')

    return redirect(url_for('products'))


if __name__ == '__main__':
    app.run(debug=True)
