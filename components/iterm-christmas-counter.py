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
        short_description='Days until Christmas',
        detailed_description='Display the number of days until christmas.',
        knobs=[],
        exemplar='🎄 93',
        update_cadence=1,
        identifier='xmas.counter'
    )

    @iterm2.StatusBarRPC
    async def counter(knobs):
        christmas = datetime.datetime(2019, 12, 25)
        return "🎄 {}".format((christmas - datetime.datetime.now()).days)

    await component.async_register(connection, counter)


iterm2.run_forever(main)
