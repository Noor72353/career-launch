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


def test_bank_account_default_balance():
    account = BankAccount("Noorwali")

    assert account.balance == 0
    assert account.show_history() == []


def test_invalid_deposit_does_not_change_balance(capsys):
    account = BankAccount("Noorwali", 1000)

    account.deposit(0)

    assert account.balance == 1000
    assert account.show_history() == []
    assert "Deposit amount must be positive." in capsys.readouterr().out


def test_invalid_withdrawal_does_not_change_balance(capsys):
    account = BankAccount("Noorwali", 1000)

    account.withdraw(0)

    assert account.balance == 1000
    assert account.show_history() == []
    assert "Withdrawal amount must be positive." in capsys.readouterr().out


def test_withdraw_more_than_balance(capsys):
    account = BankAccount("Noorwali", 1000)

    account.withdraw(1500)

    assert account.balance == 1000
    assert account.show_history() == []
    assert "Insufficient balance." in capsys.readouterr().out


def test_savings_account_interest():
    account = SavingsAccount("Noorwali", 1000, 0.05)

    account.add_interest()

    assert account.balance == 1050
    assert account.show_history() == ["Deposited 50.0"]


def test_current_account_overdraft():
    account = CurrentAccount("Ali", 1000, 500)

    account.withdraw(1300)

    assert account.balance == -300
    assert account.show_history() == ["Withdrew 1300"]


def test_current_account_exceeds_overdraft_limit(capsys):
    account = CurrentAccount("Ali", 1000, 500)

    account.withdraw(1600)

    assert account.balance == 1000
    assert account.show_history() == []
    assert "Withdrawal exceeds overdraft limit." in capsys.readouterr().out


def test_bank_account_str_and_repr():
    account = BankAccount("Noorwali", 1000)

    assert str(account) == "BankAccount(owner=Noorwali, balance=1000)"
    assert repr(account) == "BankAccount(owner='Noorwali', balance=1000)"


def test_savings_account_str():
    account = SavingsAccount("Noorwali", 1000, 0.05)

    assert str(account) == "SavingsAccount(owner=Noorwali, balance=1000)"


def test_current_account_str():
    account = CurrentAccount("Ali", 1000, 500)

    assert str(account) == "CurrentAccount(owner=Ali, balance=1000)"
