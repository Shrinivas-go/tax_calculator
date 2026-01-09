from tax import calculate_tax

def test_default_tax():
    result = calculate_tax(["tax.py"])
    assert result["tax"] == 25000
    assert result["status"] == "5% Tax Applied"

def test_high_income_tax():
    args = ["tax.py", "Anita", "TX202", "1200000"]
    result = calculate_tax(args)
    assert result["tax"] == 360000
    assert result["status"] == "30% Tax Applied"
