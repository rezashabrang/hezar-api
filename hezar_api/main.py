"""Customizing fast api."""

from typing import Union

import os

from fastapi import FastAPI, Header, HTTPException
from fastapi.openapi.utils import get_openapi

from hezar_api.routers import http_nlp

app = FastAPI()


# app.mount(
#     "/app/hezar_api/static/",
#     StaticFiles(directory="/app/hezar_api/static/"),
#     name="static",
# )


# @app.get("/docs", include_in_schema=False)
# async def custom_swagger_ui_html():
#     return get_swagger_ui_html(
#         openapi_url=app.openapi_url,
#         title=app.title + " - Swagger UI",
#         oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
#         swagger_js_url="/app/hezar_api/static/bundle.js",
#         swagger_css_url="/app/hezar_api/static/swagger.css",
#     )


DESCRIPTION = """
Hezar API Endpoints
"""


async def get_token_header(x_token: str = Header(...)) -> Union[None, Exception]:
    """."""
    if x_token != os.getenv("API_KEY"):
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    return None


def custom_openapi():
    """Defining custom API schema."""
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Hezar API",
        version="0.1",
        description=DESCRIPTION,
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi  # type: ignore


app.include_router(
    http_nlp.router,
    prefix=os.getenv("ROOT_PATH", ""),
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)
