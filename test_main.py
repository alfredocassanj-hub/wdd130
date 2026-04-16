from main import students

def test_add_students_logic():
    students.clear()

    students.append({"id": 1, "name": "Ana", "fee": 100, "paid": 0})
    students.append({"id": 2, "name": "Joao", "fee": 200, "paid": 50})

    assert len(students) == 2
    assert students[0]["name"] == "Ana"


def test_payment_and_balance():
    students.clear()

    students.append({"id": 1, "name": "Maria", "fee": 300, "paid": 100})
    students.append({"id": 2, "name": "Pedro", "fee": 200, "paid": 50})

    # cálculo de saldo
    balance1 = students[0]["fee"] - students[0]["paid"]
    balance2 = students[1]["fee"] - students[1]["paid"]

    assert balance1 == 200
    assert balance2 == 150