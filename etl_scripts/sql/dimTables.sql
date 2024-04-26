DROP TABLE IF EXISTS branchDim;
DROP TABLE IF EXISTS customerFlagDim;
DROP TABLE IF EXISTS productDim;
DROP TABLE IF EXISTS paymentDim;

DO $$
BEGIN
    IF NOT EXISTS (SELECT * FROM pg_type WHERE typname in ('gender_enum' , 'customer_type_enum', ' payment_enum')) THEN
        CREATE TYPE gender_enum as ENUM('male','female');
        CREATE TYPE customer_type_enum as ENUM('normal','member');
        CREATE TYPE payment_enum as ENUM('cash','creditcard','ewallet');    
    END IF;
END $$;


CREATE TABLE branchDim (
    branch_surrogate_key VARCHAR(5), 
    branch_ID VARCHAR(5)
);


CREATE TABLE customerFlagDim(
    customer_surrogate_key VARCHAR(10),
    gender gender_enum,
    customer_type customer_type_enum

);

CREATE TABLE productDim(
    product_surrogate_key VARCHAR(10),
    product_line_detail VARCHAR(25)
);

CREATE TABLE paymentDim(
    payment_surrogate_key VARCHAR(10),
    payment_method payment_enum
);

