**Basis voor de recommendation engine**

_In dit opdracht wordt er gewerkt aan een aanbevelingssysteem voor het huwebshop.
Het systeem maakt gebruik van 
content-based filtering en collaborative filtering.

Vereisten
PostgreSQL
psycopg2

https://github.com/Omyasar/opdracht3sp

**Duidelijkheid voor de modules;**

**database_connectie.py:**
Deze module is verantwoordelijk voor het maken van een verbinding met de PostgreSQL-database.
Het bevat de functie database_connectie(), die een connectie-object en een cursor-object retourneert
om met de database te communiceren.

**Module 2: collaborative_filtering.py**
Deze module bevat functies om met de database te communiceren en producten te filteren op basis van bepaalde criteria:
**previously_recommended_id_query():**
Haalt eerder aanbevolen producten op basis van het recommendations_id (profiel-ID) uit de recommendations-tabel.
**kenmerken_product_ids(kenmerken_list):**
Haalt productkenmerken (soort en gender) op uit de products-tabel voor een gegeven lijst van product-ID's.
**soort_gender_query(gender_value, soort_value):**
Haalt product-ID's op uit de products-tabel op basis van de opgegeven soort en gender,
gesorteerd op brand in oplopende volgorde en beperkt tot 4 producten.
**insert_collab(categorie_doelgroep_ids):**
Verwijdert alle records uit de collab_filtered_products-tabel
en voegt de aanbevolen product-ID's toe die zijn verkregen uit soort_gender_query().

**Module 3: contentfiltering.py**
**Deze module bevat functies om producten te filteren op basis van hun categorie en geslacht:**
**kenmerken_prod_id(kenmerk):**
Haalt de categorie en het geslacht van een product op uit de products-tabel op basis van de opgegeven product-ID.
**gender_category_ids(gender_value, categorie_value):**
Haalt product-ID's op uit de products-tabel die overeenkomen met de gegeven categorie en geslacht waarden, gesorteerd op prijs in aflopende volgorde en beperkt tot 4 producten.
**insert_content(content_ids):**
Verwijdert alle records uit de content_filtered_recommendations-tabel en voegt de aanbevolen product-ID's toe die zijn verkregen uit gender_category_ids().