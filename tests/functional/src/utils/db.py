from asyncpg import Connection


async def get_rows_count_from_table(conn: Connection, table_name: str, schema: str = 'emails') -> int:
    res = await conn.fetchrow(f'SELECT count(*) FROM {schema}.{table_name};')
    return int(res['count'])
