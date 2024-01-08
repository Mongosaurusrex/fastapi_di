from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from .containers import Container

router = APIRouter()


@router.get("/health")
@inject
def get_health():
    return "Healthy boi"
