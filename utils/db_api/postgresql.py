from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class DataBase:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args, fetch: bool = False, fetchval: bool = False, fetchrow: bool = False,
                      execute: bool = False):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    @staticmethod
    def __format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)
        ])
        return sql, tuple(parameters.values())

    async def select_all_conf(self):
        sql = "SELECT * FROM scientific_and_analytical_department.conference_omstu"
        return await self.execute(sql, fetch=True)

    async def get_id_and_name_conf(self):
        sql = "SELECT co_id, co_name FROM scientific_and_analytical_department.conference_omstu"
        return await self.execute(sql, fetch=True)

    async def get_full_info(self, **kwargs):
        sql = "SELECT * FROM scientific_and_analytical_department.conference_omstu WHERE "
        sql, parameters = self.__format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def get_nearest_conf(self):
        sql = "SELECT * FROM scientific_and_analytical_department.conference_omstu WHERE co_data_start > current_date"
        return await self.execute(sql, fetch=True)
