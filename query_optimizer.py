few_shots = [
    {
        "Question": "How many white Nike t-shirts are available in size XS?",
        "SQLQuery": "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS'",
        "SQLResult": "Result of the SQL query",
        "Answer": "91"
    },
    {
        "Question": "What's the total inventory value for all medium size t-shirts?",
        "SQLQuery": "SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size = 'M'",
        "SQLResult": "Result of the SQL query",
        "Answer": "18500"
    },
    {
        "Question": "What revenue will we generate by selling all Levi's t-shirts with discounts?",
        "SQLQuery": """SELECT SUM(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) 
                      FROM (SELECT SUM(price*stock_quantity) as total_amount, t_shirt_id 
                      FROM t_shirts WHERE brand = 'Levi' GROUP BY t_shirt_id) a 
                      LEFT JOIN discounts ON a.t_shirt_id = discounts.t_shirt_id""",
        "SQLResult": "Result of the SQL query",
        "Answer": "16725.4"
    }
]