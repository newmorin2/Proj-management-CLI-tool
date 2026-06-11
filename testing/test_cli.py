from types import SimpleNamespace
from main import add_user, list_users


def test_add_user(tmp_path, monkeypatch):
    args = SimpleNamespace(name="John", email="john@example.com")

    add_user(args)


def test_list_users_output(capsys):
    args = SimpleNamespace()

    list_users(args)
    captured = capsys.readouterr()

    assert isinstance(captured.out, str)