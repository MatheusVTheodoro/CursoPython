select  PRODUTOS.descricao, produtos.codigo_barra, PRODUTO_PRECOS.preco_tabela
FROM PRODUTOS
LEFT JOIN produto_precos ON (PRODUTOS.ID_PRODUTO = produto_precos.ID_PRODUTO)
WHERE (produto_precos.ativo = 1)

