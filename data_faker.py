from faker import Faker
import pandas as pd

fake = Faker()


class data_set():
    
    def __init__(self, name, start_date, end_date, granularity):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.granularity = granularity
        ALLOWED_GRAIN = {"D"}  # we will add in H, W, M later if needed
        if self.granularity not in self.ALLOWED_GRAIN:
            raise ValueError(f"Granularity {self.granularity} is not allowed. Allowed values are: {self.ALLOWED_GRAIN}")
    
    class data():
        def __init__(self, data_set):
            self.data_set = data_set
            self.dataframe = None
            # sales
            # add_to_carts
            # website_visitors
            # marketing_expense

            #ideas:
                # is_new_customer
                # is_returning_customer 
    
                # is_on_sale
                # sale_amount (in 0-1)

    

    