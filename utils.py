from faker import Faker
import pkg_resources
import requests

faker = Faker()


def generate_requirements():
    installed_packages = [(pkg.key, pkg.version) for pkg in pkg_resources.working_set]

    with open("requirements.txt", "w") as file:
        for package, version in installed_packages:
            file.write(f"{package}=={version}\n")

    requirements_content = "\n".join([f"{package}=={version}" for package, version in installed_packages])
    return requirements_content


def gen_users(quantity: int = 100) -> str:
    result = ''
    for _ in range(quantity):
        users = faker.name()
        email = faker.email(users)
        result += f'<p>Ім\'я: {users}, Електронна адреса: {email}</p>'
    return result


def space_utils():
    url = 'http://api.open-notify.org/astros.json'
    response = requests.get(url)
    return response


def commit_sql(sql: str):
    import sqlite3

    try:
        con = sqlite3.connect('example.db')
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
    finally:
        con.close()
