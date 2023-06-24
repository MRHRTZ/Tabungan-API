from pydantic import BaseModel
from typing import Tuple

def generate_insert_sql_from_model(table_name: str, model: BaseModel) -> Tuple[str, tuple]:
    columns = model.__annotations__.keys()
    values = [getattr(model, column) for column in columns]

    column_names = ', '.join(columns)
    placeholders = ', '.join(["'%s'"] * len(values))

    insert_sql = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"
    return insert_sql, tuple(values)

def generate_update_sql_from_model(table_name: str, model: BaseModel, condition: str) -> Tuple[str, tuple]:
    columns = model.__annotations__.keys()
    values = [getattr(model, column) for column in columns]

    set_clauses = ', '.join([f"{column} = %s" for column in columns])

    update_sql = f"UPDATE {table_name} SET {set_clauses} WHERE {condition}"
    return update_sql, tuple(values)

def generate_insert_sql(table_name: str, data: str) -> Tuple[str, tuple]:
    columns = list(data.keys())
    values = list(data.values())

    column_names = ', '.join(columns)
    placeholders = ', '.join(["'%s'"] * len(values))

    insert_sql = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"
    return insert_sql, tuple(values)

def generate_update_sql(table_name: str, data: str, condition: str) -> Tuple[str, tuple]:
    columns = list(data.keys())
    values = list(data.values())

    set_clauses = ', '.join([f"{column} = %s" for column in columns])

    update_sql = f"UPDATE {table_name} SET {set_clauses} WHERE {condition}"
    return update_sql, tuple(values)