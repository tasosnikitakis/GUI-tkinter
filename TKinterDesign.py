from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta

figma_token = "figd__6YEJviBV6Dcx6eUSNE7lVEElusZkju_1mKxeSXE"

handler = TA_Handler(
    symbol="AAPL",
    exchange="nasdaq",
    screener="america",
    interval="1d",
    timeout=None
)

analysis = handler.get_analysis()
print(analysis.summary)

