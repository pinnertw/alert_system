from pgi_daily.discord_utils import send_discord_alert, send_discord_message
from dc_config import pinner
import asyncio

asyncio.get_event_loop().run_until_complete(send_discord_alert(
    f'''
    test
    I
    can 
    send
    multiple
    lines
    '''
    ))
asyncio.get_event_loop().run_until_complete(send_discord_message(
    f'''
    test
    I
    can 
    send
    multiple
    lines
    ''',
    channel_id=994362506447421560
    ))
