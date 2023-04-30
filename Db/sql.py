import MySQLdb

# MySQL database connection settings
db_host = 'localhost'
db_user = 'root'
db_password = '123123'
db_name = 'fypbackend'

# Create a connection
db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)

# Create a cursor to execute queries
cursor = db.cursor()

# CREATE query to create the 'product_images' table
def create_product_images_table():
    query = "CREATE TABLE product_images (product_id INT NOT NULL, image_data BLOB NOT NULL, PRIMARY KEY (product_id))"
    cursor.execute(query)
    db.commit()

# CREATE query to create the 'product' table
def create_product_table():
    query = "CREATE TABLE product (product_id INT NOT NULL, product_name VARCHAR(255) NOT NULL, owner_id INT NOT NULL, parent INT[] NOT NULL, price INT NOT NULL, quantity INT NOT NULL, description VARCHAR(255), PRIMARY KEY (product_id), FOREIGN KEY (owner_id) REFERENCES owner(owner_id))"
    cursor.execute(query)
    db.commit()

# CREATE query to create the 'owner' table
def create_owner_table():
    query = "CREATE TABLE owner (owner_id INT NOT NULL, owner VARCHAR(255) NOT NULL, account_balance INT NOT NULL, PRIMARY KEY (owner_id))"
    cursor.execute(query)
    db.commit()

# INSERT query to insert data into the 'product_images' table
def insert_product_image(product_id, image_data):
    query = "INSERT INTO product_images (product_id, image_data) VALUES (%s, %s)"
    values = (product_id, image_data)
    cursor.execute(query, values)
    db.commit()

# INSERT query to insert data into the 'product' table
def insert_product(product_id, product_name, owner_id, parent, price, quantity, description):
    query = "INSERT INTO product (product_id, product_name, owner_id, parent, price, quantity, description) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (product_id, product_name, owner_id, parent, price, quantity, description)
    cursor.execute(query, values)
    db.commit()

# APPEND query to append data into the 'product' table
def append_product(product_id, owner_id, parent, price, quantity):
    query = "UPDATE product SET owner_id = %s, parent = array_append(parent, %s), price = %s, quantity = %s WHERE product_id = %s"
    values = (owner_id, parent, price, quantity, product_id)
    cursor.execute(query, values)
    db.commit()

# DELETE query to delete data from the 'product' table
def delete_product(product_id):
    query = "DELETE FROM product WHERE product_id = %s"
    values = (product_id,)
    cursor.execute(query, values)
    db.commit()

def get_product_info(product_id):
    query = ("SELECT * FROM product WHERE product_id = %s")
    cursor.execute(query, (product_id,))
    result = cursor.fetchone()
    cursor.close()
    return result

# function to retrieve owner information by owner ID
def get_owner_info(owner_id):
    query = ("SELECT * FROM owner WHERE owner_id = %s")
    cursor.execute(query, (owner_id,))
    result = cursor.fetchone()
    cursor.close()
    return result

# function to retrieve product image data by product ID
def get_product_image(product_id):
    query = ("SELECT image_data FROM product_images WHERE product_id = %s")
    cursor.execute(query, (product_id,))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else None


def products_for_owner(owner_id):
    query = ("SELECT * FROM product WHERE owner_id = %s")
    cursor.execute(query, (owner_id,))
    result = cursor.fetchone()
    cursor.close()
    return result

def get_product_list(product_name):
    query = ("SELECT * FROM product WHERE product_name = %s*")
    cursor.execute(query, (product_name,))
    result = cursor.fetchone()
    cursor.close()
    return result


create_product_table()

db.close()
