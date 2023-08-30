from time import sleep
from urllib.parse import urljoin

import httpx


def main():
    service_path = 'http://app:8000'
    health_path = urljoin(service_path, '/health')
    retry_count = 20

    for i in range(retry_count):
        try:
            res = httpx.get(health_path)
            res.raise_for_status()
            print(f'service is alive on {service_path}')  # noqa
            break
        except httpx.ConnectError:
            print(f'service service is not alive on {service_path}')  # noqa
        except Exception as e:
            print(e)  # noqa
        finally:
            sleep(1)


if __name__ == '__main__':
    main()
