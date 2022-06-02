from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message11': 'Hello World!'}
