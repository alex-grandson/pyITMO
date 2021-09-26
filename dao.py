import os
from typing import Dict, List, Tuple
import sqlite3

# conn = sqlite3.connect("messages.db", check_same_thread=False)
conn = sqlite3.connect("messages.db")
cursor = conn.cursor()


def insert(table: str, column_values: Dict):
    columns = ', '.join(column_values.keys())
    values = [tuple(column_values.values())]
    placeholders = ", ".join("?" * len(column_values.keys()))
    try:
        cursor.executemany(
            f"INSERT INTO {table} "
            f"({columns}) "
            f"VALUES ({placeholders})",
            values)
        conn.commit()
    except Exception as e:
        print('Insert Failed!\nException:', e)


def update(table: str, primary_key, value, data: Dict):
    """Обновление значения в таблице по параметру primary_key"""
    statements = []
    for key in data:
        statements.append(key + ' = ' + str(data[key]))
    query = ', '.join(statements)
    try:
        sql_q = f"UPDATE {table} " \
                       f"SET {query} " \
                       f"WHERE {primary_key}={value}"
        print(sql_q)
        cursor.execute(f"UPDATE {table} "
                       f"SET {query} "
                       f"WHERE {primary_key}={value}")
        conn.commit()
    except Exception as e:
        print('Update Failed!\nException:', e)


def fetchall(table: str, columns: List[str]) -> List[Tuple]:
    """Получает все данные селект запроса и выдает массив словарей (строк)"""
    columns_joined = ", ".join(columns)
    cursor.execute(f"SELECT {columns_joined} FROM {table}")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        dict_row = {}
        for index, column in enumerate(columns):
            dict_row[column] = row[index]
        result.append(dict_row)
    return result


def delete(table: str, row_id: int) -> None:
    row_id = int(row_id)
    cursor.execute(f"delete from {table} where id={row_id}")
    conn.commit()


def get_cursor():
    return cursor


def get_message(table: str, message_id: int, lang: str) -> List[str]:
    result = []
    columns = ['message_id', lang]
    cursor.execute(f'SELECT {", ".join(columns)} FROM {table} '
                   f'WHERE {columns[0]} IS {message_id}')
    rows = cursor.fetchall()
    for row in rows:
        dict_row = {}
        for index, column in enumerate(columns):
            dict_row[column] = row[index]
        result.append(dict_row[lang])
    return result


def add_user(id: int, lang: str):
    insert('users', {
        'id': id,
        'lang': lang
    })


def user_exists(id: int) -> bool:
    cursor.execute(f'SELECT * FROM users WHERE id IS {id}')
    rows = cursor.fetchall()
    return rows != []


def set_lang(id: int, lang: str):
    update('users', 'id', id, {
        'lang': '"' + lang + '"'
    })


def get_lang(id: int) -> str:
    cursor.execute(f'SELECT lang FROM users WHERE id IS {id}')
    val = cursor.fetchone()
    return val[0]


def is_russian(id: int) -> bool:
    return get_lang(id) == 'rus'


def get_plot_point(id: int) -> int:
    cursor.execute(f'SELECT plot_point FROM users WHERE id IS {id}')
    plot_point = int(cursor.fetchone()[0])
    return plot_point


def update_plot_point(id: int, plot_point: int):
    update('users', 'id', id, {
        'plot_point': plot_point
    })


def get_and_increase_plot_point(id: int) -> int:
    plot_point = get_plot_point(id)
    update_plot_point(id, plot_point + 1)
    return plot_point

# def _init_db():
#     """Инициализирует БД"""
#     with open("createdb.sql", "r") as f:
#         sql = f.read()
#     cursor.executescript(sql)
#     conn.commit()
#
#
# def check_db_exists():
#     """Проверяет, инициализирована ли БД, если нет — инициализирует"""
#     cursor.execute("SELECT name FROM sqlite_master "
#                    "WHERE type='table' AND name='messages'")
#     table_exists = cursor.fetchall()
#     if table_exists:
#         return
#     _init_db()
