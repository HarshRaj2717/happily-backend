import hashlib


def generate_hash(value: str) -> str:
    """
    Generate a SHA-256 hash and return it
    """
    return hashlib.sha256(value.encode()).hexdigest()


def verify_professional() -> bool:
    """
    TODO

    Checks if the provided user is a professional(psychologist/psychiatrist/ngo) or not

    Returns True if user verified to be a professional
    """
    return True
