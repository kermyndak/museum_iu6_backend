from fastapi import Path
from pydantic import BaseModel

class JWT_token(BaseModel):
    private_key_path: Path = APP_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = APP_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
