import subprocess
import json
import pandas as pd

def run_r_script(r_script_path, output_file='output.csv'):
    try:
        # Call the R script using subprocess
        subprocess.run(['Rscript', r_script_path, output_file], check=True)
        return pd.read_csv(output_file)
    except subprocess.CalledProcessError as e:
        print(f"Error while running R script: {e}")
    except FileNotFoundError:
        print("Rscript command not found. Make sure R is installed and added to your PATH.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Run the R script and load the result
    result = run_r_script('scatter_test.R', output_file='scatter_data.csv')

    # Print the result
    print("Result from R script:")
    print(result)