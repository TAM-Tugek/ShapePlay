# ADR 0002: Device selection policy

**Status:** Proposed

## Decision
Default to `mps` on Apple Silicon when available; otherwise `cpu`. CUDA will be evaluated in a future ADR.

## Rationale
Matches team hardware (Mac M‑series), minimizes external setup friction in Sprint 0.
