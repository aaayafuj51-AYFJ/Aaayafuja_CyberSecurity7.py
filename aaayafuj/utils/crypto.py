import hashlib
import os

def generate_asset_hash(data: bytes) -> str:
    """Generates a SHA-256 hash for asset integrity verification."""
    return hashlib.sha256(data).hexdigest()

def secure_random_bytes(length: int = 32) -> bytes:
    """Generates cryptographically secure random bytes."""
    return os.urandom(length)
