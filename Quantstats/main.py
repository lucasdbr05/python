import quantstats as qs

qs.extend_pandas()
# fetch the daily returns for a stock
stock = qs.utils.download_returns('META')
print(stock)

# show sharpe ratio
#qs.stats.sharpe(stock)

# or using extend_pandas() :)
#stock.sharpe()

#print(stock.monthly_returns())
#print(stock.max_drawdown())

print([f for f in dir(stock) if f[0]!='_'])

#qs.plots.earnings()
stock.plot_earnings(savefig='output/meta_earnings.png', start_balance= 100000)
stock.plot_monthly_heatmap(savefig='output/meta_earnings.png', start_balance= 100000  )