import pytest
from Table import TableClass

db = TableClass("postgresql://postgres:26041995@localhost:5432/QA")

@pytest.mark.bd
def test_add_user():
    #создание юзера
    user_id = 3334
    user_email = 'mail2@mail.ru'
    subject_id  = 10
    db.create_user(user_id, user_email, subject_id)

    #получение данных юзера
    new_user = db.get_users()[-1]

    #удаление юзера
    db.delete(user_id)

    assert new_user["user_id"] == user_id
    assert new_user["user_email"] == user_email
    assert new_user["subject_id"] == subject_id

@pytest.mark.bd
def test_edit_user():
    #создание юзера
    user_id = 3337
    user_email = 'mail3@mail.ru'
    subject_id  = 10
    db.create_user(user_id, user_email, subject_id)

    #изменение юзера
    new_email = "new@mail"
    id = user_id
    db.update_user(new_email, id)

    #получение данных юзера
    new_user = db.get_users()[-1]

    #удаление юзера
    db.delete(user_id)

    assert new_user["user_email"] == new_email

@pytest.mark.bd
def test_delete_user():
    #создание юзера
    user_id = 3338
    user_email = 'mail4@mail.ru'
    subject_id  = 10
    db.create_user(user_id, user_email, subject_id)
    count_before = len(db.get_users())

    #удаление юзера
    db.delete(user_id)

    #количество строк уменьшилось на 1 после удаления
    count_after = len(db.get_users())
    assert count_after == count_before - 1


