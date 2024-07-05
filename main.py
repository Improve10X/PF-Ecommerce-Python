from DummyDataFactory import DummyDataFactory
from MainMenu import MainMenu
from ProductCatalog import ProductCatalog

if __name__ == "__main__":
    product_catalog = ProductCatalog()
    DummyDataFactory.preloadData(product_catalog)

    main_menu = MainMenu(product_catalog)
    while True:
        main_menu.display_main_menu()
        main_menu.handle_main_menu_input()
