few_shots = [
    {
        "Question": "Count of Adidas t-shirts?",
        "SQLQuery": "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Adidas'",
        "SQLResult": "[(42,)]",
        "Answer": "42 Adidas t-shirts available"
    },
    {
        "Question": "Nike t-shirt colors?",
        "SQLQuery": "SELECT DISTINCT color FROM t_shirts WHERE brand = 'Nike' LIMIT 5",
        "SQLResult": "[('black',), ('white',)]",
        "Answer": "Available colors: black, white"
    }
]