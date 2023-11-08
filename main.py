from flask import Flask, request
from utils import generate_requirements, gen_users, space_utils, commit_sql
from create_table import create_table

app = Flask(__name__)
create_table()


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


@app.route('/phones/create/')
def phones_create():
    contact_name = request.args.get('contactName', 'Unknown')
    phone_value = request.args.get('phone', 'a')

    sql = f"""
    INSERT INTO Phones (contactName, phoneValue)
    VALUES ('{contact_name}', '{phone_value}');
    """
    commit_sql(sql)

    return 'phones_create'


@app.route('/phones/read')
def phones_read():
    import sqlite3
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    sql = """
    SELECT * FROM Phones;
    """
    cur.execute(sql)

    result = cur.fetchall()
    con.close()

    return result


@app.route('/phones/update/')
def phones_update():
    contact_name = request.args.get('contactName', 'Unknown')
    phone_value = request.args.get('phone')

    phone_id = request.args.get('id')

    sql = f"""
    UPDATE Phones
    SET contactName = '{contact_name}', phoneValue = '{phone_value}'
    WHERE phoneID = {phone_id};
    """
    commit_sql(sql)

    return 'phones_update'


@app.route('/phones/delete/')
def phones_delete():
    phone_id = request.args.get('id')

    sql = f"""
    DELETE FROM Phones
    WHERE phoneID = {phone_id};
    """
    commit_sql(sql)

    return 'phones_delete'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
