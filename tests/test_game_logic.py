from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    outcome, _ = result
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    outcome, _ = result
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    outcome, _ = result
    assert outcome == "Too Low"


def test_negative_guess_is_handled_gracefully():
    # Negative integers should parse and evaluate without crashing
    ok, guess_int, err = parse_guess("-5")
    assert ok is True
    assert guess_int == -5
    assert err is None

    outcome, _ = check_guess(guess_int, 50)
    assert outcome == "Too Low"


def test_decimal_guess_is_rejected_gracefully():
    # Decimal strings should be rejected cleanly as invalid input
    ok, guess_int, err = parse_guess("42.5")
    assert ok is False
    assert guess_int is None
    assert err == "That is not a number."


def test_extremely_large_guess_is_handled_gracefully():
    # Very large integers should not crash logic comparisons
    big_guess = "999999999999999999999999999999"
    ok, guess_int, err = parse_guess(big_guess)
    assert ok is True
    assert guess_int == int(big_guess)
    assert err is None

    outcome, _ = check_guess(guess_int, 50)
    assert outcome == "Too High"
