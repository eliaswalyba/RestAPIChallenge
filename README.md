![](./family-eating.jpg "Wallpaper")

# RestAPIChallenge
RESTful API for the management of the orders in the restaurant mobile application MonMenu by Suite 2.0

## Database diagramme
![](./models.png "Database diagramme")

## Ressources Endpoints
| METHOD | URL               | DESCRIPTION                                 |
|--------|-------------------|---------------------------------------------|
| GET    | /api/orders/      | displays all orders in the database         |
|        | /api/orderlines/  | displays all orderlines in the database     |
|        | /api/meals/       | displays all meals in the database          |
|        | /api/menus/       | displays all menus in the database          |
|        | /api/customers/   | displays all customers in the database      |
|        | /api/restaurants/ | displays all restaurants in the database    |
|        | /api/categories/  | displays all categories in the database     |
|        | /api/geopoints/   | displays all geopoints in the database      |     
| POST   | /api/orders/      | creates one order in the database           |
|        | /api/orderlines/  | creates one orderline in the database       |
|        | /api/meals/       | creates one meal in the database            |
|        | /api/menus/       | creates one menu in the database            |
|        | /api/customers/   | creates one customer in the database        |
|        | /api/restaurants/ | creates one orderline in the database       |
|        | /api/categories/  | creates one category in the database        |
|        | /api/geopoints/   | creates one geopoint in the database        |
| PUT    | /api/orders/\<pk> | edits the order with id = pk in the database|
|        | /api/orderlines/\<pk>  | edits the orderline with id = pk in the database       |
|        | /api/meals/\<pk>       | edits the meal with id = pk in the database           |
|        | /api/menus/\<pk>       | edits the menu with id = pk in the database           |
|        | /api/customers/\<cellphone>   | edits the customer with cellphone = cellphone in the database; cellphone should be 9 characters long string not more not less         |
|        | /api/restaurants/\<pk> | edits the restaurant with id = pk in the database         |
|        | /api/categories/\<name>  | edits the category with name = name in the database; name should be string          |
|        | /api/geopoints/\<pk>   | edits the geopoint with id = pk in the database          |
| DELETE   | /api/orders/\<pk>      | deletes the order with id = pk in the database             |
|        | /api/orderlines/\<pk>  | deletes the orderline with id = pk in the database         |
|        | /api/meals/\<pk>       | deletes the meal with id = pk in the database            |
|        | /api/menus/\<pk>       | deletes the menu with id = pk in the database             |
|        | /api/customers/\<cellphone>   | deletes the customer with cellphone = cellphone in the database; cellphone should be 9 characters long string not more not less         |
|        | /api/restaurants/\<pk> | deletes the meal restaurant id = pk in the database       |
|        | /api/categories/\<name>  | deletes the category with name = name in the database; name should be string        |
|        | /api/geopoints/\<pk>   | deletes the geopoint with id = pk in the database        |

## Environnement
### OS
* Ubuntu

### Programming language
* Python 3.5

### Frameworks
* Django 1.11.7
* DjangoRestFramework 3

### Editor
* Visual Studio Code 1.18.1