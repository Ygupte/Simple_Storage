from brownie import accounts, SimpleStorage


def test_deploy():
    account =accounts[0]
    simple_storage= SimpleStorage.deploy({"from":account})
    start_value =simple_storage.retrieve()
    expected =0
    assert start_value == expected



def test_update():
    account =accounts[0]
    simple_storage= SimpleStorage.deploy({"from":account})
    expected = 69
    simple_storage.store(69,{"from":account})
    assert expected == simple_storage.retrieve()
