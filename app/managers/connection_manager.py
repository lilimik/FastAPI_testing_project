import asyncpg


class ConnectionManager:

    def __init__(self):
        self.conn = None

    async def get_conn(self):
        self.conn = await asyncpg.connect(
            database="testing_task",
            user="postgres",
            password="11235813mixa",
            port="5432"
        )
        return self.conn

    async def get_connection(self):
        if self.conn is None:
            self.conn = await self.get_conn()
        return self.conn

    async def close_connection(self):
        await self.conn.close()


async def save_devices(conn, values):
    query = f'INSERT INTO devices (dev_id, dev_type) values {values} returning id;'

    try:
        response_query = await conn.fetch(query)
        return response_query
    except Exception as msg:
        print(msg)


async def save_endpoints(conn, values):
    query = f'INSERT INTO endpoints (device_id) values {values};'

    try:
        response_query = await conn.execute(query)
        return response_query
    except Exception as msg:
        print(msg)
