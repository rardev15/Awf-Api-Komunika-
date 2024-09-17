import jwt
from datetime import datetime, timedelta, timezone

def create_jwt_token(payload):
    # Your secret key (guard it with your life!)
    secret_key = 'supersecretkey'
    # secret_key = 'lalalala'
    # Algorithm for token generation
    algorithm = 'HS256'
    token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return token

def validate_jwt_token(token_to_validate):
    secret_key = 'supersecretkey'
    algorithm = 'HS256'
    try:
        test = datetime.now()
        print(test)
        decoded_payload = jwt.decode(token_to_validate, secret_key, algorithms=[algorithm])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        print("Token has expired. Please log in again.")
    except jwt.InvalidTokenError:
        print("Invalid token. Access denied.")
    return None

payload = {
    'user_id': 777,
    'username': 'tom',
    'role': 'mouse_catcher',
    'exp': datetime.now(tz=timezone.utc) + timedelta(seconds=15) # Token will expire in 1 hour
}
# payload = ["asdadasd",12313,"2wrewr"]
print("JWT TOKEN: ", create_jwt_token(payload))


result = validate_jwt_token("""eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo3NzcsInVzZXJuYW1lIjoidG9tIiwicm9sZSI6Im1vdXNlX2NhdGNoZXIiLCJleHAiOjE3MjE3NDkwMjZ9.Vl12y_JHQsEDagDseC19jcT2GR9FNmKL24ZR1JCXW9s""")
print(result)
