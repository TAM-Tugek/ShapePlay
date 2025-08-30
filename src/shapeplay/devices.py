import torch


def detect_device() -> str:
    """Return best-available compute device: 'mps' (Apple Silicon) else 'cpu'."""

    try:
        if torch.backends.mps.is_available():
            return "mps"
    except Exception:
        # If Torch is present but MPS query fails, fall back to CPU
        pass
    return "cpu"
