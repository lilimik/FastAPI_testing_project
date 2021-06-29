from fastapi import APIRouter, Depends
from app.api.hooks import redis_conn
router = APIRouter()


@router.get('/annograms/{string1}/{string2}')
async def checking_annograms(string1: str, string2: str, redis=Depends(redis_conn)):
    annograms_status = False
    count = int(await redis.pool.get('count'))
    if string1 and string2 is not None:
        string1 = list(string1.strip().lower())
        string2 = list(string2.strip().lower())
        string1.sort()
        string2.sort()
        if string1 == string2:
            annograms_status = True
            count += 1
            await redis.pool.set('count', count)
    return {'annograms_status': annograms_status,
            'redis_count': count}
