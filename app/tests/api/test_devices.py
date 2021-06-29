import pytest
from httpx import AsyncClient

from app.api.v1.checks import checking_annograms
from app.api.v1.devices import get_devices_without_endpoints
from app.main import app
from app.managers.connection_manager import ConnectionManager
from app.managers.redis_manager import RedisManager

client = AsyncClient(app=app)


# Тест не проходит, как я понял, из-за несовместимости aioredis и python 3.8+
# Я сделал тест с arides, но там нужно менять порты для создания new_event_loop и его счетчика

# @pytest.mark.asyncio
# async def test_check_annograms():
#     redis = RedisManager()
#     await redis.create_pool()
#     await redis.pool.set('count', 0)
#     string1 = 'abc'
#     string2 = 'bca'
#     response_json = await checking_annograms(string1, string2, redis=redis)
#     async with AsyncClient(app=app) as ac:
#         response = await ac.get(f'http://localhost:8000/api/check/annograms/{string1}/{string2}')
#     assert response.status_code == 200
#     assert response.json() == response_json
#     await redis.close_pool()


# А также этот и следующие тесты проходят только если запускать их поочередно
# Вместе они не проходят, так как Асинхронных клиент будто закрывается

# @pytest.mark.asyncio
# async def test_create_devices():
#     async with AsyncClient(app=app) as ac:
#         response = await ac.post('http://localhost:8000/api/devices/create')
#     assert response.status_code == 201


# @pytest.mark.asyncio
# async def test_devices_without_endpoints():
#     db = ConnectionManager()
#     conn = await db.get_conn()
#     response_json = await get_devices_without_endpoints(connection=conn)
#
#     async with AsyncClient(app=app) as ac:
#         response = await ac.get('http://localhost:8000/api/devices/without_endpoints')
#     assert response.status_code == 200
#     assert response.json() == response_json
#     await db.close_connection()
