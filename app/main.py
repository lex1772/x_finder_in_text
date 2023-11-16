import uvicorn
from fastapi import FastAPI


def create_app():
    app = FastAPI(docs_url='/')

    @app.on_event("startup")
    async def startup_event():
        ...

    return app


def main():
    uvicorn.run(
        f"{__name__}:create_app",
        host='0.0.0.0', port=8888,
        debug=True,
    )


if __name__ == 'main':
    main()
