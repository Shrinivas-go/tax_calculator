import sys

def calculate_tax(argv):
    if len(argv) == 4:
        script_name = argv[0]
        name = argv[1]
        taxpayer_id = argv[2]
        income = float(argv[3])
    else:
        script_name = argv[0]
        name = "Ravi Kumar"
        taxpayer_id = "TX101"
        income = 500000

    if income <= 250000:
        tax = 0
        status = "No Tax"
    elif income <= 500000:
        tax = income * 0.05
        status = "5% Tax Applied"
    elif income <= 1000000:
        tax = income * 0.20
        status = "20% Tax Applied"
    else:
        tax = income * 0.30
        status = "30% Tax Applied"

    net_income = income - tax

    return {
        "name": name,
        "taxpayer_id": taxpayer_id,
        "income": income,
        "tax": tax,
        "net_income": net_income,
        "status": status
    }

if __name__ == "__main__":
    result = calculate_tax(sys.argv)
    print("Name:", result["name"])
    print("Taxpayer ID:", result["taxpayer_id"])
    print("Annual Income:", result["income"])
    print("Tax Amount:", result["tax"])
    print("Net Income:", result["net_income"])
    print("Status:", result["status"])
