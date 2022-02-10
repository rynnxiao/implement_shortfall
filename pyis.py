"""
Implementation shortfall can be described in terms of the following three
examples:
1. Complete Execution
2. Opportunity Cost (Andre Perold)
3. Expanded Implementation Shortfall (Wayne Wagner)
"""
import attr
from tabulate import tabulate


@attr.define
class Fee:
    commission = attr.ib(type=float)

    def total_fee(self):
        return self.commission

@attr.define
class Transaction:
    share_num = attr.ib(type=float)
    execute_num = attr.ib(type=float)
    delay_price = attr.ib(type=float)
    execute_avg_price = attr.ib(type=float)
    determined_price = attr.ib(type=float)
    end_price = attr.ib(type=float, default=None)
    fee = attr.ib(type=Fee, default=None)

    def is_valition(self):
        if not self.is_fully_executed():
            return self.end_price is not None

    def is_fully_executed(self):
        return self.share_num == self.execute_num


@attr.define
class Cost:
    cost_name = attr.ib(type=str)
    delay_cost = attr.ib(type=float)
    trading_cost = attr.ib(type=float)
    opportunity_cost = attr.ib(type=float)
    fee_cost = attr.ib(type=float)
    execution_cost = attr.ib(type=float, default=attr.Factory(
        lambda self: self.trading_cost + self.delay_cost, takes_self=True))
    total_cost = attr.ib(type=float, default=attr.Factory(
        lambda self: self.execution_cost + self.opportunity_cost + self.fee_cost, takes_self=True))

class TCAEngine:
    def __init__(self):
        self.cost_results = []

    def tca_run(self, transaction_obj: Transaction):
        raise NotImplementedError()

    def reset_result(self):
        self.cost_results = []


class ImplementationShortfallEngine(TCAEngine):
    def complete_execution(self, transaction_obj):
        executed_cost = transaction_obj.share_num * \
            (transaction_obj.execute_avg_price -
             transaction_obj.determined_price) + transaction_obj.fee.total_fee()
        self.cost_results.append(
            Cost("Executation Cost", 0, executed_cost,
                 0, transaction_obj.fee.total_fee())
        )

    def opportunity_cost(self, transaction_obj):
        executed_cost = transaction_obj.execute_num * \
            (transaction_obj.execute_avg_price - transaction_obj.determined_price)
        opportunity_cost = (transaction_obj.share_num - transaction_obj.execute_num) * (
            transaction_obj.end_price - transaction_obj.determined_price)

        self.cost_results.append(
            Cost("Opportunity Cost", 0, executed_cost,
                 opportunity_cost, transaction_obj.fee.total_fee())
        )

    def expanded_implementation_shortfall(self, transaction_obj):
        delay_cost = transaction_obj.share_num * \
            (transaction_obj.delay_price - transaction_obj.determined_price)
        trading_cost = transaction_obj.execute_num * \
            (transaction_obj.execute_avg_price - transaction_obj.delay_price)
        opportunity_cost = (transaction_obj.share_num - transaction_obj.execute_num) * (
            transaction_obj.end_price - transaction_obj.delay_price)

        self.cost_results.append(
            Cost("Expanded IS Cost", delay_cost, trading_cost,
                 opportunity_cost, transaction_obj.fee.total_fee())
        )

    def tca_run(self, transaction_obj: Transaction):
        self.reset_result()
        if transaction_obj.is_fully_executed():
            self.complete_execution(transaction_obj)
        else:
            self.opportunity_cost(transaction_obj)
            self.expanded_implementation_shortfall(transaction_obj)

    def format_data(self):
        self.result_formated_data = [[getattr(item, name) for name in Cost.__dict__ if not name.startswith("_")]
        for item in self.cost_results]

    def pprint(self):
        header = sorted([name for name in Cost.__dict__ if not name.startswith("_")])
        self.format_data()
        print(self.result_formated_data)
        print(
            tabulate(
                self.result_formated_data,
                headers=header,
                tablefmt="orgtbl"
            )
        )


if __name__ == "__main__":
    engine = ImplementationShortfallEngine()
    print("Transaction 1:")
    trans = Transaction(
        share_num=5000, 
        execute_num=4000, 
        delay_price=10.25, 
        execute_avg_price=10.5, 
        determined_price=10, 
        end_price=11, 
        fee=Fee(80)
        )
    engine.tca_run(trans)
    engine.pprint()
    print("\nTransaction 2:")
    trans = Transaction(
        share_num=5000, 
        execute_num=5000, 
        delay_price=10.25, 
        execute_avg_price=10.5, 
        determined_price=10, 
        end_price=11, 
        fee=Fee(80)
        )
    engine.tca_run(trans)
    engine.pprint()
