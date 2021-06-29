from app.managers.connection_manager import ConnectionManager
from app.managers.redis_manager import RedisManager

from fastapi import Request

_db = ConnectionManager()
_redis = RedisManager()


async def db_conn(request: Request):
    conn = await request.state.db.get_connection()
    return conn


def redis_conn(request: Request):
    return request.state.redis


def setup_hooks(app):
    @app.middleware('http')
    async def db_session_middleware(request: Request, call_next):
        request.state.redis = _redis
        request.state.db = _db
        response = await call_next(request)
        return response

    @app.on_event('startup')
    async def startup():
        await _redis.create_pool()
        await _redis.pool.set('count', 0)

    @app.on_event('shutdown')
    async def shutdown():
        await _db.close_connection()
        await _redis.close_pool()
