import json
import datetime
import sys
from pathlib import Path

import iterm2

def expand_path(path: str) -> str:
    return Path(path).expanduser().resolve().__str__()

REAL_ROOTDIR_PATH = Path(__file__).resolve().parent
sys.path.append(REAL_ROOTDIR_PATH.__str__())
CONFIG = json.load(open(REAL_ROOTDIR_PATH / 'config.json'))
sys.path.append(expand_path(CONFIG['PipPackagePath']))

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Days employed',
        detailed_description='Display the number of days at Kubra.',
        knobs=[],
        exemplar='💼 93',
        update_cadence=1,
        identifier='employment.counter'
    )

    @iterm2.StatusBarRPC
    async def days_employed_counter(knobs):
        employed_at = datetime.datetime(month=6, day=24, year=2019)
        return "💼 {}".format((datetime.datetime.now() - employed_at).days)

    await component.async_register(connection, days_employed_counter)


iterm2.run_forever(main)
