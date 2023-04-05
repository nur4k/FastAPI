from typing import Union

from fastapi import FastAPI


app = FastAPI(title="Traiding App")


@app.get('/')
def say_hello():
    return "Hello world!"
