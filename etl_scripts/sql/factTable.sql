DROP TABLE IF EXISTS salesFact;




CREATE TABLE salesFact (
    invoice_id INTEGER PRIMARY KEY ,
    unit_price FLOAT,
    quantity INTEGER,
    tax_five_percent FLOAT,
    total FLOAT,
    cogs FLOAT,
    gross_margin_percentage FLOAT
);