import pytest


@pytest.mark.parametrize("count", [3])
def test_cart_work(app, count):
    app.open_main_page()
    for _ in range(count):
        app.open_items_details_page()
        app.add_items_in_cart()
        app.open_main_page()
    app.clear_cart()
