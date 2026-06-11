create table Produtos (
    Id_produto int primary key,
    Nome_produto varchar(50),
    Preco_unitario decimal(10,2)
);

insert into Produtos (Id_produto, Nome_produto, Preco_unitario) values
(1, 'arroz', 15.00),
(2, 'feijão', 8.00),
(3, 'òleo', 5.00);

create table Compras (
    Id_compra int primary key,
    Id_produto int,
    Quantidade int,
    FOREIGN KEY (Id_produto) REFERENCES Produtos(Id_produto)
);

insert into Compras (Id_compra, Id_produto, Quantidade) values
(101, 1, 2),
(102, 2, 3),
(103, 3, 1);

/*questão1*/

SELECT
    c.Id_compra,
    p.Nome_produto,
    c.Quantidade,
    p.Preco_unitario,
    (c.quantidade * p.Preco_unitario) AS Valor_total
FROM
    Compras c   
INNER JOIN
    Produtos p 
ON 
c.Id_produto = p.Id_produto;


/*questão2*/

SELECT
    p.Id_produto,
    p.Nome_produto,
    SUM(c.quantidade) AS Quantidade_total_comprada
FROM 
    Produtos p
INNER JOIN
    Compras c
ON
p.Id_produto = c.Id_produto
GROUP BY
    p.Id_produto, p.Nome_produto
ORDER BY
    Quantidade_total_comprada DESC;



/*questão3*/
SELECT
    p.Id_produto,
    p.Nome_produto,
    Coalesce(SUM(c.quantidade), 0) AS Quantidade_total
FROM
    Produtos p
LEFT JOIN
    Compras c
ON p.Id_produto = c.Id_produto
GROUP BY
    p.Id_produto,
    p.Nome_produto
    