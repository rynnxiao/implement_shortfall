# implement_shortfall


Transaction 1:
| cost_name              |   delay_cost |   execution_cost |   fee_cost |   opportunity_cost |   total_cost |   trading_cost |
|------------------------+--------------+------------------+------------+--------------------+--------------+----------------|
| Opportunity Cost tran1 |            0 |             2000 |         80 |               1000 |         3080 |           2000 |
| Expanded IS Cost tran1 |         1250 |             2250 |         80 |                750 |         3080 |           1000 |

Transaction 2:
| cost_name              |   delay_cost |   execution_cost |   fee_cost |   opportunity_cost |   total_cost |   trading_cost |
|------------------------+--------------+------------------+------------+--------------------+--------------+----------------|
| Executation Cost tran2 |            0 |             2600 |        100 |                  0 |         2700 |           2600 |

Transaction batch:
| cost_name              |   delay_cost |   execution_cost |   fee_cost |   opportunity_cost |   total_cost |   trading_cost |
|------------------------+--------------+------------------+------------+--------------------+--------------+----------------|
| Executation Cost tran2 |            0 |             2600 |        100 |                  0 |         2700 |           2600 |
| Executation Cost tran2 |            0 |             2600 |        100 |                  0 |         2700 |           2600 |
| Executation Cost tran2 |            0 |             2600 |        100 |                  0 |         2700 |           2600 |
| Opportunity Cost tran1 |            0 |             2000 |         80 |               1000 |         3080 |           2000 |
| Expanded IS Cost tran1 |         1250 |             2250 |         80 |                750 |         3080 |           1000 |
| Opportunity Cost tran1 |            0 |             2000 |         80 |               1000 |         3080 |           2000 |
| Expanded IS Cost tran1 |         1250 |             2250 |         80 |                750 |         3080 |           1000 |
