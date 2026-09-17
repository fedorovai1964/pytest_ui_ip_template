from pages.AuthPage import AuthPage
from pages.MainPage import MainPage


def test_auth(browser):
    email = "fedorovatkach@gmail.com"
    password = "8Pouk3Xd!"
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    assert  main_page.get_current_url().endswith("boards")
    assert info[0] == "Ирина Федорова"
    assert info[1] == email





