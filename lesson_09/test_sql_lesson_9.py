from sqlalchemy import create_engine, text

db = create_engine("postgresql://postgres:1977@localhost:5432/QA")


def test_create_students():
    # Проверка таблицы студентов пока остаётся прежней
    with db.connect() as connection:
        students = connection.execute(text("SELECT * FROM student")).fetchall()
        print(students)


def test_create_subjects():
    with db.connect() as connection:
        initial_count = connection.execute(text("SELECT COUNT(*) FROM subject")).scalar_one()

        # Выбираем следующий доступный subject_id путем max(subject_id)+1
        next_subject_id = connection.execute(text("SELECT MAX(subject_id) FROM subject")).scalar_one_or_none()
        if next_subject_id is None:
            next_subject_id = 1
        else:
            next_subject_id += 1

        # Добавляем новый предмет
        connection.execute(text("INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)"),
                           {"id": next_subject_id, "title": "Физика"})

        final_count = connection.execute(text("SELECT COUNT(*) FROM subject")).scalar_one()
        assert final_count == initial_count + 1


def test_update_subject_name():
    with db.connect() as connection:
        initial_count = connection.execute(text("SELECT COUNT(*) FROM subject")).scalar_one()

        # Определяем следующий доступный subject_id аналогично предыдущему тесту
        next_subject_id = connection.execute(text("SELECT MAX(subject_id) FROM subject")).scalar_one_or_none()
        if next_subject_id is None:
            next_subject_id = 1
        else:
            next_subject_id += 1

        # Создаем новую запись для тестирования обновления названия
        new_subject_title = 'Baseball'
        connection.execute(text("INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)"),
                           {"id": next_subject_id, "title": new_subject_title})

        # Обновляем название и проверяем обновление
        updated_subject_title = 'Биология'
        connection.execute(text("UPDATE subject SET subject_title=:title WHERE subject_id=:id"),
                           {"id": next_subject_id, "title": updated_subject_title})

        fetched_subject = connection.execute(text("SELECT subject_title FROM subject WHERE subject_id=:id"),
                                             {"id": next_subject_id}).scalar_one()
        assert fetched_subject == updated_subject_title


def test_delete_subject():
    with db.connect() as connection:
        initial_count = connection.execute(text("SELECT COUNT(*) FROM subject")).scalar_one()

        # Получаем последний созданный subject_id для удаления
        last_subject_id = connection.execute(text("SELECT MAX(subject_id) FROM subject")).scalar_one()

        # Удаление последней записи
        connection.execute(text("DELETE FROM subject WHERE subject_id=:id"), {"id": last_subject_id})

        final_count = connection.execute(text("SELECT COUNT(*) FROM subject")).scalar_one()
        assert final_count == initial_count - 1