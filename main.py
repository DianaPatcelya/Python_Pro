from flask import Flask, request
from utils import generate_requirements, gen_users, space_utils

app = Flask(__name__)


@app.route("/requirements")
def requirements():
    generate_requirements()
    with open("requirements.txt", "r") as file:
        requirements_content = file.readlines()
    return "<br>".join(requirements_content)


@app.route("/generate-users")
def generate_users():
    quantity = request.args.get('quantity', '100')

    if quantity.isdigit():
        quantity = int(quantity)
        max_quantity = 1000

        if quantity > max_quantity:
            return f'Quantity should be less then {max_quantity}'

        return gen_users(quantity)

    return f'Invalid quantity value {quantity}'


@app.route('/space', methods=['GET'])
def space():
    request = space_utils()
    if request.status_code != 200:
        return 'Помилка отримання даних зі сторінки', request.status_code

    data = request.json()
    number = data.get('number', None)
    if number is not None:
        return f'Number of astronauts: {number}'

    return '"number" не знайдено у відповіді з сервера'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
