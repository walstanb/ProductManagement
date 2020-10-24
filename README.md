
# Inventory Management Web Application

*The goal is to create a web application using Flask framework to manage inventory of a list of products in respective warehouses. Imagine this application will be used in a shop or a warehouse that needs to keep track of various products and various locations.*

The application should cover following functionalities:

**Database Tables:**  
Product (`product_id`)   
Location (`location_id`)   
ProductMovement (`movement_id`, `timestamp, from_location`,` to_location`, `product_id`, `qty`)  

**Note:**
Primary keys can be text / varchar Any one, or both of `from_location` and `to_location` can be filled. If you want to move things into a location, `from_location` will be blank, if you want to move things out, then `to_location` will be blank.

**Views:**  
Add/Edit/View `Product`  
Add/Edit/View `Location`  
Add/Edit/View `ProductMovement`  

**Report:**  
Balance quantity in each location  

**Use Cases:**  
Create 3/4 `Products`  
Create 3/4 `Locations`  
Make ProductMovements
Move `Product A` to `Location X`  
Move `Product B` to `Location X`  
Move `Product A` from `Location X` to `Location Y`  
(make 20 such movements)  

Get product balance in each Location in a grid view, with 3 columns: `Product`, `Warehouse`, `Qty`  

**Setup a Virtual Enviorment for your system**
```
python -m venv env
```

**Activate Virtual Enviorment**

- For Windows 
```
env\Scripts\activate
```
- For Linux
```
source env\bin\activate
```

**Installing dependencies:**  
```
pip3 install -r requirements.txt
```

**Execution:**  
```
flask run
```
or
```
python -m flask run
```

## ProductManagement

**![](https://github.com/walstanb/ProductManagement/blob/master/screenshots/Screenshot(287).png?raw=true)**

**![](https://github.com/walstanb/ProductManagement/blob/master/screenshots/Screenshot(288).png?raw=true)**

**![](https://github.com/walstanb/ProductManagement/blob/master/screenshots/Screenshot(289).png?raw=true)**

**![](https://github.com/walstanb/ProductManagement/blob/master/screenshots/Screenshot(290).png?raw=true)**
