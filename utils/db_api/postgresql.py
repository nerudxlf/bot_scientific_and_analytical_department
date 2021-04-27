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
        sql = "SELECT * FROM scientific_and_analytical_department.conferences_omstu"
        return await self.execute(sql, fetch=True)

    async def get_id_and_name_conf(self):
        sql = "SELECT co_id, co_short_name FROM scientific_and_analytical_department.conferences_omstu"
        return await self.execute(sql, fetch=True)

    async def get_full_info(self, **kwargs):
        sql = "SELECT * FROM scientific_and_analytical_department.conferences_omstu WHERE "
        sql, parameters = self.__format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def get_nearest_conf(self):
        sql = "SELECT * FROM scientific_and_analytical_department.conferences_omstu WHERE co_date_start > current_date"
        return await self.execute(sql, fetch=True)

    async def get_info_nti(self, name):
        sql = """
                SELECT * FROM scientific_and_analytical_department.conferences_omstu AS conf_omstu
	            LEFT JOIN scientific_and_analytical_department.nti_conf AS nti_conf  ON conf_omstu.co_id = nti_conf.nc_conf_omstu_id
	            INNER JOIN scientific_and_analytical_department.nti_names AS nti_names
	            ON nti_names.nn_id = nti_conf.nc_nti_names
	            WHERE nti_names.nn_name = $1 
            """
        return await self.execute(sql, name, fetch=True)

    async def get_info_sntr(self, name):
        sql = """
                    SELECT * FROM scientific_and_analytical_department.conferences_omstu AS conf_omstu
    	            LEFT JOIN scientific_and_analytical_department.sntr_conf AS sntr_conf  ON conf_omstu.co_id = sntr_conf.sc_conf_omstu_id
    	            INNER JOIN scientific_and_analytical_department.sntr_names AS sntr_names
    	            ON sntr_names.sn_id = sntr_conf.sc_sntr_names
    	            WHERE sntr_names.sn_name = $1 
                """
        return await self.execute(sql, name, fetch=True)
