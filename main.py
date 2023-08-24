import os

import uvicorn

from app.build_app import build_app
from app.settings import get_settings


if __name__ == '__main__':
    uvicorn.run(
        build_app(get_settings()),
        host=os.getenv('server_address', get_settings().server.host),
        port=int(os.getenv('server_port', get_settings().server.port)),
        # https://www.uvicorn.org/settings/#http
        proxy_headers=True,
        forwarded_allow_ips='*',
    )
