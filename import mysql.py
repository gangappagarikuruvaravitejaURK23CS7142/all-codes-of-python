import mysql.connector

class VegetableShopDatabase:
    def _init_(self):
        self.conn = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        self.cursor = self.conn.cursor()
        self.create_tables()
        
    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cart (
                id INT AUTO_INCREMENT PRIMARY KEY,
                vegetable VARCHAR(255),
                quantity INT,
                total_price DECIMAL(10, 2)
            )
        """)
        
    def add_to_cart(self, vegetable, quantity, total_price):
        sql = "INSERT INTO cart (vegetable, quantity, total_price) VALUES (%s, %s, %s)"
        val = (vegetable, quantity, total_price)
        self.cursor.execute(sql, val)
        self.conn.commit()
        
    def close(self):
        self.conn.close()