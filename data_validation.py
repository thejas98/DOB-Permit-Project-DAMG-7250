import great_expectations as gx
import os
from dotenv import load_dotenv
load_dotenv()

path_to_gx = 'great_expectations/'
context = gx.get_context(context_root_dir=path_to_gx)


print(context)

