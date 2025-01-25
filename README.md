# online_sales_analysis
Sistem za analizu prodajnih podataka u online prodavnici

product.py
Implementira klasu Product za predstavljanje pojedinačnog proizvoda sa sledećim atributima i metodama:
name - naziv proizvoda
price - cijena proizvoda
quantity - količina proizvoda
display_info() - prikazuje informacije o proizvodu
update_quantity(new_quantity) - ažurira količinu proizvoda

product_manager.py
Implementira klasu ProductManager, koja upravlja listom dostupnih proizvoda sa sledećim funkcionalnostima:
Dodavanje proizvoda (add_product)
Prikaz svih proizvoda (display_all_products)
Prikaz ukupne vrednosti svih proizvoda u inventaru (total_inventory_value)
Uklanjanje proizvoda prema imenu (remove_product_by_name)

cart.py
Implementira klasu Cart, koja upravlja korpom kupca sa sledećim funkcionalnostima:
Dodavanje proizvoda u korpu (add_to_cart)
Računanje ukupne vrednosti korpe (calculate_total)
Prikaz sadržaja korpe (display_cart)

main.py
Glavna skripta aplikacije:
Kreiranje i upravljanje instancom klase ProductManager.
Dodavanje proizvoda u menadžer.
Kreiranje korpe (Cart) i dodavanje proizvoda u korpu.
Prikaz sadržaja korpe i vrijednosti korpe.


Kako Pokrenuti Projekat
Klonirajte ili preuzmite repozitorijum:
git clone https://github.com/urosdedic/online_sales_analysis
cd online_sales_analysis

Pokrenite aplikaciju:
python main.py
