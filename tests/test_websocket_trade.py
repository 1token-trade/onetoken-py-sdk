import asyncio
from pathlib import Path

import pytest
import yaml


@pytest.mark.asyncio
async def test_trade_subscribe():
    import onetoken as ot
    ot.log.info('hello')
    r = Path('~/.onetoken/demo-vnpy.yml').expanduser().read_text()
    r = yaml.load(r)

    o = ot.Account('okex/mock-vnpy', api_key=r['ot_key'], api_secret=r['ot_secret'])

    async def h(*args, **kwargs):
        print(args, kwargs)

    await o.subscribe_info(h)
    for _ in range(10):
        await asyncio.sleep(1)
