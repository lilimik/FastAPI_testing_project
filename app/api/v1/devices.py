import random

from fastapi import APIRouter, Depends

from ..hooks import db_conn
from app.managers.connection_manager import save_endpoints, save_devices
from app.models.dev_types import DevType


router = APIRouter()


def random_mac():
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))


@router.post('/create', status_code=201)
async def create_device(connection=Depends(db_conn)):
    quantity = 10

    values = ''
    for i in range(quantity):
        dev_id = random_mac()
        dev_type = DevType.RANDOM
        value = f'(\'{dev_id}\', \'{dev_type}\')'

        if values == '':
            values = value
        else:
            values += ', ' + value

    if not values == '':
        response_query = await save_devices(connection, values)

        list_ids = [record['id'] for record in response_query[:5]]
        values = ''
        for list_id in list_ids:
            value = f'(\'{list_id}\')'

            if values == '':
                values = value
            else:
                values += ', ' + value

        await save_endpoints(connection, values)


@router.get('/without_endpoints')
async def get_devices_without_endpoints(connection=Depends(db_conn)):
    query = f'with data as (' \
            f'select d.*, e.device_id as e_device_id ' \
            f'from devices d left outer join endpoints e ' \
            f'on d.id = e.device_id' \
            f') ' \
            f'select dev_type, count(id) ' \
            f'from data ' \
            f'where e_device_id is null ' \
            f'group by dev_type;'
    response_query = await connection.fetch(query)

    response_query = dict(response_query)

    return response_query
