## 从单细胞表达矩阵中，按 cluster 聚合成“每个 cluster 的平均表达矩阵”
def get_bulk_exp(adata, bulk_labels, layer='var'):
    if layer=='raw':
        res = pd.DataFrame(columns=adata.raw.var_names, index=adata.obs[bulk_labels].cat.categories)
    else:
        res = pd.DataFrame(columns=adata.var_names, index=adata.obs[bulk_labels].cat.categories)                                                                                                 
    
    for clust in adata.obs[bulk_labels].cat.categories: 
        if layer=='raw':
            res.loc[clust] = adata[adata.obs[bulk_labels].isin([clust]),:].raw.X.mean(0)
        else:
            res.loc[clust] = adata[adata.obs[bulk_labels].isin([clust]),:].X.mean(0)

    res.index=adata.obs[bulk_labels].cat.categories

    return res.T.astype(float)
