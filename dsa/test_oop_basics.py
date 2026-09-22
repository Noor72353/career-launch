from oop_basics import BankAccount, SavingsAccount, CurrentAccount


def test_bank_account_deposit_and_withdraw():
    account = BankAccount("Noorwali", 1000)

    account.deposit(500)
    account.withdraw(300)

    assert account.balance == 1200
    assert account.show_history() == [
        "Deposited 500",
        "Withdrew 300",
    ]


def test_savings_account_interest():
    account = SavingsAccount("Noorwali", 1000, 0.05)

    account.add_interest()

    assert account.balance == 1050


def test_current_account_overdraft():
    account = CurrentAccount("Ali", 1000, 500)

    account.withdraw(1300)

    assert account.balance == -300
