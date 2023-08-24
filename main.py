import os

import uvicorn
from fastapi import FastAPI
from starlette.responses import PlainTextResponse

import config_loader

app_config = config_loader.load_config()

app = FastAPI(
    version="1.0.0",
    title="Test app for functional testing",
)


@app.get('/health', response_class=PlainTextResponse)
async def health() -> str:
    return 'Healthy'


if __name__ == '__main__':
    uvicorn.run(
        app,
        debug=app_config["api"]["debug"],
        host=os.getenv('server_address', '127.0.0.1'),
        port=int(os.getenv('server_port', 8000)),
        proxy_headers=True,
        forwarded_allow_ips='*',
    )
