from datetime import time
from typing import Dict

import jwt

JWT_SECRET = "asdasdasdas"
JWT_ALGORITHM = "HS256"

def sign_jwt(user_id: str) -> str:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token