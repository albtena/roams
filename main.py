import argparse
import asyncio
import uvicorn
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import platform

from app.util import path as Path

DEVELOPER = "dev"
DOCKER = "docker"

FILE_ENVIRONMENT_DEVELOPER = ".env.dev"
FILE_ENVIRONMENT = ".env"


# Funciones que se ejecutaran en segundo plano
async def startup():
    pass


def main(env=None):
    root_path = Path.get_current_path()

    if env == DEVELOPER:
        env_file = Path.get_path_file(root_path, FILE_ENVIRONMENT_DEVELOPER)
        print("Loading ", FILE_ENVIRONMENT_DEVELOPER)

    elif env == DOCKER:
        env_file = Path.get_path_file(root_path, FILE_ENVIRONMENT)
        print("Loading ", FILE_ENVIRONMENT)

    else:
        env_file = Path.get_path_file(root_path, FILE_ENVIRONMENT_DEVELOPER)
        print("Loading ", FILE_ENVIRONMENT_DEVELOPER)

    load_dotenv(env_file)

    from app.api.fastapi.api import app

    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # # Se incorpora al bucle de eventos asincronos de FastApi
    app.add_event_handler("startup", startup)

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load a enviroment to execute the app")
    parser.add_argument(
        "--env",
        type=str,
        help='OPTIONS [ dev | docker ]" - E.g: python main.py --env dev',
    )

    args = parser.parse_args()
    if args.env:
        main(env=args.env)
    else:
        main()
