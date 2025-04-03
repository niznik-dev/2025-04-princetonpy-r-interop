from rpy2.robjects import r, pandas2ri
import pandas as pd

# Enable automatic conversion between R and pandas
pandas2ri.activate()

def run_r_script_with_rpy2(r_script_path='example_script.R'):
    try:
        # Read the R script from the file
        with open(r_script_path, 'r') as file:
            r_code = file.read()

        # Execute the R code and return the dataframe
        r_dataframe = r(r_code)
        return r_dataframe
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Run the R script and load the result
    result = run_r_script_with_rpy2('scatter_test.R')

    # Print the result
    print("Result from R script:")
    print(result)