# ShapePlay 3D

Local-first toolkit to generate and refine 3D assets. **Sprint 0** provides a minimal CLI,
device detection, linting, tests, and CI.

## Quickstart

```bash
make setup && shapeplay --help
```

If `torch` supports MPS on your Mac, `detect_device()` will report `mps`; otherwise `cpu`.

## Development
- Lint/format: `make lint` / `make format`
- Test: `make test`
