from fastapi import APIRouter, Depends, HTTPException, Request

router = APIRouter()


# -----------------------------------------------------------------------------
# GET /
# -----------------------------------------------------------------------------
@router.get('/', tags=['v1'])
async def get_root(request: Request):
    return {
        'message': 'MoonShuttle Project Template',
        'client_host': request.client.host,
        'system_status': 'UP'
    }


# -----------------------------------------------------------------------------
# GET /people
# -----------------------------------------------------------------------------
@router.get('/users', tags=['v1'])
async def get_users():
    return [
        {
            "name": "Juan",
            "email": "juan@example.com"
        },
        {
            "name": "Ana",
            "email": "ana@example.com"
        },
        {
            "name": "Luis",
            "email": "luis@example.com"
        },
        {
            "name": "Maria",
            "email": "maria@example.com"
        }
    ]
