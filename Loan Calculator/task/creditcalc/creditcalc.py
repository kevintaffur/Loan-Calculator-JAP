import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type",
                    choices=["diff", "annuity"],
                    help="Incorrect parameters")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()


def print_monthly_payments(months):
    years = months // 12
    months = months % 12

    years_word = "years"
    months_word = "months"

    if years == 1:
        years_word = "year"

    if months == 1:
        months_word = "month"

    if years == 0:
        print(f"It will take {months} {months_word} to repay this loan!")
    elif months == 0:
        print(f"It will take {years} {years_word} to repay this loan!")
    else:
        print(f"It will take {years} {years_word} and {months} {months_word} to repay this loan!")


if args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")
elif args.interest is None:
    print("Incorrect parameters")
elif args.type == "diff":
    loan_principal = int(args.principal)
    periods = int(args.periods)
    interest = float(args.interest)

    interest = interest / (12 * 100)

    paid = 0
    for i in range(1, periods + 1):
        payment = (loan_principal / periods) + interest * (loan_principal - (loan_principal * (i - 1)) / periods)
        payment = math.ceil(payment)
        print(f"Month {i}: payment is {payment}")
        paid += payment

    print(f"Overpayment = {paid - loan_principal}")

elif args.type == "annuity":
    if args.principal is None:
        payment = float(args.payment)
        periods = int(args.periods)
        interest = float(args.interest)

        interest = interest / (12 * 100)

        loan_principal = payment / ((interest * math.pow((1 + interest), periods)) / (pow((1 + interest), periods) - 1))
        loan_principal = round(loan_principal)
        print(f"Your loan principal = {loan_principal}!")
    if args.periods is None:
        loan_principal = int(args.principal)
        payment = int(args.payment)
        interest = float(args.interest)

        interest = interest / (12 * 100)

        periods = math.log(payment / (payment - interest * loan_principal), (1 + interest))
        periods = math.ceil(periods)
        print_monthly_payments(periods)
        print(f"Overpayment = {(payment * periods) - loan_principal}")
    if args.payment is None:
        loan_principal = int(args.principal)
        periods = int(args.periods)
        interest = float(args.interest)

        interest = interest / (12 * 100)

        payment = loan_principal * ((interest * math.pow((1 + interest), periods)) / (math.pow((1 + interest), periods) - 1))
        payment = math.ceil(payment)
        print(f"Your monthly payment = {payment}!")
