# implement_shortfall


Transaction 1:<br>
| cost_name              |   delay_cost |   execution_cost |   fee_cost |   opportunity_cost |   total_cost |   trading_cost |<br>
|------------------------+--------------+------------------+------------+--------------------+--------------+----------------|<br>
| Opportunity Cost tran1 |            0 |             2000 |         80 |               1000 |         3080 |           2000 |<br>
| Expanded IS Cost tran1 |         1250 |             2250 |         80 |                750 |         3080 |           1000 |<br>
<br>
Transaction 2:<br>
| cost_name              |   delay_cost |   execution_cost |   fee_cost |   opportunity_cost |   total_cost |   trading_cost |<br>
|------------------------+--------------+------------------+------------+--------------------+--------------+----------------|<br>
| Executation Cost tran2 |            0 |             2600 |        100 |                  0 |         2700 |           2600 |<br>
<br>
Transaction batch:<br>
| cost_name              |   delay_cost |   execution_cost |   fee_cost |   opportunity_cost |   total_cost |   trading_cost |<br>
|------------------------+--------------+------------------+------------+--------------------+--------------+----------------|<br>
| Executation Cost tran2 |            0 |             2600 |        100 |                  0 |         2700 |           2600 |<br>
| Executation Cost tran2 |            0 |             2600 |        100 |                  0 |         2700 |           2600 |<br>
| Executation Cost tran2 |            0 |             2600 |        100 |                  0 |         2700 |           2600 |<br>
| Opportunity Cost tran1 |            0 |             2000 |         80 |               1000 |         3080 |           2000 |<br>
| Expanded IS Cost tran1 |         1250 |             2250 |         80 |                750 |         3080 |           1000 |<br>
| Opportunity Cost tran1 |            0 |             2000 |         80 |               1000 |         3080 |           2000 |<br>
| Expanded IS Cost tran1 |         1250 |             2250 |         80 |                750 |         3080 |           1000 |<br>
