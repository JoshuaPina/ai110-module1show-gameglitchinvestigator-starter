# Bug Fix Log

## 2026-03-24

1. Refactored game logic into `logic_utils.py` and implemented:
   - `get_range_for_difficulty`
   - `parse_guess`
   - `check_guess`
   - `update_score`
2. Fixed hint and comparison glitch by removing type mismatch between `guess` and `secret`.
3. Fixed session state flow in `app.py`:
   - Attempts now start at `0`.
   - Difficulty changes reset game state safely.
   - New Game now resets attempts, score, status, and history.
4. Added Rich console logging for key gameplay/debug events.
5. Validation:
   - `python -m pytest -q` -> `3 passed`.
